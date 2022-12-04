#!/home/pi/robotEnv/bin python 

import os
import os.path
import yaml
import time
import multiprocessing

import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
talkingInput = 18
io.setup(talkingInput, io.IN)

import Adafruit_PCA9685

pwm1 = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
pwm2 = Adafruit_PCA9685.PCA9685(address=0x41, busnum=1)

servo_min = 100 
servo_max = 600 

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))

def readYaml():
    with open('{}/src/servoConfiguration.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        servoConfig = yaml.load(conf, Loader=yaml.FullLoader)
    return servoConfig


def writeYaml(s=None):
    with open('{}/src/servoConfiguration.yaml'.format(ROOT_PATH),'w', encoding='utf8') as conf:
            yaml.dump(s,conf)


servoConfig = readYaml()

if servoConfig == None:
    with open('{}/src/servoConfigurationBackUp.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        servoBackUp = yaml.load(conf, Loader=yaml.FullLoader)
    writeYaml(servoBackUp)
    servoConfig = readYaml()
    if servoConfig == None:
        print('close')
        exit()


Initial = servoConfig['initialPosition']
Current = servoConfig['currentPosition']


def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    
    pulse_length //= 60       
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096      
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm1.set_pwm(channel, 0, pulse)
    pwm2.set_pwm(channel, 0, pulse)

pwm1.set_pwm_freq(60)
pwm2.set_pwm_freq(60)

def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))

def servoMove(n, v):
    v = int(mapRange(v, 0, 180, 100, 600))
    if(n<16):
        pwm1.set_pwm(n, 0, v)
    else:
        n -= 16
        pwm2.set_pwm(n, 0, v)

def changeDegree(pin,newDegree,time1=0.05,time2=0):
    maxChange = 0
    pinSize = len(pin)
    for i in range(0,pinSize):
        maxChange = max(abs(Current[pin[i]]-newDegree[i]),maxChange)
    for deg in range(0,maxChange,5):
        for i in range(0,pinSize):
            if Current[pin[i]]<newDegree[i]:
                Current[pin[i]] += 5
            elif Current[pin[i]]>newDegree[i]:
                Current[pin[i]] -= 5

        for i in range(0,pinSize):
            servoMove(pin[i], Current[pin[i]])
            servoConfig['currentPosition'][pin[i]] = Current[pin[i]]
        writeYaml()
        time.sleep(time1)



def moveJaw(mv=1):
    for _ in range(mv):
        servoMove(15,90)
        time.sleep(0.2)
        servoMove(15,70)
        time.sleep(0.2) 

def speakingContinue():
    while True:
        if io.input(talkingInput):
            #print("robot is speaking")
            moveJaw()
        else:
            #print("speaking off")

def speakingModeOn():
    speakingOn = multiprocessing.Process(target=speakingContinue, args=())
    speakingOn.start()










    









