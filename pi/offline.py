"""
Controls the logic of the r-pi window management when no network is available
"""

#imports
import main

#checks whether the window should be open or closed
def update(data):
    temp = data["temp"]
    humidity = data["humidity"]
    precip = data["precip"]
    window_state = data["windowState"]
    
    #TODO logic here
    if (window_state == "close"):
        main.set_window_state("open")
    else:
        main.set_window_state("close")

    print("Connection error. Attempting offline logic.")
    print("Current state: ")
    print("Temp: " + str(temp))
    print("Hum.: " + str(humidity))
    print("Prec: " + str(precip))
    print("Win.: " + window_state)
