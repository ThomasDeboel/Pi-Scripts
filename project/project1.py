# hoe werkt het
import time
import wiringpi
import sys
import spidev
from ch7_ClassLCD import LCD
import requests
import json
# get current time 
from datetime import datetime
#https://www.programiz.com/python-programming/datetime/current-time

wiringpi.wiringPiSetup()

#triggercounter 
triggercounter = 0 #start the counter at 0
status ="armed" #set status as armed
#triggercounter end

#motor 
pin_1=0 #pin 1 of motor
pin_2=1 #pin 2 of motor
pin_3=2 #pin 3 of motor
pin_4=5 #pin 4 of motor
wiringpi.pinMode(pin_1,1)
wiringpi.pinMode(pin_2,1)
wiringpi.pinMode(pin_3,1)
wiringpi.pinMode(pin_4,1)
turning = 0
#motor end

#alarm
alarmpin=4
wiringpi.pinMode(alarmpin,1)
#alarm end

#buttons
buttontrigger = 6
buttonreset = 7
wiringpi.pinMode(buttontrigger,0)
wiringpi.pinMode(buttonreset,0)
#buttons end

#lcd
#defenitions for led

def ActivateLCD():
        wiringpi.digitalWrite(pin_CS_lcd, 0)       # Actived LCD using CS
        time.sleep(0.000005)

def DeactivateLCD():
        wiringpi.digitalWrite(pin_CS_lcd, 1)       # Deactived LCD using CS
        time.sleep(0.000005)

#defenitions for led end

#This is from the slides in class
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
wiringpi.pinMode(pin_CS_lcd , 1)            # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)
#lcd end

#echo
trgpin = 7 #pin 5 (w1)
echopin= 8 #pin 7 (w2)
wiringpi.wiringPiSetup()
wiringpi.pinMode(trgpin,1)
wiringpi.pinMode(echopin,0)
#echo end

#ubeac setup
url="http://thomasdb.hub.ubeac.io/iotessThomas"
uid="IOTESSThomas"
#ubeac end

def motordraai(aantalturns): #laat de motor draaien voor "aantal turns"
    while (turning<aantalturns):
        turning +=1
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

def motordraaireverse(aantalturns): #laat de motor draaien voor "aantal turns in revers"
    while (turning<aantalturns):
        turning +=1
        wiringpi.digitalWrite(pin_4,1)
        wiringpi.digitalWrite(pin_2,0)
        time.sleep(0.005)
        wiringpi.digitalWrite(pin_1,1)
        wiringpi.digitalWrite(pin_3,0)
        time.sleep(0.005)
        wiringpi.digitalWrite(pin_2,1)
        wiringpi.digitalWrite(pin_4,0)
        time.sleep(0.005)
        wiringpi.digitalWrite(pin_3,1)
        wiringpi.digitalWrite(pin_1,0)
        time.sleep(0.005)

def alarmlightson(): #turns alarm on met alternerende led
    wiringpi.digitalWrite(alarmpin,1)

def alarmlightoff(): #turns alarm light off
    wiringpi.digitalWrite(alarmpin,0)

#lcd starting
lcd_1.clear()
lcd_1.set_backlight(1)
#lcd starting

def lcd(triggercounter, currenttime,status): #laat lcd werken met de currenttime, status van de trap en de aantal triggers sinds het begin.
    ActivateLCD()
    lcd_1.clear()
    lcd_1.go_to_xy(0, 0) #gaat naar 0,0 op het scherm
    lcd_1.put_string("Current Time =" + currenttime +"\nTrapstatus: "+ status +"\nnumber of alarms: "+ triggercounter) #toont dit op heet scherm
    lcd_1.refresh()
    DeactivateLCD()

def ubeac(triggercount, time, status):
    data= {
            " id": uid,
            " sensors ":[{
            "id": 'aantalTrigs',
            ' data': triggercounter},
            {'id': 'Status',
            'data':status}]
    }
    r=requests.post(url, verify=False, json=data)


try:
    #onderstaande code leest de afstand
    wiringpi.digitalWrite(trgpin, 1)
    time.sleep(.000010)
    wiringpi.digitalWrite(trgpin, 0)
    print("send signal")
    while (wiringpi.digitalRead(echopin)==0):
        time.sleep(.000010)
    signal_high=time.time()
    while (wiringpi.digitalRead(echopin)==1):
        time.sleep(.00001)
    signal_low = time.time()
    time_passed = signal_low - signal_high
    distance= time_passed *17000
    #afstand lezen klaar

    #geeft de tijd van nu
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #tijdlezen klaar

    if(distance<5) or (wiringpi.digitalRead(buttontrigger)==1) and (status!="triggered"): 
#kijkt of dat de afstand van de sensor klein genoeg is dater een muis in de val kan zitten of kijkt of dat ik manueel de knop heb ingedrukt
        motordraai(500) #doet de motor draaien zodat de deur dicht gaat
        triggercounter +=1 #zet trigcounter eentje hoger
        status="triggered" #zet status op triggered
        lcd(triggercounter,current_time,status) #geeft de data door naar de lcd
        alarmlightson() #zet het alarm aan

    
    if(wiringpi.digitalRead(buttonreset)==1): #kijkt of dat ik de reset knop in heb gedrukt
        status ="armed" #zet dan status op armed
        alarmlightoff() #zet allarm uit
        motordraaireverse(500) # laat de motor terug draaien
    lcd(triggercounter, current_time, status) #stuurt een update naar lcd ook al gebeurt er niks
    ubeac(triggercounter,current_time,status) #stuurt een update naar ubeac ook al gebeurt er niks
    time.sleep(.5)


except KeyboardInterrupt:#set everything to off
    print("stopping")
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    alarmlightoff()
    print("\nProgram terminated")