"""
Data Taken from frontend, interfaces front end
"""
from threading import Thread
import getData
import manageData
import webScraper
from flask import Flask, redirect, request
from time import sleep

app = Flask(__name__)
info = {"temp": {}, "settings":{"location":{"country":"", "city":""}, "open_time": "", "close_time": ""},"humidity":{}}
URL = "http://10.10.10.160/data/"

@app.route("/data/settings", methods = ["POST", "GET"])
def frontEndSettings():
        if request.method == "POST":
                info["settings"] = request.form['data']
        else:#get
                return(info["settings"])

@app.route("/data/humidity", methods = ["POST", "GET"])
def frontEndHumidity():
        if request.method == "POST":
                info["humidity"] = request.form['humidity']
        else:#get
                return(info["humidity"])

@app.route("/data/precip", methods = ["POST", "GET"])
def frontEndPercip():
        if request.method == "POST":
                info["precip"] = request.form['precip']
        else:#get
                return(info["precip"])

@app.route("/data/temp", methods = ["POST", "GET"])
def frontEndTemp():
        if request.method == "POST":
                info["temp"] = request.form['temp']
        else:#get
                return(info["temp"])

@app.route("/data/command", methods=["POST"])
def sendWindowState():
        if request.method == "POST":
                getData.post_request(URL+"command",{"data": info["command"]})
                
                
def getInfo():
        global info
        while True:
            info["temp"]["inside"] = getData.getTemp()
            info["humidity"] = getData.getHumidity()
            info["precip"]= getData.getPercipitation()
            info["windowState"] = getData.getWindowState()
            info["settings"] = getData.getSettings()
            info["command"] = "open"
            info["temp"]["outside"], info["humidity"]["outside"] = webScraper.main(info["setting"]["location"]["city"], info["setting"]["location"]["country"])
            manageData.main(info)
            sleep(6)

if __name__ == "__main__":
       Thread(target = getInfo).start()
       app.run(debug=True)
       

