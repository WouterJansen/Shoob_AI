import time
from pyfiglet import Figlet
import NeoPixel


def initialSetup():
    f = Figlet(font='small')
    print f.renderText('           SHOOB AI')
    print " " * 18 + "Virtual Assistant v1.0"
    print " " * 14 + "github.com/WouterJansen/Shoob_AI"
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
    setupNeoThread = NeoPixel.SetupGreen()
    setupNeoThread.daemon = True
    setupNeoThread.start()
    time.sleep(100)
    setupNeoThread.done = True


if __name__ == '__main__':
    main()
