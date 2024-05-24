""" Consumers for producing openbadges by listening for messages on fedmsg

Authors:  Ross Delinger
          Ralph Bean
          Aurelien Bompard
"""

import asyncio
import datetime
import logging
import threading
import time
from functools import partial

import datanommer.models
import fasjson_client
import tahrir_api.dbapi
from fedora_messaging.api import Message
from fedora_messaging.config import conf as fm_config

from .aio import Periodic
from .cached import configure as configure_cache
from .cached import on_message as update_cached_values
from .rulesrepo import RulesRepo
from .utils import datanommer_has_message, notification_callback


log = logging.getLogger(__name__)

DEFAULT_DELAY_LIMIT = 100
DEFAULT_RULES_RELOAD_INTERVAL = 15  # in minutes
MAX_WAIT_DATANOMMER = 5  # seconds


class FedoraBadgesConsumer:
    delay_limit = 100

    def __init__(self):
        self.config = fm_config["consumer_config"]
        self.delay_limit = int(self.config.get("delay_limit", DEFAULT_DELAY_LIMIT))
        self.badge_rules = []
        self.lock = threading.Lock()

        self.loop = asyncio.get_event_loop()
        self._ready = self.loop.create_task(self.setup())
        if not self.loop.is_running():
            self.loop.run_until_complete(self._ready)

    async def setup(self):
        # Five things need doing at start up time
        # 0) Set up a request local to hang thread-safe db sessions on.
        # 1) Initialize our connection to the Tahrir DB
        # 2) Initialize our connection to the datanommer DB.
        # 3) Load our badge definitions and rules from YAML.
        # Cache
        await self.loop.run_in_executor(None, self._initialize_cache)

        # Tahrir stuff.
        await self.loop.run_in_executor(None, self._initialize_tahrir_connection)

        # Datanommer stuff
        await self.loop.run_in_executor(None, self._initialize_datanommer_connection)

        # FASJSON stuff
        self.fasjson = await self.loop.run_in_executor(
            None, fasjson_client.Client, self.config["fasjson_base_url"]
        )

        # Load badge definitions
        self._rules_repo = RulesRepo(self.config, self.issuer_id, self.fasjson)
        self._rules_repo.setup()

        rules_reload_inteval = self.config.get(
            "rules_reload_interval", DEFAULT_RULES_RELOAD_INTERVAL
        )
        self._refresh_badges_task = Periodic(
            partial(self.loop.run_in_executor, None, self._reload_rules), rules_reload_inteval * 60
        )
        await self._refresh_badges_task.start(run_now=True)

    def _initialize_cache(self):
        cache_args = self.config.get("cache")
        configure_cache(**cache_args)

    def _initialize_tahrir_connection(self):
        database_uri = self.config.get("database_uri")
        if not database_uri:
            raise ValueError("Badges consumer requires a database uri")
        issuer = self.config["badge_issuer"]
        self.tahrir = tahrir_api.dbapi.TahrirDatabase(
            dburi=database_uri,
            autocommit=False,
            notification_callback=notification_callback,
        )
        self.issuer_id = self.tahrir.add_issuer(
            issuer.get("issuer_origin"),
            issuer.get("issuer_name"),
            issuer.get("issuer_url"),
            issuer.get("issuer_email"),
        )
        self.tahrir.session.commit()

    def _get_tahrir_client(self, session=None):
        return self.tahrir

    def _initialize_datanommer_connection(self):
        datanommer.models.init(self.config["datanommer_db_uri"])

    def award_badge(self, username, badge_rule, link=None):
        email = f"{username}@fedoraproject.org"
        client = self._get_tahrir_client(self.tahrir.session)
        client.add_person(email)
        self.tahrir.session.commit()
        client.add_assertion(badge_rule.badge_id, email, None, link)
        self.tahrir.session.commit()

    def __call__(self, message: Message):
        # First thing, we receive the message, but we put ourselves to sleep to
        # wait for a moment.  The reason for this is that, when things are
        # 'calm' on the bus, we receive messages "too fast".  A message that
        # arrives to the badge awarder triggers (usually) a check against
        # datanommer to count messages.  But if we try to count them before
        # this message arrives at datanommer, we'll get skewed results!  Race
        # condition.  We go to sleep to allow ample time for datanommer to
        # consume this one before we go and start doing checks on it.
        # TODO: Option 1, easy: make a SQL query in datanommer instead of waiting
        # TODO: Option 2, a bit harder: check if the current message is in the
        #       matched messages when querying datanommer, and if it's not add 1
        #       to the count.

        self._wait_for_datanommer(message)

        log.debug("Updating cached values for %s on %s", message.id, message.topic)
        update_cached_values(message)

        datagrepper_url = self.config["datagrepper_url"]
        link = f"{datagrepper_url}/id?id={message.id}&is_raw=true&size=extra-large"

        # Define this so we can refer to it in error handling below
        badge_rule = None

        # Award every badge as appropriate.
        log.debug("Processing rules for %s on %s", message.id, message.topic)

        tahrir = self._get_tahrir_client()
        for badge_rule in self.badge_rules:
            try:
                for recipient in badge_rule.matches(message, tahrir):
                    log.debug(
                        "Rule %s matched for %s (message %s on %s)",
                        badge_rule.badge_id,
                        recipient,
                        message.id,
                        message.topic,
                    )
                    self.award_badge(recipient, badge_rule, link)
            except Exception:
                log.exception("Rule: %s, message: %s", repr(badge_rule), repr(message))

        log.debug("Done with %s, %s", message.topic, message.id)

    def _reload_rules(self):
        log.debug("Check for badges updates in the repo")
        tahrir = self._get_tahrir_client()
        self.badge_rules = self._rules_repo.load_all(tahrir)

    def _wait_for_datanommer(self, message: Message):
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        a_minute_ago = now - datetime.timedelta(minutes=1)
        try:
            sent_at = message._headers["sent-at"]
            if sent_at.endswith("Z"):
                # Python 3.10 compatibility
                sent_at = sent_at[:-1] + "+00:00"
            sent_at = datetime.datetime.fromisoformat(sent_at)
        except (KeyError, TypeError, ValueError) as e:
            log.debug("Could not read the sent-at value: %s: %s", e.__class__.__name__, e)
            sent_at = None
        if sent_at is not None and sent_at < a_minute_ago:
            return  # It's kinda old, datanommer surely has it already

        yesterday = now - datetime.timedelta(days=1)
        for _i in range(MAX_WAIT_DATANOMMER * 2):
            if datanommer_has_message(message.id, since=yesterday):
                break
            log.debug("Waiting for the message to land in datanommer")
            time.sleep(0.5)
