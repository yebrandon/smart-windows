"""
Data Taken from frontend, interfaces front end
"""
from threading import Thread
import getData
import manageData
import webScraper
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS, cross_origin
from time import sleep
import json

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
info = {"temp": {}, "settings":{"country":"", "city":"", "mode":"", "pref_temp":"", "open_time": "", "close_time": ""},"humidity":{},"windowState":""}
# URL = "http://10.10.10.160/data/"
URL = "http://130.15.38.40/data/"

@app.route("/data/settings", methods = ["POST", "GET"])
@cross_origin()
def frontEndSettings():
        if request.method == "POST":
                data = request.get_json()
                info["settings"] = data
                getData.post_request(URL+"settings", {'data': data})
                return jsonify(error=False, msg="Success", code=200, data='')
        else:#get
                return jsonify(error=False, msg="Success", code=200, data=info["settings"])

@app.route("/data/humidity", methods = ["POST", "GET"])
@cross_origin()
def frontEndHumidity():
        if request.method == "POST":
                data = request.get_json()
                info["humidity"] = data
                getData.post_request(URL+"humidity", {'data': data})
                return jsonify(error=False, msg="Success", code=200, data='')
        else:#get
                return jsonify(error=False, msg="Success", code=200, data=info["humidity"])

@app.route("/data/precip", methods = ["POST", "GET"])
@cross_origin()
def frontEndPercip():
        if request.method == "POST":
                data = request.get_json()
                info["precip"] = data
                getData.post_request(URL+"precip", {'data': data})
                return jsonify(error=False, msg="Success", code=200, data='')
        else:#get
                return jsonify(error=False, msg="Success", code=200, data=info["precip"])

@app.route("/data/temp", methods = ["POST", "GET"])
@cross_origin()
def frontEndTemp():
        if request.method == "POST":
                data = request.get_json()
                info["temp"] = data
                getData.post_request(URL+"temp", {'data': data})
                return jsonify(error=False, msg="Success", code=200, data='')
        else:#get
                return jsonify(error=False, msg="Success", code=200, data=info["temp"])

@app.route("/data/windowState", methods=["POST", "GET"])
@cross_origin()
def sendWindowState():
        if request.method == "POST":
                data = request.get_json()
                info["command"] = data
                getData.post_request(URL+"command",{"data": info["command"]})
                return jsonify(error=False, msg="Success", code=200, data='')
        else:
                return jsonify(error=False, msg="Success", code=200, data=info["windowState"])

@app.route("/data/command", methods=["POST"])
@cross_origin()
def sendCommand():
        if request.method == "POST":
                data = request.get_json()
                info["command"] = data
                getData.post_request(URL+"command",{"data": info["command"]})
                return jsonify(error=False, msg="Success", code=200, data='')
                
                
def getInfo():
        global info
        while True:
                info["temp"]["inside"] = getData.getTemp()
                info["humidity"] = getData.getHumidity()
                info["precip"]= getData.getPercipitation()
                info["windowState"] = getData.getWindowState()
                info["settings"] = getData.getSettings()
                info["command"] = "open"
                try:
                        info["temp"]["outside"], info["humidity"]["outside"] = webScraper.main(info["settings"]["location"]["city"], info["settings"]["location"]["country"])
                        manageData.main(info)
                except:
                        pass
                sleep(6)

if __name__ == "__main__":
       Thread(target = getInfo).start()
       app.run(debug=True, port=5000)
       

