from lib import action


class VaultReadAction(action.VaultBaseAction):
    def run(self, path, profile_name=None):
        super().run(profile_name=profile_name)
        value = self.vault.read(path)
        if value:
            return (True, value)

        return (False, f"Key was not found in path {path}")
