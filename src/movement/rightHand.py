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
    td = 0.1
    servoMove(1, 120)
    sleep(0.5)
    for x in range(120, 150):
        servoMove(1, x)
        sleep(td)
    sleep(1)
    for x in range(60, 30, -1):
        servoMove(3, x)
        sleep(td)
    servoMove(4, 20)
    sleep(1)
    grip(100)
    sleep(2)
    open()
    for x in range(30, 60):
        servoMove(3, x)
        sleep(td)
    sleep(1)
    servoMove(4, 90)
    for x in range(150, 120, -1):
        servoMove(1, x)
        sleep(td)
    
    
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
    



def shoulderUp():
    t = 0.1
    r = 100
    for _ in range(20):
        servoMove(0, r)
        servoMove(16, l)
        r += 1
        sleep(t)

def shoulderDown():
    t = 0.1
    r = 120
    for _ in range(20):
        servoMove(0, r)
        r -= 1
        sleep(t)


def omoplateUp():
    t = 0.1
    r = 120
    for _ in range(20):
        servoMove(1, r)
        r+=1
        sleep(t)
        
def omoplateDown():
    t = 0.1
    r = 140
    for _ in range(20):
        servoMove(1, r)
        r -= 1
        sleep(t)

def bicepUp():
    t = 0.1
    r = 60
    for _ in range(30):
        servoMove(3, r)
        r -= 1
        sleep(t)

def bicepDown():
    t = 0.1
    r = 30
    for _ in range(20):
        servoMove(3, r)
        r += 1
        sleep(t)


def rotateArm():
    t = 0.1
    r = 130
    for _ in range(40):
        servoMove(2, r)
        r -= 1
        sleep(t)
    sleep(1)
    r = 90
    for _ in range(40):
        servoMove(2, r)
        r += 1
        sleep(t)
