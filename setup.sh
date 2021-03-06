#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
	exit
fi

echo "Installing SHOOB AI. Please respond to input when it shows."
echo "TIP: When there is a value in brackets like [default_value], hit Enter to use it."
echo ""
apt-get update
pip install pyfiglet
echo ""
echo "-- Installing SCONS --"
echo ""
apt-get install build-essential python-dev git scons swig -y
cd ./rpi_ws281x
scons
cd ./python
python setup.py install
cd ..
cd ..
echo ""
echo "-- Installing PulseAudio --"
echo ""
sudo apt install pulseaudio pavucontrol -y
sudo apt remove pavumeter paman padevchooser -y
cd python-pulseaudio
python setup.py install
echo ""
echo "-- Configuring AlexaPi --"
echo ""
cd ..
cd AlexaPi/src/scripts
./setup.sh
echo ""
echo "-- Disabling audio kernel module --"
echo ""
cat <<EOF >/etc/modprobe.d/snd-blacklist.conf
blacklist snd_bcm2835
EOF
echo ""
echo "-- Running PA in system-wide mode --"
echo ""
mkdir -p /var/lib/AlexaPi/.config/pulse
cp /etc/pulse/client.conf /var/lib/AlexaPi/.config/pulse/
echo "autospawn=no" | sudo tee --append /var/lib/AlexaPi/.config/pulse/client.conf > /dev/null
adduser pulse audio
NAME_default="pi"
echo "Which is the username?"
read -r -p "Your username [${NAME_default}]: " NAME
if [ "${NAME}" == "" ]; then
    NAME=${NAME_default}
fi
adduser "${NAME}" pulse-access
adduser root pulse-access
cat <<EOF >/etc/systemd/system/pulseaudio.service
[Unit]
Description=PulseAudio Daemon

[Install]
WantedBy=multi-user.target

[Service]
Type=simple
PrivateTmp=true
ExecStart=/usr/bin/pulseaudio --system --realtime --disallow-exit --no-cpu-limit
EOF
systemctl enable pulseaudio.service
cd ..
sed -i '13s/.*/  input_device: "pulse"/' config.yaml
sed -i '22s/.*/  output: "pulse"/' config.yaml
sed -i '25s/.*/  output_device: ""/' config.yaml

echo ""
echo "-- SHOOB AI setup completed. Reboot now! --"
echo ""
