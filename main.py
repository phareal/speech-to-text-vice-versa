# import the google speech text
import gtts
import datetime
from playsound import playsound
from utils import is_connected
import pyttsx3



def onlineConversion(input):
    print("Veuillez patientez pendant la conversion")
    input = gtts.gTTS(input)
    ts = datetime.datetime.now().timestamp()
    input.save("output/"+str(ts)+'.mp3')
    print("conversion terminé: la lecture debute :)")
    playsound("output/"+str(ts)+'.mp3')

def offlineConversion(input):
    print("Veuillez patientez pendant la conversion")
    engine = pyttsx3.init()
    print("conversion terminé: la lecture debute :)")
    engine.say(input)
    engine.runAndWait()


def main():
    _input = input("Veuillez entrer votre texte: ")
    print(_input)
    if is_connected():
        onlineConversion(_input)
    else:
        offlineConversion(_input)


if __name__ == "__main__":
    main()
