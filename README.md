# SHOOB AI
A developing virtual assistant for your home to run on a Raspberry PI. The goal of this project is to implement several new modules to the
Amazon Alexa system by having a Neopixel LED ring react to the sound and implement several custom modules to support Google Cast, home automation and others.

# What can be found in this Git?
This git has the entire project. 

# Requirements
* Raspberry PI running Raspbian
* PulseAudio (add ```sudo pulseaudio --daemonize=no --system --realtime``` to your startup scripts for it to work)
* a Neopixel ring connected as in the picture below and the following setup followed:
  * ```sudo apt-get install build-essential python-dev git scons swig```
  [raspberry-pi-neopixel]
  from: https://raspberrytips.nl/neopixel-ws2811-raspberry-pi/
  [raspberry-pi-neopixel]: https://cdn.raspberrytips.nl/wp-content/uploads/2016/05/neopixel-raspberry-pi-led-ws281x-600x292.png "from :https://raspberrytips.nl/neopixel-ws2811-raspberry-pi/"



