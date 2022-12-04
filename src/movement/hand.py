from move import servoMove
from time import sleep
t = 0.00005

def shoulderUp():
    l = 105
    r = 100
    for _ in range(60):
        servoMove(0, r)
        servoMove(16, l)
        r += 1
        l -= 1
        sleep(t)

def shoulderDown():
    l = 50
    r = 160
    for _ in range(60):
        servoMove(0, r)
        servoMove(16, l)
        r -= 1
        l += 1
        sleep(t)
def fly():
    shoulderUp()
    sleep(3)
    shoulderDown()

        
