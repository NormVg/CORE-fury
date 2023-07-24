import os

from plugs.transcriber import speech_To_text
from plugs.api_manager import *
from plugs.carter_client_fury import *


def clear_temp(file):
    os.remove(f"temp/{file}")



def fury_init(file):
    print(file)
    
    command = speech_To_text(file)
    print(command)
    intent = IRS(command)
    print(intent)
    if intent['irs'] == "000":
        #not recognised 
        resp = fury_response(command)
        return resp
    else:    
        resp = fury_response(command)
        return resp