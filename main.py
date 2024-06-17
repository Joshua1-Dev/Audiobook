from gtts import gTTS
import time
file = input("what kind of file? csv,xlsx,txt,json,sql,html,pdf...\n")
path = input("input file path\n")
audio = input("what would you like to name the audio? \n")
from PyPDF2 import PdfReader

def pdf():
    reader = PdfReader(path)
    pages = len(reader.pages)
    for i in range(0, pages):
        page = reader.pages[i]
        data = page.extract_text()
        if data == '':
            print("empty page unto the next")
        else:
            tts = gTTS(text=data, lang='en')
            tts.save(audio)

            from pygame import mixer  # Load the popular external library

            mixer.init()
            mixer.music.load(audio)
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                time.sleep(1)
def other_files():
    try:
        with open(path) as file:
            data = file.readlines()
            if data == '':
                print("empty page unto the next")
            else:
                tts = gTTS(text=data, lang='en')
                tts.save(audio)

                from pygame import mixer  # Load the popular external library

                mixer.init()
                mixer.music.load(audio)
                mixer.music.play()
                while mixer.music.get_busy():  # wait for music to finish playing
                    time.sleep(1)
    except:
        print("program does not accept this kind of file")

if file == 'pdf':
    pdf()
else:
    other_files()