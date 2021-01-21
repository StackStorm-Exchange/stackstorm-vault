from st2tests.base import BaseActionTestCase

from create_token import VaultCreateTokenAction
from .fixtures.config import dummy_config

class CreateTokenActionTestCase(BaseActionTestCase):
    action_cls = VaultCreateTokenAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run()
