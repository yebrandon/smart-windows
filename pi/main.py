"""
Acts as the central processing file for the r-pi
"""

#imports
import server_interactions as server
import time as t
import check_sensors as sense
import offline

#define the end URL and setup the node
URL = "http://10.10.10.160/data/"
node = sense.setupNode()
window_state = "open"
cmd_location = "command"
#set_location = "settings"
response = {} 
timeout_counter = 0
delay = 2

#updates the current data from the r-pi
def update_data(node):
    return {"temp" : sense.get_temp(node), "humidity" : sense.get_hum(node), "precip" : sense.get_prec(node), "windowState" : window_state}

#states whether the window should be held in the current position or not for a set amount of time
"""
def hold_window(start_time, end_time):
    if (end_time <= start_time):
        return False
    return True
"""

#main loop
while(True):
    #update the data
    data = update_data(node)
    disconnect = False

    #upload the current data to the server
    for key, dat in data.items():
        try:
            response[key] = server.post_request(URL+key, {"data" : dat})
        except (Exception):
            response[key] = {"error" : True}
            print("Error occurred while saving " + key + " data. Route issue?")
        
        #if an error occurred
        if (response[key]["error"]):
            disconnect = True
            print("Failed to send " + key + " data.")
            print(response[key])

    #retrieve instructions from the server
    try:
        cmd = server.get_request(URL+cmd_location)
    except (Exception):
        cmd = {"error" : True}
        print("Error occurred while retrieving cmd data. Route issue?")
    
    """
    try:
        setting = server.get_request(URL+set_location)
    except (Exception):
        setting = {"error" : True}
        print("Error occurred while retrieving setting data. Route issue?")
    """
    
    if (cmd["data"] == ""):
        print("No commands found.")
    elif (cmd["error"]):
        disconnect = True
        print("Failed to recieve cmd data.")
        print(cmd)
    elif (cmd["data"] == "open" or cmd["data"] == "close"):
        window_state = cmd["data"]
        print(cmd)
    
    """
    if (setting["error"]):
        disconnect = True
        print("Failed to recieve setting data.")
        print(setting["error"])
    else:
        #calculate time
        end_time = t.time() + setting["time"]
        hold_window(t.time(), end_time)
    """

    #preform offline logic if server cannot be reached
    if (disconnect):
        window_state, delay, timeout_counter = offline.update(data, timeout_counter)
    elif (timeout_counter != 0):
        timeout_counter = 0
        delay = 2

    print("Current state: ")
    print("Temp: " + str(data["temp"]))
    print("Hum.: " + str(data["humidity"]))
    print("Prec: " + str(data["precip"]))
    print("Win.: " + window_state)

    print("--------------------------------")
    #wait
    t.sleep(delay)
