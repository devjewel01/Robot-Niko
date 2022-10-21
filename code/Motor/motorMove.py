#!/usr/bin/env python3

from time import sleep
import RPi.GPIO as io
io.setmode(io.BCM)
io.setwarnings(False)
PWM_MAX = 100


# Left
L_L_EN = 22 
L_R_EN = 23 
L_L_PWM = 18 
L_R_PWM = 17

# Right
R_L_EN = 13 
R_R_EN = 19 
R_L_PWM = 12 
R_R_PWM = 6 


leftmotor_in1_pin = L_L_EN
leftmotor_in2_pin = L_R_EN
io.setup(leftmotor_in1_pin, io.OUT)
io.setup(leftmotor_in2_pin, io.OUT)


rightmotor_in1_pin = R_L_EN
rightmotor_in2_pin = R_R_EN
io.setup(rightmotor_in1_pin, io.OUT)
io.setup(rightmotor_in2_pin, io.OUT)


io.output(leftmotor_in1_pin, True)
io.output(leftmotor_in2_pin, True)
io.output(rightmotor_in1_pin, True)
io.output(rightmotor_in2_pin, True)



leftmotorpwm_pin_l = L_L_PWM 
leftmotorpwm_pin_r = L_R_PWM

rightmotorpwm_pin_l = R_L_PWM
rightmotorpwm_pin_r = R_R_PWM


io.setup(leftmotorpwm_pin_l, io.OUT)
io.setup(leftmotorpwm_pin_r, io.OUT)

io.setup(rightmotorpwm_pin_l, io.OUT)
io.setup(rightmotorpwm_pin_r, io.OUT)


leftmotorpwm_l = io.PWM(leftmotorpwm_pin_l,100)
leftmotorpwm_r = io.PWM(leftmotorpwm_pin_r,100)

rightmotorpwm_l = io.PWM(rightmotorpwm_pin_l,100)
rightmotorpwm_r = io.PWM(rightmotorpwm_pin_r,100)


leftmotorpwm_l.start(0)
leftmotorpwm_r.start(0)

leftmotorpwm_l.ChangeDutyCycle(0)
leftmotorpwm_r.ChangeDutyCycle(0)


rightmotorpwm_l.start(0)
rightmotorpwm_r.start(0)

rightmotorpwm_l.ChangeDutyCycle(0)
rightmotorpwm_r.ChangeDutyCycle(0)



def Forward(speed=50):
   io.output(leftmotor_in1_pin, True)
   io.output(leftmotor_in2_pin, False)
   io.output(rightmotor_in1_pin, True)
   io.output(rightmotor_in2_pin, False)

   leftmotorpwm_l.ChangeDutyCycle(speed)
   leftmotorpwm_r.ChangeDutyCycle(0)	
   rightmotorpwm_l.ChangeDutyCycle(speed)
   rightmotorpwm_r.ChangeDutyCycle(0)

def Backward(speed=50):
   io.output(leftmotor_in1_pin, False)
   io.output(leftmotor_in2_pin, True)
   io.output(rightmotor_in1_pin, False)
   io.output(rightmotor_in2_pin, True)

   leftmotorpwm_l.ChangeDutyCycle(0)
   leftmotorpwm_r.ChangeDutyCycle(speed)	
   rightmotorpwm_l.ChangeDutyCycle(0)
   rightmotorpwm_r.ChangeDutyCycle(speed)

def Left(speed=50):
   io.output(leftmotor_in1_pin,  False)
   io.output(leftmotor_in2_pin,  True)
   io.output(rightmotor_in1_pin, True)
   io.output(rightmotor_in2_pin, False)

   leftmotorpwm_l.ChangeDutyCycle(speed)
   leftmotorpwm_r.ChangeDutyCycle(0)	
   rightmotorpwm_l.ChangeDutyCycle(speed)
   rightmotorpwm_r.ChangeDutyCycle(0)

   sleep(1)
   Stop()

def Right(speed=50):
   io.output(leftmotor_in1_pin,  True)
   io.output(leftmotor_in2_pin,  False)
   io.output(rightmotor_in1_pin, False)
   io.output(rightmotor_in2_pin, True)

   leftmotorpwm_l.ChangeDutyCycle(speed)
   leftmotorpwm_r.ChangeDutyCycle(0)	
   rightmotorpwm_l.ChangeDutyCycle(0)
   rightmotorpwm_r.ChangeDutyCycle(speed)

   sleep(1)
   Stop()

def leftCircle(speed=50):
   io.output(leftmotor_in1_pin,  False)
   io.output(leftmotor_in2_pin,  True)
   io.output(rightmotor_in1_pin, True)
   io.output(rightmotor_in2_pin, False)

   leftmotorpwm_l.ChangeDutyCycle(speed)
   leftmotorpwm_r.ChangeDutyCycle(0)	
   rightmotorpwm_l.ChangeDutyCycle(speed)
   rightmotorpwm_r.ChangeDutyCycle(0)
   

def rightCircle(speed=50):
   io.output(leftmotor_in1_pin,  True)
   io.output(leftmotor_in2_pin,  False)
   io.output(rightmotor_in1_pin, False)
   io.output(rightmotor_in2_pin, True)

   leftmotorpwm_l.ChangeDutyCycle(speed)
   leftmotorpwm_r.ChangeDutyCycle(0)	
   rightmotorpwm_l.ChangeDutyCycle(0)
   rightmotorpwm_r.ChangeDutyCycle(speed)


def Stop(speed=50):
   io.output(leftmotor_in1_pin, False)
   io.output(leftmotor_in2_pin, False)
   io.output(rightmotor_in1_pin, False)
   io.output(rightmotor_in2_pin, False)

   leftmotorpwm_l.ChangeDutyCycle(0)
   leftmotorpwm_r.ChangeDutyCycle(0)	
   rightmotorpwm_l.ChangeDutyCycle(0)
   rightmotorpwm_r.ChangeDutyCycle(0)


def setMotorLeft(power):
   int(power)
   if power < 0:
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      leftmotorpwm_l.ChangeDutyCycle(pwm)
      leftmotorpwm_r.ChangeDutyCycle(0)	  
   elif power > 0:
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      leftmotorpwm_l.ChangeDutyCycle(0)
      leftmotorpwm_r.ChangeDutyCycle(pwm)
   else:
      leftmotorpwm_l.ChangeDutyCycle(0)
      leftmotorpwm_r.ChangeDutyCycle(0)
	  

def setMotorRight(power):
   int(power)
   if power < 0:
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      rightmotorpwm_l.ChangeDutyCycle(pwm)
      rightmotorpwm_r.ChangeDutyCycle(0)
   elif power > 0:
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      rightmotorpwm_l.ChangeDutyCycle(0)
      rightmotorpwm_r.ChangeDutyCycle(pwm)
   else:
      rightmotorpwm_l.ChangeDutyCycle(0)
      rightmotorpwm_r.ChangeDutyCycle(0)
   


def exit():
   io.output(leftmotor_in1_pin,  False)
   io.output(leftmotor_in2_pin,  False)
   io.output(rightmotor_in1_pin, False)
   io.output(rightmotor_in2_pin, False)
   io.cleanup()
   

