from lib import action


class VaultReadKVAction(action.VaultBaseAction):
    def run(self, path, kv_version, mount_point, version):
        value = None

        if kv_version == 1:
            value = self.vault.kv.v1.read_secret(path=path, mount_point=mount_point)
        elif kv_version == 2:
            value = self.vault.kv.v2.read_secret_version(path=path, mount_point=mount_point,
                                                         version=version)

        if value:
            return value['data']
        else:
            raise KeyError("Key was not found in Vault")
