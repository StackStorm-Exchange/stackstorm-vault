# Vault Integration Pack

This pack is for Hashicorp Vault integrations

## Configuration

Copy the example configuration in [vault.yaml.example](./vault.yaml.example)
to `/opt/stackstorm/configs/vault.yaml` and edit as required.

It should contain:

* `url` - URL for the Vault server
* `cert` - Path to client-side certificate
* `verify` - Whether to verify the SSL certificate or not
* `auth_method` - Which authentication method to use.
  Only `token` (the default), `approle` and `kubernetes` are implemented so far.

Also include the relevant auth_method-specific config:

* `token` - Authentication token for `auth_method=token`. If not specified,
  also tries using the `VAULT_TOKEN` env var or the `~/.vault-token` file.
* `role_id` - Authentication role_id for `auth_method=approle`.
* `secret_id` - Authentication secret_id for `auth_method=approle`.
* `role` - Authentication role for `auth_method=kubernetes`

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

* `delete` - Delete value from Vault server
* `get_policy` - Read policy from Vault server
* `is_initialized` - Read initialization status from Vault server
* `list_policies` - List policies from Vault server
* `read` - Read value from Vault server
* `write` - Write key/value to Vault server
* `read_kv` - Read key-value secrets from Vault server
