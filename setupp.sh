#!/bin/bash

set -o nounset # Fail when variable is used, but not initialized
set -o errexit # Fail on unhandled error exits
popd > /dev/null
OS_default="pi"
echo "Which username are you using?"
read -r -p "Your username [${OS_default}]: " OS
if [ "${OS}" == "" ]; then
    OS=${OS_default}
fi
adduser "${OS}" pulse-access
