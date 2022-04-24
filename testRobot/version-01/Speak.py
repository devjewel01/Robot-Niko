import pyttsx3 

def speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',200)
    print("    ")
    print(f"Robot : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")
