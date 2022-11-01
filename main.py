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

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
