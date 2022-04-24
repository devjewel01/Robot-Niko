import speech_recognition as sr 


def Listen():
    recog = ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Robot Listening.....")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Robto try to Recognizing....")
        recog = r.recognize_google(audio, language = 'en-US')
        print(f"You Said : {recog}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    recog = str(recog)
    return recog.lower()
