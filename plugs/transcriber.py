import speech_recognition as sr
from googletrans import Translator
import edge_tts
import asyncio

from plugs.filename_gen import filename_gen


translator = Translator()

def speech_To_text(file):
    r = sr.Recognizer()
                                                            
    audio = sr.AudioFile(file)

    with audio as source:
        try:
            audio = r.record(source)                  
            result = r.recognize_google(audio,language="hi")
            result = translator.translate(result,dest="en").text
        except:
            result = ""
    print(result)
    return result

def text_to_speech(text):
    
    VOICE = "en-IN-PrabhatNeural"
    OUTPUT_FILE = filename_gen(extention=".wav")
    async def amain():

        communicate = edge_tts.Communicate(text, VOICE,rate="+10%")
        await communicate.save(OUTPUT_FILE)
    asyncio.run(amain())

# text_to_speech("hi")