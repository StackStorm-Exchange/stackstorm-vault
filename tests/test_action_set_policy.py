from set_policy import VaultPolicySetAction
from tests.vault_action_tests_base import VaultActionTestCase


class PolicySetActionTestCase(VaultActionTestCase):
    action_cls = VaultPolicySetAction

    def test_method(self):
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run(
            name="",
            rules="",
        )
