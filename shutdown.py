import speech_recognition as sr
import pyttsx3
import os
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine

r = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        engine.setProperty("voice" , voices[1].id)
        engine.say("Are you ready to shutdown? just say shutdown ill do that for you")
        engine.runAndWait()
        print("Speak now...")
        audio = r.listen(source)
        text = r.recognize_google(audio)


        if text == "shutdown" or text == 'shut down':
            engine.say("Shutting down now asap")
            engine.runAndWait()
            os.system("shutdown /s /t 0")
            break
        else:

            engine.say("Invalid command i cant do that")
            engine.runAndWait()
            print(text)