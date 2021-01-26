from st2tests.base import BaseActionTestCase

from delete import VaultDeleteAction
from tests.fixtures.config import dummy_config


class DeleteActionTestCase(BaseActionTestCase):
    action_cls = VaultDeleteAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run(path="")
