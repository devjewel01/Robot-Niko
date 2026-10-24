from talk_gtts import say
from time import sleep
from movement.right_hand import handshake
sleep(3)

# Names already greeted, lower-cased so labels that differ only in case count once
appear = []

def detect(name):
    key = name.lower()
    if key not in appear:
        appear.append(key)
        if key == "jewel nath":
            cmd = "Hello Mr. Jewel. My programmer. How are you"
            say(cmd)
            handshake()
            say("I am also fine. Have a great day")
        else:
            cmd = "Hello " + name + ", I can recognise you now. How are you? I am happy to see you."
            say(cmd)
            handshake()
