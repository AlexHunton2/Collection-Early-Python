import speech_recognition as sr
import os, re, webbrowser, smtplib, requests, wave, pyttsx3

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