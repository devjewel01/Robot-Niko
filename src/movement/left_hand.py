from move import servoMove
from time import sleep
t = 0.001

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

def thumbsup():
    servoMove(20, 90)
    sleep(t)    
    for d in range(180):
        servoMove(21, 180-d)
        servoMove(22, d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)
        sleep(t)

def twofinger():
    servoMove(20, 90)
    sleep(t)    
    for d in range(180):
        servoMove(21, d)
        servoMove(22, 180-d)
        servoMove(23, 180-d)
        servoMove(24, d)
        servoMove(25, d)
        sleep(t)

def gunshot():
    servoMove(20, 2)
    sleep(t)
    for d in range(180):
        servoMove(21, 180-d)
        servoMove(22, 180-d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)

def pointing():
    servoMove(20, 10)
    sleep(t)
    for d in range(180):
        servoMove(21, d)
        servoMove(22, 180-d)
        servoMove(23, d)
        servoMove(24, d)
        servoMove(25, d)
        sleep(t)

def lhf(a,b,c,d,e):
    grip()
    servoMove(20, 10)
    sleep(1)
    if a== True :
        servoMove(21, 0)
    if b== True :
        servoMove(22, 0)
    if c== True :
        servoMove(23, 0)
    if d== True :
        servoMove(24, 0)
    if e== True :
        servoMove(25, 0)
    sleep(4)
    grip()

def lhnumber(a,b,c,d,e):
    servoMove(16, 150)
    sleep(1)
    servoMove(18, 45)
    sleep(1)
    #bicepkoibro
    sleep(1)
    servoMove(17, 95)
    sleep(1)
    lhf(a,b,c,d,e)

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

