"""
Controls the logic of the r-pi window management when no network is available
"""

#checks whether the window should be open or closed
def update(data):
    temp = data["temp"]
    humidity = data["humidity"]
    precip = data["precip"]
    window_state = data["windowState"]
    
    #TODO logic here
    print("Connection error. Attempting offline logic.")
    print("Current state: ")
    print("Temp: " + temp)
    print("Hum.: " + humidity)
    print("Prec: " + precip)
    print("Win.: " + window_state)
