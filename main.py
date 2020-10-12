# import the google speech text
import gtts
import datetime
from playsound import playsound
from utils import is_connected


def onlineConversion(input):
    input = gtts.gTTS(input)
    ts = datetime.datetime.now().timestamp()
    input.save("output/"+str(ts)+'.mp3')
    playsound("output/"+str(ts)+'.mp3')

def offlineConversion(input):
    print("from offline")


def main():
    _input = input("Veuillez entrer votre texte: ")
    print(_input)
    if is_connected():
        onlineConversion(_input)
    else:
        offlineConversion(_input)


if __name__ == "__main__":
    main()
