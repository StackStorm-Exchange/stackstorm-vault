from st2tests.base import BaseActionTestCase

from list_policies import VaultPolicyListAction
from tests.fixtures.config import dummy_config


class PolicyListActionTestCase(BaseActionTestCase):
    action_cls = VaultPolicyListAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run()
