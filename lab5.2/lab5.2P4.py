import wiringpi
import sys
import time

wiringpi.wiringPiSetup()
pinLed= 3
pinSwitch= 2
_pin=3
wiringpi.pinMode(pinLed,1)
wiringpi.pinMode(pinSwitch,0)

while True:
    if(wiringpi.digitalRead(pinSwitch)==0):
        print("No SOS needed")
        time.sleep(.3)
        wiringpi.digitalWrite(pinLed, 0)
    else:
        print("short")
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(.5)
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(.5)
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(.5)
        print("long")
        #long
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(1.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(1.5)
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(1.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(1.5)
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(1.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(1.5)

        #short
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(.5)
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(.5)
        wiringpi.digitalWrite(_pin, 1)
        time.sleep(.5)
        wiringpi.digitalWrite(_pin, 0)
        time.sleep(.5)