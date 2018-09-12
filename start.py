#!/usr/bin/python3

#-*- coding: utf-8 -*-

#from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import re
import os, signal
import speech_recognition as sr
#from threading import Thread
import pyttsx3
import time
from gtts import gTTS
#from pygame import mixer
import vlc

speaker = pyttsx3.init()

def criarvoz(text,lang,filename):
    file = gTTS(text = text, lang=lang)
    filenamez = '/usr/tmp/'+str(filename)
    file.save(filenamez)

def speak(text):
    speaker.say(text)
    speaker.runAndWait()    

bot = ChatBot('Bot_teste',read_only=True)

r = sr.Recognizer()

#criarvoz('Em que posso lhe ser útil?','pt','util.mp3')


with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    while True:
        try:
            print("esperando")
            falainicial = r.listen(s)
            fala = r.recognize_google(falainicial, language='pt')
            fala = fala.lower()
            print(fala)
            if fala == 'lara':
                player = vlc.MediaPlayer("voz/util.mp3")
                
                #mixer.music.play()
                player.play()
                time.sleep(0.5)
               # speak('Em que posso lhe ser útil')
                try:
                    variavelnome = ''
                    time.sleep(0.5)
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
                                os.system('/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=spotify --file-forwarding com.spotify.Client @@u %U @@ &')   
                                print("Abriu spotify via flatpak")
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


                except:
                    print("..")        
    
        
        except:
            print("Lara inativa")    


# TREINAR FALAS BOT
#"""bot.set_trainer(ListTrainer)
#
#for _file in os.listdir('chats'): #ler todoshtop arqs de chat
#    lines = open('chats/'+_file,'r').readlines() 
#    bot.train(lines)
#"""
#
