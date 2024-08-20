import speech_recognition as sr
import pyttsx3
import os
import subprocess

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Capture voice input from the microphone and recognize it."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

def open_application(command):
    """Open system applications based on voice commands."""
    if "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad.exe")
    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc.exe")
    elif "open browser" in command:
        speak("Opening Browser")
        subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])
    elif "search google for" in command:
        search_google(command)
    elif "run" in command:
        execute_terminal_command(command)
    else:
        speak("Sorry, I can't open that application.")

def search_google(command):
    """Open Google and search for the specified query."""
    query = command.replace("search google for", "").strip()
    speak(f"Searching Google for {query}")

    # Initialize WebDriver
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH or provide the path here
    driver.get("https://www.google.com")

    # Find the search bar and type the query
    search_bar = driver.find_element("name", "q")
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.RETURN)

    # Keep the browser open for a few seconds to view the results
    time.sleep(10)
    driver.quit()

def execute_terminal_command(command):
    """Execute terminal command based on voice commands."""
    terminal_command = command.replace("run", "").strip()
    speak(f"Executing {terminal_command}")
    result = subprocess.run(terminal_command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        speak(f"Command executed successfully: {result.stdout}")
    else:
        speak(f"Error executing command: {result.stderr}")

def main():
    speak("Hello, I am Jarvis. How can I help you today?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "quit" in command or "stop" in command:
                speak("Goodbye!")
                break
            open_application(command)

if __name__ == "__main__":
    main()
