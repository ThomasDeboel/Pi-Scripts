import time
import wiringpi
import sys

print("start")
pinSwitch = 2
pin_1=0
pin_2=1
pin_3=2
pin_4=5
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinSwitch,0)
wiringpi.pinMode(pin_1,1)
wiringpi.pinMode(pin_2,1)
wiringpi.pinMode(pin_3,1)
wiringpi.pinMode(pin_4,1)

while True:
        wiringpi.digitalWrite(pin_4,0)
        wiringpi.digitalWrite(pin_2,1)
        time.sleep(0.005)
        wiringpi.digitalWrite(pin_1,0)
        wiringpi.digitalWrite(pin_3,1)
        time.sleep(0.005)
        wiringpi.digitalWrite(pin_2,0)
        wiringpi.digitalWrite(pin_4,1)
        time.sleep(0.005)
        wiringpi.digitalWrite(pin_3,0)
        wiringpi.digitalWrite(pin_1,1)
        time.sleep(0.005)