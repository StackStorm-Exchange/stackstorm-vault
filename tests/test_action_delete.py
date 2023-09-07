from delete import VaultDeleteAction
from tests.vault_action_tests_base import VaultActionTestCase


class DeleteActionTestCase(VaultActionTestCase):
    action_cls = VaultDeleteAction

    def test_delete_existing_key(self):
        # setup
        self.client.write("secret/stanley", st2="awesome")

        # test
        action = self.get_action_instance(config=self.dummy_pack_config)
        _, action_result = action.run(path="secret/stanley")
        # hvac does not return anything here
        self.assertIsNone(action_result)

        result = self.client.read("secret/stanley")
        self.assertIsNone(result)
