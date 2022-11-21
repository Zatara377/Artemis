# Nosso arquivo principal


"""
import speech_recognition as sr

# Cria um reconhecedor
r = sr.Recognizer()

# Abrir o Microfone para captura

#Essa captura funciona pelo google, ou seja, apenas online
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # Define microfone como fonte de áudio

        print(r.recognize_google(audio)) #para reconhecer em português: (audio, language = 'pt')
"""

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json

#Síntese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#Reconhecedor de fala
model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000, exception_on_overflow=False) #setting to false resolves the input overflow error
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)
            speak(text)
