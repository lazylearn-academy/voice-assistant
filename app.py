import subprocess
import time
import os
import speech_recognition as sr
import pyttsx3
import datetime

def open_jupyter():
    subprocess.Popen("jupyter-notebook", shell=True)


def open_browser():
    subprocess.Popen(["start", "msedge.exe"], shell=True)


def close_browser():
    subprocess.Popen(["taskkill", "/im", "msedge.exe", "/f"], shell=True)


def desktop():
    subprocess.Popen(["explorer", "C:/Users/danil/OneDrive/Desktop"], shell=True)


def downloads():
    subprocess.Popen(["explorer", "C:/Users/danil/Downloads"], shell=True)


def shutdown():
    os.system("shutdown /s")


def console():
    subprocess.Popen("cmd.exe /K cd /", shell=True)


def listen_for_command():
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)

    IS_ACTIVE = False

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            print("Слушаю команду...")
            audio = recognizer.listen(source)

            try:
                command = recognizer.recognize_google(audio, language="ru-RU").lower()
                print(f"Вы произнесли: {command}")

                if command == "открой юпитер" and IS_ACTIVE:
                    engine.say("Yes sir!")
                    engine.runAndWait()
                    open_jupyter()

                elif command == "открой браузер" and IS_ACTIVE:
                    engine.say("Yes sir!")
                    engine.runAndWait()
                    open_browser()

                elif command == "закрой браузер" and IS_ACTIVE:
                    engine.say("Yes sir!")
                    engine.runAndWait()
                    close_browser()

                
                elif command == "рабочий стол" and IS_ACTIVE:
                    engine.say("Yes sir!")
                    engine.runAndWait()
                    desktop()

                elif command == "загрузки" and IS_ACTIVE:
                    engine.say("Yes sir!")
                    engine.runAndWait()
                    downloads()

                elif command == "время" and IS_ACTIVE:
                    now = datetime.datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    engine.say(f"Time is {current_time}")
                    engine.runAndWait()

                elif command == "дата" and IS_ACTIVE:
                    today = datetime.date.today()
                    engine.say(f"Date is {today}")
                    engine.runAndWait()

                elif command == "выруби комп" and IS_ACTIVE:
                    engine.say("Goodbye my dear friend!")
                    engine.runAndWait()
                    shutdown()

                elif command == "консоль" and IS_ACTIVE:
                    engine.say("Yes sir!")
                    engine.runAndWait()
                    console()
                elif command == "активация ассистента":
                    engine.say("Assistant activated")
                    engine.runAndWait()
                    IS_ACTIVE = True

                elif command == "деактивация ассистента":
                    engine.say("Assistant deactivated")
                    engine.runAndWait()
                    IS_ACTIVE = False

                
            except sr.UnknownValueError:
                print("Не распознала команду.")
            except sr.RequestError:
                print("Ошибка соединения с сервисом распознавания.")



if __name__ == "__main__":
    while True:
        listen_for_command()
        time.sleep(1)
