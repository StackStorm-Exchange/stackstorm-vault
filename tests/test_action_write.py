from write import VaultWriteAction
from tests.vault_action_tests_base import VaultActionTestCase


class WriteActionTestCase(VaultActionTestCase):
    action_cls = VaultWriteAction

    def test_write_key(self):
        # test
        action = self.get_action_instance(config=self.dummy_pack_config)
        action_result = action.run(
            path="secret/stanley",
            values='{"st2": "awesome"}',
        )
        # action_result is a requests.response object
        assert action_result is not None

        result = self.client.read("secret/stanley")
        assert result["data"]["st2"] == "awesome"

        # cleanup
        self.client.delete("secret/stanley")
