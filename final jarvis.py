
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

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

    speak("HELLO I AM JARVIS HOW MAY I HELP YOU")

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

        if 'wikipedia' in query:
            speak("Searching Wikipedia......")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia.....")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'search' and 'youtube' in query:
            webbrowser.open("youtube/query.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'search' in query:
            webbrowser.open("google/query.com")
            
        
