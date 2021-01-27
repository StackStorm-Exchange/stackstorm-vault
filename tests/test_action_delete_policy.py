from delete_policy import VaultPolicyDeleteAction
from tests.vault_action_tests_base import VaultActionTestCase


class PolicyDeleteActionTestCase(VaultActionTestCase):
    action_cls = VaultPolicyDeleteAction

    def test_method(self):
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run(name="")
