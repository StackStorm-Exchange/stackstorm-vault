from st2tests.base import BaseActionTestCase

from write import VaultWriteAction

class WriteActionTestCase(BaseActionTestCase):
    action_cls = VaultWriteAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
