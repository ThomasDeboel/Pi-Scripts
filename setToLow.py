import wiringpi
import sys
import time

wiringpi.wiringPiSetup()
i=0
while i != 16:
    wiringpi.pinMode(i, 1)
    wiringpi.digitalWrite(i,0)
    i+=1
    print("put pin " + str(i) + " in off state")
print("done")