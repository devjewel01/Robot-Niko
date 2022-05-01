#!/usr/bin/env python3


import sys, tty, termios, os, readchar


import BTS7960BHBridge as HBridge


speedleft = 0
speedright = 0


print("w/s: accelerate")
print("a/d: steer")
print("q: stop robot")
print("x: exit programm")


def getch():
   ch = readchar.readchar()
   return ch


def printscreen():
   os.system('clear')
   print("w/s: accelerate")
   print("a/d: steer")
   print("q:   stop robot")
   print("x:   exit programm")
   print("========== speed indicator ==========")
   print("Left motor speed: ", speedleft)
   print("Right motor speed ", speedright)

while True:
   char = getch()
   
   if(char == "w"):
      speedleft = speedleft + 0.1
      speedright = speedright + 0.1

      if speedleft > 1:
         speedleft = 1
      if speedright > 1:
         speedright = 1

      HBridge.setMotorLeft(speedleft)
      HBridge.setMotorRight(speedright)
      printscreen()

   if(char == "s"):
      speedleft = speedleft - 0.1
      speedright = speedright - 0.1

      if speedleft < -1:
         speedleft = -1
      if speedright < -1:
         speedright = -1
         
     
      HBridge.setMotorLeft(speedleft)
      HBridge.setMotorRight(speedright)
      printscreen()


   if(char == "q"):
      speedleft = 0
      speedright = 0
      HBridge.setMotorLeft(speedleft)
      HBridge.setMotorRight(speedright)
      printscreen()

   if(char == "d"):      
      speedright = speedright - 0.1
      speedleft = speedleft + 0.1
      
      if speedright < -1:
         speedright = -1
      
      if speedleft > 1:
         speedleft = 1
      
      HBridge.setMotorLeft(speedleft)
      HBridge.setMotorRight(speedright)
      printscreen()
      

   if(char == "a"):
      speedleft = speedleft - 0.1
      speedright = speedright + 0.1
         
      if speedleft < -1:
         speedleft = -1
      
      if speedright > 1:
         speedright = 1
      
      HBridge.setMotorLeft(speedleft)
      HBridge.setMotorRight(speedright)
      printscreen()
      

   if(char == "x"):
      HBridge.setMotorLeft(0)
      HBridge.setMotorRight(0)
      HBridge.exit()
      print("Program Ended")
      break
   

   char = ""
   
