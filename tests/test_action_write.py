from st2tests.base import BaseActionTestCase

from write import VaultWriteAction
from tests.fixtures.config import dummy_config


class WriteActionTestCase(BaseActionTestCase):
    action_cls = VaultWriteAction

    def test_method(self):
        action = self.get_action_instance(config=dummy_config)
        result = action.run(
            path="",
            values="",
        )
