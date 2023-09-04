from lib import action


class VaultDeleteAction(action.VaultBaseAction):
    """
    Delete a v1 path.
    """
    def run(self, path, profile_name=None):
        super().run(profile_name=profile_name)
        return (True, self.vault.delete(path))
