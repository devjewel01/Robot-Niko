from move import servoMove
from time import sleep

def grip(deg=180):
    for d in range(deg):
        servoMove(5, d)
        servoMove(6, d)
        servoMove(7, d)
        servoMove(8, d)
        servoMove(9, d)

def gripHalf():
    for d in range(90):
        servoMove(5, d)
        servoMove(6, d)
        servoMove(7, d)
        servoMove(8, d)
        servoMove(9, d)

def open():
    for d in range(180, 0, -1):
        servoMove(5, d)
        servoMove(6, d)
        servoMove(7, d)
        servoMove(8, d)
        servoMove(9, d)

def wristOutside():
    for d in range(90, 170):
        servoMove(4, d)

def wristInside():
    for d in range(90, 170):
        servoMove(4, d)

def wristPosition():
    servoMove(4, 90)

def test():
    for d in range(180):
        servoMove(5, d)
        servoMove(6, d)
        servoMove(7, d)
        servoMove(8, d)
        servoMove(9, d)

    sleep(2)

    for d in range(180, 0, -1):
        servoMove(5, d)
        servoMove(6, d)
        servoMove(7, d)
        servoMove(8, d)
        servoMove(9, d)
    
    sleep(2)

