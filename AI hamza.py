import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
hamza = pyttsx3.init()
voices = hamza.getProperty('voices')
hamza.setProperty('voice', voices[0].id)

def talk(text):
    hamza.say(text)
    hamza.runAndWait()

def talk_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hamza' in command:
                command = command.replace('hamza', '')
    except:
       pass
    return command
def run_hamza():
    command = talk_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for,1)
        talk(info)

while True:
     run_hamza
