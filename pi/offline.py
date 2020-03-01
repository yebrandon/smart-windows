"""
Controls the logic of the r-pi window management when no network is available
"""

#checks whether the window should be open or closed
def update(data, timeout_counter):
    temp = data["temp"]
    humidity = data["humidity"]
    precip = data["precip"]
    window_state = data["windowState"]

    if (timeout_counter == 0):
        print("Connection error. Attempting to reconnect.")
    else:
        print("Reconnection fail #" + str(timeout_counter) + ". Attempting another reconnection.")

    quit, timeout_counter = timeout(timeout_counter)
    if (quit):
        return "close", 10, timeout_counter
    return window_state, 5, timeout_counter

#controls the timeout of a connect
def timeout(timeout_counter):
    timeout_counter += 1
    
    if (timeout_counter == 7):
        print("All reconnection attempts failed.")
        print("Closing windows until connection can be restablished.")
        return True, timeout_counter
    return False, timeout_counter