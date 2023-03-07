import wiringpi
import sys
import time

wiringpi.wiringPiSetup()
pinLed= 3
pinRelay = 4
pinSwitch= 2
wiringpi.pinMode(pinLed,1)
wiringpi.pinMode(pinSwitch,0)
while True:
    if(wiringpi.digitalRead(pinSwitch)==0):
        print("LED not flashing")
        time.sleep(.3)
        wiringpi.digitalWrite(pinLed, 0)
        wiringpi.digitalWrite(pinRelay, 0)
    else:
        print("LED blinks")
        time.sleep(.3)
        wiringpi.digitalWrite(pinLed, 1)
        wiringpi.digitalWrite(pinRelay, 1)
        time.sleep(.3)
        wiringpi.digitalWrite(pinLed, 0)
        wiringpi.digitalWrite(pinRelay, 0)