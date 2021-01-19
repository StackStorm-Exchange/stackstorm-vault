from st2tests.base import BaseActionTestCase

from set_policy import VaultSetPolicyAction

class SetPolicyActionTestCase(BaseActionTestCase):
    action_cls = VaultSetPolicyAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
