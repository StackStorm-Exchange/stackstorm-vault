from st2tests.base import BaseActionTestCase

from get_policy import VaultGetPolicyAction

class GetPolicyActionTestCase(BaseActionTestCase):
    action_cls = VaultGetPolicyAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
