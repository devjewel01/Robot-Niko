from move import servoMove
from time import sleep
t = 0.0008
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

def thumbsup():
    servoMove(4, 170)
    sleep(t)    
    for d in range(180):
        servoMove(5, 180-d)
        servoMove(6, d)
        servoMove(7, d)
        servoMove(8, d)
        servoMove(9, d)
        sleep(t)

def twofinger():
    servoMove(4, 90)
    sleep(t)    
    for d in range(180):
        servoMove(5, d)
        servoMove(6, 180-d)
        servoMove(7, 180-d)
        servoMove(8, d)
        servoMove(9, d)
        sleep(t)

def pointing():
    servoMove(4, 90)
    sleep(t)
    for d in range(180):
        servoMove(5, d)
        servoMove(6, 180-d)
        servoMove(7, d)
        servoMove(8, d)
        servoMove(9, d)
        sleep(t)

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

def handshake():
    servoMove(1, 140)
    sleep(1)
    servoMove(4, 50)
    sleep(1)
    grip(100)
    sleep(3)
    open()
    sleep(1)
    servoMove(4, 90)
    sleep(1)
    servoMove(1, 120)
