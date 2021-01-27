from delete import VaultDeleteAction
from tests.vault_action_tests_base import VaultActionTestCase


class DeleteActionTestCase(VaultActionTestCase):
    action_cls = VaultDeleteAction

    def test_method(self):
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run(path="")
