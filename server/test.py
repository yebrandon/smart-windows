# Tests basic GET and POST requests on the server
# Make sure to run server.py first before this

import urllib.request
import json

def get_request(url):
    request = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data

def post_request(url, b):
    body = urllib.parse.urlencode(b).encode('ascii')
    request = urllib.request.Request(url, data=body, method="POST")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data

test_data = {
    "data": 12
}

# This should return a dict with a key "data" that has a string value with the contents of the temp file
print(get_request("http://127.0.0.1/data/temp"))

# This should write "12" to the temp file
print(post_request("http://127.0.0.1/data/temp", test_data))