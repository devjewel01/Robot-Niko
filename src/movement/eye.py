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

def moveLeft():
    servoMove(10, 60)

def moveRight():
    servoMove(10, 120)

def moveUp():
    servoMove(26, 110)

def moveDown():
    servoMove(26, 160)


    