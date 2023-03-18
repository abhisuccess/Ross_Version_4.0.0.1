# import pyjokes
import pyttsx3
import speech_recognition as sr
# import datetime
import wikipedia
import webbrowser
import time
import os
import subprocess
# import json
import requests
import pywhatkit as pw
from translate import Translator

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Ross is listening.....!")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Ross is Recognizing......!")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except Exception as e:
            txspeech("Pardon me, please say that again")
            return "None"
        return data

def txspeech(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(x)
    engine.runAndWait()
txspeech("Loading your personal voice assistant , ross")
txspeech("we believe , that we can transform the technology")

if __name__=='__main__':
    # if "start running" in sptext().lower():
        while True:
            txspeech("so, how can i help you")
            data1 = sptext().lower()
            if data1 == 0:
                continue
            elif "are you" in data1:
                name = "i am ross, your personal voice assistant"
                txspeech(name)
            elif "your name" in data1:
                name1 = "i am ross, your personal voice assistant"
                txspeech(name1)
            elif "abhi" in data1:
                pw.search("who is abhi success")
                txspeech("Abhi Success , Founder and CEO , Ne-Ent Tech Developer")
                time.sleep(5)
            # elif "right now" in data1:
            #     time = datetime.datetime.now().strftime("%I%M%p")
            #     txspeech(time)
            elif "search" in data1:
                txspeech("Entering , into the mode of search console")
                txspeech("Kindly wait")
                while True:
                    abgh = wikipedia.summary(sptext(), sentences=2)
                    txspeech(abgh)
                    time.sleep(2)
                    if "exit" in abgh:
                        txspeech("Successfully , Exited from search console mode")
                        txspeech("Please, wait")
                        txspeech("Entering, into the Normal mode")
                        break
            elif "time" in data1:
                pw.search("time right now")
                time.sleep(5)
            elif "youtube" in data1:
                yout = "opening youtube"
                txspeech(yout)
                webbrowser.open("www.youtube.com/")
                time.sleep(5)
            # elif "joke" in data1:
            #     jokess = pyjokes.get_jokes(language="en", category="neutral")
            #     print(jokess)
            #     txspeech(jokess)
            elif "favourite song" in data1:
                fav = "i know my team favourite song , wait i am opening"
                fav1 = "playing dandelions by ruth b on youtube"
                txspeech(fav)
                txspeech(fav1)
                webbrowser.open("https://youtu.be/fXbfBUNJ9mY")
                time.sleep(5)
            elif "made" in data1:
                ma = "team alpha developers, created me to helping you all people"
                txspeech(ma)
            elif "gmail" in data1:
                gma = "opening gmail"
                txspeech(gma)
                webbrowser.open("https://mail.google.com/mail/")
                time.sleep(5)
            elif "birth date" in data1:
                bd =  "hahahaha, i was created on march 2023, now calculate my present age ,i know you are genius in mathematics"
                txspeech(bd)
            elif "song for me" in data1:
                sfm = "well, i don't know your favourite song but still i am trying"
                sfm1 = "i can open music player for you , here you can play your favourite song"
                sfm2 = "opening player"
                txspeech(sfm)
                txspeech(sfm1)
                txspeech(sfm2)
                webbrowser.open("www.gaana.com/")
                time.sleep(5)

            elif "weather" in data1:
                api_key = "8ef61edcf1c576d65d836254e11ea420"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"
                txspeech("whats the city name")
                city_name = sptext()
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    txspeech(" Temperature in kelvin unit is " +
                          str(current_temperature) +
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description  " +
                          str(weather_description))
                    print(" Temperature in kelvin unit = " +
                          str(current_temperature) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))

                else:
                    txspeech(" City Not Found ")



            elif "eat" in data1:
                e = "well, i eat 100 of mb, and some part of your phone battery , hahahaha"
                txspeech(e)

            elif 'find' in data1:
                data1= data1.replace("search", "")
                webbrowser.open_new_tab(data1)
                time.sleep(5)

            elif 'news' in data1:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                txspeech('Here are some headlines from the Times of India,Happy reading')
                time.sleep(5)

            elif "file manager" in data1:
                txspeech("opening file manager")
                os.system('explorer')
                time.sleep(5)

            elif "calculator" in data1:
                txspeech("Opening calculator")
                subprocess.call('calc.exe')
                time.sleep(5)

            elif "notepad" in data1:
                txspeech("opening notepad")
                subprocess.call('notepad.exe')
                time.sleep(5)

            elif "media player" in data1:
                txspeech("Opening vlc media player")
                subprocess.call('C://Program Files//VideoLAN//VLC//vlc.exe')
                time.sleep(5)

            elif "date" in data1:
                d = "well, don't tell anyone , its alexa"
                txspeech(d)

            elif "calendar" in data1:
                cd = "opening calender on google"
                txspeech(cd)
                webbrowser.open("https://www.google.com/calendar")

            elif "alarm" in data1:
                al = "opening alarm on google"
                txspeech(al)
                webbrowser.open("https://support.google.com/clock/answer/2840926?hl=en")

            elif "youtube" in data1:
                txspeech("opening youtube")
                webbrowser.open("https://www.youtube.com/")

            elif "alpha" in data1:
                pk="team alpha developers consists of following members"
                pk1 ="Abhi Success , Pranav Mehta , piyush kumar , Fahim ul haq , harshit soni"
                pk2 = "we believe , that we can transform the technology"
                txspeech(pk)
                txspeech(pk1)
                txspeech(pk2)

            elif "english" in data1:
                txspeech("Successfully opened , kindly write your query")
                translator = Translator(to_lang="Hindi")
                translation = translator.translate(input("Enter the text in english to translate : "))
                print(translation)

            elif "between two" in data1:
                txspeech("Successfully opened , kindly write your query")
                translator1 = Translator(from_lang="german",to_lang="spanish")
                translation1 = translator1.translate(input("Enter the text in Germen to translate : "))
                print(translation1)

            elif "stop" in data1:
                txspeech("Thank you , for using ross personal voice assistant")
                break
time.sleep(3)
    # else:
#     print("Sorry, i couldn't get your voice")

