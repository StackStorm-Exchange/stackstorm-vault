from lib import action


class VaultCreateTokenAction(action.VaultBaseAction):
    """
    Request a child token to be created.  Useful for one time use
    or fixed time.
    """

    def run(
        self,
        display_name=None,
        entity_alias=None,
        explicit_max_ttl="1h",
        meta=None,
        mount_point="token",
        no_default_policy=False,
        no_parent=False,
        num_uses=None,
        period=None,
        policies=None,
        profile_name=None,
        renewable=True,
        role_name=None,
        token_id=None,
        token_type=None,
        ttl=None,
        wrap_ttl=None,
    ):
        super().run(profile_name=profile_name)
        return (
            True,
            self.vault.auth.token.create(
                display_name=display_name,
                entity_alias=entity_alias,
                explicit_max_ttl=explicit_max_ttl,
                id=token_id,
                meta=meta,
                mount_point=mount_point,
                no_default_policy=no_default_policy,
                no_parent=no_parent,
                num_uses=num_uses,
                period=period,
                policies=policies,
                renewable=renewable,
                role_name=role_name,
                ttl=ttl,
                type=token_type,
                wrap_ttl=wrap_ttl,
            ),
        )
