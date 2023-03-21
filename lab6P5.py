

import wiringpi
import time
import json
import requests

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
url="http://thomasdb.hub.ubeac.io/iotessThomas"
uid="IOTESSThomas"

try :
    while True :
        ActivateADC ()
        tmp0 = readadc(2) # read channel 2
        DeactivateADC()
        ActivateADC ()
        tmp1 = readadc(3) # read channel 2
        DeactivateADC()
        
        

        data= {
            " id": uid,
            " sensors ":[{
            "id": 'adc ch0',
            ' data': tmp0},
            {'id': 'adc chl',
             'data':tmp1}]
        }
        r=requests.post(url, verify=False, json=data)
        print(tmp0,tmp1)
        time.sleep(1)

except KeyboardInterrupt:
    DeactivateADC()
    print("\nProgram terminated")