NAME_default="pi"
echo "Which is the username?"
read -r -p "Your username [${NAME_default}]: " NAME
if [ "${NAME}" == "" ]; then
    NAME=${NAME_default}
fi
adduser "${NAME}" pulse-access
