from distutils.command import check
from random import random
from tkinter.tix import Tree
import speech_recognition as sr
from PyDictionary import PyDictionary
from pywikihow import search_wikihow
import pyttsx3 
import socket
import datetime
import wikipedia 
import webbrowser
import pywhatkit
import pyautogui
import pyjokes
import keyboard
from playsound import playsound
import os
from Speak import speak
from Listen import takeCommand
import re
import random
from PIL import Image
import time as ttt





def vision():

    while True:
        # speak("Yes")
        query = takeCommand()


        def checking(list_lst):
            for x in list_lst:
                x = x.lower()
                if x in query:
                    return True
            return False

        def gretting():
            patterns = ["hello","hii","hey","wake up","hey robot"]
            return checking(patterns)==True

        def Good_Bye():
            patterns = ["bye","good day","you around","you later"]
            return checking(patterns) == True

        def health():
            patterns = ["how are you","how you","are you fine", "you feeling"]
            return checking(patterns) == True

        def about_vision():
            vision_qu = ["about yourself", "who are you" ,"what are you","your name"]
            return checking(vision_qu)==True

        def robo_ques():
            robo = ["are you robot","are you a robot"]
            return checking(robo) == True

        def searching():
            sea = ['search', 'find']
            return checking(sea)==True

        def question():
            sea = ['tell me', 'who', 'what is', 'where']
            return checking(sea)==True

        def dict():
            speak("Dictionary activated successfully.")
            while True:
                speak("what do you want to know...")
                word = takeCommand()
                word = word.replace('what','')
                word = word.replace('tell me','')
                word = word.replace('is','')
                word = word.replace('the','')
                print(word)

                if 'close' in word:
                    speak("Dictionary closed...")
                    break

                elif 'meaning' in word:
                    word = word.replace('meaning','')
                    word = word.replace('of','')
                    word = word.replace(' ','')
                    mean = PyDictionary.meaning(word)
                    speak(f"The meaning for {word} is {mean}")
                
                elif 'synonym' in word:
                    word = word.replace('synonym','')
                    word = word.replace('of','')
                    word = word.replace(' ','')
                    syn = PyDictionary.synonym(word)
                    speak(f"The synonym of {word} is {syn}")

                elif 'antonym' in word:
                    word = word.replace('antonym','')
                    word = word.replace('of','')
                    word = word.replace(' ','')
                    ant = PyDictionary.antonym(word)
                    speak(f"The antonym of {word} is {ant}")

        def validate_time(alarm_time):
            if len(alarm_time) != 8:
                speak("Invalid HOUR format! Please try again.")
                return False
            else:
                if int(alarm_time[0:2]) > 12:
                    speak("Invalid HOUR format! Please try again.")
                    return False
                elif int(alarm_time[3:5]) > 59:
                    speak("Invalid HOUR format! Please try again.")
                    return False
                else:
                    speak("Ok")
                    return True

        def family():
            patterns = ["have a family", "have any family", "your family member", "any family"]
            return checking(patterns) == True
        
        def food():
            patterns = ["you eat","your food", "feel hungry","feeling hungry"]
            return checking(patterns) == True

        def feelings():
            patterns = ["cry","cried", "any feelings","feelings","you feel sad","are you happy"]
            return checking(patterns) == True

        def DC_Officer():
            patterns = ["your DC", "Deputy Commissioner name","your Deputy Commissioner","DC of comilla","kamilla DC","comilla DC", "your District Magistrate"]
            return checking(patterns) == True

        def collectorate():
            patterns = ["DC office","Deputy Commissioner office","District Magistrate office"]
            return checking(patterns) == True

        def DC():
            patterns = ["word DC","of DC","by DC","Deputy Commissioner","District Magistrate","DC"]
            return checking(patterns) == True

        def mujib():
            patterns = ["father of nation", "Sheikh Mujib","father of the nation","bangabandhu"]
            return checking(patterns) == True
        
        def Fablab():
            patterns = ["What is Fab lab", "about Fab lab","what  Fab lab","fab lab","fablab"]
            return checking(patterns) == True

        def robo_pro():
            patterns = ["Robotics and programming","programming and robotics"]
            return checking(patterns) == True

        def Digital_Bangladesh():
            patterns = ["digital bangladesh"]
            return checking(patterns) == True
        
        def vision_41():
            patterns = ["vision 2041", "Vision 41"]
            return checking(patterns) == True












        if gretting():
            responses = ["Hello","Always For You","Here's Your Robot.","I am here"]
            speak(random.choice(responses))

        elif Good_Bye():
            responses = ["Bye","Good Bye","It'll be Nice To Meet You Again.","Nice to meet you","See You Later","have a good day"]
            speak(random.choice(responses))

        elif health():
            responses = ["I am Fine, How are you","Feeling Perfect, How you doing","Feeling Cool, how do you do"]
            speak(random.choice(responses))

        elif about_vision():
            speak(" I am a Robot, my name is vision. version 1.0.")

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')   
            speak(f"Sir, the time is {time}")

        elif 'date' in query:
            today = datetime.date.today()
            speak(f"The Date is: {today}")

        elif 'day' in query:
            day = datetime.datetime.now().strftime("%A")
            speak(day)

        elif 'thank you' in query:
            speak("you are most welcome.")

        elif 'good' in query:
            speak("Thank you...")

        elif family():
            responses = ["Cumilla DC office is my family", "My familly is comilla DC office"]
            speak(random.choice(responses))

        elif food():
            responses = ["i am a robot, i don't eat food. i might need electricity to charge my battries"]
            speak(random.choice(responses))

        elif feelings():
            responses = ["We robots don't have feelings"]
            speak(random.choice(responses))

        elif DC_Officer():
            responses = ["Mohammad Kamrul Hasan sir is the Deputy Commissioner of Cumilla, Here you can see him"]
            speak(random.choice(responses))
            im = Image.open("dc_sir.png")
            im.show()
            ttt.sleep(3)
            keyboard.press_and_release('Alt + F4')

        elif collectorate():
            responses = ["DC office means The office of Deputy Commissioner"]
            speak(random.choice(responses))

        elif DC():
            responses = ["Deputy Commissioner popularly abbreviated to DC or District Magistrate is the chief administrative and revenue officer of a district or an administrative sub-unit of a division"]
            speak(random.choice(responses))

        elif mujib():
            responses = ["Bangabundhu Sheikh Mujibur Rahman widely known as Bangabandhu was a Bangladeshi politician, statesman, and Founding Father of Bangladesh who served as the first President and later as the Prime Minister of Bangladesh"]
            speak(random.choice(responses))

        elif Fablab():
            responses = ["Fab Lab - Digital Fabrication Laboratory, is a place where anyone can make (almost) anything, using digital design, 3D printers, laser cutting and other advanced technological means. In its essence, Fab-Lab is about turning ideas into reality.", "A Fab Lab, or digital fabrication laboratory, is a place to play, to create, to mentor and to invent: a place for learning and innovation."]
            speak(random.choice(responses))

        elif robo_pro():
            responses = ["Its a Dream Of our Honourable Dc Sir to train school students robotics and programming . In three rounds students will be taught electronics, programming, math Olympiad and hand-to-hand teaching through Arduino microcontroller." ]
            speak(random.choice(responses))

        elif Digital_Bangladesh():
            responses = ["The philosophy of “Digital Bangladesh” comprises ensuring people's democracy and human rights, transparency, accountability, establishing justice, and ensuring delivery of government services to the citizens of Bangladesh through maximum use of technology.", "Bangladesh is amongst one of the only countries that initiated Digital Bangladesh dated back as early as 2008. It is empowering its resources by its advanced, robust training programs on Intelligent Enterprise, Digital Trust, Cyber Security and SMAC (Social Media, Mobility, Analytics and Cloud) and robotics. So, Bangladesh is gradually aging towards to becoming a Digital Country"]
            speak(random.choice(responses))

        elif vision_41():
            responses = ["Vision 2041 is a national strategic plan to farther develop the socio-economic standing of the Peoples Republic of Bangladesh, issued by Prime Minister Sheikh Hasina and formulated by National Economic Council"]
            speak(random.choice(responses))

        elif "play" in query and "youtube" in query:
            speak("playing your song on youtube.....")
            query = query.replace('play','')
            query = query.replace('youtube','')
            query = query.replace('on','')
            pywhatkit.playonyt(query)

        elif 'open youtube' in query:
            speak("What do you want me to search sir...")
            qur = takeCommand()
            qur = qur.replace('search','')
            qur = qur.replace(' ','+')
            web = 'https://www.youtube.com/results?search_query='+qur
            webbrowser.open(web)
            speak("Here you go sir...")

        elif searching():
            query = query.replace('search','')
            query = query.replace('find','')
            pywhatkit.search(query)
            speak("Done sir...")

        elif 'send' in query and 'whatsapp' in query:
            speak("Tell me the number sir...")
            qur = takeCommand()
            hr = None
            mn = None

            while True:
                speak("When do you want to send the message...")
                time = takeCommand()
                time = time.replace('.','')

                if time[1]==':':
                    hr = time[0]
                    mn = time[2:4]
                    send_time = '0' + time
                else:
                    hr = time[0:2]
                    mn = time[3:5]
                    send_time = time

                print(f"valid Time: {send_time}")
                if validate_time(send_time):
                    break

            
            speak("And the message is....")
            qur1 = takeCommand()
            qur = qur.replace(' ','')
            speak("Ok sir, the message will be send in time...")
            pywhatkit.sendwhatmsg("+880"+qur, qur1, int(hr), int(mn),20)
            keyboard.press_and_release("Enter")
            speak("Done Sir...")

        elif 'you there' in query or 'you listening' in query:
            responses = ["yes, i am here","yeah, i am listening","it's clear","listening carefully", "Yeah, my microphone is ok", "yes, cristal clear sound"]
            speak(random.choice(responses))
        
        elif 'dare you' in query:
            speak("I am sorry, if i did something wrong...")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        
        elif 'dictionary' in query:
            dict()
        
        elif 'how to' in query:
            speak("Getting data from Internet: ")
            op = query.replace('tell me','')
            op = op.replace('show me', '')
            max_result = 1
            func = search_wikihow(op,max_result)
            assert len(func) == 1
            speak(func[0].summary)

        elif question():
            query = query.replace('who is','')
            query = query.replace('what is','')
            query = query.replace('tell me','')
            query = query.replace('about','')

            try:
                pywhatkit.search(query)
                results = wikipedia.summary(query, sentences=1)
                speak(results)
            except:
                speak("No speakable data vailable...")
        
        elif 'alarm' in query:
            
            while  True:
                speak("Give me the time sir...")
                time = takeCommand()
                time = time.replace('.','')

                if time[1]==':':
                    alarm_time = '0' + time
                else:
                    alarm_time = time

                print(f"valid Time: {alarm_time}")
                if validate_time(alarm_time):
                    break
                

            alarm_hour = alarm_time[0:2]
            alarm_min = alarm_time[3:5]
            alarm_period = alarm_time[6:].upper()

            while True:
                now = datetime.datetime.now()
                current_hour = now.strftime("%I")
                current_min = now.strftime("%M")
                current_period = now.strftime("%p")
                if alarm_period == current_period:
                    if alarm_hour == current_hour:
                        if alarm_min == current_min:
                            speak("Time to wake up sir...")
                            music_dir2 = 'C:\\Users\\Anik Chakraborty\\Helloworld\\music'
                            songs1 = os.listdir(music_dir2)
                            os.startfile(os.path.join(music_dir2, songs1[0]))
                            break

        elif 'enter' in query or 'show' in query:
            speak("Ok,sir...")
            keyboard.press_and_release("Enter")
        
        elif 'next' in query or 'right' in query:
            speak("Okay...")
            keyboard.press_and_release("Right")

        elif 'previous' in query or 'left' in query:
            speak("Okay....")
            keyboard.press_and_release('Left')
        
        elif 'up' in query:
            speak("Okay....")
            keyboard.press_and_release('Up')

        elif 'down' in query:
            speak("Okay....")
            keyboard.press_and_release('Down')

        elif 'close' in query:
            speak("Okay...")
            keyboard.press_and_release('Alt + F4')







vision()






