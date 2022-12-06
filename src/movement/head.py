from move import servoMove
from time import sleep
t = 0.1

def rotate():
    # servoMove(11, 0)
    for d in range(90, 30, -1):
        servoMove(11, d)
        sleep(t)
    sleep(1)
    # servoMove(11, 180)
    for d in range(0, 150):
        servoMove(11, d)
        sleep(t)
    sleep(1)
    for d in range(150, 90, -1):
        servoMove(11, d)
        sleep(t)
    #servoMove(11, 90)

def moveLeft():
    servoMove(11, 30)
    
def moveLeftmid():
    servoMove(11, 60)

def moveRight():
    servoMove(11, 150)
    
def moveRightmid():
    servoMove(11, 120)

def setOnPosition():
    servoMove(11, 90)

