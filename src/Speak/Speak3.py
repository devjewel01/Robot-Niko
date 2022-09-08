# Pyttsx3 - Module
# Os Based Framework

import pyttsx3  

engine = pyttsx3.init("espeak")
voices = engine.getProperty('voices')
# print(voices[17].id)
engine.setProperty('voices',voices[17].id)

def Speak(Text):
    lengthcode = len(Text)
    if lengthcode>30:
        engine.setProperty('rate',170)
    else:
        engine.setProperty('rate',150)
    print("    ")
    print(f"A.I : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")