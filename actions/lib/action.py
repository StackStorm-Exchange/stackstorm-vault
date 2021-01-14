import hvac
from st2common.runners.base_action import Action


class VaultBaseAction(Action):

    def __init__(self, config):
        super(VaultBaseAction, self).__init__(config)
        self.vault = self._get_client()

    def _get_client(self):
        url = self.config['url']
        verify = self._get_verify()

        auth_method = self.config.get("auth_method", "token")
        token = self.config["token"]

        # token is passed during client init to allow client to also
        # get the token from VAULT_TOKEN env var or ~/.vault-token
        client = hvac.Client(url=url, token=token, verify=verify)

        # token is handled during client init
        # other auth methods will override it as needed
        if auth_method == "token":
            pass

        # where implemented prefer: client.auth.<method>.login
        # as many client.auth_* methods are deprecated.

        elif auth_method == "approle":
            client.auth.approle.login(
                role_id=self.config["role_id"],
                secret_id=self.config["secret_id"],
            )

        return client

    def _get_verify(self):
        verify = self.config['verify']
        cert = self.config['cert']
        if verify and cert:
            return cert
        return verify
