"""
back end stuff
"""
import getData
import datetime
import time
#import webScraper
#import localData

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
    set_temp = info["settings"]["pref_temp"]
    set_humid = 45

    percipitation = info["precip"]

    tempDiff = info["temp"]["outside"] - info["temp"]["inside"]
    tempin = info["temp"]["inside"]
    tempout = info["temp"]["outside"]
    safetemphigh = set_temp + 6.0
    safetemplow = set_temp - 6.0

    humidin = info["humidity"]["inside"]
    humidout = info["humidity"]["outside"]
    safehumidhigh = set_humid + 2.0
    safehumidlow = set_humid - 2.0
    humidDiff = info["humidity"]["outside"] - info["humidity"]["inside"]

    check = "temp"

    if percipitation == True: #if rain or not
        info["windowState"] = closeWindow(info["windowState"])
    elif tempin >= safetemplow and tempin <= safetemphigh:  # safe range of the set temp
        check = "hum"
    elif tempin < set_temp: # compare the temp to know if open or not
        if tempout >= set_temp:
            info["windowState"] = openWindow(info["windowState"])
        elif tempout < set_temp:
            if tempDiff > 5:
                info["windowState"] = openWindow(info["windowState"])
            else:
                info["windowState"] = closeWindow(info["windowState"])
    elif tempin > set_temp:
        if tempout < set_temp:
            info["windowState"] = openWindow(info["windowState"])
        elif tempout > set_temp:
            if tempDiff < 5:
                info["windowState"] = openWindow(info["windowState"])
            else:
                info["windowState"] = closeWindow(info["windowState"])

    if check == "hum":
        if humidin >= safehumidlow and humidin <= safehumidhigh:  # safe humid range
            pass
        elif humidin < set_humid:  # compare the humid to determent if open or close
            if humidout >= set_humid:
                info["windowState"] = openWindow(info["windowState"])
            elif humidout < set_humid:
                if humidDiff > 10:
                    info["windowState"] = openWindow(info["windowState"])
                else:
                    info["windowState"] = closeWindow(info["windowState"])
        elif humidin >= set_humid:
            if humidout <= set_humid:
                info["windowState"] = openWindow(info["windowState"])
            elif humidout > set_humid:
                if humidDiff < 10:
                    info["windowState"] = openWindow(info["windowState"])
                else:
                    info["windowState"] = closeWindow(info["windowState"])
    return info

def manual(info):
    now = datetime.datetime.now()
    opentime = info["settings"]["open_time"]
    if now.hour == opentime[0] and now.minute == opentime[1]:
        info["windowState"] = openWindow(info["windowState"])

    closetime = info["settings"]["close_time"]
    if now.hour == closetime[0] and now.minute == closetime[1]:
        info["windowState"] = closeWindow(info["windowState"])

    if info["command"] == "open":
        info["windowState"] = openWindow(info["windowState"])
    elif info["command"] == "close":
        info["windowState"] = closeWindow(info["windowState"])

    return info

def main(info):
    time.sleep(10)
    mode = info["setting"]["mode"]
    if mode == "auto":
        allinfo = automatic(info)
    else:
        allinfo = manual(info)

    state = allinfo["windowState"]
    
    return state

if __name__ == '__main__':
    test = {}
    temp = {}
    temp["inside"] = 25
    temp["outside"] = 30
    test["temp"] = temp
    hum = {}
    hum["inside"] = 20
    hum["outside"] = 40
    test["humidity"] = hum
    test["precip"] = False
    test["windowState"] = "close"
    settings={}
    settings["mode"] = "man"
    o_time = [19,16]
    c_time = [18,10]
    settings["open_time"] = o_time
    settings["close_time"] = c_time
    settings["pref_temp"] = 30
    test["settings"] = settings
    test["command"] = "off"


    if test["settings"]["mode"] == "auto":
        allinfo = automatic(test)
    else:
        allinfo = manual(test)

    state = allinfo["windowState"]

    print(state)


