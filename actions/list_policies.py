from lib import action


class VaultPolicyListAction(action.VaultBaseAction):
    def run(self):
        return self.vault.list_policies()
