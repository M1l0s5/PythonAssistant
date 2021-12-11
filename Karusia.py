import speech_recognition as sr #pip install SpeechRecognition
import webbrowser as wb
import cv2 #pip install opencv-python
import datetime
import pyautogui #pip install pyautogui
from win32com.client import Dispatch #pip install pywin32
import os
import winshell
import keyboard #keyboard.send('przyciski do klikania') #pip install keyboard
import winsound
import time
speak=Dispatch("SAPI.SpVoice")
a=1
def screenek(zdjcounter):
    pyautogui.screenshot()
    ss=pyautogui.screenshot()
    nazwazdjecia="ss_{}.png".format(zdjcounter)
    ss.save(nazwazdjecia)
#def muzyczka():
#    winsound.PlaySound('rocky.wav',winsound.SND_ASYNC)
def oproznieniekosza():
    winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
    speak.Speak("Kosz został opróżniony") 
def czasteraz():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clock
    speak.Speak("teraz jest ")
    speak.Speak(Time)
def googlowanie():
    speak.Speak("Co mam wyszukać?")
    szukanegooglowskie = take_cmd().lower()
    wb.open('https://www.google.com/search?q='+szukanegooglowskie)
def selficzek():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("kamera")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("błąd")
            break
        cv2.imshow("kamera", frame)
        k = cv2.waitKey(1)
        if k%256 == 27: #escape na klawicie
            break
        elif k%256 == 32:
        # SPACE pressed
            img_name = "selficzek_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            speak.Speak('Zapisano zdjecie')
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
def powitanie():
    speak.Speak('Dzień dobry, nazywam się Karusia i jestem do waszych usług')
def odpalsteama():
    steamowadroga=r"C:\Program Files (x86)\Steam\steam.exe"
    os.startfile(steamowadroga)
def randomgra():
    gra1droga=r"W:\Games\steamapps\common\DOOM\DOOMx64.exe"
    gra2droga=r"W:\Games\steamapps\common\ShadowOfMordor\x64\ShadowOfMordor"
    gra3droga=r"W:\Games\steamapps\common\the witcher 2\Launcher.exe"
    gra4droga=r"D:\Games\Assassin's Creed II\AssassinsCreedGame.exe"
    gra5droga=r"D:\Games\Assassin's Creed Revelations\AssassinsCreedRevelations.exe"
    gra6droga=r"D:\Games\Assassin's Creed Syndicate\ACS.exe"
def dziendobry():
    speak.Speak('Dzień dobry')
def odpalubi():
    ubidroga=r"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\UbisoftConnect.exe"
    os.startfile(ubidroga)
def odpalepica():
    epicdroga=r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"
    os.startfile(epicdroga)
def datarmd():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak.Speak("Dzisiejsza pełna data to")
    speak.Speak(date)
    speak.Speak(month)
    speak.Speak(year)
def ytszukanko():
    speak.Speak('co chcesz wyszukać?')
    szukany_filmik=take_cmd().lower()
    wb.open('https://www.youtube.com/results?search_query='+szukany_filmik)
def take_cmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Słucham...')
        r.pasue_threshold=1
        audio=r.listen(source)
    try:
        print('Rozpoznaję dźwięk...')
        query=r.recognize_google(audio , language='pl-in')
        print(query)
    except Exception as e:
        print(e)
        print('Nie rozumiem co mówisz, powtorz')
        return 'none'
    return query
powitanie()
while True:
    query=take_cmd().lower()
    if 'youtube' in query:
        ytszukanko()
    elif 'selfie' in query:
        selficzek()
    elif 'jak się masz' in query:
        speak.Speak('spoko')
    elif 'kim jesteś' in query:
        speak.Speak('Twoim prywatnym asystentem')
    elif 'notatka' in query:
        speak.Speak('co mam zapamietac')
        notes=take_cmd()
        file=open('notes.txt', 'a')
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(strTime)
        file.write(" :- ")
        file.write(notes)
        speak.Speak('skonczono pisac notatke')
        file.close()
    elif 'googluj' in query or 'google' in query:
        googlowanie()
    elif 'data' in query:
        datarmd()
    elif 'opróżnij kosz' in query:
        oproznieniekosza()
    elif 'wyloguj' in query:
        os.system("shutdown -l")
    elif 'restart' in query:
        os.system("shutdown /r /t 1")
    elif 'zamknij system' in query:
        speak.Speak('Zamykanie systemu')
        os.system("shutdown /s /t 1")
    elif 'czas' in query:
        czasteraz()
    elif 'do widzenia' in query:
        quit()
    elif 'word' in query:
        msword=r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
        os.startfile(msword)
    elif 'screenshot' in query:
        screenek(a)
        a+=1
    elif 'steam' in query:
        odpalsteama()
    elif 'ubisoft' in query:
        odpalubi()
    elif 'epic' in query:
        odpalepica()
    #elif 'zablokuj' in query:
    #    keyboard.send('win+l')
    elif 'wszystko do grania' in query:
        odpalsteama()
        odpalepica()
        odpalubi()
    elif 'dzień dobry' in query:
        dziendobry()
    elif 'jasiunio' in query:
        speka.Speak('jasiunio być musi przy swojej karusi')
    elif 'przestań słuchać' in query:
        speak.Speak('Na ile sekund mam przestać słuchać?')
        odpdotyczacaczasu=int(take_cmd())
        time.sleep(odpdotyczacaczasu)
        print(odpdotyczacaczasu)
    elif 'gdzie jest' in query:
        query=query.replace("gdzie jest","")
        location=query
        speak.Speak(location+"jest tutaj")
        wb.open_new_tab("https://google.com/maps/place/"+location)
    elif 'dzięki' in query or 'dziękuję' in query:
        speak.Speak('nie ma za co')
