from lib import action


class VaultPolicySetAction(action.VaultBaseAction):
    def run(self, name, rules):
        return self.vault.set_policy(name, rules)
