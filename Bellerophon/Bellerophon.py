from gtts import gTTS
from io import BytesIO
import speech_recognition as sr
import os, re, webbrowser, smtplib, requests, wave, pyttsx3
import simpleaudio as sa
from weather import Weather

def talkToMe(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    print(audio)

def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        order = r.listen(source)
        purforder = r.recognize_google(order)
    return purforder

#broken :?
class Command:
    
    def __init__(self):
        commmands = {
            "repeat after me":"repeat",
        }
        talkToMe("I am listening")
        command = listen()
        for k,v in commands: 
            if k == command:
               return v
                

    def Repeat():
        talkToMe("Okay, I will repeat after you")
        skeet = listen()
        print(str(skeet))
        talkToMe(skeet)
        Command()
                
startcmd = Command()


