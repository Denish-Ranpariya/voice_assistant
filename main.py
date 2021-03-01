import speech_recognition as sr
from time import ctime
import webbrowser
import datetime
import pyttsx3
import time

r = sr.Recognizer()

def record_audio(question):
    with sr.Microphone() as source:
        print(question)
        play_audio(question)

        

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ''
        
        time.sleep(3)

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I didn\'t get it.')
            play_audio('Sorry, I didn\'t get it.')
        except sr.RequestError:
            print('Sorry, my voice recognition service is down.')
            play_audio('Sorry, my voice recognition service is down.')

        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Den.')
        play_audio('My name is Den.')

    if 'what time is it' in voice_data:
        now = datetime.datetime.now();
        time = str(now.hour) + ':' + str(now.minute)
        print(time)
        play_audio(time)
        
    if 'search' in voice_data:
        search = record_audio('What do you want to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)
        play_audio('Here is what I found for ' + search)

    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location
        webbrowser.get().open(url)
        print('Here is the location of ' + location)
        play_audio('Here is the location of ' + location)

    if 'exit' in voice_data:
        print('bye bye')
        play_audio('bye bye')
        exit()

def play_audio(question):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125) 
    engine.say(question)  
    engine.runAndWait()

time.sleep(5)
while True:
    voice_data = record_audio('How can I help you?')
    respond(voice_data)