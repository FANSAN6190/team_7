############## Modules #############
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import time
from multiprocessing import Process
import pyautogui
import random

##############Functions###############
#----------important Function-----------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        speak("Sorry sir i couldn't recognise you")
        print("Say that again please...")
        return "None"
    return query
    
def runinparallel(*fns,):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()
#---------------------------------------
#----------Extra Functions--------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("my name is AaBot Sir. Please tell me how may I help you")

def wiki(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=3)
    speak("According to Wikipedia")
    print(results)
    speak(results)

        

def reminder(text,local_time):
    local_time = local_time * 60
    time.sleep(local_time)
    speak(text)
       
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('test.mail.test370@gmail.com', 'tmttmt370')
    server.sendmail('test.mail.test370@gmail.com', to, content)
    server.close()
    
############Main#############

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #----------normal conversation------------
        if ("who are you")in query :
            speak("""I'm an Assistance bot, or aabot, i can help you to perform simple tasks like , 
                  opening an aplication, playing a music, sending a mail, 
                  giving imformation from wikipedia, etcetra.""")
            
        elif ('time' or "what's the time") in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif "thank you" in query:
            speak("you are most welcome sir")
        
        elif ("hello" or "hello aabot") in query:
            speak("Hello Sir")
        #-----------------------------------------
        #-----------open aplications--------------
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'open code' in query:
            codePath = "C:\\Users\\fanin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif "open fusion" in query:
            codePath = "C:\\Users\\fanin\\Desktop\\fusion360.exe"
            os.startfile(codePath)
        elif("reminder" in query):
            speak("What shall I remind you about?")
            text = takeCommand()
            speak("In how many minutes? please type here.")      
            
            local_time = int(input())
            runinparallel(reminder(text,local_time),takeCommand())  
        #----------------------------------------
        #----------------services----------------   
        elif 'wikipedia' in query:
            try:
                wiki(query)
            except:
                speak("sorry sir i'm not able to understand . can you say something else")
                query=takeCommand()
                wiki(query)

        elif ('play music' or "music") in query:
            music_dir = 'C:\\Users\\Admin\\Music\\Music\\YTD'
            songs = os.listdir(music_dir)
            print(songs)   
            rang=range(0,65)
            r=random.choice(rang) 
            os.startfile(os.path.join(music_dir, songs[r])) 
        elif 'email' in query:
            try:
                speak("to whom")
                sa=takeCommand()
                to=" "
                if sa==("Praveen" or "ravin" ):
                    to = "211b221@juetguna.in"
                
                elif sa==("kazi" or "kaazi"):
                    to = "211b233@juetguna.in"
                
                elif sa==("fanin" or "fanindra" or "funny" or "fani"):
                    to ="211b116@juetguna.in"
                    
                speak("What should I say?")
                content = takeCommand()
                    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
                      
        elif ("exit" or "close") in query:
            speak("Yes sir")
            quit()