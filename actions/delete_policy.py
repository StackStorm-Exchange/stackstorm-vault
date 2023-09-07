from lib import action


class VaultPolicyDeleteAction(action.VaultBaseAction):
    def run(self, name, profile_name=None):
        super().run(profile_name=profile_name)
        return (True, self.vault.sys.delete_policy(name))
