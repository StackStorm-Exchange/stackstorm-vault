# Change Log

## 1.1.0

- Added `kuberentes` auth method.

## 1.0.0

* Drop Python 2.7 support

## 0.6.0

WARNING: This is the last version that "supports" python2.7.
The next version will be 1.0.0 and "2" will be dropped from python_versions.

- Add ability to authenticate with approle instead of with token.
- Drop testing with python2.7 due to broken infrastructure.
- Add unit tests for all actions.
- Update minimum required version of hvac to 0.10.6.
- Migrate from deprecated hvac methods to their replacements.

## 0.5.2

- Pass certificate correctly to hvac

## 0.5.1

- Version bump to fix tagging issues

## 0.5.0

- Added action `read_kv` to read key-value secrets.

## 0.4.0

- Updated action `runner_type` from `run-python` to `python-script`

## 0.2.0

- Rename `config.yaml` to `config.schema.yaml` and update to use schema.

## 0.1.0

- First release 
