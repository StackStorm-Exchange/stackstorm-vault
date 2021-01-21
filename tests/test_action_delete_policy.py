from st2tests.base import BaseActionTestCase

from delete_policy import VaultPolicyDeleteAction
from .fixtures.config import dummy_config


class PolicyDeleteActionTestCase(BaseActionTestCase):
    action_cls = VaultPolicyDeleteAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run(name="")
