import time
import wiringpi
import sys

def controlLEDs(sig1, sig2, cnt, wait):
    wiringpi.softPwmWrite(sig1, cnt)
    wiringpi.softPwmWrite(sig2, cnt *(-1))
    time. sleep (wait)

#Setup
print("Start")
pin2 =2
pin5 =5
pause_time = 0.02   # you can change this to slow down/speed up
wiringpi.wiringPiSetup()

#Set pins as a softPWM output
wiringpi.softPwmCreate(pin2, 0, 100)
wiringpi.softPwmCreate(pin5, 0, 100)

#start pwm
wiringpi.softPwmWrite(pin2, 0)
wiringpi.softPwmWrite(pin5, 0)

try:
    while True:
        for i in range(0,101):  
            controlLEDs(pin2,pin5,i,pause_time)
        for i in range (100,-1,-1):
            controlLEDs(pin2,pin5,i,pause_time)
        for i in range (0,-101,-1):
            controlLEDs(pin2,pin5,i,pause_time)
        for i in range(-100,0):  
            controlLEDs(pin2,pin5,i,pause_time)
        
        

except KeyboardInterrupt:
    wiringpi.softPwmWrite(pin2,0)   #stops the pwm output
    wiringpi.softPwmWrite(pin5,0)   #stops the pwm output
    print("\nDone")