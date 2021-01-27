from write import VaultWriteAction
from tests.vault_action_tests_base import VaultActionTestCase


class WriteActionTestCase(VaultActionTestCase):
    action_cls = VaultWriteAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run(
            path="",
            values="",
        )
