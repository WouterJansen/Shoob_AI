import sys
import threading
import time
from pyfiglet import Figlet
from datetime import datetime
from Queue import Queue
from ctypes import POINTER, c_ubyte, c_void_p, c_ulong, cast

import thread
from neopixel import *
from pulseaudio.lib_pulseaudio import *

SINK_NAME = 'alsa_output.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00-Device.analog-stereo'
METER_RATE = 344
MAX_SAMPLE_VALUE = 127
DISPLAY_SCALE = 2
MAX_SPACES = MAX_SAMPLE_VALUE >> DISPLAY_SCALE
LED_COUNT = 12
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255
LED_INVERT = False

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
setupDone = False
listen = False


def fadeIn(color):
    strip.setBrightness(0)
    strip.show()
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    for j in range(255):
        strip.setBrightness(j)
        strip.show()
        time.sleep(2 / 1000.0)


def fadeOut(color):
    strip.setBrightness(255)
    strip.show()
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    for j in range(255, -1, -1):
        strip.setBrightness(j)
        strip.show()
        time.sleep(2 / 1000.0)


def errorRed():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 255, 0))
    strip.show()


def setupGreen():
    global setupDone
    while not setupDone:
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, Color(255, 0, 0))
            strip.show()
            time.sleep(50 / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def rotateBlue():
    for i in range(0, 11, 1):
        strip.setPixelColor(i, Color(0, 0, 255))
        if i + 1 > 11:
            strip.setPixelColor(i + 1 - 12, Color(0, 0, 160))
        else:
            strip.setPixelColor(i + 1, Color(0, 0, 160))
        if i + 2 > 11:
            strip.setPixelColor(i + 2 - 12, Color(0, 0, 100))
        else:
            strip.setPixelColor(i + 2, Color(0, 0, 100))
        if i + 3 > 11:
            strip.setPixelColor(i + 3 - 12, Color(0, 0, 50))
        else:
            strip.setPixelColor(i + 3, Color(0, 0, 50))
        if i + 4 > 11:
            strip.setPixelColor(i + 4 - 12, Color(0, 0, 100))
        else:
            strip.setPixelColor(i + 4, Color(0, 0, 100))
        if i + 5 > 11:
            strip.setPixelColor(i + 5 - 12, Color(0, 0, 160))
        else:
            strip.setPixelColor(i + 5, Color(0, 0, 160))
        if i + 6 > 11:
            strip.setPixelColor(i + 6 - 12, Color(0, 0, 255))
        else:
            strip.setPixelColor(i + 6, Color(0, 0, 255))
        if i + 7 > 11:
            strip.setPixelColor(i + 7 - 12, Color(0, 0, 160))
        else:
            strip.setPixelColor(i + 7, Color(0, 0, 160))
        if i + 8 > 11:
            strip.setPixelColor(i + 8 - 12, Color(0, 0, 100))
        else:
            strip.setPixelColor(i + 8, Color(0, 0, 100))
        if i + 9 > 11:
            strip.setPixelColor(i + 9 - 12, Color(0, 0, 50))
        else:
            strip.setPixelColor(i + 9, Color(0, 0, 50))
        if i + 10 > 11:
            strip.setPixelColor(i + 10 - 12, Color(0, 0, 100))
        else:
            strip.setPixelColor(i + 10, Color(0, 0, 100))
        if i + 11 > 11:
            strip.setPixelColor(i + 11 - 12, Color(0, 0, 160))
        else:
            strip.setPixelColor(i + 11, Color(0, 0, 160))
        strip.show()
        time.sleep(0.2)


class PeakMonitor(object):
    def __init__(self, sink_name, rate):
        print "STARTING PULSEAUDIO"
        self.sink_name = sink_name
        self.rate = rate

        self._context_notify_cb = pa_context_notify_cb_t(self.context_notify_cb)
        self._sink_info_cb = pa_sink_info_cb_t(self.sink_info_cb)
        self._stream_read_cb = pa_stream_request_cb_t(self.stream_read_cb)

        self._samples = Queue()

        _mainloop = pa_threaded_mainloop_new()
        _mainloop_api = pa_threaded_mainloop_get_api(_mainloop)
        context = pa_context_new(_mainloop_api, 'peak_demo')
        pa_context_set_state_callback(context, self._context_notify_cb, None)
        pa_context_connect(context, None, 0, None)
        pa_threaded_mainloop_start(_mainloop)

    def __iter__(self):
        while True:
            yield self._samples.get()

    def context_notify_cb(self, context, _):
        state = pa_context_get_state(context)
        if state == PA_CONTEXT_READY:
            print "Pulseaudio connection ready..."
            o = pa_context_get_sink_info_list(context, self._sink_info_cb, None)
            pa_operation_unref(o)

        elif state == PA_CONTEXT_FAILED:
            global setupDone
            setupDone = True
            errorRed()
            print "Connection PulseAudio failed"
            time.sleep(3)
            sys.exit()

        elif state == PA_CONTEXT_TERMINATED:
            errorRed()
            print "Connection PulseAudio terminated"
            time.sleep(3)
            sys.exit()

    def sink_info_cb(self, context, sink_info_p, _, __):
        if not sink_info_p:
            return

        sink_info = sink_info_p.contents
        print 'index:', sink_info.index
        print 'name:', sink_info.name
        print 'description:', sink_info.description

        if sink_info.name == self.sink_name:
            print 'setting up peak recording using', sink_info.monitor_source_name

            print '-' * 60
            samplespec = pa_sample_spec()
            samplespec.channels = 1
            samplespec.format = PA_SAMPLE_U8
            samplespec.rate = self.rate

            pa_stream = pa_stream_new(context, "peak detect demo", samplespec, None)
            pa_stream_set_read_callback(pa_stream,
                                        self._stream_read_cb,
                                        sink_info.index)
            pa_stream_connect_record(pa_stream,
                                     sink_info.monitor_source_name,
                                     None,
                                     PA_STREAM_PEAK_DETECT)

    def stream_read_cb(self, stream, length, index_incr):
        data = c_void_p()
        pa_stream_peek(stream, data, c_ulong(length))
        data = cast(data, POINTER(c_ubyte))
        for i in xrange(length):
            self._samples.put(data[i])
        pa_stream_drop(stream)


def setupNeoPixel():
    print "STARTING NEOPIXEL"
    strip.begin()
    print "Neopixel started..."
    print '-' * 60


def endSetup():
    print "SETUP COMPLETE"
    print '-' * 60
    global setupDone
    setupDone = True
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.setBrightness(255)
    strip.show()
    time.sleep(2)


def setupPulseAudio():
    try:
        monitor = PeakMonitor(SINK_NAME, METER_RATE)
        return monitor
    except:
        global setupDone
        setupDone = True
        errorRed()
        time.sleep(3)
        sys.exit()


class AudioReact(threading.Thread):
    def __init__(self, monitor):
        threading.Thread.__init__(self)
        self.monitor = monitor

    def run(self):
        print datetime.now().strftime('%H:%M:%S') + "- NEOPIXEL - listening and reacting"
        global listen
        fadeIn(Color(0, 0, 255))
        for sample in self.monitor:
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, Color(0, 0, (sample - 128) * 2))
            strip.show()
            if not listen:
                fadeOut(Color(0, 0, 255))
                print datetime.now().strftime('%H:%M:%S') + "- NEOPIXEL - stopped listening"
                return


def initialSetup():
    f = Figlet(font='slant')
    print f.renderText('SHOOB AI')
    print "Shoob Virtual Assistant 1.0"
    print '-' * 60
    thread.start_new_thread(setupGreen, ())


def main():
    initialSetup()
    setupNeoPixel()
    monitor = setupPulseAudio()
    time.sleep(3)
    endSetup()
    fadeIn(Color(0, 0, 255))
    audioReactThread = AudioReact(monitor)
    audioReactThread.daemon = True
    global listen
    listen = True
    audioReactThread.start()
    time.sleep(5)
    listen = False
    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
