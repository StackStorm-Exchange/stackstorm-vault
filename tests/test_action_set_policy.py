from set_policy import VaultPolicySetAction
from tests.vault_action_tests_base import VaultActionTestCase


class PolicySetActionTestCase(VaultActionTestCase):
    action_cls = VaultPolicySetAction

    def test_method(self):
        # same as self.prep_policy
        rules_text = """
        path "sys" { policy = "deny" }
        path "secret" { policy = "write" }
        """
        # rules_obj = {"path": {"sys": {"policy": "deny"}, "secret": {"policy": "write"}}}

        action = self.get_action_instance(config=self.dummy_pack_config)
        action_result = action.run(
            name="stanley",
            rules=rules_text,
        )
        self.assertIsNone(action_result)

        result = self.client.get_policy("stanley")
        self.assertEqual(result, rules_text)

        # cleanup
        self.client.delete_policy("stanley")
