import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os
import pyjokes
from requests import get
import pywhatkit as kit
import sys
from datetime import date

#====================================================================================================================================================================================

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)



def speak(audio):
   print(audio)
   engine.say(audio)
   engine.runAndWait()
#    print(audio)


def wishMe():

  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
      speak("good morning")
      speak("i amm kiki. please tell me how can i help you")

  elif hour>=12 and hour<18:
      speak("good afternoon")
      speak("i amm kiki. please tell me how can i help you")

  else:
      speak("Good evening")    
      speak("i amm kiki. please tell me how can i help you")


def takecommand():
   #it takes microphone input from the user and returns string output
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("listening...")
      r.pause_threshold = 0.6
      r.energy_threshold = 300
      audio = r.listen(source)
      try:
         print("recognizing...")
         query = r.recognize_google(audio, language='en-in')
         print("user said:",query)
         # return "none"
      except Exception as e:
      
         print("say it again please...") 
   
      return query





if __name__== "__main__":
     wishMe()
     while True:
        query = takecommand().lower()

        if 'search' in query:  

     #     query = takecommand().lower()
         speak('searching wikipedia...')
         query = query.replace("wikipedia","")
         results = wikipedia.summary(query,sentences=2)
         speak("according to wikipedia")
         print(results)
         speak(results)
         
        elif 'open youtube' in query : 
         webbrowser.open('youtube.com')
         
        elif 'open google' in query:
         speak("what should i search for")
         cm = takecommand().lower()
         webbrowser.open(f"{cm}")  

        elif 'open stackoverflow' in query:
         webbrowser.open('stackoverflow.com')    

        elif 'play music' in query:
          music_dir= 'E:\\Sakshi\\AI python'    
          songs = os.listdir(music_dir)    
          print(songs) 
          os.startfile(os.path.join(music_dir,songs[0]))   

        elif 'ip address' in query:
          ip = get('https://api.ipify.org').text
          # print(f"your ip addresss is {ip}")
          speak(f"your ip address is{ip}")
    
        elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H %M %S")  
          # print(f"the time is{strTime}")
          speak(f"the time is{strTime}")

        elif 'open code'in query:
           codePath = "C:\\Users\\viki\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)

        elif 'open mail' in query:
          codePath = "https://mail.google.com/mail/u/0/#inbox" 
          os.startfile(codePath)

        elif 'who created you' in query:
          speak("sakshi phadtare and prajakta kadam created me and my name is kiki")      

        elif 'who are you' in query:
          speak("i am virtual voice assistant created using python programming language and my mname is kiki")     

        elif 'open dictionary' in query:
          codePath = "https://www.dictionary.com/browse/google"
          os.startfile(codePath)

        elif 'tell me a joke' in query: 
          joke = pyjokes.get_joke() 
          speak(joke)   

        elif 'send message' in query:
          kit.sendwhatmsg("+7249060959","dhantBAHJGHJSGFHJGSFHJSJ",12,31)   

        elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%I:%m %p")
          print(f"it is {strTime}")
          speak(f"the time is {strTime}")
          strTime.sleep(1)

        elif 'the date' in query:
          strDate = datetime.datetime.now().strftime("%d/%m/%y")
     #  print(f"today is {strDate}")
          speak(f"today is {strDate}")
     #  strDate.sleep(1)
        
          # speak("do u have any other command?")
        elif 'exit' in query or 'stop' in query or 'sleep' in query:
          sys.exit()




