from read import VaultReadAction
from tests.vault_action_tests_base import VaultActionTestCase


class ReadActionTestCase(VaultActionTestCase):
    action_cls = VaultReadAction

    def test_method(self):
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run(path="")
