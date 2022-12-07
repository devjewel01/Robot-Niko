from talk import say
from time import sleep
from movement.rightHand import handshake
import multiprocessing
sleep(3)

appear = []

def detect(name):
    print("detected mr ", name)
    if appear.count(name)==0:
        print("first time found")
        appear.append(name)
        if name == "togor hasan" or name=="togor hasan":
            cmd = "Hello Honorable togor hasan sir, the owener of halima group"
            say(cmd)
            handshake()
            say("it's a honour to have you with us... Have a beautiful day sir")
            
        else:
            cmd = "Hello " + name + " sir, I am now able to perfectly recognise you...,  how are you sir, I am happy to see you"
            say(cmd)
            #p1 = multiprocessing.Process(target=say, args=(cmd))
            #p1.start()
            #sleep(3)
            #print("doing handshake")
            handshake()

