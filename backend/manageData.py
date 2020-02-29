import getData
import datetime

def openWindow():
    print("Opening Window")
    sleep(10)
    print("Window State: Open")

def closeWindow():
    print("Closing Window")
    sleep(10)
    print("Window State: Closed")
    
def automatic(temp, humidity, smoke, percipitation):
    now = datetime.datetime.now()
    currentTime = datetime.time(now.hour, now.minute)
    smokeDif = smoke["data"]["inside"] - smoke["data"]["outside"]
    tempDiff = temp["data"]["inside"] - temp["data"]["outside"]
    humidDiff = humidity["data"]["inside"] - humidity["data"]["outside"]
    smokeDiff = smoke["data"]["inside"] - smoke["data"]["outside"]
    if smokeDif > 5:
        openWindow()
    elif 

def manual():
    

while True:
    time.sleep(30)
    temp = getData.getTemp()
    humidity = getData.getHumidity()
    smoke = getData.getSmoke()
    percipitation = getData.getPercipitation()
    settings = getData.getSettings()
    

