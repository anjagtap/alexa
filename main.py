import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

#talking to Alexa:
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone()as source:
            print('listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
                talk(command)

    except:
        pass
    return command

def run_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is"+time)
    elif 'tell me about' in command:
        person=command.replace("tell me about",'')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    else:
        talk(command)

run_alexa()