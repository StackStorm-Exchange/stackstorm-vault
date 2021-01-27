from is_initialized import VaultIsInitializedAction
from tests.vault_action_tests_base import VaultActionTestCase


class IsInitializedActionTestCase(VaultActionTestCase):
    action_cls = VaultIsInitializedAction

    def test_method(self):
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run()
