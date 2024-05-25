import json
import requests
from .config import VER, BASE_URL_API

def Description():
    print(f"Tikos Platform {VER}")

def Version():
    print(VER)

def CreateExtractionRequest(url: str="", orgId: str="", orgToken: str="", userId: str="0", numOfFiles: str="1"):
    if url == "":
        url = BASE_URL_API

    result = requests.post(url + '/client/extractionrequest', json={'orgId': orgId, 'token': orgToken, 'userId': userId, 'numOfFiles': numOfFiles})
    return result.status_code, result.reason, result.text

def AddExtractionText(url: str="", requestId: str="", authToken: str="", text: str=""):
    if url == "":
        url = BASE_URL_API

    result = requests.post(url + '/client/storeprocesstext',
                           json={'requestId': requestId, 'authToken': authToken, 'chunk': text})
    return result.status_code, result.reason, result.text

def GetGraph(url: str="", requestId: str="", authToken: str=""):
    pass

def GenerateSC(url: str="", requestId: str="", authToken: str=""):
    pass

def GetRetrival(url: str="", orgId: str="", requestId: str="", authToken: str=""):
    pass
