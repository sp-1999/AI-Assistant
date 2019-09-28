import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import vlc
import pyglet
import threading 

def Animation():
    ag_file = "circle_story_by_gleb.gif"
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)
    win = pyglet.window.Window(width=800, height=600,fullscreen = True)
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()
    pyglet.app.run()
    
def Program():
    engine = pyttsx3.init('sapi5')
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 200)
    client = wolframalpha.Client('P32Q9J-976AAG95X6')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[len(voices)-1].id)


    def speak(audio):
        print('Anna: ' + audio)
        engine.say(audio)
        engine.runAndWait()

    def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            speak('Good Morning!')

        if currentH >= 12 and currentH < 16:
            speak('Good Afternoon!')

        if currentH >= 16 and currentH !=0:
            speak('Good Evening!')

    def myCommand():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration = 1)
            r.energy_threshold = 300
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print('User: ' + query + '\n')
        except sr.UnknownValueError:
            print("!")
            query=myCommand()
        return query

    def Command():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration = 1)
            r.energy_threshold = 300
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            query=Command()
        return query

    def online():
        speak('hello sir')
        speak('starting all system applications')
        speak('installing all drivers')
        speak('every driver is installed')
        speak('all systems have been started')
        speak('now i am online sir')

    def shutdown():
        speak('understood sir')
        speak('connecting to command prompt')
        speak('shutting down your computer')
        os.system('shutdown -s')
            
    def gooffline():
        speak('ok sir')
        speak('closing all systems')
        speak('disconnecting to servers')
        speak('going offline')
        quit()

    greetMe()
    online()
    speak('How may I help you?')
    while True:
        query = myCommand()
        query = query.lower()
        
        if 'open youtube' in query or 'youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query or 'google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query or 'gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
    
        elif 'send mail' in query or 'send email' in query or 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()
            if 'me' in recipient:
                speak('What should I say? ')
                content = myCommand()
                receiver_email='sangamprasad1999@gmail.com'  
            else:
                speak('Receiver Email Address please!')
                receiver_email=myCommand()
                speak('What should I say? ')
                content = myCommand()

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login("sangamprasad1999@gmail.com", 'Sangam123@')
                server.sendmail('sangamprasad1999@gmail.com', receiver_email, content)
                server.close()
                speak('Email sent!')
            except:
                speak('Sorry Sir! I am unable to send your message at this moment!')

        elif 'bye' in query or 'nothing' in query or 'abort' in query or 'stop' in query:
            gooffline()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'shutdown' in query:
            shutdown()
                                    
        elif 'play music' in query or 'next music' in query or 'music' in query:
            music_folder ="D:\\song\\1920_Evil_Returns_(2012)_IndiaMp3.Com\\1920 - Evil Returns (2012)\\songs\\"
            music = ["Apnaa", "Jaavedaan Hai", "Khud", "Majboor","Uska"]
            random_music = music_folder + random.choice(music) + '.mp3'
            player = vlc.MediaPlayer(random_music)
            player.play()
            speak('Okay, here is your music! Enjoy!')
            while( Command() not in ["stop","stop music"] ):
                pass
            else:
                player.stop()
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        nextmsgs = ['Next Command! Sir!', 'What more I can do for you sir!', 'Anything else! Sir!', 'What else can i do','Any more request sir...']
        speak(random.choice(nextmsgs))
            

if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=Program) 
    t2 = threading.Thread(target=Animation) 

    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 

    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 

    # both threads completely executed 
    print("Done!") 
