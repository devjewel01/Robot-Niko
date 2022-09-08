from vosk import Model, KaldiRecognizer 
import pyaudio

model = Model("DataBase/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def Listen():
    print("")
    print("Listening...")
    print("")

    while True:

        data = stream.read(4096)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            p = text[14:-3]
            print(f"You Said : {p}")

            if len(p)>0:
                return p
            
            else:
                break


 