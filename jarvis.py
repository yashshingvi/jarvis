import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os

import webbrowser



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak(" Sir Im Jarvis")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("hearing....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e) hiding error
    
        print("can you please speak again sir")
        return "None"
        #return string none
    return query


if __name__ == "__main__":

    wishMe()
    speak("yash is a good f boy")
    print("hi")
    query = takeCommand().lower()
 

    if 'wikepedia' in query:
        speak("searching wiki")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wiki")
        print(results)
        speak(results)

    elif 'open' in query:
        if 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'facebook' in query:
            webbrowser.open("fb.com")
        elif 'instagram' in query:
            webbrowser.open("instagram.com")
        elif 'facebook' in query:
            webbrowser.open("fb.com")







