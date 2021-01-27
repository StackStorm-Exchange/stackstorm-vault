from read import VaultReadAction
from tests.vault_action_tests_base import VaultActionTestCase


class ReadActionTestCase(VaultActionTestCase):
    action_cls = VaultReadAction

    def test_read_existing_key(self):
        # setup
        self.client.write("secret/stanley", st2="awesome")

        # test
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run(path="secret/stanley")
        assert result["st2"] == "awesome"

        # cleanup
        self.client.delete("secret/stanley")
