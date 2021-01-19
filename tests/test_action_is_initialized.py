from st2tests.base import BaseActionTestCase

from is_initialized import VaultIsInitializedAction

class IsInitializedActionTestCase(BaseActionTestCase):
    action_cls = VaultIsInitializedAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
