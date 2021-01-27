from list_policies import VaultPolicyListAction
from tests.vault_action_tests_base import VaultActionTestCase


class PolicyListActionTestCase(VaultActionTestCase):
    action_cls = VaultPolicyListAction

    def test_method(self):
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run()
