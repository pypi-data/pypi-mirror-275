import hashlib
import logging
import sys
import traceback

import backoff
import click
import requests
from fedora_messaging.config import conf as fm_config
from tahrir_api.dbapi import TahrirDatabase

import fedbadges.utils

from .utils import award_badge, option_debug, setup_logging


log = logging.getLogger(__name__)

HTTP_TIMEOUT = 5


def _backoff_hdlr(details):
    log.warning("Request to Libravatar failed, retrying.")


def _giveup_hdlr(details):
    log.warning(
        f"Request to Libravatar failed, giving up. {traceback.format_tb(sys.exc_info()[2])}"
    )


@backoff.on_exception(
    backoff.expo,
    (requests.exceptions.SSLError, requests.exceptions.ConnectionError),
    max_tries=10,
    on_backoff=_backoff_hdlr,
    on_giveup=_giveup_hdlr,
    raise_on_giveup=False,
)
def query_libravatar(nickname):
    openid = f"http://{nickname}.id.fedoraproject.org/"
    hash = hashlib.sha256(openid.encode("utf-8")).hexdigest()
    url = f"https://seccdn.libravatar.org/avatar/{hash}?d=404"
    return requests.get(url, timeout=HTTP_TIMEOUT)


@click.command()
@option_debug
def main(debug):
    setup_logging(debug=debug)
    config = fm_config["consumer_config"]
    uri = config["database_uri"]
    tahrir = TahrirDatabase(
        uri,
        notification_callback=fedbadges.utils.notification_callback,
    )
    badge = tahrir.get_badge(badge_id="mugshot")

    persons = tahrir.get_all_persons()
    already_has_it = [assertion.person for assertion in badge.assertions]

    good, bad = [], []
    for person in persons:

        if person in already_has_it:
            good.append(person)
            log.debug("Skipping %s", person)
            continue

        response = query_libravatar(person.nickname)
        if response is None:
            # Query failed, ignore
            continue

        if response.ok:
            log.info("%s totally gets the mugshot badge.", person.nickname)
            good.append(person)
            award_badge(tahrir, badge, person.email, check_existing=False)
        else:
            bad.append(person)

    log.info("%s good peoples", len(good))
    log.info("%s bad peoples", len(bad))


if __name__ == "__main__":
    main()
