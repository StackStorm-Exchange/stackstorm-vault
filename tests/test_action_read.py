from st2tests.base import BaseActionTestCase

from read import VaultReadAction
from tests.fixtures.config import dummy_config


class ReadActionTestCase(BaseActionTestCase):
    action_cls = VaultReadAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run(path="")
