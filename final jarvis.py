import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 185)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<=15:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hey Buddy Whats Up How can I help you.")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Wait....Calibrating Microphone")
        r.adjust_for_ambient_noise(source,duration=5)
        r.dynamic_energy_threshold = True
        print("Now Listening....")
        r.phrase_threshold = 0.8
        audio = r.listen(source)
   
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-in')
        print("User said:",query)
    except Exception as e:
        print("SAY THAT AGAIN PLEASE...")
        return "None"
    
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
        #print(query);

        if ( query.find('hello')!=-1 or query.find('hey')!=-1 ) :
            speak('Hey Buudy How can I help you')

        elif ( query.find('time')!=-1) :
            time=str(datetime.datetime.now().time())
            time=time.replace(":"," ")
            time=time[0:5]
            speak("The time is "+time)
        
        elif ( query.find('wikipedia')!=-1 or query.find('where')!=-1 or query.find('what')!=-1 )  :
            query = query.replace("wikipedia"," ")
            query = query.replace("what"," ")
            results = wikipedia.summary(query,sentences=3)
            print(results)
            speak(results)
        
        elif query.find('open youtube')!=-1:
            webbrowser.get('windows-default').open('http://www.youtube.com')
        
        elif query.find('youtube')!=-1:
            query=query.replace("youtube"," ")
            webbrowser.get('windows-default').open('https://www.youtube.com/results?search_query='+query)
        
        elif query.find('open google')!=-1:
            webbrowser.get('windows-default').open('http://www.google.com')
        elif query.find('bye')!=-1:
            speak('Bye Have a good Day Ahead')
            sys.exit()    
        else:
            webbrowser.get('windows-default').open("https://www.google.com/search?q="+query)
            
        
