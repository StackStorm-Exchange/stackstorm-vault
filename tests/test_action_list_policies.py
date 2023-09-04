from list_policies import VaultPolicyListAction
from tests.vault_action_tests_base import VaultActionTestCase


class PolicyListActionTestCase(VaultActionTestCase):
    action_cls = VaultPolicyListAction

    def test_method(self):
        # setup
        self.prep_policy("stanley")

        # test
        action = self.get_action_instance(config=self.dummy_pack_config)
        _, result = action.run()
        self.assertIn("stanley", result["policies"]["data"]["policies"])

        self.client.sys.delete_policy("stanley")

        action = self.get_action_instance(config=self.dummy_pack_config)
        _, result = action.run()
        self.assertNotIn("stanley", result["policies"]["data"]["policies"])
