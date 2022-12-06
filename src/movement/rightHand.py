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

def gunshot():
    servoMove(4, 0)
    sleep(t)
    for d in range(180):
        servoMove(5, 180-d)
        servoMove(6, 180-d)
        servoMove(7, d)
        servoMove(8, d)
        servoMove(9, d)
        
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

def gripOnOff():
    for d in range(180):
        servoMove(5, d)
        servoMove(6, d)
        servoMove(7, d)
        servoMove(8, d)
        servoMove(9, d)
        sleep(t)
    sleep(2)

    for d in range(180, 0, -1):
        servoMove(5, d)
        servoMove(6, d)
        servoMove(7, d)
        servoMove(8, d)
        servoMove(9, d)
        sleep(t)
    sleep(2)

def handshake():
    servoMove(1, 150)
    sleep(2)
    servoMove(3,30)
    sleep(2)
    servoMove(4, 20)
    sleep(2)
    grip(100)
    sleep(1)
    for _ in range(3):
        servoMove(3, 50)
        sleep(1)
        servoMove(3, 30)
    sleep(2)
    open()
    sleep(1)
    servoMove(3, 60)
    sleep(1)
    servoMove(4, 90)
    servoMove(1, 120)

def rhf(a,b,c,d,e):
    grip()
    servoMove(4, 90)
    sleep(1)
    if a== True :
        servoMove(5, 0)
    if b== True :
        servoMove(6, 0)
    if c== True :
        servoMove(7, 0)
    if d== True :
        servoMove(8, 0)
    if e== True :
        servoMove(9, 0)
    sleep(4)
    grip()

def rhbicepup():
    servoMove(3, 35)

def rhnumber(a,b,c,d,e):
    servoMove(0, 110)
    sleep(1)
    servoMove(2, 130)
    sleep(1)
    rhbicepup()
    sleep(1)
    servoMove(1, 130)
    sleep(1)
    rhf(a,b,c,d,e)
    

    