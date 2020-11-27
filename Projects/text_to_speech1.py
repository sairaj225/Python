from gtts import gTTS # pip install gtts

from playsound import playsound # pip install playsound

audio = 'speech.mp3'

language = 'en'

text = input("Enter text which you want to convert into speech: ")

sp = gTTS(text = text, lang=language, slow=False)

sp.save(audio)

playsound(audio)