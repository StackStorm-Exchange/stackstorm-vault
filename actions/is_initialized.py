from lib import action


class VaultIsInitializedAction(action.VaultBaseAction):
    def run(self):
        return self.vault.sys.is_initialized()
