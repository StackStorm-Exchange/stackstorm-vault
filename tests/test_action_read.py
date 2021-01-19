from st2tests.base import BaseActionTestCase

from read import VaultReadAction

class ReadActionTestCase(BaseActionTestCase):
    action_cls = VaultReadAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
