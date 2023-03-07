import time
import wiringpi
import sys
    

print("start")
pin=2
pin_2=3
pin_3=4
pin_4=6
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin,1)
wiringpi.pinMode(pin_2,1)
wiringpi.pinMode(pin_3,1)
wiringpi.pinMode(pin_4,1)
i=0

while i>=0:
    i+=1
    wiringpi.digitalWrite(pin, 1)
    time.sleep(.1)
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
    time.sleep(.5)
    print(i)