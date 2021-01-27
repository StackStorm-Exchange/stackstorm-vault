from list_policies import VaultPolicyListAction
from tests.vault_action_tests_base import VaultActionTestCase


class PolicyListActionTestCase(VaultActionTestCase):
    action_cls = VaultPolicyListAction

    def test_method(self):
        # setup
        rules_text, rules_obj = self.prep_policy("stanley")

        # test
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run()
        assert "stanley" in result

        self.client.delete_policy("stanley")

        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run()
        assert "stanley" not in result
