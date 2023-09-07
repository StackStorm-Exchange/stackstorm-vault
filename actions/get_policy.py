from lib import action


class VaultGetPolicyAction(action.VaultBaseAction):
    def run(self, name, profile_name=None):
        super().run(profile_name=profile_name)
        return (True, self.vault.get_policy(name))
