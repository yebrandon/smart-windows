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
    set_temp = info["settings"]["pref_temp"]
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

    if percipitation == True: #if rain or not
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

def manual(info):
    now = datetime.datetime.now()

    if info["command"] == "on":
        info["WindowState"] = openWindow(info["WindowState"])
    elif info["command"] == "off":
        info["WindowState"] = closeWindow(info["WindowState"])

    opentime = info["setting"]["open_time"]
    if now.hour == opentime[0] and now.minute == opentime[1]:
        info["WindowState"] = openWindow(info["WindowState"])

    closetime = info["srtting"]["close_time"]
    if now.hour == closetime[0] and now.minute == closetime[1]:
        info["WindowState"] = closeWindow(info["WindowState"])

    return info

def main():
    time.sleep(10)
    info = getData.getInfo()
    mode = info["setting"]["mode"]
    if mode == "auto":
        allinfo = automatic(info)
    else:
        allinfo = manual(info)

    state = allinfo["WindowState"]

    return state

main()

if __name__ == '__main__':
    test = {}
    temp = {}
    temp["inside"] = 20
    temp["outside"] = 30
    test["temp"] = temp
    hum = {}
    hum["inside"] = 10
    hum["outside"] = 10
    test["humidity"] = hum
    test["percipitation"] = False
    test["WindowState"] = "close"
    settings={}
    settings["mode"] = "auto"
    o_time = [18,11]
    c_time = [18,12]
    settings["open_time"] = o_time
    settings["close_time"] = c_time
    settings["pref_temp"] = 30
    test["settings"] = settings


    if test["settings"]["mode"] == "auto":
        allinfo = automatic(test)
    else:
        allinfo = manual(test)

    state = allinfo["WindowState"]

    print(state)


