from read_kv import VaultReadKVAction
from tests.vault_action_tests_base import VaultActionTestCase


class ReadKVActionTestCase(VaultActionTestCase):
    action_cls = VaultReadKVAction

    def test_method(self):
        action = self.get_action_instance(config=self.dummy_pack_config)
        result = action.run(
            path="",
            kv_version=1,
            mount_point="",
            version="1",
        )
