from lib import action


class VaultReadKVAction(action.VaultBaseAction):
    def run(self, path, kv_version, mount_point, version, profile_name=None):
        super().run(profile_name=profile_name)

        value = None

        if kv_version == 1:
            value = self.vault.secrets.kv.v1.read_secret(path=path, mount_point=mount_point)
        elif kv_version == 2:
            value = self.vault.secrets.kv.v2.read_secret_version(
                path=path, mount_point=mount_point, version=version
            )
        else:
            return (False, f"Unsupported kv version {kv_version}.")

        if value:
            return (True, value)

        return (False, f"Secret was not found at mount: {mount_point}, path: {path}")
