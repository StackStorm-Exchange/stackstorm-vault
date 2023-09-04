# Vault Integration Pack
_StackStorm pack integration with HashiCorp Vault_

*Author:* steve.neuharth <steve.neuharth@target.com>

## Maintainers
Active pack maintainers with review & write repository access and expertise with vault:
* Jacob Floyd ([@cognifloyd](https://github.com/cognifloyd)) <cognifloyd@gmail.com> Copart
* Carlos ([@nzlosh](https://github.com/nzlosh))

### Contributors
- Andy Moore <andrew.moore@pearson.com>
- Jacob Floyd <cognifloyd@gmail.com>
- Carlos <nzlosh@yahoo.com>


## Configuration

The following options are required to be configured for the pack to work correctly.

| Option | Type | Required | Secret | Description |
|---|---|---|---|---|
| `default_profile` | string | True | default | _The default profile to use in an action when none is given._ |
| `profiles` | array | True | default | _Profiles definitions_ |
| - `name` | string | True | default | _Name of the profile._ |
| - `url` | string | True | False | _URL for the Vault server_ |
| - `verify` | boolean | False | default | _Verify the TLS certificate for HTTPS requests. Default false (this option is ignored if ca_cert_path is supplied)._ |
| - `ca_cert_path` | string | False | default | _CA Certificate path. Defaults to empty string. When path is provided, TLS certificates are verified._ |
| - `client_cert_path` | string | False | default | _Client side certificates for HTTPS request_ |
| - `client_key_path` | string | False | default | _Client private key for HTTPS request_ |
| - `auth_method` | string | False | default | _Authentication method_ |
| - `token` | string | False | True | _Authentication token (method=token)_ |
| - `role_id` | string | False | True | _Authentication approle role-id (method=approle)_ |
| - `secret_id` | string | False | True | _Authentication approle secret-id (method=approle)_ |


## Actions


The pack provides the following actions:

### delete
_Delete value from Vault server_
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `path` | string | True | default | _Path to delete from Vault_ |


### generate_secret
_Generate a secret and write it to vault._
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `mount_point` | string | False | default | _Vault moint point in the URL_ |
| `path` | string | True | default | _Path to the secrets_ |
| `key_name` | string | True | default | _Name of the key to write the secret._ |
| `update_tactic` | string | False | default | _The logic to use when writing secret to Vault.  See readme for details._ |
| `string_set` | string | default | default | _Unavailable_ |
| `secret_length` | integer | default | default | _The number of characters to use in the secret._ |


### read
_Read value from Vault server_
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `path` | string | True | default | _Key to read from Vault_ |


### create_token
_Create a new Token_
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `token_id` | string | False | default | _The ID of the client token.  By default, this is an auto-generated value._ |
| `role_name` | string | False | default | _The name of the token role._ |
| Items are of type |  ||||
| `policies` | array | False | default | _List of policy names to associate with this token._ |
| `meta` | string | False | default | _Metadata to associate with the token. This metadata will show in the audit log when the token is used._ |
| `no_parent` | boolean | False | default | _This argument only has effect if used by a root or sudo caller._ |
| `no_default_policy` | boolean | False | default | _Detach the 'default' policy from the policy set for this token._ |
| `renewable` | boolean | False | default | _True: Permit the token to be renewable up to the system/mount maximum TTL. False: Token can't be renewed past its initial TTL._ |
| `ttl` | string | False | default | _Initial TTL to associate with the token, provided as '1h', where hour is the largest suffix. (default unit: seconds)_ |
| `token_type` | string | False | default | _The token type. Can be 'batch' or 'service'. Defaults to the type specified by the role configuration named by role_name._ |
| `explicit_max_ttl` | string | False | default | _If set, the token will never be able to be renewed or used past the value set at issue time._ |
| `display_name` | string | False | default | _Name to associate with this token. This is a non-sensitive value that can be used to help identify created secrets (e.g. prefixes)._ |
| `num_uses` | string | False | default | _Number of times this token can be used. After the last use, the token is automatically revoked._ |
| `period` | string | False | default | _If specified, the token will be periodic; it will have no maximum TTL (unless an 'explicit-max-ttl' is also set) but every renewal will use the given period. Requires a root token or one with the sudo capability._ |
| `entity_alias` | string | default | default | _Name of the entity alias to associate with during token creation._ |
| `wrap_ttl` | string | False | default | _Specifies response wrapping token creation with duration. IE: '15s', '20m', '25h'._ |
| `mount_point` | string | False | default | _The 'path' the method/backend was mounted on._ |


### write
_Write a key/value to Vault_
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `path` | string | True | default | _Path to the Vault secrets_ |
| `values` | string | True | default | _Keys and values to write in Vault ({"key":"value", "key2": "value2"}_ |


### get_policy
_Read policy from Vault server_
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `name` | string | True | default | _Policy to read from Vault_ |


### delete_policy
_Delete policy from Vault server_
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `name` | string | True | default | _Policy to delete from Vault_ |


### read_kv
_Read a kv value from Vault server_
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `path` | string | True | default | _Key to read from Vault_ |
| `kv_version` | number | True | default | _The version of the KV store in vault.  Use 1 for legacy kv stores, 2 for newer kv stores_ |
| `mount_point` | string | True | default | _The mount point of the kv store_ |
| `version` | string | True | default | _The version of the kv *data*_ |


### set_policy
_Create a new Vault policy_
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `name` | string | True | default | _Name of new Vault Policy_ |
| `rules` | string | True | default | _Policy rules_ |


### list_policies
_List Policies from Vault server_
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |


### write_secret
_Write a secret to Vault._
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `mount_point` | string | False | default | _Vault moint point in the URL_ |
| `path` | string | True | default | _Path to the secrets_ |
| `key_name` | string | True | default | _Name of the key to write the secret._ |
| `secret` | string | True | True | _Secret contents to be written._ |
| `decode_json` | boolean | False | default | _Secret is formatted as a json and should be decode to be sent to Vault_ |
| `update_tactic` | string | False | default | _The logic to use when writing secret to Vault.  See readme for details._ |


### revoke_token
_Revoke a token and all its child tokens._
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |
| `token` | string | True | default | _Token to revoke._ |
| `mount_point` | string | False | default | _The 'path' the method/backend was mounted on._ |


### is_initialized
_Read initialization status from Vault server_
| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run this action._ |





### generate secret

This action is written to pre-populate keys with a random secret.

The following string sets are available

 - ascii_letters
   ```abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ```
 - ascii_lowercase
   ```abcdefghijklmnopqrstuvwxyz```
 - ascii_uppercase
   ```ABCDEFGHIJKLMNOPQRSTUVWXYZ```
 - digits
   ```0123456789```
 - punctuation
   ```!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~```
 - printable
   ```0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c```
 - alphanumeric
   ```abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789```

### Update tactic

The update tactic controls how the action will update existing secrets.  It's intended to ensure idempotence on multiple runs of the secret generation action.  The currently supported tactics are:
 - `overwrite`: Overwrite an existing secret.
 - `refrain`: Do not overwrite an existing secret.

## Sensors

There are no sensors available for this pack.


## Authentication methods

Authentication methods are defined per profile and are mutally exclusive.  Only configure the
method that should be used.

### Supported
 - approle
 - token

### Unsupported
 - app-id
 - ali-cloud
 - aws-iam  # aka aws
 - aws-ec2
 - azure
 - cert  # aka tls
 - gcp
 - github
 - jwt
 - kubernetes
 - ldap
 - mfa
 - oidc
 - okta
 - radius
 - userpass

<sub>Documentation generated using [pack2md](https://github.com/nzlosh/pack2md)</sub>