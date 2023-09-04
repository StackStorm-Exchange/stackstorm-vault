from lib import action


class VaultPolicyListAction(action.VaultBaseAction):
    def run(self, profile_name=None):
        super().run(profile_name=profile_name)
        return (True, {"policies": self.vault.sys.list_policies()})
