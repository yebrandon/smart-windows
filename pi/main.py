"""
Acts as the central processing file for the r-pi
"""

#imports
import server_interactions as server
import time
import check_sensors as sense
import offline

#define the end URL and setup the node
URL = "http://10.10.10.160/data/"
cmd_location = "command"
node = sense.setupNode()
window_state = "open"
settings = ""
response = {} 
timeout_counter = 0

#updates the current data from the r-pi
def update_data(node):
    return {"temp" : sense.get_temp(node), "humidity" : sense.get_hum(node), "precip" : sense.get_prec(node), "windowState" : window_state}

#main loop
while(True):
    #update the data
    data = update_data(node)
    disconnect = False
    delay = 2

    #upload the current data to the server
    for key, dat in data.items():
        response[key] = server.post_request(URL+key, {"data" : dat})
        
        #if an error occurred
        if (response[key]["error"]):
            disconnect = True
            print("Failed to send " + key + " data.")
            print(response[key])

    #retrieve instructions from the server
    cmd = server.get_request(URL+cmd_location)
    if (cmd["error"]):
        disconnect = True
        print("Failed to recieve cmd data.")
        print(cmd)

    if (cmd["data"] == "open" or cmd["data"] == "close"):
        window_state = cmd

    #preform offline logic if server cannot be reached
    if (disconnect):
        window_state, delay, timeout_counter = offline.update(data, timeout_counter)

    print("--------------------------------")
    #wait
    time.sleep(delay)