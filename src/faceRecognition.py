from talkOld import say
from time import sleep
from movement.rightHand import handshake
import multiprocessing

appear = []

def detect(name):
    print("deteted mr ", name)
    if appear.count(name)==0:
        print("first time found")
        appear.append(name)
        cmd = "Hello " + name + " sir, how are you, I am happy to see you"
        say(cmd)
        #p1 = multiprocessing.Process(target=say, args=(cmd))
        #p1.start
        #sleep(5)
        print("doing handshake")
        handshake()

