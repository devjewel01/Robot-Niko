from move import servoMove
from time import sleep
t = 0.0008

def grip(deg=180):
    for d in range(deg):
        servoMove(21, 70)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)
        sleep(t)

def gripHalf(deg=90):
    for d in range(deg):
        servoMove(21, 70)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)
        sleep(t)

def open():
    for d in range(90, 0, -1):
        servoMove(21, d)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)
        sleep(t)

def wristOutside():
    for d in range(90, 170):
        servoMove(20, d)
        sleep(t)

def wristInside():
    for d in range(90, 10, -1):
        servoMove(20, d)
        sleep(t)

def wristPosition():
    servoMove(20, 90)

def test():
    for d in range(120):
        servoMove(21, 80)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)
        sleep(t)

    sleep(2)

    for d in range(120, 0, -1):
        servoMove(21, d)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)
        sleep(t)
    
    sleep(2)

