from move import servoMove
from time import sleep
import multiprocessing

import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
talkingInput = 18
io.setup(talkingInput, io.IN)


def moveJaw(t=1):
    for _ in range(t):
        servoMove(15,110)
        sleep(0.5)
        servoMove(15,60)
        sleep(0.5)


def openMouth():
    servoMove(15, 120)


def closeMouth():
    servoMove(15, 60)

def speakingContinue():
    while True:
        if io.input(talkingInput):
            # print("speaking detecting")
            moveJaw()
        else:
            # print("speaking off")
            sp = None 

def speakingModeOn():
    speakingOn = multiprocessing.Process(target=speakingContinue, args=())
    speakingOn.start
