#!/bin/bash
echo "Installing all necessary tools for SHOOB AI"
apt-get update
apt-get install build-essential python-dev git scons swig -y
cd ./rpi_ws281x
scons
cd ./python
python setup.py install
cd ..
cd..
sudo apt install pulseaudio pavucontrol -y
sudo apt remove pavumeter paman padevchooser -y
cd python-pulseaudio
python setup.py install
