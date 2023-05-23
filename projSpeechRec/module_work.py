# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:54:08 2023

@author: Proph
"""
import webbrowser
import subprocess
import os

def open_site(x):
    webbrowser.open_new_tab(x)
    
def open_prog(x):
    if x == 1:
        subprocess.Popen('C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
    elif x == 2:
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    elif x == 3:
        subprocess.Popen('C:\\Program Files (x86)\\Steam\\steam.exe')
    elif x == 4:
        subprocess.Popen('C:\\Users\\Proph\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe')
    #subprocess.call("taskkill", "/f", "/im", "calc.exe")
    

def close_prog(x):
    os.system("taskkill /f /im Calculator.exe")
    #calculator
    #subprocess.call(["taskkill","/K","/IM","EpicGamesLauncher.exe"])
    
#open_prog()
#close_prog()