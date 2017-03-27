#!/bin/bash
echo "Installing SHOOB AI dependencies"
echo ""
apt-get update
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
echo "-- Disabling audio kernel module --"
echo ""
cat <<EOF >/etc/modprobe.d/snd-blacklist.conf
blacklist snd_bcm2835
EOF
