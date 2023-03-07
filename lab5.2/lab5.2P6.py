import time
import wiringpi
import sys
    

print("start")
pinSwitch_1 = 2
pinSwitch_2 = 3
pinR_1 = 4
pinR_2 = 6

wiringpi.wiringPiSetup()
wiringpi.pinMode(pinSwitch_1,0)
wiringpi.pinMode(pinSwitch_2,0)
wiringpi.pinMode(pinR_1,1)
wiringpi.pinMode(pinR_2,1)

if(wiringpi.digitalRead(pinSwitch_1)==0):
    wiringpi.digitalWrite(pinR_1,1)
else:
    wiringpi.digitalWrite(pinR_1,0)

if(wiringpi.digitalRead(pinSwitch_2)==0):
    wiringpi.digitalWrite(pinR_2,1)
else:
    wiringpi.digitalWrite(pinR_2,0)