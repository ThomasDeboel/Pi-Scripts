import time
import wiringpi
import sys

print("start")
pin_1=3
pin_2=4
pin_3=6
pin_4=9
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin_1,1)
wiringpi.pinMode(pin_2,1)
wiringpi.pinMode(pin_3,1)
wiringpi.pinMode(pin_4,1)

while True:
    wiringpi.digitalWrite(pin_4,0)
    wiringpi.digitalWrite(pin_2,1)
    time.sleep(0.005)
    time.sleep(0.995)
    wiringpi.digitalWrite(pin_1,0)
    wiringpi.digitalWrite(pin_3,1)
    time.sleep(0.005)
    time.sleep(0.995)
    wiringpi.digitalWrite(pin_2,0)
    wiringpi.digitalWrite(pin_4,1)
    time.sleep(0.005)
    time.sleep(0.995)
    wiringpi.digitalWrite(pin_3,0)
    wiringpi.digitalWrite(pin_1,1)
    time.sleep(0.005)
    time.sleep(0.995)
