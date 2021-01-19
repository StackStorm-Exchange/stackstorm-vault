from st2tests.base import BaseActionTestCase

from delete_policy import VaultDeletePolicyAction

class DeletePolicyActionTestCase(BaseActionTestCase):
    action_cls = VaultDeletePolicyAction

    def test_method(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
