import speech_recognition as sr
from gtts import gTTS
import random
#import playsound
import os

def listen():
    voice_recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Buyruq ayt (Произнесите комманду)")
        audio = voice_recognizer.listen(source)
    
    try:
        voice_text = voice_recognizer.recognize_google(audio, language="uz")#ru
        print(f"Siz aytdingiz (Вы сказали): {voice_text}")
        return voice_text
    except sr.UnknownValueError:
        return "tanib olish xatosi(ошибка распознавания)"
    except sr.RequerestError:
        return "So‘rov bajarilmadi(ошибка запроса)"

def say(text):
    voice = gTTS(text, lang="ru")
    unique_file = "audio_" + str(random.randint(0,10000)) + ".mp3"
    voice.save(unique_file)
    
    #playsound.playsound(unique_file)
    os.remove(unique_file)
    
    print(f"Yordamchi(Ассистент): {text}")

def handle_command(command):
    command = command.lower()
    
    if command == "salom":
        say("Salom(Привет)")
    elif command == "xayr":
        stop()
    elif command == "televizorni yoqing":
        say("Televizorni yoqyapman(Включаю телевизор)")
    elif command == "сhoynakni yoqing":
        say("Choynakni yoqaman(Включаю чайник)")
    elif command == "сhoynakning yoqing":
        say("Choynakni yoqaman(Включаю чайник)")
    elif command == "choynakning yoki":
        say("Choynakni yoqaman(Включаю чайник)")
    elif command == "chiroqlarni yoqing":
        say("Men chiroqni yoqaman(Включаю свет)")
    elif command == "chiroqni oʻchiring":
        say("chiroqni oʻchiring (Выключаю свет)")
    elif command == "tilni o'zgartirish":
        say("Выполняю смену языка")
    else:
        say("Неизвестная команда")

def stop():
    say("Ko'rishguncha(До скорого)")
    exit()

def start():
    print("Assistantni ishga tushiring(Запуск ассистента)")
    
    while True:
        command = listen()
        handle_command(command)

try:
    start()
except KeyboardInterrupt:
    stop()