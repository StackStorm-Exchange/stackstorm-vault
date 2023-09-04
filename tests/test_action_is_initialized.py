from is_initialized import VaultIsInitializedAction
from tests.vault_action_tests_base import VaultActionTestCase


class IsInitializedActionTestCase(VaultActionTestCase):
    action_cls = VaultIsInitializedAction

    def test_already_initialized(self):
        action = self.get_action_instance(config=self.dummy_pack_config)
        _, result = action.run()
        self.assertTrue(result)

    def test_before_and_after_initialization(self):
        self.manager.restart_vault_cluster(perform_init=False)

        action = self.get_action_instance(config=self.dummy_pack_config)
        _, result = action.run()
        self.assertFalse(result)

        self.manager.restart_vault_cluster(perform_init=True)

        action = self.get_action_instance(config=self.dummy_pack_config)
        _, result = action.run()
        self.assertTrue(result)
