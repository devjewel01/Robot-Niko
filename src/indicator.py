#!/home/pi/robotEnv/bin python 

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Indicators
listeningindicator=4
speakingindicator=6

GPIO.setup(listeningindicator, GPIO.OUT)
GPIO.setup(speakingindicator, GPIO.OUT)
GPIO.output(listeningindicator, GPIO.LOW)
GPIO.output(speakingindicator, GPIO.LOW)

def assistantindicator(activity):
    activity=activity.lower()
    if activity=='listening':
        GPIO.output(speakingindicator,GPIO.LOW)
        GPIO.output(listeningindicator,GPIO.HIGH)
       
    elif activity=='speaking':
        GPIO.output(speakingindicator,GPIO.HIGH)
        GPIO.output(listeningindicator,GPIO.LOW)
       
        
    elif (activity=='off' or activity=='unmute'):
        GPIO.output(speakingindicator,GPIO.LOW)
        GPIO.output(listeningindicator,GPIO.LOW)

        
    elif (activity=='on' or activity=='mute'):
        GPIO.output(speakingindicator,GPIO.HIGH)
        GPIO.output(listeningindicator,GPIO.HIGH)
        

