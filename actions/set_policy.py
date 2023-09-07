from lib import action


class VaultPolicySetAction(action.VaultBaseAction):
    def run(self, name, rules, profile_name=None):
        super().run(profile_name=profile_name)
        return (True, self.vault.sys.create_or_update_policy(name, rules))
