import requests
import json
from plugs.config import *


def fury_response(command,user="Vishnu",key=carter_key_fury):
    response = requests.post("https://api.carterlabs.ai/chat", headers={
        "Content-Type": "application/json"
    }, data=json.dumps({
        "text": f"{user} : {command}",
        "key": key,
        "user_id": user 
    }))
    return response.json()['output']['text']

def opener_fury(key=carter_key_fury):

    reqUrl = "https://api.carterlabs.ai/opener"
    headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json" 
    }

    payload = json.dumps({
    "key":key,
    "user_id": "007",
    "personal": True  
    })

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
    return response.json()['output']['text']

def paraphraser_fury(text,key=carter_key_fury):

    reqUrl = "https://api.carterlabs.ai/personalise"

    headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json" 
    }

    payload = json.dumps({
    "key": key,
    "text": text,
    "user_id": "007",
    "speak": False
    })

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

    return response.json()['output']['text']

