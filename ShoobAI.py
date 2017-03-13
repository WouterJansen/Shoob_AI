import time
from pyfiglet import Figlet
import NeoPixel


def initialSetup():
    f = Figlet(font='slant')
    print f.renderText('SHOOB AI')
    print "Shoob Virtual Assistant 1.0"
    print '-' * 60
    NeoPixel.setupNeoPixel()
    setupNeoThread = NeoPixel.SetupGreen()
    setupNeoThread.daemon = True
    setupNeoThread.start()
    time.sleep(5)
    print "SETUP COMPLETE"
    print '-' * 60
    setupNeoThread.done = True


def main():
    initialSetup()
    time.sleep(3)
    audioReactThread = NeoPixel.AudioReact()
    audioReactThread.daemon = True
    audioReactThread.listening = True
    audioReactThread.start()
    time.sleep(5)
    audioReactThread.listening = False
    time.sleep(5)


if __name__ == '__main__':
    main()
