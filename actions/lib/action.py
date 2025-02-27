import hvac
from st2common.runners.base_action import Action


class VaultBaseAction(Action):
    """
    Base Action includes st2 profile and vault client functions
    for child classes.
    """

    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.vault = None

    def run(self, profile_name=None):
        """
        The base action selects the profile and initialises the vault client.
        """
        if profile_name is None:
            profile_name = self.config.get("default_profile")
            if profile_name is None:
                raise ValueError(
                    "No default profile found, check the pack configuration."
                )

        for profile in self.config.get("profiles", []):
            if profile_name == profile["name"]:
                self._configure_client(profile)
                break
        else:
            raise ValueError(
                f"Profile '{profile_name}' doesn't exist, check the pack configuration."
            )

    def _configure_client(self, profile):
        """
        Set-up of the Vault client from the pack configuration.
        """
        auth_methods = {"token": self._auth_token, "approle": self._auth_approle}

        client_kwargs = {"url": profile["url"]}

        # Server TLS validation
        if profile.get("ca_cert_path"):
            client_kwargs["verify"] = profile["ca_cert_path"]
        else:
            client_kwargs["verify"] = profile.get("verify", False)

        # Client certificate (HVAC expects a cert/key tuple)
        cert = (profile.get("client_cert_path"), profile.get("client_key_path"))
        # Both the key and certificate must be provided.
        if bool(cert[0]) ^ bool(cert[1]):
            raise ValueError(
                "Client-side TLS requires the client's certificate and key but one was provided."
            )
        # Use the key/cert tuple with HVAC if they are both defined.
        if cert[0] and cert[1]:
            client_kwargs["cert"] = cert

        self.vault = hvac.Client(**client_kwargs)
        auth_method = profile.get("auth_method")
        if auth_method not in auth_methods:
            raise ValueError(f"Auth method '{auth_method}' is not supported.")

        # Authenticate the client connection.
        auth_methods[auth_method](profile)

        if self.vault.token is None:
            raise ValueError(
                "Failed to set a valid token for the client, check the pack configuration."
            )

    def _auth_token(self, profile):
        """
        A vault token provided directly in the pack configuration
        """
        self.vault.token = profile.get("token")

    def _auth_approle(self, profile):
        """
        Authenticate using a vault app role to acquire the vault token.
        """
        # Check if mount_point is provided in the profile
        mount_point = profile.get("mount_point")

        # Prepare login arguments
        login_kwargs = {
            "role_id": profile["role_id"],
            "secret_id": profile["secret_id"],
        }

        # Add mount_point to kwargs if it exists in the profile
        if mount_point:
            login_kwargs["mount_point"] = mount_point

        # Replace the direct login call with kwargs-based call
        self.vault.auth.approle.login(**login_kwargs)
