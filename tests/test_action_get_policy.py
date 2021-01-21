from st2tests.base import BaseActionTestCase

from get_policy import VaultGetPolicyAction
from .fixtures.config import dummy_config

class GetPolicyActionTestCase(BaseActionTestCase):
    action_cls = VaultGetPolicyAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run()
