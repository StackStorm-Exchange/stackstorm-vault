#!/bin/bash
set -eux

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
HVAC_DIR="${ROOT_DIR}/.hvac"

# main = the release branch; devel = the active development branch
git clone -b main git://github.com/hvac/hvac.git "${HVAC_DIR}"

# These scripts "install" the binaries in ${HOME}/.local/bin by default.
${HVAC_DIR}/tests/scripts/install-consul.sh
${HVAC_DIR}/tests/scripts/install-vault.sh

# using symlinks allows us to import tests.utils.* without adding the rest of the hvac tests.
# tests.utils also uses config_files, so make that available
for x in utils config_files; do
    rm -f ${ROOT_DIR}/tests/${x}
    # relative (-r) allows the symlink to work in vagrant
    ln -rs ${HVAC_DIR}/tests/${x} ${ROOT_DIR}/tests/${x}
done
