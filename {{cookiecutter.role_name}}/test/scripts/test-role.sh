#!/bin/sh

# See https://github.com/travis-ci/travis-ci/issues/1066
# Fail if one of the commands of this script fails
set -e

ansible-lint .
kitchen diagnose --all
# Uncomment the --concurrency flag to run multiple tests in parallel
kitchen test #--concurrency

set +e
