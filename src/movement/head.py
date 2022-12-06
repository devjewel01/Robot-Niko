from move import servoMove
from time import sleep
t = 0.1
ft = 0.05

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
    for d in range(90, 30, -1):
        servoMove(11, d)
        sleep(ft)
    
def moveLeftmid():
    for d in range(90, 60, -1):
        servoMove(11, d)
        sleep(ft)

def moveRight():
    for d in range(90, 150):
        servoMove(11, d)
        sleep(ft)
    
def moveRightmid():
    for d in range(0, 120):
        servoMove(11, d)
        sleep(ft)

def setOnPosition():
    servoMove(11, 90)

