"""
front end type stuff
"""
import urllib.request
from multiprocessing import Process, Queue, Pipe
import json

#URL = "https://yebrandon.github.io/smart-windows/data/"
URL = "http://10.10.10.160/data/"
#URL = "http://130.15.38.40/data/"

#for getting data
def get_request(url):
    request = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data['data']

#for sending data
def post_request(url, b):
    body = urllib.parse.urlencode(b).encode('ascii')
    request = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data['data']

#returns temp inside value
def getTemp():
    tempURL = URL+"temp"
    temp = get_request(tempURL)
    return temp

#returns humidity inside value
def getHumidity():
    humidityURL = URL+"humidity"
    humidity = get_request(humidityURL)
    return humidity

#returns percipitation value
def getPercipitation():
    percipitationURL = URL+"precip"
    percipitation = get_request(percipitationURL)
    return percipitation

#returns window state
def getWindowState():
    windowURL = URL+"windowState"
    window = get_request(windowURL)
    return window

#returns settings
def getSettings():
    settingsURL = URL+"settings"
    settings = get_request(settingsURL)
    return settings
    
if __name__ == "__main__":
    print(getTemp())

