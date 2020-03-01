"""
Author: Evan kilburn
Description: Takes the country and city as apramaters in the main function and returns the temp and humidity in a list
"""
import json
import urllib.request

#request messages
def get_request(url):
    request = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('ascii'))
    return data

#finds ID for weather AP
def findID(city, country): #city is ex. newmarket country is CA
    f= open("cityList.json", 'r')
    data = json.load(f)
    json_data = [] # your list with json objects (dicts)
    for x in data:
        #print(x)
        if x["name"].lower() == city.lower() and x["country"] == country.upper():
            return x["id"]

#returns temp and humidity outside values using openweathermap API    
def main(city, country):
    url = "http://api.openweathermap.org/data/2.5/weather?"
    APIKEY = "a42df1a0b008bd4fe512b771184734de"
    cityID = findID(city, country)
    dictHeaders = {"id":cityID, "APPID":APIKEY}#appid is api key
    allData = (get_request("http://api.openweathermap.org/data/2.5/weather?id="+str(cityID)+"&APPID="+str(APIKEY)))
    temp = allData["main"]["feels_like"] - 273.15
    humidity = allData["main"]["humidity"]
    return([temp, humidity])
    
if __name__ == "__main__":
    print(main("NEWMARKET", "CA"))
    print(main("KINGSTON", "CA"))
    print(main("VANCOUVER", "CA"))
