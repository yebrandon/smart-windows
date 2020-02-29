import getData
import datetime
import time

windowStats = 0

def openWindow():
    time.sleep(10)
    global windowStats
    if windowStats == 0:
        print("Opening Window")
        print("Window State: Open")
        windowStats += 1
    else:
        print("Window State: Open")

def closeWindow():
    time.sleep(10)
    global windowStats
    if windowStats == 1:
        print("Closing Window")
        print("Window State: Closed")
        windowStats -= 1
    else:
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
    safetemphigh = set_temp + 2.0
    safetemplow = set_temp - 2.0

    humidin = info["humidity"]["inside"]
    humidout = info["humidity"]["outside"]
    safehumidhigh = set_humid + 2.0
    safehumidlow = set_humid - 2.0
    humidDiff = info["humidity"]["outside"] - info["humidity"]["inside"]


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

#def manual():

    


def main():

    time.sleep(30)
    info = getData.getInfo()
    automatic(info)

main()

