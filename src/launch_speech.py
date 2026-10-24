# Niko's launch speech: call a1() to a7() in turn.
from talk_gtts import say
from move import speakingModeOn
from time import sleep
sleep(2)
speakingModeOn()

def a1():
    say("Hello World")

def a2():
    say("I am Robot Niko... version 1.0. speed 1.5 Giga Hertz...,  64-bit quad-core ARM  processor..... with 8 Giga Byte RAM and  120 Giga byte  ROM")

def a3():
    say(" I have 27 degrees of freedom..... I have a 7 inch display for operating me...... I have two high torque motor for my mobility.")

def a4():
    say("I am created by a group of aspired students from Comilla University  named Quanta Robotics make it happen.......I want mention their name. They are Shanjit Mondol from physics department, Jewel Nath from ICT department, Anik Chakraborty from ICT department, Tawsif Bin Parves from ICT department, Mahin Khan from ICT department")

def a5():
    say(" Let's talk about my features... I can answer your questions.")

def a6():
    say("I can recognize humans and differentiate individual person..... I am trying to be a great assistant to the humans")

def a7():
    say("I am  created with a scientific goal in mind.....  Until now it was challenging to create a body of a robot, since it required complex, expensive manufacturing methods..... In just a few days, it is now possible to experiment with different body shapes thanks to 3D printing, which is used to create my body.")
