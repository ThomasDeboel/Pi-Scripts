import time
import wiringpi
import spidev
from ch7_ClassLCD import LCD

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

def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
    time.sleep(0.000005)

def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
    time.sleep(0.000005)

PIN_OUT     =   {  
                'SCLK'  :   14,
                'DIN'   :   11,
                'DC'    :   9, 
                'CS'    :   13, #We will not connect this pin! --> we use w13
                'RST'   :   10,
                'LED'   :   6, #backlight   
}

#IN THIS CODE WE USE W13 (PIN 22) AS CHIP SELECT
pin_CS_lcd = 13
wiringpi.wiringPiSetup() 
wiringpi.wiringPiSPISetupMode(1, 0, 400000, 0)  #(channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd , 1)                # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)
pin_CS_adc = 16
pinl1=1
pinl2=2
wiringpi.pinMode (pin_CS_adc, 1)
wiringpi.pinMode (pinl1, 1)
wiringpi.pinMode (pinl2, 1)
wiringpi.wiringPiSPISetupMode (1,0,500000,0)


try:
    lcd_1.clear()
    lcd_1.set_backlight(1)
    while True:
        ActivateADC ()
        tmp0 = readadc(0) # read channel 0
        DeactivateADC()
        ActivateADC ()
        tmp1 = readadc(1) # read channel 0
        DeactivateADC()
        ActivateLCD()
        print (" input0 : " , tmp0)
        print (" input1 : " , tmp1)
        lcd_1.clear()
        lcd_1.go_to_xy(0, 0)
        lcd_1.put_string('ADC value \non display \nin0 = ' + str(tmp0) + '\nin2 = ' + str(tmp1)) #display the text
        lcd_1.refresh()
        DeactivateLCD()
        time.sleep(1)

except KeyboardInterrupt:
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    print("\nProgram terminated")