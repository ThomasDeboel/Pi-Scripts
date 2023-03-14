import time
import wiringpi
import sys

trgpin = 1
echopin= 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(trgpin,1)
wiringpi.pinMode(echopin,0)
print("start")
while True:
    wiringpi.digitalWrite(trgpin, 1)
    time.sleep(.000010)
    wiringpi.digitalWrite(trgpin, 0)
    print("send signal")
    while (wiringpi.digitalRead(echopin)==0):
        time.sleep(.000010)
        #print("low")
    signal_high=time.time()
    while (wiringpi.digitalRead(echopin)==1):
        time.sleep(.00001)
    signal_low = time.time()
    time_passed = signal_low - signal_high
    #print(time_passed)
    distance= time_passed *17000
    print(distance)
    time.sleep(.5)

#cleanup
print("done")