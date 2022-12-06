from move import servoMove
from time import sleep
t = 0.005

def shoulderUp():
    r = 100
    l = 105
    for _ in range(20):
        servoMove(0, r)
        servoMove(16, l)
        r += 1
        l -= 1
        sleep(t)

def shoulderDown():
    l = 85
    r = 120
    for _ in range(20):
        servoMove(0, r)
        servoMove(16, l)
        r -= 1
        l += 1
        sleep(t)

def fly():
    shoulderUp()
    sleep(3)
    shoulderDown()

def omoplateUp():
    r = 120
    l = 110
    for _ in range(20):
        servoMove(1, r)
        servoMove(17, l)
        r+=1
        l-=1
        sleep(t)
        
def omoplateDown():
    r = 140
    l = 90
    for _ in range(20):
        servoMove(1, r)
        servoMove(17, l)
        r -= 1
        l += 1
        sleep(t)

def bicepUp():
    r = 60
    l = 110
    for _ in range(20):
        servoMove(3, r)
        r -= 1
        servoMove(19, l)
        l -= 1
        sleep(t)
def bicepDown():
    r = 40
    l = 90
    for _ in range(20):
        servoMove(3, r)
        r += 1
        servoMove(19, l)
        l -= 1
        sleep(t)

def rotateArm():
    r = 130
    l = 45
    for _ in range(30):
        servoMove(2, r)
        servoMove(18, l)
        r -= 1
        l += 1
        sleep(t)
    sleep(1)
    r = 100
    l = 75
    for _ in range(30):
        servoMove(2, r)
        servoMove(18, l)
        r += 1
        l -= 1
        sleep(t)



    
