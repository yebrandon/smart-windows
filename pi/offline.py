"""
Controls the logic of the r-pi window management when no network is available
"""

#file attributes
timeout_counter = 0

#checks whether the window should be open or closed
def update(data):
    temp = data["temp"]
    humidity = data["humidity"]
    precip = data["precip"]
    window_state = data["windowState"]

    if (timeout_counter == 0):
        print("Connection error. Attempting to reconnect.")
    else:
        print("Reconnection fail #" + str(timeout_counter) + ". Attemting another reconnection.")
    
    print("Current state: ")
    print("Temp: " + str(temp))
    print("Hum.: " + str(humidity))
    print("Prec: " + str(precip))
    print("Win.: " + window_state)

    if (timeout()):
        return "close", 10
    return window_state, 5

#controls the timeout of a connect
def timeout():
    timeout_counter += 1
    
    if (timeout_counter > 6):
        print("All reconnection attempts failed.")
        print("Closing windows until connection can be restablished.")
        return True
    return False