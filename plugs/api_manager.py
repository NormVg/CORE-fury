import requests

client  =  requests.Session()

def IRS(text):
    url = "https://ner-irs.onrender.com/api/irs?input="+text
    resp = client.get(url).json()
    return resp.get("exe")

def NER(text):
    url = "https://ner-irs.onrender.com/api/ner?input="+text
    resp = client.get(url).json()
    print(resp)

def Gender_reco(file):
    pass

