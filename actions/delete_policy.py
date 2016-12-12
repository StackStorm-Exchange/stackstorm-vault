from lib import action


class VaultPolicyDeleteAction(action.VaultBaseAction):
    def run(self, name):
        return self.vault.delete_policy(name)

