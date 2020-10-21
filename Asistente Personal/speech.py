import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import winsys
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Buenos Dias!")

    elif hour>=12 and hour<18:
        speak("Buenas Tardes!")   

    else:
        speak("Buenas Noches!")  

    speak("Hola señor, soy Jarvis, estoy aca para servirle")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Escuchando...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Usted Dijo: {query}\n")
        

    except Exception as e:
        # print(e)    
        print("Por favor repite...")  
        speak("Por favor repite señor")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    password = 'Loljuan234'
    
    server.starttls()
    server.login('pablogsjuan75@gmail.com', password)
    server.sendmail('pablogsjuan75@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Buscando en Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Acorde con Wikipedia")
            print(results)
            speak(results)

        elif 'abrir youtube' in query:
            webbrowser.open("youtube.com")

        elif 'abrir google' in query:
            webbrowser.open("google.com")

        elif 'abrir stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'pon musica' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'que dia es hoy' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Señor, hoy es {strTime}")

        elif 'quién eres' in query:  
            speak("yo soy su asistente personal señor que quiere hacer?")
        
        elif 'como estas' in query:  
            speak("muy bien señor, y que tal su dia?")
        
        elif 'opera' in query:  
            speak("ya lo abro señor")
            direccion = ""
            
            os.system('launcher.exe')

        elif 'quien eres' in query:  
            speak("yo soy su asistente personal señor que quiere hacer?")

        elif 'eres una puta' in query:  
            speak("la puta eres tu señor jajaja")
        
        elif 'turn off' in query:  
            speak("ya me apago señor nos vemos")
            exit(0)

            
        elif 'correo' in query:
            try:
                speak("Que quieres decir?")
                content = takeCommand()
                to = "pablogsjuan75@gmail.com"    
                sendEmail(to, content)

                speak("El correo fue enviado!")
            except Exception as e:
                print(e)
                speak("Lo siento señor no pude enviar el correo")    
