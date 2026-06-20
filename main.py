# Main File

import speech_recognition as sr

# Cria um reconhecedor
r = sr.Recognizer()

# Abrir o Microfone para captura
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) #define microfone como fonte de audio
        print(r.recognize_google(audio, language='pt-br'))