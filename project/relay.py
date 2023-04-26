import time
import wiringpi
import sys

wiringpi.wiringPiSetup()

pinRelay = 3

wiringpi.pinMode(pinRelay,1)
while True:
    wiringpi.digitalWrite(pinRelay, 0)
    time.sleep(1)
    wiringpi.digitalWrite(pinRelay, 1)
    time.sleep(1)
