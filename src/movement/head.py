from move import servoMove
from time import sleep

def rotate():
    servoMove(11, 0)
    sleep(1)
    servoMove(11, 180)
    sleep(1)
    servoMove(11, 90)

def moveLeft():
    servoMove(11, 0)

def moveRight():
    servoMove(11, 180)

def setOnPosition():
    servoMove(11, 90)

