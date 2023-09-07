from lib import action


class VaultIsInitializedAction(action.VaultBaseAction):
    def run(self, profile_name=None):
        super().run(profile_name=profile_name)
        return (True, self.vault.sys.is_initialized())
