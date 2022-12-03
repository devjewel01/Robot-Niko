from move import servoMove
from time import sleep

def setOnPosition():
    servoMove(12, 30)
    servoMove(13, 100)
    servoMove(14, 85)
