""" Utilities for fedbadges that don't quite fit anywhere else. """

# These are here just so they're available in globals()
# for compiling lambda expressions
import datetime
import json
import logging
import re
import sys
import traceback
import types

import backoff
import datanommer.models
import fasjson_client
import sqlalchemy as sa
from fedora_messaging import api as fm_api
from fedora_messaging import exceptions as fm_exceptions
from fedora_messaging.config import conf as fm_config
from twisted.internet import reactor, threads


log = logging.getLogger(__name__)


def construct_substitutions(message: fm_api.Message):
    subs = dict_to_subs({"msg": message.body})
    subs["topic"] = message.topic
    subs["usernames"] = message.usernames
    return subs


def dict_to_subs(msg: dict):
    """Convert a fedmsg message into a dict of substitutions."""
    subs = {}
    for key1 in msg:
        if isinstance(msg[key1], dict):
            subs.update(
                dict(
                    [
                        (".".join([key1, key2]), val2)
                        for key2, val2 in list(dict_to_subs(msg[key1]).items())
                    ]
                )
            )
            subs[key1] = msg[key1]
        elif isinstance(msg[key1], str):
            subs[key1] = msg[key1].lower()
        else:
            subs[key1] = msg[key1]
    return subs


def format_args(obj, subs):
    """Recursively apply a substitutions dict to a given criteria subtree"""

    if isinstance(obj, dict):
        for key in obj:
            obj[key] = format_args(obj[key], subs)
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return [format_args(item, subs) for item in obj]
    elif isinstance(obj, str) and obj[2:-2] in subs:
        obj = subs[obj[2:-2]]
    elif isinstance(obj, (int, float)):
        pass
    else:
        obj = obj % subs

    return obj


def single_argument_lambda_factory(expression, name="value"):
    """Compile a lambda expression with a single argument"""

    code = compile(f"lambda {name}: {expression}", __file__, "eval")
    lambda_globals = {
        "__builtins__": __builtins__,
        "json": json,
        "re": re,
    }
    return types.LambdaType(code, lambda_globals)()


def single_argument_lambda(expression, argument, name="value"):
    """Execute a lambda expression with a single argument"""
    func = single_argument_lambda_factory(expression, name)
    return func(argument)


def recursive_lambda_factory(obj, arg, name="value"):
    """Given a dict, find any lambdas, compile, and execute them."""

    if isinstance(obj, dict):
        for key in obj:
            if key == "lambda":
                # If so, *replace* the parent dict with the result of the expr
                obj = single_argument_lambda(obj[key], arg, name)
                break
            else:
                obj[key] = recursive_lambda_factory(obj[key], arg, name)
    elif isinstance(obj, list):
        return [recursive_lambda_factory(e, arg, name) for e in obj]
    else:
        pass

    return obj


def graceful(default_return_value):
    """A decorator that gracefully handles exceptions."""

    def decorate(method):
        def inner(self, *args, **kwargs):
            try:
                return method(self, *args, **kwargs)
            except Exception:
                log.exception(
                    "From method: %r self: %r args: %r kwargs: %r", method, self, args, kwargs
                )
                return default_return_value

        return inner

    return decorate


def _publish_backoff_hdlr(details):
    log.warning(f"Publishing message failed. Retrying. {traceback.format_tb(sys.exc_info()[2])}")


@backoff.on_exception(
    backoff.expo,
    (fm_exceptions.ConnectionException, fm_exceptions.PublishException),
    max_tries=3,
    on_backoff=_publish_backoff_hdlr,
)
def _publish(message):
    # Use fm_api.twisted_publish() when available
    threads.blockingCallFromThread(
        reactor,
        fm_api._twisted_service._service.factory.publish,
        message=message,
        exchange=fm_config["publish_exchange"],
    )


def notification_callback(message):
    """This is a callback called by tahrir_api whenever something
    it deems important has happened.

    It is just used to publish fedmsg messages.
    """
    try:
        _publish(message)
    except fm_exceptions.BaseException:
        log.error(f"Publishing message failed. Giving up. {traceback.format_tb(sys.exc_info()[2])}")


def user_exists_in_fas(fasjson, user):
    """Return true if the user exists in FAS."""
    return nick2fas(user, fasjson) is not None


def get_pagure_authors(authors):
    """Extract the name of pagure authors from
    a dictionary

    Args:
    authors (list): A list of dict that contains fullname and name key.
    """
    authors_name = []
    for item in authors:
        if isinstance(item, dict):
            try:
                if item["name"] is not None:
                    authors_name.append(item["name"])
            except KeyError as e:
                raise ValueError("Multiple recipients: name not found in the message") from e
    return authors_name


def _fasjson_backoff_hdlr(details):
    log.warning(f"FASJSON call failed. Retrying. {traceback.format_tb(sys.exc_info()[2])}")


@backoff.on_exception(
    backoff.expo,
    (ConnectionError, TimeoutError),
    max_tries=3,
    on_backoff=_fasjson_backoff_hdlr,
)
def nick2fas(nick, fasjson):
    """Return the user in FAS."""
    try:
        return fasjson.get_user(username=nick).result["username"]
    except fasjson_client.errors.APIError as e:
        if e.code == 404:
            return None
        raise


def email2fas(email, fasjson):
    """Return the user with the specified email in FAS."""
    if email.endswith("@fedoraproject.org"):
        return nick2fas(email.rsplit("@", 1)[0], fasjson)

    @backoff.on_exception(
        backoff.expo,
        (ConnectionError, TimeoutError),
        max_tries=3,
        on_backoff=_fasjson_backoff_hdlr,
    )
    def _search_user(email):
        return fasjson.search(email=email).result

    result = _search_user(email)

    if not result:
        return None
    return result[0]


def datanommer_has_message(msg_id: str, since: datetime.datetime | None = None):
    query = sa.select(sa.func.count(datanommer.models.Message.id)).where(
        datanommer.models.Message.msg_id == msg_id
    )
    if since is not None:
        since = since.replace(tzinfo=None)
        query = query.where(datanommer.models.Message.timestamp >= since)
    return datanommer.models.session.scalar(query) > 0
