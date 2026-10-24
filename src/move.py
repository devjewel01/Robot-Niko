#!/usr/bin/env python3

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

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))

def readYaml():
    with open('{}/config/servo-configuration.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        servoConfig = yaml.load(conf, Loader=yaml.FullLoader)
    return servoConfig


def writeYaml(s=None):
    with open('{}/config/servo-configuration.yaml'.format(ROOT_PATH),'w', encoding='utf8') as conf:
            yaml.dump(s,conf)


servoConfig = readYaml()

if servoConfig == None:
    with open('{}/config/servo-configuration-backup.yaml'.format(ROOT_PATH),'r+', encoding='utf8') as conf:
        servoBackUp = yaml.load(conf, Loader=yaml.FullLoader)
    writeYaml(servoBackUp)
    servoConfig = readYaml()
    if servoConfig == None:
        print('close')
        exit()


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


def moveJaw(mv=1):
    for _ in range(mv):
        servoMove(15,110)
        time.sleep(0.2)
        servoMove(15,70)
        time.sleep(0.2) 

def speakingContinue():
    while True:
        if io.input(talkingInput):
            moveJaw()

def speakingModeOn():
    speakingOn = multiprocessing.Process(target=speakingContinue, args=())
    speakingOn.start()
