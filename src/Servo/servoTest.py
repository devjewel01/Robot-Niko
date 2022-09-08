
from __future__ import division
import time

import Adafruit_PCA9685

pwm1 = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
pwm2 = Adafruit_PCA9685.PCA9685(address=0x41, busnum=1)

servo_min = 100  
servo_max = 600 

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    
    pulse_length //= 60       
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096      
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm1.set_pwm(channel, 0, pulse)
    pwm2.set_pwm(channel, 0, pulse)

pwm1.set_pwm_freq(60)
pwm2.set_pwm_freq(60)

def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))

print("......Enter servoNumber and Degree.........")

while True:
    n, v = map(int, input().split())
    n -= 1
    v = int(mapRange(v, 0, 180, 100, 600))
    if(n<16):
        pwm1.set_pwm(n, 0, v)
    else:
        n -= 16
        pwm2.set_pwm(n, 0, v)



