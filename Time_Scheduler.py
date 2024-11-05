import os
import datetime
import pyttsx3
import time
import Project_G


def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    with open("log.txt", 'a') as f:
        f.write(f"You drank water {now} \n")
    return 0


def getTimeInput():
    # hour = int(input(speak("hours of interval :")))
    speak("Please set the hours: ")
    # Here voice command is changed into the integer value
    # hour = int(proj1.takeCommand())
    hour = int(input("Enter the hour: "))
    speak("Please set the minutes: ")
    # minutes = int(proj1.takeCommand())
    minutes = int(input("Enter the minutes: "))
    speak("Please set the seconds: ")
    # seconds = int(proj1.takeCommand())
    seconds = int(input("Enter the seconds: "))
    time_interval = seconds+(minutes*60)+(hour*3600)
    return time_interval


def notify(title, text):
    # log()
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


notify("Please, Drink Water", "Heres an alert")

engine = pyttsx3.init()


def speak(audio):
    # audio = str(audio)

    engine.say(audio)
    engine.runAndWait()


speak('Please, Drink Water Sir')


def starttime(time_interval):
    while True:
        time.sleep(time_interval)
        notify("Please, Drink Water", "Heres an alert")
        log()
        speak("Please, Drink Water Sir")


# if __name__ == '__main__':
time_interval = getTimeInput()
starttime(time_interval)
