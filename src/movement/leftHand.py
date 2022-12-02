from move import servoMove
from time import sleep

def grip():
    for d in range(180):
        servoMove(21, d)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)

def gripHalf():
    for d in range(90):
        servoMove(21, d)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)

def open():
    for d in range(180, 0, -1):
        servoMove(21, d)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)

def wristOutside():
    for d in range(90, 170):
        servoMove(20, d)

def wristInside():
    for d in range(90, 170):
        servoMove(20, d)
def wristPosition():
    servoMove(20, 90)

def test():
    for d in range(180):
        servoMove(21, d)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)

    sleep(2)

    for d in range(180, 0, -1):
        servoMove(21, d)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)
    
    sleep(2)

