import wiringpi
import time
def ActivateADC():
    wiringpi.digitalWrite(pin_CS_adc,0)
    time.sleep(0.000005)
def DeactivateADC():
    wiringpi.digitalWrite(pin_CS_adc,1)
    time.sleep(0.000005)

def readadc(adcnum) :
    if ( (adcnum > 7) or (adcnum < 0)) :
        return -1
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes ( [ 1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout= ( (recvData[1] &3)<< 8) + recvData [2]
    return adcout

#Setup
pin_CS_adc = 16
pinl1=1
pinl2=2
wiringpi.wiringPiSetup ()
wiringpi.pinMode (pin_CS_adc, 1)
wiringpi.pinMode (pinl1, 1)
wiringpi.pinMode (pinl2, 1)
wiringpi.wiringPiSPISetupMode (1,0,500000,0)

try :
    while True :
        ActivateADC ()
        tmp0 = readadc(4) # read channel 3
        DeactivateADC()
        lightlevel=tmp0*100/1023
        print(lightlevel)
        time.sleep (0.5)
except KeyboardInterrupt:
    DeactivateADC()
    print("\nProgram terminated")