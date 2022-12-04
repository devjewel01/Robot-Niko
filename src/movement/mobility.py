#!/home/pi/robotEnv/bin python 

from time import sleep

import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)

PWM_MAX = 100


leftForward = 5
leftBackward = 0
leftMotorSpeed = 13 

rightForward = 6
rightBackward = 26
rightMotorSpeed = 19

io.setup(leftForward, io.OUT)
io.setup(leftBackward, io.OUT)
io.setup(rightForward, io.OUT)
io.setup(rightBackward, io.OUT)

io.output(leftForward, True)
io.output(leftBackward, True)
io.output(rightForward, True)
io.output(rightBackward, True)

io.setup(leftMotorSpeed, io.OUT)
io.setup(rightMotorSpeed, io.OUT)


leftMotorSpeed = io.PWM(leftMotorSpeed,100)
leftMotorSpeed.start(0)
leftMotorSpeed.ChangeDutyCycle(0)

rightMotorSpeed = io.PWM(rightMotorSpeed,100)
rightMotorSpeed.start(0)
rightMotorSpeed.ChangeDutyCycle(0)



def Forward(speed=50):
   io.output(leftForward, True)
   io.output(leftBackward, False)
   io.output(rightForward, True)
   io.output(rightBackward, False)
   leftMotorSpeed.ChangeDutyCycle(speed)
   rightMotorSpeed.ChangeDutyCycle(speed)


def Backward(speed=50):
   io.output(leftForward, False)
   io.output(leftBackward, True)
   io.output(rightForward, False)
   io.output(rightBackward, True)
   leftMotorSpeed.ChangeDutyCycle(speed)
   rightMotorSpeed.ChangeDutyCycle(speed)


def Left(speed=50):
   io.output(leftForward,  False)
   io.output(leftBackward,  True)
   io.output(rightForward, True)
   io.output(rightBackward, False)
   leftMotorSpeed.ChangeDutyCycle(speed)
   rightMotorSpeed.ChangeDutyCycle(speed)
   sleep(1)
   Stop()


def Right(speed=50):
   io.output(leftForward,  True)
   io.output(leftBackward,  False)
   io.output(rightForward, False)
   io.output(rightBackward, True)
   leftMotorSpeed.ChangeDutyCycle(speed)
   rightMotorSpeed.ChangeDutyCycle(speed)
   sleep(1)
   Stop()


def leftCircle(speed=50):
   io.output(leftForward,  False)
   io.output(leftBackward,  True)
   io.output(rightForward, True)
   io.output(rightBackward, False)
   leftMotorSpeed.ChangeDutyCycle(speed)
   rightMotorSpeed.ChangeDutyCycle(speed)
   

def rightCircle(speed=50):
   io.output(leftForward,  True)
   io.output(leftBackward,  False)
   io.output(rightForward, False)
   io.output(rightBackward, True)
   leftMotorSpeed.ChangeDutyCycle(speed)
   rightMotorSpeed.ChangeDutyCycle(speed)


def Stop(speed=50):
   io.output(leftForward, False)
   io.output(leftBackward, False)
   io.output(rightForward, False)
   io.output(rightBackward, False)
   leftMotorSpeed.ChangeDutyCycle(0)
   rightMotorSpeed.ChangeDutyCycle(0)


def setMotorLeft(power):
   int(power)
   if power < 0:
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      io.output(leftForward, False)
      io.output(leftBackward, True)
      io.output(rightForward, False)
      io.output(rightBackward, True)
      leftMotorSpeed.ChangeDutyCycle(pwm)
   elif power > 0:
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      io.output(leftForward, True)
      io.output(leftBackward, False)
      io.output(rightForward, True)
      io.output(rightBackward, False)
      leftMotorSpeed.ChangeDutyCycle(pwm)
   else:
      leftMotorSpeed.ChangeDutyCycle(0)
	  

def setMotorRight(power):
   int(power)
   if power < 0:
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      io.output(leftForward, False)
      io.output(leftBackward, True)
      io.output(rightForward, False)
      io.output(rightBackward, True)
      rightMotorSpeed.ChangeDutyCycle(pwm)
   elif power > 0:
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      io.output(leftForward, True)
      io.output(leftBackward, False)
      io.output(rightForward, True)
      io.output(rightBackward, False)
      rightMotorSpeed.ChangeDutyCycle(pwm)
   else:
      rightMotorSpeed.ChangeDutyCycle(0)


def exit():
   io.output(leftForward,  False)
   io.output(leftBackward,  False)
   io.output(rightForward, False)
   io.output(rightBackward, False)
   io.cleanup()
   

