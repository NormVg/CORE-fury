import os

from plugs.transcriber import speech_To_text,text_to_speech
from plugs.api_manager import *
from plugs.carter_client_fury import *


def clear_temp(file):
    os.remove(f"temp/{file}")

def clear_all_speak():
    
    li = os.listdir("temp/speak/")
    if len(li )>7:
        for i in li:
            os.remove("temp/speak/"+i)

def fury_init(file):
    print(file)
    
    command = speech_To_text(file)
    print(command)
    intent = IRS(command)
    print(intent)
    if intent['irs'] == "000":
        #not recognised 
        resp = fury_response(command)
        
    else:    
        resp = fury_response(command)
    
    file = text_to_speech(resp)
    data = {"reply":resp,"audio":file}
    
    return data