from st2tests.base import BaseActionTestCase

from is_initialized import VaultIsInitializedAction
from .fixtures.config import dummy_config


class IsInitializedActionTestCase(BaseActionTestCase):
    action_cls = VaultIsInitializedAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run()
