from st2tests.base import BaseActionTestCase

from set_policy import VaultPolicySetAction
from tests.fixtures.config import dummy_config


class PolicySetActionTestCase(BaseActionTestCase):
    action_cls = VaultPolicySetAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run(
            name="",
            rules="",
        )
