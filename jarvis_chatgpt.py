import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os

from openai import OpenAI

# ------------------- OpenAI Setup -------------------
client = OpenAI()  # reads OPENAI_API_KEY from environment

# ------------------- Voice Setup -------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print("🤖 Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
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
        return ""

# ------------------- ChatGPT Function -------------------
def ask_chatgpt(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant for Windows laptop."},
                {"role": "user", "content": question}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except:
        return "Sorry, I am unable to connect to ChatGPT now."

# ------------------- Command Execution -------------------
def execute_command(command):

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
        speak("Tell me what to search")
        query = listen()
        if query:
            speak("Searching " + query)
            pywhatkit.search(query)

    elif "play" in command:
        song = command.replace("play", "").strip()
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif "wikipedia" in command:
        speak("Tell me the topic")
        topic = listen()
        if topic:
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("Sorry, I couldn't find that topic.")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "stop" in command or "exit" in command:
        speak("Okay sir, shutting down Jarvis")
        exit()

    else:
        # 🔥 ChatGPT fallback
        speak("Let me think...")
        answer = ask_chatgpt(command)
        speak(answer)

# ------------------- Main Program -------------------
speak("Jarvis with ChatGPT is ready. Say Hey Jarvis to activate.")

while True:
    wake = listen()

    if "hey jarvis" in wake:
        speak("Yes sir, tell me your command")
        cmd = listen()
        if cmd:
            execute_command(cmd)