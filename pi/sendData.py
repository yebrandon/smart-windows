"""
Sends all the sensor readings from the Raspberry PI to the server.
"""

#import the requests library
import urllib
import json
import time
import checkSensors as sense

#define the end URL and setup the node
URL = "http://TODO"
node = sense.setupNode()

#updates the current data from the r-pi
def updateData(node):
    return {"temp" : sense.getTemp(node), "hum%" : sense.getHum(node), "prec" : sense.getPrec(node)}

#main loop
while(True):
    data = updateData(node)
    print(data)
    time.sleep(2)
    """
    text = post_request(URL, data)
    print(text)
    time.sleep(2)
    """

#sends the collected data
def post_request(url, b):
    body = urllib.parse.urlencode(b).encode('ascii')
    request = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data

def get_URL():
    return URL