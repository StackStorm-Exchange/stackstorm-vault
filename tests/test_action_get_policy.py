from get_policy import VaultGetPolicyAction
from tests.vault_action_tests_base import VaultActionTestCase


class GetPolicyActionTestCase(VaultActionTestCase):
    action_cls = VaultGetPolicyAction

    def test_method(self):
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run(name="")
