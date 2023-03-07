import time
import wiringpi
import sys

def blink (_pin):
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


print("start")
pin=2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin,1)
i=0

while i>=0:
    i+=1
    blink(pin)
    print(i)