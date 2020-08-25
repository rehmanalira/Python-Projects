
'''

Author : Rehman Ali RA
date: 25 Auguest 2020

This is a Jarvis Program which will executed take voice and give your required desire you can also as much you want


NOTE : WHEN YOU RUN THIS IT WILL GAVE ERROR BECAUE FIRST YOU IMPORT OR INSTALL THE REQUIRED MODULE AFTER THAT
IT WILL GAVE ONE MORE ERROR WHICH IS PYAUDIO NOT FOUND  YOU JUST SOLVE ALOSO THIS ERROE AND THEN IT WILL BE RUN EXACTLY

error which it gives:
                    AttributeError: Could not find PyAudio; check installation


'''

import pyttsx3 # a module which is used for voice assistant
import datetime # module which tells about date and time
import speech_recognition as sr # it is used to get the microphone voice and also it converts voice in to string
import wikipedia # a module which search strings in the wikipedia
import webbrowser # a module which is used to open websites
import os # it deals with our operating systems
import random

engine=pyttsx3.init('sapi5') # sapi5 is just like a voice which speaks
voices=engine.getProperty('voices')
#print(voices[1].id) # if we print this will give the name of assistant whic speaks

engine.setProperty('voice',voices[1].id) # here we set our voice to the assistane who has id index 1 means


def speak(audio): # a function which will be speak
    engine.say(audio) # assitant say these words
    engine.runAndWait() # wait for little

def time_teller(): # it is a function which is tell the curreent date and time
    ghanty=int(datetime.datetime.now().hour)
    if ghanty>0 and ghanty<12: # these are used to saying time
        print("Good Morning sir Rehman Ali R A")
        speak("Good Morning sir Rehman Ali R A")
    elif ghanty>=12 and ghanty<18:
        print("Good After Noon sir Rehman Ali R A")
        speak("Good After Noon sir Rehman Ali R A")
    else:
        print("Good Evening sir Rehman Ali R A")
        speak("Good Evening sir Rehman Ali R A")

    speak("Hello,sir i am Jarvis Assistant of Rehman Ali R A How Can i help you?")

def take_command(): # it is a function first which is used to convert audio and return us as stirng also we can say which is used
                    # to recongnize our voice through the microphone

    r=sr.Recognizer()  # it start recongnizing from here
    with sr.Microphone() as source: # we use microphone which is in the module of speech_recognizer which is used to take
                                # voice from the microphone
        print("Sir I am Listening......") # after using microphone it starts listing

        r.pause_threshold=1 # thrus hold means it take delay 1 second means if we cant speak in one second  it cant execute
                                # after 1 sec if we not speak then it will start execution

        audio=r.listen(source) # here we store all the listening microphone string in the audio and it will be play


    try: # as we know try and except if it will run then this process executed
        print("Recognizing....")
        querry=r.recognize_google(audio,language='en-us') # it will use the google languge ex google assistant here
    except Exception as e:
      #  print(e) it prints the problem if occured
        print("Sorry sir i cant listen you please say again..")
        return "None" # return none as string No Problem

    return querry # return querry if there will any problem it again return the querry
if __name__ == '__main__':
    time_teller()
    while True: # use while run again and again
        querry=take_command().lower()  # it takes all the string as lower case which will not create  problem

        if 'wikipedia' in querry: # if we say anyname and after that in wikipedia it will search and give details
            print("Searching in wikipedia...")
            querry=querry.replace("wikipedia", "") # here we replace wikipedia with empty string

            results=wikipedia.summary(querry, sentences=2) # here we store all summry in results and sentence means it will read only two sentences
            print(results) # it will prints the all search from wiki pedia

            speak(results) # iit will speaks the search result

        elif 'open google' in querry:  # which website you want just write
            webbrowser.open("google.com")

        elif 'open youtube' in querry:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in querry:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in querry:
            webbrowser.open("facebook.com")

        elif 'open instagram' in querry:
            webbrowser.open("instagram.com")
        elif 'play music' in querry:

            songs_directory='R:\\RA new songs' # here we gave the directory of our favrout songs \\ means who escape the sequence
            songs=os.mkdir(songs_directory) # it will have directory of the sogs

            #songs=songs[random.randint(len(songs))] it will pick the random but i not implement this

            print(songs)
            os.startfile(os.path.join(songs_directory,songs[1])) #[1] means it will play that song who as that index we can also use random


        # now write as much as you want add more websites also add your computer
        # if you adding your computer file rember change the directory in this code directory is mine used













