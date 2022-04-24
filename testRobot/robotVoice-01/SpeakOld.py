import pyttsx3 


def Say(Text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 150)
    engine.setProperty('voices', 'english') 
    print("    ")
    print(f"Robot : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")
