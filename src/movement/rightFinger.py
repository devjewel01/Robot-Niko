from move import servoMove
from time import sleep

for d in range(180):
    servoMove(4, d)
    servoMove(5, d)
    servoMove(6, d)
    servoMove(7, d)
    servoMove(8, d)
