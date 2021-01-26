#!/bin/bash

# For python deps, please use requirements.txt or requirements-test.txt.
# Do not install python requirements with this script.

# Some packs need to install and configure additional packages to properly
# run their test suite. Other packs need to clone other repositories to
# reuse standardized testing infrastructure. And other functional or end-to-end
# tests might need additional system setup to access external APIs via
# an enterprise bus or something else.
# That is the purpose of this script. Setup the testing environment
# to do mock-less regression or end-to-end testing.

# This script is called by `deployment` housed in StackStorm-exchange/ci.
# `deployment` will only run this script if it is executable.
ROOT_DIR="${ROOT_DIR:-$(pwd)}"
HVAC_DIR="${ROOT_DIR}/hvac"
HVAC_VAULT_VERSION="${HVAC_VAULT_VERSION:-STABLE}"
HVAC_VAULT_LICENSE="${HVAC_VAULT_LICENSE:-OSS}"

# master = the release branch; devel = the active development branch
git clone -b master git://github.com/hvac/hvac.git "${HVAC_DIR}"

# This script needs to work both in CI, and for local testing.
# These scripts "install" the binaries in ${HOME}/bin by default, which is
# only ok in CI. To avoid passing in CONSUL_VERSION (as $1), we specify install
# dir with $HOME instead of CONSUL_DIR (as $2).
HOME=${HVAC_DIR} ${HVAC_DIR}/tests/scripts/install-consul.sh
${HVAC_DIR}/tests/scripts/install-vault.sh ${HVAC_VAULT_VERSION} ${HVAC_VAULT_LICENSE} ${HVAC_DIR}/bin

# hvac uses tox+nosetests to run tests
# using a symlink allows us to import tests.utils.* without adding the rest of the hvac tests.
rm -f ${ROOT_DIR}/tests/utils
ln -s ${HVAC_DIR}/tests/utils ${ROOT_DIR}/tests/utils
