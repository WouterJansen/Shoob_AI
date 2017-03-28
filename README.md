# SHOOB AI
A developing virtual assistant for your home to run on a Raspberry PI. 

## Setup
* clone this git in your preferred location ```git clone --recursive https://github.com/WouterJansen/Shoob_AI.git```
* run the setup inside Shoob_AI folder ```sudo ./setup.sh``` and follow any promts it might give.
* reboot
* Set your audio device correctly in ```NeoPixel.py``` on line 9. In this example we use an audio USB device but yours can differ. To find out what the name is of yours you can run ```pactl list short sinks```
* Run ```ShoobAI.py``` as ```sudo python ShoobAI.py``` to test if all works. It will print out any problems found.

## Requirements
* Raspberry PI running Raspbian
* a 12 LED Neopixel ring connected as in the picture below:
  ![raspberry-pi-neopixel]
  
  
## Notes
* The setup script will blacklist your Broadcom audio kernel module to make sure the NeoPixel works correctly.
* The setup script will add a new service pulseaudio.service to start PulseAudio at boot. 
* Everything is ran as root to work correctly.
* 


## References
* Using PulseAudio in Python: http://freshfoo.com/posts/pulseaudio_monitoring/
* Using NeoPixel on Raspberry Pi: https://learn.adafruit.com/neopixels-on-raspberry-pi/overview & https://raspberrytips.nl/neopixel-ws2811-raspberry-pi/
* see https://github.com/alexa-pi/AlexaPi for most troubleshooting and guides for Alexa itself.  
  
  [raspberry-pi-neopixel]: https://cdn.raspberrytips.nl/wp-content/uploads/2016/05/neopixel-raspberry-pi-led-ws281x-600x292.png "from  :https://raspberrytips.nl/neopixel-ws2811-raspberry-pi/"



