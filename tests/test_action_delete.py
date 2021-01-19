from st2tests.base import BaseActionTestCase

from delete import VaultDeleteAction

class DeleteActionTestCase(BaseActionTestCase):
    action_cls = VaultDeleteAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
