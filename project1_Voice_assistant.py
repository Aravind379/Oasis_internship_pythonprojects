import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    """Speaks the given text."""
    engine.say(text)
    engine.runAndWait()

def get_audio():
    """Listens for user input and returns recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return None

def respond(text):
    """Predefined responses."""
    if "hello" in text:
        speak("Hello there!")
    elif "how are you" in text:
        speak("I am doing well, thank you.")
    elif "what time is it" in text:
        now = datetime.datetime.now()
        speak(f"The current time is {now.strftime('%I:%M %p')}.")
    elif "what is the date today" in text:
        today = datetime.date.today()
        speak(f"Today is {today.strftime('%B %d, %Y')}.")
    else:
        speak("I'm still learning. I don't understand that yet.")

def search_web(query):
    """Searches the web for the given query."""
    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    speak(f"Searching for {query} on the web.")

if __name__ == "__main__":
    speak("Hello, I'm ready to assist you.")
    while True:
        user_input = get_audio()
        if not user_input:
            continue
        
        text = user_input.lower()
        
        if "exit" in text or "quit" in text or "stop" in text:
            speak("Goodbye!")
            break
        
        if text.startswith("search "):
            query = text.replace("search ", "", 1)
            search_web(query)
        else:
            respond(text)
