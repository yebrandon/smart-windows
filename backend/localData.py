"""
Data Taken from frontend, interfaces front end
"""
from threading import Thread
import getData
from flask import Flask, redirect, request
from time import sleep

app = Flask(__name__)
info = {}
URL = "http://10.10.10.160/data/"

@app.route("/data/settings", methods = ["POST", "GET"])
def frontEndSettings():
        if request.method == "POST":
                info["settings"] = request.form['mode']
        else:#get
                return(info["setting"])

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
            info['temp'] = getData.getTemp()
            info["humidity"] = getData.getHumidity()
            info["precip"]= getData.getPercipitation()
            info["windowState"] = getData.getWindowState()
            info["setting"] = getData.getSettings()
            info["command"] = "open"
            sleep(6)

if __name__ == "__main__":
       Thread(target = getInfo).start()
       app.run(debug=True)
       

