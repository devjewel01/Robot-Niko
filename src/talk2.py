#!/home/pi/robotEnv/bin python 

from googletrans import Translator
from gtts import gTTS
import os
import os.path


TTSChoice='GTTS'

translator = Translator()
femalettsfilename="/tmp/female-say.mp3"
malettsfilename="/tmp/male-say.wav"
ttsfilename="/tmp/gcloud.mp3"
language='en-US'
translanguage=language.split('-')[0]
gender='Female'



#gTTS
def gttssay(phrase,saylang,specgender):
    tts = gTTS(text=phrase, lang=saylang)
    tts.save(femalettsfilename)
    
    os.system('sox ' + femalettsfilename + ' ' + malettsfilename + ' pitch -450')
    os.remove(femalettsfilename)
    os.system('aplay ' + malettsfilename)
    os.remove(malettsfilename)
    


def trans(words,destlang,srclang):
    transword= translator.translate(words, dest=destlang, src=srclang)
    transword=transword.text
    transword=transword.replace("Text, ",'',1)
    transword=transword.strip()
    print(transword)
    return transword



#Text to speech converter with translation
def say(words,sourcelang=None,destinationlang=None):
    if sourcelang!=None and destinationlang!=None:
        
        sayword=trans(words,destinationlang,sourcelang)
        gttssay(sayword,translanguage,gender)
    else:
        if sourcelang==None:
            sourcelanguage='en'
        else:
            sourcelanguage=sourcelang
        if sourcelanguage!=translanguage:
            sayword=trans(words,translanguage,sourcelanguage)
        else:
            sayword=words
        
        gttssay(sayword,translanguage,gender)
