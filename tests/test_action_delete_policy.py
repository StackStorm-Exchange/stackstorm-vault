from delete_policy import VaultPolicyDeleteAction
from tests.vault_action_tests_base import VaultActionTestCase


class PolicyDeleteActionTestCase(VaultActionTestCase):
    action_cls = VaultPolicyDeleteAction

    def test_method(self):
        # setup
        self.prep_policy("stanley")

        # test
        action = self.get_action_instance(config=self.dummy_pack_config)
        action_result = action.run(name="stanley")
        assert action_result is None

        result = self.client.get_policy("stanley")
        assert result is None
