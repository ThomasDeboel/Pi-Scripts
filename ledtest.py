import time
import wiringpi
import sys
def blink (_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(.5)
    wiringpi.digitalWrite(_pin, 0)
    time.sleep(.5)

#setup
print("start")
pin=2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin,1)

#main
for i in range(0,10):
    blink(pin)

print("done")