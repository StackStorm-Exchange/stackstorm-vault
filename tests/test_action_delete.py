from delete import VaultDeleteAction
from tests.vault_action_tests_base import VaultActionTestCase


class DeleteActionTestCase(VaultActionTestCase):
    action_cls = VaultDeleteAction

    def test_delete_existing_key(self):
        # setup
        self.client.write("secret/stanley", st2="awesome")

        # test
        action = self.get_action_instance(config=self.dummy_pack_config)
        action_result = action.run(path="secret/stanley")
        # action_result is a requests.response object

        result = self.client.read("secret/stanley")
        assert result is None
