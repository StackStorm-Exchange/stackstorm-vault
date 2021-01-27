from get_policy import VaultGetPolicyAction
from tests.vault_action_tests_base import VaultActionTestCase


class GetPolicyActionTestCase(VaultActionTestCase):
    action_cls = VaultGetPolicyAction

    def test_method(self):
        # setup
        rules_text, rules_obj = self.prep_policy("stanley")

        # test
        action = self.get_action_instance(config=self.dummy_pack_config)
        action_result = action.run(name="stanley")
        assert action_result == rules_text

        # cleanup
        self.client.delete_policy("stanley")
