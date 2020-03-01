"""
Sends and recieves all the sensor readings from the Raspberry PI to the server.
"""

#import the requests library
import urllib.request
import json
import time

#sends the collected data to the server
def post_request(url, b):
    body = urllib.parse.urlencode(b).encode('ascii')
    request = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data

#recieves data from the server
def get_request(url):
    request = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data