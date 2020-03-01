"""
back end stuff
"""
import getData
import datetime
import time
import getData
#import webScraper
#import localData
URL = "http://10.10.10.160/data/"
#URL = "http://130.15.38.40/data/"

#for autonomous use
def automatic(info):
    """
    the auto open and close function
    :param info: the infomation contain the temp humid and other stuff
    :return:
    """
    set_temp = float(info["settings"]["pref_temp"])
    set_humid = 45

    percipitation = info["precip"]

    tempDiff = abs(info["temp"]["outside"] - float(info["temp"]["inside"]))
    tempin = float(info["temp"]["inside"])
    tempout = info["temp"]["outside"]
    safetemphigh = set_temp + 6.0
    safetemplow = set_temp - 6.0

    humidin = float(info["humidity"]["inside"])
    humidout = info["humidity"]["outside"]
    safehumidhigh = set_humid + 2.0
    safehumidlow = set_humid - 2.0
    humidDiff = abs(info["humidity"]["outside"] - float(info["humidity"]["inside"]))

    check = "temp"

    if percipitation == "True": #if rain or not
        getData.post_request(URL+"command",{"data":"close"})
    elif tempin >= safetemplow and tempin <= safetemphigh:  # safe range of the set temp
        check = "hum"
    elif tempin < set_temp: # compare the temp to know if open or not
        if tempout >= set_temp:
            getData.post_request(URL+"command",{"data":"open"})
        elif tempout < set_temp:
            if tempDiff > 5:
                getData.post_request(URL+"command",{"data":"open"})
            else:
                getData.post_request(URL+"command",{"data":"close"})
    elif tempin > set_temp:
        if tempout < set_temp:
            getData.post_request(URL+"command",{"data":"open"})
        elif tempout > set_temp:
            if tempDiff < 5:
                getData.post_request(URL+"command",{"data":"open"})
            else:
                getData.post_request(URL+"command",{"data":"close"})

    if check == "hum":
        if humidin >= safehumidlow and humidin <= safehumidhigh:  # safe humid range
            pass
        elif humidin < set_humid:  # compare the humid to determent if open or close
            if humidout >= set_humid:
                getData.post_request(URL+"command",{"data":"open"})
            elif humidout < set_humid:
                if humidDiff > 10:
                    getData.post_request(URL+"command",{"data":"open"})
                else:
                    getData.post_request(URL+"command",{"data":"close"})
        elif humidin >= set_humid:
            if humidout <= set_humid:
                getData.post_request(URL+"command",{"data":"open"})
            elif humidout > set_humid:
                if humidDiff < 10:
                    getData.post_request(URL+"command",{"data":"open"})
                else:
                    getData.post_request(URL+"command",{"data":"close"})
    return info

#user manual control
def manual(info):
    now = datetime.datetime.now()
    opentime = info["settings"]["open_time"]
    if now.hour == opentime[0] and now.minute == opentime[1]:
        getData.post_request(URL+"command",{"data":"open"})
    
    closetime = info["settings"]["close_time"]
    if now.hour == closetime[0] and now.minute == closetime[1]:
        getData.post_request(URL+"command",{"data":"close"})

    return info

def main(info):
    mode = info["settings"]["mode"]
    if mode == "auto":
        print("auto")
        allinfo = automatic(info)
    else:
        print("manual")
        allinfo = manual(info)
    state = allinfo["windowState"]
    print("done itteration")
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


