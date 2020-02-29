"""
Acts as the central processing file for the r-pi
"""

#imports
import server_interactions as server
import time
import check_sensors as sense

#updates the current data from the r-pi
def updateData(node):
    return {"temp" : sense.getTemp(node), "humidity" : sense.getHum(node), "precip" : sense.getPrec(node), "window" : window_state}

#define the end URL and setup the node
URL = "http://10.10.10.160/data/"
cmd_location = "commands"
node = sense.setupNode()
window_state = True

#main loop
while(True):
    #upload the current data to the server
    data = updateData(node)
    for key, dat in data.items():
        print(server.post_request(URL+key, {"data" : dat}))
    
    #retrieve instructions from the server
    print(server.get_request(URL+cmd_location))

    time.sleep(10)