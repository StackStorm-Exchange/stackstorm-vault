from st2tests.base import BaseActionTestCase

from read_kv import VaultReadKVAction
from .fixtures.config import dummy_config


class ReadKVActionTestCase(BaseActionTestCase):
    action_cls = VaultReadKVAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run(
            path="",
            kv_version=1,
            mount_point="",
            version="1",
        )
