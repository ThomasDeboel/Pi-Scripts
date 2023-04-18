import time
import wiringpi
import sys

def controlLEDs(sig1, sig2, cnt, wait):
    wiringpi.softPwmWrite(sig1, cnt)
    wiringpi.softPwmWrite(sig2, 100-cnt)
    time. sleep (wait)

print("Start")
pin2 =2
pin5 =5
pause_time = 0.02
wiringpi.wiringPiSetup()

wiringpi.softPwmCreate(pin2, 0, 100)
wiringpi.softPwmCreate(pin5, 0, 100)

wiringpi.softPwmWrite(pin2, 0)
wiringpi.softPwmWrite(pin5, 100)

try:
    while True:
        for i in range (0,101):
            controlLEDs(pin2,pin5,i,pause_time)
        for i in range(100,-1,-1):
            controlLEDs(pin2,pin5,i,pause_time)

except KeyboardInterrupt:
    wiringpi.softPwmWrite(pin2,0)
    wiringpi.softPwmWrite(pin5,0)
    print("\nDone")