from st2tests.base import BaseActionTestCase

from set_policy import VaultPolicySetAction

class PolicySetActionTestCase(BaseActionTestCase):
    action_cls = VaultPolicySetAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
