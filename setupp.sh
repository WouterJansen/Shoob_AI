#!/bin/bash

set -o nounset # Fail when variable is used, but not initialized
set -o errexit # Fail on unhandled error exits

OS_default="pi"
echo "Which username are you using?"
read -r -p "Your username [${OS_default}]: " OS
if [ "${OS}" == "" ]; then
    OS=${OS_default}
elif [ ! -f "./inc/os/${OS}.sh" ]; then
    echo "Incorrect value. Exiting."
    exit
fi
adduser "${OS}" pulse-access
