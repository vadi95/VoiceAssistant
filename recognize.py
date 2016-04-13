import webbrowser
import subprocess
import speech_recognition as sr
import os
import colorama
from colorama import Fore

colorama.init()

def music_handler(text):
    if "play" in text:
        os.system("rhythmbox-client --play")
    elif "pause" in text:
        os.system("rhythmbox-client --pause")
    elif "stop" in text:
        os.system("rhythmbox-client --quit")
    elif "next" in text:
        os.system("rhythmbox-client --next")
    elif "previous" in text:
        os.system("rhythmbox-client --previous")
    elif "lyrics" in text:
        title = os.popen("rhythmbox-client --print-playing").read()
        webbrowser.open_new_tab("https://www.google.co.in/search?q=" + title + " lyrics&btnI=")


def execute_task(text):
    parameter = ""
    text = text.lower()
    command = text.split(' ', 1)[0]
    if ' ' in text:
        parameter = text.split(' ', 1)[1]

    if command == "chrome":
        if parameter != "":
            webbrowser.open_new_tab("http://" + parameter.replace(" ", "") + ".com")
        else:
            webbrowser.open_new_tab("http://google.co.in")
    elif command == "search":
        webbrowser.open_new_tab("https://www.google.co.in/#q=" + parameter.replace(" ", "+"))
    elif text.startswith("i'm feeling lucky") or text.startswith("i am feeling lucky"):
        webbrowser.open_new_tab("https://www.google.co.in/search?q=" + text.replace("i'm feeling lucky", "")
                                .replace(" ", "+") + "&btnI=").replace("i am feeling lucky", "")
    elif "music" in text or "song" in text:
        music_handler(text)
    elif "javascript" in text:
        subprocess.Popen(["webstorm.sh"])
    elif "python" in text:
        subprocess.Popen(["pycharm.sh"])
    elif "kill" in text:
        os.system("pkill " + str(parameter))
    elif "shutdown" == text:
        os.system("sudo poweroff")
    elif "restart" == text:
        os.system("sudo reboot")
    elif "terminal" == text:
        os.system("gnome-terminal &")
    else:
        subprocess.Popen([text])

# obtain audio from the microphone
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Hey there! What can I help you with?")
        audio = r.listen(source)

    print "Analysing ... "

    try:
        text = r.recognize_google(audio)
        print("You said : " + Fore.RED + text + Fore.WHITE)
        execute_task(text)

        if text == "stop":
            break
    except sr.UnknownValueError:
        print("Didn't catch that!")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
    except:
        pass
