from servo import servoMove
from time import sleep

for x in range(3):
    servoMove(0, 100)
    sleep(0.3)
    servoMove(0, 70)
    sleep(0.3)

servoMove(0, 60)
