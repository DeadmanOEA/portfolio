import PySimpleGUI as sg
import speech_recognition as sr
import neuro
import module_work


def listen():
    voice_recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Buyruq ayt (Произнесите комманду)")
        audio = voice_recognizer.listen(source)
    
    try:
        voice_text = voice_recognizer.recognize_google(audio, language="uz")#ru
        #print(f"Siz aytdingiz (Вы сказали): {voice_text}")
        return voice_text
    except sr.UnknownValueError:
        return "tanib olish xatosi(ошибка распознавания)"
    except sr.RequerestError:
        return "So‘rov bajarilmadi(ошибка запроса)"

def handle_command(command):
    #command = command.lower()
    if command == 0.001:
        print(0.001)
    elif command == 0.002:
        print(0.002)
    elif command == 0.003:
        module_work.open_site('https://google.com')
    elif command == 0.004:
        module_work.open_site('https://google.com')
    elif command == 0.005:
        module_work.open_site('https://vk.com')
    elif command == 0.006:
        module_work.open_site('https://www.gismeteo.ru/weather-moscow-4368/now/')
    elif command == 0.007:
        module_work.open_prog(1)
    elif command == 0.008:
        module_work.open_prog(2)
    elif command == 0.009:
        module_work.open_prog(3)
    elif command == 0.010:
        module_work.open_prog(4)
    else:
        print("Noma'lum jamoa")

def stop():
    exit()

def start():
    print("Assistantni ishga tushiring")
    command = listen()
    print(command)
    outputs = neuro.find_command(command)
    print(outputs)
    print(round(outputs, 3))
    
    handle_command(round(outputs, 3))
        
        


sg.theme("DarkBlue")

layout = [
    [sg.Button("Yugur", key = ("START")), sg.Button("Tugatish", key = ("STOP"))],
    [sg.Output(size=(60, 20))],
    [sg.Cancel()]
]
window = sg.Window('File Compare', layout)

while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'START':
        start()
    elif event == 'STOP':
        stop()
window.close()