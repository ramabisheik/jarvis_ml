import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os

# ------------------- Voice Setup -------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("🤖 Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("🧠 Recognizing...")
        command = r.recognize_google(audio)
        command = command.lower()
        print("✅ You said:", command)
        return command
    except:
        speak("Sorry, I didn't understand. Please repeat.")
        return ""

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning sir")
    elif hour < 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

    speak("I am your Jarvis. How can I help you?")

def run_jarvis():
    wish_me()

    while True:
        command = take_command()

        if "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak("Current time is " + time)

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + date)

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "search" in command:
            speak("What should I search?")
            query = take_command()
            if query != "":
                speak("Searching " + query)
                pywhatkit.search(query)

        elif "play" in command:
            song = command.replace("play", "")
            speak("Playing " + song + " on YouTube")
            pywhatkit.playonyt(song)

        elif "wikipedia" in command:
            speak("Tell me what to search in wikipedia")
            topic = take_command()
            if topic != "":
                try:
                    result = wikipedia.summary(topic, sentences=2)
                    speak(result)
                    print(result)
                except:
                    speak("Sorry, I couldn't find that topic.")

        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        elif "open calculator" in command:
            speak("Opening Calculator")
            os.system("calc")

        elif "stop" in command or "exit" in command or "quit" in command:
            speak("Okay sir, Jarvis is shutting down")
            break

        else:
            if command != "":
                speak("Sorry, I can't do that now. Try another command.")

run_jarvis()