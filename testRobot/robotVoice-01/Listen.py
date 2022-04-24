import speech_recognition as sr

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language="en-US")
        print(f"You Said : {query}")

    except Exception as e:
        print("I didn't get it, will you Say that again please...")  
        return "None"
    return query.lower()

