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
        if name == "DC":
            cmd = "Hello Honorable DC Kamrul Hasan sir, it's good to see you"
            say(cmd)
            handshake()
            sleep(1)
            say("its a honour to have you with us... Have a beautiful day")
            
        else:
            cmd = "Hello " + name + " sir, how are you, I am happy to see you"
            say(cmd)
            # p1 = multiprocessing.Process(target=say, args=(cmd))
            # p1.start()
            # sleep(2)
            # print("doing handshake")
            handshake()

