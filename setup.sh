#!/bin/bash
echo "Installing all necessary tools for SHOOB AI"
apt-get install build-essential python-dev git scons swig
cd ./rpi_ws281x
scons
cd ./python
python setup.py install
cd ..
cd..
sudo apt install pulseaudio pavucontrol
sudo apt remove pavumeter paman padevchooser
cd python-pulseaudio
python setup.py install
