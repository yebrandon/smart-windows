"""
Sends all the sensor readings from the Raspberry PI to the server.
"""

#import the requests library
import urllib
import json
import time

#define the end URL
URL = "http://TODO"

#TODO, gather data
data = {"Konami" : "UP UP DOWN DOWN LEFT RIGHT LEFT RIGHT B A START"}

#main loop
while(True):
    text = post_request(URL, data)
    print(text)
    time.sleep(2)



#sends the collected data
def post_request(url, b):
    body = urllib.parse.urlencode(b).encode('ascii')
    request = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data

def get_URL():
    return URL