# from urllib3.contrib import pyopenssl
# pyopenssl.inject_into_urllib3()
import os

print(os.getcwd())

import logging
import http.client

httpclient_logger = logging.getLogger("http.client")


def httpclient_logging_patch(level=logging.DEBUG):
    """Enable HTTPConnection debug logging to the logging framework"""

    def httpclient_log(*args):
        httpclient_logger.log(level, " ".join(args))

    # mask the print() built-in in the http.client module to use
    # logging instead
    http.client.print = httpclient_log
    # enable debugging
    http.client.HTTPConnection.debuglevel = 1


httpclient_logging_patch()

from create_token import VaultCreateTokenAction
from tests.vault_action_tests_base import VaultActionTestCase


class CreateTokenActionTestCase(VaultActionTestCase):
    action_cls = VaultCreateTokenAction

    # Use None here to avoid this error:
    #   "expiring root tokens cannot create non-expiring root tokens"
    default_token_lease = None

    def test_method(self):
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run(
            # token_id=None,
            # policies=None,
            # meta=None,
            # no_parent=False,
            # display_name=None,
            # num_uses=None,
            # no_default_policy=False,
            # ttl=None,
            # orphan=False,
            # wrap_ttl=None,
        )
        self.assertIsNotNone(result["auth"]["client_token"])
