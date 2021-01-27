from create_token import VaultCreateTokenAction
from tests.vault_action_tests_base import VaultActionTestCase


class CreateTokenActionTestCase(VaultActionTestCase):
    action_cls = VaultCreateTokenAction

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
