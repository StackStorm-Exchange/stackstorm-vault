from st2tests.base import BaseActionTestCase

from list_policies import VaultPolicyListAction

class PolicyListActionTestCase(BaseActionTestCase):
    action_cls = VaultPolicyListAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
