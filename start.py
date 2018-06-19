#-*- coding: utf-8 -*-

#importando os modulos do chatbot

#from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import re
import os
import speech_recognition as sr
#from threading import Thread
#import pyttsx3
#import gtts

#speaker = pyttsx3.init()

#def speak(text):
    
#    speaker.say(text)
#    speaker.runAndWait()


bot = ChatBot('Bot_teste',read_only=True)

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    while True:
        try:
            variavelnome = ''
            audio = r.listen(s)
            speech = r.recognize_google(audio, language='pt')
            print('Você disse: ',speech)
            response = bot.get_response(speech)
            abrir = speech.split(' ')[0]
            #print (a)            
            speech_cortada = speech.split(None, 1)[1]
            #print(speech_cortada)
            if abrir.lower() =='abrir':
                variavelnome = speech_cortada.lower()
                print (variavelnome)
                if (variavelnome == 'visual studio code') :
                    print("abrindo visual sutdio code")
                    variavelnome = '/opt/visual-studio-code/code'
                elif variavelnome == 'steam':
                    print("abrindo steam-runtime")
                    variavelnome = '/usr/bin/steam-runtime %U'
                elif variavelnome == 'android studio':
                    print("Abrindo androidstudio")
                    variavelnome = '~/android-studio/bin/studio.sh'
                elif variavelnome == 'google chrome':# or 'chrome':
                    print("abrindo chrome")
                    variavelnome = 'google-chrome-stable'
                elif variavelnome == 'spotify':
                    print("abrindo spotify")
                    try:
                        #OPEN FLATPAK SPOTIFY
                        os.system('/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=spotify --file-forwarding com.spotify.Client @@u %U @@')   
                        print("taqui")
                    except:
                        #SPOTIFY ON usr/bin
                        variavelnome = 'spotify'    


                #if variavelnome == 'sublime' or 'sublime text 3' or 'sublime text': #or 'sublime text 3' or 'sublime':
                #    variavelnome = '/usr/bin/subl3'  
                os.system(variavelnome+'&')
            if abrir.lower() =='procure' or abrir.lower() =='pesquise' :
                variavelprocura = speech_cortada.lower()
                print (variavelprocura) 
                #STRING PARA GOOGLE
                googlestr = re.sub(' ','%20',variavelprocura)
                os.system('google-chrome-stable https://www.google.com.br/search?q='+googlestr)
                

            
            #subprocess.call('/usr/bin/atom')#'/usr/bin/'+speech.lower())
            #print('Bot: ',bot.get_response(speech))
            #speak(response)

        except:
            print(".")
        


# TREINAR FALAS BOT
"""bot.set_trainer(ListTrainer)

for _file in os.listdir('chats'): #ler todoshtop arqs de chat
    lines = open('chats/'+_file,'r').readlines() 
    bot.train(lines)
"""
