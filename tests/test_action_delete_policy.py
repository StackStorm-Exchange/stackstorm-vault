from st2tests.base import BaseActionTestCase

from delete_policy import VaultPolicyDeleteAction

class PolicyDeleteActionTestCase(BaseActionTestCase):
    action_cls = VaultPolicyDeleteAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
