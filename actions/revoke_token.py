from lib import action


class VaultRevokeTokenAction(action.VaultBaseAction):
    """
    Revoke a token and all child tokens.

    When the token is revoked, all dynamic secrets generated with it are also revoked.
    """

    def run(self, token, profile_name=None, mount_point="token"):
        super().run(profile_name=profile_name)

        return (
            True,
            self.vault.auth.token.revoke(
                token=token,
                mount_point=mount_point,
            ),
        )
