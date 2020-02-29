import getData
import datetime
import time
import webScraper
import localData

def openWindow(state):
    """
    when the window needs to be open call the function if the window is open then do nothing
    :return: window state?
    """
    time.sleep(10)
    if state == "close":
        print("Opening Window")
        print("Window State: Open")
        state = "open"
    else:
        print("Window State: Open")
    return state


def closeWindow(state):
    """
    to close the window
    :return:
    """
    time.sleep(10)

    if state == "open":
        print("Closing Window")
        print("Window State: Closed")
        state= "close"
    else:
        print("Window State: Closed")
    return state
    
def automatic(info):
    """
    the auto open and close function
    :param info: the infomation contain the temp humid and other stuff
    :return:
    """
    now = datetime.datetime.now()
    currentTime = datetime.time(now.hour, now.minute)

    set_temp = info["set"]["temp"]
    set_humid = 10

    percipitation = info["percipitation"]

    tempDiff = info["temp"]["outside"] - info["temp"]["inside"]
    tempin = info["temp"]["inside"]
    tempout = info["temp"]["outside"]
    safetemphigh = set_temp + 2.0
    safetemplow = set_temp - 2.0

    humidin = info["humidity"]["inside"]
    humidout = info["humidity"]["outside"]
    safehumidhigh = set_humid + 2.0
    safehumidlow = set_humid - 2.0
    humidDiff = info["humidity"]["outside"] - info["humidity"]["inside"]

    if percipitation == False: #if rain or not
        info["WindowState"] = closeWindow(info["WindowState"])
    elif tempin >= safetemplow and tempin <= safetemphigh: # safe range of the set temp
        pass
    elif tempin < set_temp: # compare the temp to know if open or not
        if tempout >= set_temp:
            info["WindowState"] = openWindow(info["WindowState"])
        elif tempout < set_temp:
            if tempDiff > 5:
                info["WindowState"] = openWindow(info["WindowState"])
            else:
                info["WindowState"] = closeWindow(info["WindowState"])
    elif tempin >= set_temp:
        if tempout <= set_temp:
            info["WindowState"] = openWindow(info["WindowState"])
        elif tempout > set_temp:
            if tempDiff < 5:
                info["WindowState"] = openWindow(info["WindowState"])
            else:
                info["WindowState"] = closeWindow(info["WindowState"])
    elif humidin >= safehumidlow and humidin <= safehumidhigh: # safe humid range
        pass
    elif humidin < set_humid:#compare the humid to determent if open or close
        if humidout >= set_humid:
            info["WindowState"] = openWindow(info["WindowState"])
        elif humidout < set_temp:
            if humidDiff > 5:
                info["WindowState"] = openWindow(info["WindowState"])
            else:
                info["WindowState"] = closeWindow(info["WindowState"])
    elif humidin >= set_humid:
        if humidout <= set_humid:
            info["WindowState"] = openWindow(info["WindowState"])
        elif humidout > set_temp:
            if humidDiff < 5:
                info["WindowState"] = openWindow(info["WindowState"])
            else:
                info["WindowState"] = closeWindow(info["WindowState"])
    return info

def manual(mode,info):
    if mode == "on":
        info["WindowState"] = openWindow(info["WindowState"])
    elif mode == "off":
        info["WindowState"] = closeWindow(info["WindowState"])

    return info

def main():
    time.sleep(10)
    info = getData.getInfo()
    mode = localData.getMode
    if mode["mode"] == "auto":
        allinfo = automatic(info)
    else:
        allinfo = manual(mode["manual"],info)



main()

