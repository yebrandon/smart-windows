import urllib.request
import json

URL = "https://yebrandon.github.io/smart-windows/data/"

def get_request(url):#getting data
    request = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data

def post_request(url, b):#sending data
    body = urllib.parse.urlencode(b).encode('ascii')
    request = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data

def getTemp():
    #temp["houseTemp"] is house temp, temp["outsideTemp"], temp["set"]
    tempURL = URL+"temp"
    temp = get_request(tempURL);
    return temp

def getHumidity():
    humidityURL = URL+"humidity"
    humidity = get_request(humidityURL)
    return humidity

def getPercipitation():
    percipitationURL = URL+"percipitation"
    percipitation = get_request(percipitationURL)
    return percipitation

def getWindowState():
    windowURL = URL+"windowState"
    window = get_request(windowURL)
    return window

def getSettings():
    settingsURL = URL+"settings"
    settings = get_request(settingsURL)
    return settings
