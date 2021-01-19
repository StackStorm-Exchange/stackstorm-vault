from st2tests.base import BaseActionTestCase

from read_kv import VaultReadKVAction

class ReadKVActionTestCase(BaseActionTestCase):
    action_cls = VaultReadKVAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
