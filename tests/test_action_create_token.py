from urllib3.contrib import pyopenssl
pyopenssl.inject_into_urllib3()

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
