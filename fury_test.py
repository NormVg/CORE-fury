import speech_recognition as sr
from googletrans import Translator
import requests

translator = Translator()
client = requests.Session()


def fury():
    r = sr.Recognizer()
                                                            
    audio = sr.Microphone()

    with audio as source:
        audio = r.listen(source)
        with open("fury_test_spr.wav","wb") as f:
            f.write(audio.get_wav_data())

    files = {'file': open('fury_test_spr.wav', 'rb')}
    res = client.post("http://127.0.0.1:2002/fury",files=files).text
    print(res)

while True:
    input("> ")
    fury()

