from st2tests.base import BaseActionTestCase

from list_policies import VaultListPoliciesAction

class ListPoliciesActionTestCase(BaseActionTestCase):
    action_cls = VaultListPoliciesAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
