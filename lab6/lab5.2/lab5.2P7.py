import time
import wiringpi
import sys
    
print("start")

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
        wiringpi.digitalWrite(pin_4, 1)
        time.sleep(.01)
        wiringpi.digitalWrite(pin_4, 0)
        wiringpi.digitalWrite(pin_3, 1)
        time.sleep(.01)
        wiringpi.digitalWrite(pin_3, 0)
        wiringpi.digitalWrite(pin_2, 1)
        time.sleep(.01)
        wiringpi.digitalWrite(pin_2, 0)
        wiringpi.digitalWrite(pin, 1)
        time.sleep(.01)
        wiringpi.digitalWrite(pin, 0)
        

