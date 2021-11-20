import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import smtplib
from playsound import playsound
# import pyaudio
import os 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[2])
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    hour=datetime.datetime.now().hour
    print(hour)
    
    if hour>0 and hour<12:
        speak("Good morning  ")
    elif hour>=12 and hour<17:
        speak("Good afternoon  ")
    else:
        speak("Good evening  ")
    minutes=datetime.datetime.now().minute
    print(minutes)
    if hour>12:
        hour-=12

        speak(f" i am lady jarvis ,     time is {hour}, {minutes} PM")
    else:
        speak(f" i am lady jarvis ,     time is {hour}, {minutes} AM")
        
    speak("   How can i help you ?")

def first():
    
    r=sr.Recognizer()
    # print(sr.__version__)
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=0.7
        r.energy_threshold =300
        audioe=r.listen(source)  
        
        
    try:
        print("Recognising....")
        query=r.recognize_google(audioe,language='en-in')
        print(f"user said : {query}")
    except Exception as e:     
        print("Say again..")
        return "none"
        
    return query 

        

def takecommand():
    
    r=sr.Recognizer()
    # print(sr.__version__)
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=0.6
        r.energy_threshold =400
        audioe=r.listen(source)  
        
        
    try:
        print("Recognising....")
        query=r.recognize_google(audioe,language='en-in')
        print(f"user said : {query}")
    except Exception as e:
        print("Say again..")
        return "none"
        
    return query 

def sendemail(to,ac,content):
 try:
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    speak("write down your account password")
    server.login(ac,input())
    server.sendmail(ac,to,content)
 except Exception as e:
    speak("Sorry! failed to send email")
    
    
    
def meme():
  
        playsound("D:\\Jarvis_assistant\\meme.mp3")
    
if __name__=='__main__':
    speak("call me if you want to use me and my name is jarvis")

    while True:
        
        firstquery=first().lower()
        if 'hey jarvis' or 'jarvis' in firstquery:
            speak("hello ")
            wish()
            # query=  takecommand().lower()
            while True:
    
                query=  takecommand().lower()
                if 'wikipedia' in query:
                    query=query.replace("wikipedia", "")
                    res= wikipedia.summary(query,sentences=3)
                    speak("According to wikipedia")
                    speak(res)
                elif 'open youtube' in query:
                    webbrowser.open('youtube.com')
                elif 'open google' in query:
                    webbrowser.open('google.com')
                elif 'open chrome' in query:
                    webbrowser.open('chrome.com')
                elif 'open bizsouk' in query:
                    webbrowser.open('bizsouk.in')   
                elif 'open stackoverflow' in query:
                    webbrowser.open('stackoverflow.com')
                

        
                elif 'play music'  in query:
                    music_dir="C:\\Users\\vishwajith\\Music"
                    songs= os.listdir(music_dir)
                    print(songs)
                    if len(songs)==1:
                        speak("You Dont have music to play")
                        
                    else:  
                        r=round(random.random()*100)
                        try:
                            os.startfile(os.path.join(music_dir,songs[r]))
                        

                        except Exception as e:
                            os.startfile(os.path.join(music_dir,songs[round(random.random()*10)]))
                        


                elif 'time now' in query:
                    speak("time is ")
                    speak(datetime.datetime.now().hour)
                    speak(" ")
                    speak(datetime.datetime.now().minute)
                    
                
                elif 'open vs code'  in query:
                    code_path="C:\\Users\\vishwajith\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(code_path)
                    
                elif 'send email' in query:
                    speak("To who you want to send, Tell me receiver email id write down")
                    to=input()
                    speak("From which account you want to send tell me your email id write down")
                    ac=input()
                    speak("Tell me what to say")
                    content=takecommand()
                    sendemail(to,ac,content)
                
                elif "bye" in query:
                    speak("Thanks for using me, have a good day bye")
                    
                
                else:
                    meme()
    

                
            
            

            
            
        
        