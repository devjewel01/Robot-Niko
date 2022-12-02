from move import servoMove
from time import sleep

def moveEyeX():
    servoMove(10, 120)
    sleep(0.5)
    servoMove(10, 60)
    sleep(0.5)
    servoMove(10, 90)

def moveEyeY():
    servoMove(26, 110)
    sleep(0.5)
    servoMove(26, 160)
    sleep(0.5)
    servoMove(26, 120)

def moveEye():
    moveEyeX()
    moveEyeY()

def setOnPosition():
    servoMove(10, 90)
    servoMove(26, 120)
    