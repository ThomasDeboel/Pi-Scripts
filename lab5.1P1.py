import wiringpi
import sys

def blink (_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(.5)
    wiringpi.digitalWrite(_pin, 0)
    time.sleep(.5)

print("start")
pin=2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin,1)

while i>=0:
    i+=1
    blink(pin)
    print(i)