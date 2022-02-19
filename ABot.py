
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import time
from multiprocessing import Process
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def runinparallel(*fns,):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("my name is AaBot Sir. Please tell me how may I help you")       
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
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('test.mail.test370@gmail.com', 'tmttmt370')
    server.sendmail('test.mail.test370@gmail.com', to, content)
    server.close()
def reminder(text,local_time):
    local_time = local_time * 60
    time.sleep(local_time)
    speak(text)
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\Admin\\Music\\Music\\YTD\\JokerBGMSong(Bass Boosted).mp3'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\fanin\\Desktop\\Code.exe"
            os.startfile(codePath)
        elif ("exit" "close") in query:
            speak("Yes sir")
            quit()
        elif "thank you" in query:
            speak("you are most welcome sir")
        elif ("hello" or "hello aabot") in query:
            speak("Hello Sir")
        elif ("what is your name" or "who are you")in query :
            speak("""I'm an Assistance bot, or aabot, i can help you to perform simple tasks like , 
                  opening an aplication, playing a music, sending a mail, 
                  giving imformation from wikipedia, etcetra.""")
        elif("reminder" ):
            speak("What shall I remind you about?")
            text = takeCommand()
            speak("In how many minutes?")
            local_time = int(input())
            runinparallel(reminder(text,local_time),takeCommand)
        
            
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "211b221@juetguna.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        
        
            
            
                
            
