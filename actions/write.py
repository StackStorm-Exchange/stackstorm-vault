import json
from lib import action


class VaultWriteAction(action.VaultBaseAction):
    def run(self, path, values, profile_name=None):
        super().run(profile_name=profile_name)
        return (True, self.vault.write(path, **json.loads(values)))
