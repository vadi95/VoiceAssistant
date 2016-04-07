import webbrowser
import subprocess
import speech_recognition as sr
import os

# obtain audio from the microphone
r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Hey there! What can I help you with ?")
        audio = r.listen(source)

    print "Analysing ... "

    text = ""

    try:
        text = r.recognize_google(audio)
        print("You said : " + text)
        parameter = ""
        text = text.lower()
        command = text.split(' ', 1)[0]
        if ' ' in text:
            parameter = text.split(' ', 1)[1]

        if text == "stop":
            break

        if command == "chrome":
            if parameter != "":
                webbrowser.open_new_tab("http://" + parameter.replace(" ", "") + ".com")
            else:
                webbrowser.open_new_tab("http://google.co.in")
        elif command == "search":
            webbrowser.open_new_tab("https://www.google.co.in/#q=" + parameter.replace(" ", "+"))
        else:
            if "javascript" in text:
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
        print("You said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
    except:
        pass


