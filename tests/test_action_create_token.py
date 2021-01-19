from st2tests.base import BaseActionTestCase

from create_token import VaultCreateTokenAction

class CreateTokenActionTestCase(BaseActionTestCase):
    action_cls = VaultCreateTokenAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
