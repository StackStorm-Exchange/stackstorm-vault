import secrets
import string
import logging
import json

from lib import action

import hvac

LOG = logging.getLogger(__name__)

string.alphanumeric = f"{string.ascii_letters}{string.digits}"


def generate_secret(string_set="ascii_letters", length=8):
    """
    Return a random string.
    """
    if not 0 < length < 256:
        raise ValueError("Secret length must be between 1 and 255 characters.")
    if string_set not in [
        "ascii_letters",
        "ascii_lowercase",
        "ascii_uppercase",
        "digits",
        "punctuation",
        "printable",
        "alphanumeric",
    ]:
        raise ValueError(f"'{string_set}' is not a supported string set.")
    return "".join([secrets.choice(list(getattr(string, string_set))) for _ in range(length)])


def read_secret(client, mount_point, path):
    """
    Read secret from Vault.
    """
    try:
        tmp = client.secrets.kv.v1.read_secret(path=path, mount_point=mount_point)
        res = tmp.get("data", {})
    except hvac.exceptions.InvalidPath:
        res = {}
    return res


def write_secret(client, mount_point, path, payload):
    """
    Write the key_name secret to vault.
    """
    return client.secrets.kv.v1.create_or_update_secret(
        path, secret=payload, mount_point=mount_point
    )


class VaultGenerateSecretAction(action.VaultBaseAction):
    """
    Generate a secert and write it to a secret path.

    mount_point :string: the mount point for the kv store.
    path :string: the path to the secret.
    key_name :string: the name of the key to generated
    eng_ver :string: the kv store version (only v1 is currently supported)
    string_set :string: the character set to use in the secret generation.
    secret_length :integer: the number of characters to create in the secret.
    update_tactic :string: the logic to use when generating a secret.

    Return :tuple: [0] execution success [1] query result
    """

    def run(
        self,
        mount_point,
        path,
        key_name,
        update_tactic="refrain",
        profile_name=None,
        secret=None,
        decode_json=False,
        string_set=None,
        secret_length=None,
    ):
        super().run(profile_name=profile_name)

        if string_set and secret_length:
            secret = generate_secret(string_set, secret_length)

        if secret is None:
            raise ValueError(
                "No secret to write!  Either provide a secret or the string_set and"
                " secret_length parameters to generate a secret."
            )

        if update_tactic not in ["refrain", "overwrite"]:
            raise ValueError(f"Unknown update tactic '{update_tactic}'")

        current_secret = read_secret(self.vault, mount_point, path)
        if update_tactic == "refrain" and key_name in current_secret.keys():
            allow_overwrite = False
            msg = f"Refrain from updating existing secret {mount_point}/{path}"
        else:
            allow_overwrite = True

        if allow_overwrite:
            if decode_json:
                secret = json.loads(secret)
            current_secret.update({key_name: secret})
            write_result = write_secret(self.vault, mount_point, path, current_secret)
            if write_result.ok:
                msg = f"Wrote secret {key_name} to {mount_point}/{path}"
            else:
                allow_overwrite = write_result.ok
                msg = write_result.reason

        return (True, {"updated": allow_overwrite, "message": msg})
