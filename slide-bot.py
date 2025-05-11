import speech_recognition as sr
import pyttsx3
import pyautogui
import time

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening......")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("Heard:" , command)
        return command.lower()
    except sr.UnknownValueError:
        #speak("Sorry i didnt catch that.")
        return ''
    except sr.RequestError:
        speak("Speech service unavailable")
        return ""
    
def handle_command(command):
    if 'next' in command:
        pyautogui.press('right')
        speak("Next slide")
    elif 'previous' in command:
        pyautogui.press('left')
        speak("previous slide")
    elif 'start' in command:
        pyautogui.press('f5')
        speak("Starting presentation")
    elif 'end' in command:
        pyautogui.press('esc')
        speak("Ending presentation")


speak("Hello i am twinvenom your slide assistant im ready to work with yousaa....")
while True:
    cmd = listen()
    if 'exit' in cmd or 'quit' in cmd:
        speak("Goodbyee")
        break
    handle_command(cmd)