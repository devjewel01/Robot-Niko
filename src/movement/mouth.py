from move import servoMove
from time import sleep

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




