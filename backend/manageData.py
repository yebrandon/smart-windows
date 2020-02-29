import getData
import datetime
import time

def openWindow():
    print("Opening Window")
    time.sleep(10)
    print("Window State: Open")

def closeWindow():
    print("Closing Window")
    time.sleep(10)
    print("Window State: Closed")
    
def automatic(info):
    now = datetime.datetime.now()
    currentTime = datetime.time(now.hour, now.minute)

    set_temp = info["set"]["temp"]
    set_humid = 10

    percipitation = info["percipitation"]["per"]

    tempDiff = info["temp"]["outside"] - info["temp"]["inside"]
    tempin = info["temp"]["inside"]
    tempout = info["temp"]["outside"]
    safetemphigh = set_temp + 2
    safetemplow = set_temp - 2

    humidin = info["humidity"]["inside"]
    humidout = info["humidity"]["outside"]
    safehumidhigh = set_humid + 2
    safehumidlow = set_humid - 2
    humidDiff = humidity["data"]["outside"] - humidity["data"]["inside"]


    if percipitation > 0:
        closeWindow()
    elif tempin >= safetemplow and tempin <= safetemphigh:
        pass
    elif tempin < set_temp:
        if tempout >= set_temp:
            openWindow()
        elif tempDiff > 0:
            openWindow()
    elif tempin >= set_temp:
        if tempout <= set_temp:
            openWindow()
        elif tempDiff < 0:
            openWindow()
    elif humidin >= safehumidlow and humidin <= safehumidhigh:
        pass
    elif humidin < set_humid:
        if humidout >= set_humid:
            openWindow()
        elif humidDiff > 0:
            openWindow()
    elif humidin >= set_humid:
        if humidout <= set_humid:
            openWindow()
        elif humidDiff < 0:
            openWindow()

def manual():
    


while True:
    time.sleep(30)
    temp = getData.getTemp()
    humidity = getData.getHumidity()
    smoke = getData.getSmoke()
    percipitation = getData.getPercipitation()
    settings = getData.getSettings()
    

