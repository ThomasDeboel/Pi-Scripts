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
statusint =0 #set status as armed
#triggercounter end

#motor 
pin_1=3 #pin 1 of motor
pin_2=4 #pin 2 of motor
pin_3=6 #pin 3 of motor
pin_4=5 #pin 4 of motor
wiringpi.pinMode(pin_1,1)
wiringpi.pinMode(pin_2,1)
wiringpi.pinMode(pin_3,1)
wiringpi.pinMode(pin_4,1)
#motor end

#alarm
alarmpin=2
wiringpi.pinMode(alarmpin,1)
#alarm end

#buttons
buttontrigger = 7
buttonreset = 8
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
                'LED'   :   15, #backlight  was 6  
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
trgpin = 1 #pin 5 (w1)
echopin= 0 #pin 7 (w2)
wiringpi.wiringPiSetup()
wiringpi.pinMode(trgpin,1)
wiringpi.pinMode(echopin,0)
#echo end

#ubeac setup
url="http://orangepilts.hub.ubeac.io/IOTESSThomas"
uid="IOTESSThomas"
#ubeac end

def motordraai(aantalturns): #laat de motor draaien voor "aantal turns"
    turning=0
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
    turning=0
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
    wiringpi.digitalWrite(alarmpin,0)

def alarmlightoff(): #turns alarm light off
    wiringpi.digitalWrite(alarmpin,1)

#lcd starting
lcd_1.clear()
lcd_1.set_backlight(1)
#lcd starting

def lcd(triggercounter, currenttime,status): #laat lcd werken met de currenttime, status van de trap en de aantal triggers sinds het begin.
    ActivateLCD()
    lcd_1.clear()
    lcd_1.go_to_xy(0, 0) #gaat naar 0,0 op het scherm
    lcd_1.put_string("Current Time =" + currenttime +"\nTrapstatus: "+ status +"\nnumber of alarms: "+ str(triggercounter)) #toont dit op heet scherm
    lcd_1.refresh()
    DeactivateLCD()

def ubeac(triggercount, statusint):
    data= {
            "uid":uid,
            "sensors":[{
            "id":'aantalTrigs',
            'data':triggercount},
            {'id':'status',
            'data':statusint}]
    }
    r=requests.post(url, verify=False, json=data)


try:
    while True:
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
        print(status)
        if(((distance<15) or (wiringpi.digitalRead(buttontrigger)==0)) and (status!="triggered")): 
            print("this is triggered")
            #kijkt of dat de afstand van de sensor klein genoeg is dater een muis in de val kan zitten of kijkt of dat ik manueel de knop heb ingedrukt
            alarmlightson() #zet het alarm aan
            motordraai(500) #doet de motor draaien zodat de deur dicht gaat
            triggercounter +=1 #zet trigcounter eentje hoger
            status="triggered" #zet status op triggered
            statusint = 100 #zet status op 1 (voor ubeac)
            lcd(triggercounter,current_time,status) #geeft de data door naar de lcd


    
        if((wiringpi.digitalRead(buttonreset)==0) and (status =="triggered")): #kijkt of dat ik de reset knop in heb gedrukt
            print("reset knop")
            status ="armed" #zet dan status op armed
            statusint= 0 #zet de status op 0 (voor ubeac)
            alarmlightoff() #zet allarm uit
            motordraaireverse(20) # laat de motor terug draaien
        lcd(triggercounter, current_time, status) #stuurt een update naar lcd ook al gebeurt er niks
        ubeac(triggercounter,statusint) #stuurt een update naar ubeac ook al gebeurt er niks
        time.sleep(.5)
        print("loop")


except KeyboardInterrupt:#set everything to off
    print("stopping")
    lcd_1.clear()
    lcd_1.refresh()
    lcd_1.set_backlight(0)
    DeactivateLCD()
    alarmlightoff()
    wiringpi.digitalWrite(pin_4,0)
    wiringpi.digitalWrite(pin_3,0)
    wiringpi.digitalWrite(pin_2,0)
    wiringpi.digitalWrite(pin_1,0)
    print("\nProgram terminated ")
    