import pyttsx3

def speak(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set the properties for the engine
    engine.setProperty('rate', 150)    # Speed of speech (words per minute)
    engine.setProperty('volume', 0.9)  # Volume of speech (0 to 1)
    
    # Set the voice for the engine
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.languages[0] == 'en_US':
            engine.setProperty('voice', voice.id)
            break
    
    # Say the text
    engine.say(text)
    engine.runAndWait()

speak("Hello i am robot niko")

