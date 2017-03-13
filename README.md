# SHOOB AI
A developing virtual assistant for your home to run on a Raspberry PI. The goal of this project is to implement several new modules to the
Amazon Alexa system by having a Neopixel LED ring react to the sound and implement several custom modules to support Google Cast, home automation and others.

# Setup
* clone this git in your preferred location ```git clone https://github.com/WouterJansen/Shoob_AI.git```
* ```sudo apt-get install build-essential python-dev git scons swig```
* Go to ```rpi_ws281x/python``` and run ```sudo python setup.py install```
* Install PulseAudio ```sudo apt-get install pulseaudio```
* Go to ```python-pulseaudio``` and run ```sudo python setup.py install```
* Make sure PulseAudio starts on launch as follows ```sudo pulseaudio --daemonize=no --system --realtime``` (for example with ``` sudo crontab -e```

# Requirements
* Raspberry PI running Raspbian
* a 12 LED Neopixel ring connected as in the picture below:
  ![raspberry-pi-neopixel]
  
  
  
  
  
  
  
  
  
  
  
  [raspberry-pi-neopixel]: https://cdn.raspberrytips.nl/wp-content/uploads/2016/05/neopixel-raspberry-pi-led-ws281x-600x292.png "from  :https://raspberrytips.nl/neopixel-ws2811-raspberry-pi/"



