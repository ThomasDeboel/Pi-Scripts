import time
import wiringpi
import sys
    

print("start")
pinSwitch = 2
pin=3
pin_2=4
pin_3=6
pin_4=9
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin,1)
wiringpi.pinMode(pin_2,1)
wiringpi.pinMode(pin_3,1)
wiringpi.pinMode(pin_4,1)

while True:
    if(wiringpi.digitalRead(pinSwitch)==0):
        print("reverse")
        wiringpi.digitalWrite(pin_4, 1)
        time.sleep(.1)
        wiringpi.digitalWrite(pin_3, 1)
        time.sleep(.1)
        wiringpi.digitalWrite(pin_2, 1)
        time.sleep(.1)
        wiringpi.digitalWrite(pin, 1)
        time.sleep(.5)
        wiringpi.digitalWrite(pin_4, 0)
        time.sleep(.1)
        wiringpi.digitalWrite(pin_3, 0)
        time.sleep(.1)
        wiringpi.digitalWrite(pin_2, 0)
        time.sleep(.1)
        wiringpi.digitalWrite(pin, 0)

    else:
        time.sleep(.1)
        wiringpi.digitalWrite(pin, 1)
        wiringpi.digitalWrite(pin_2, 1)
        time.sleep(.1)
        wiringpi.digitalWrite(pin_3, 1)
        time.sleep(.1)
        wiringpi.digitalWrite(pin_4, 1)
        time.sleep(.5)
        wiringpi.digitalWrite(pin, 0)
        time.sleep(.1)
        wiringpi.digitalWrite(pin_2, 0)
        time.sleep(.1)
        wiringpi.digitalWrite(pin_3, 0)
        time.sleep(.1)
        wiringpi.digitalWrite(pin_4, 0)