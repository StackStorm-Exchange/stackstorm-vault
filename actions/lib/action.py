import hvac
from st2common.runners.base_action import Action


class VaultBaseAction(Action):
    def __init__(self, config):
        super(VaultBaseAction, self).__init__(config)
        self.vault = self._get_client()

    def _get_client(self):
        url = self.config["url"]
        token = self.config["token"]
        verify = self._get_verify()

        client = hvac.Client(url=url, token=token, verify=verify)
        return client

    def _get_verify(self):
        verify = self.config["verify"]
        cert = self.config["cert"]
        if verify and cert:
            return cert
        return verify
