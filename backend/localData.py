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
info = {"temp": {"inside":"", "outside":""}, "settings":{"country":"", "city":"", "mode":"", "pref_temp":"", "open_time": "", "close_time": ""},"humidity":{"inside":"", "outside":""},"windowState":""}
URL = "http://10.10.10.160/data/"#for pi
#URL = "http://130.15.38.40/data/"

#settings
@app.route("/data/settings", methods = ["POST", "GET"])
@cross_origin()
def frontEndSettings():
        if request.method == "POST":
                data = request.get_json()
                info["settings"] = data
                getData.post_request(URL+"settings", {'data': json.dumps(data)})
                return jsonify(error=False, msg="Success", code=200, data='')
        else:#get
                return jsonify(error=False, msg="Success", code=200, data=info["settings"])

#humidity
@app.route("/data/humidity", methods = ["POST", "GET"])
@cross_origin()
def frontEndHumidity():#
        if request.method == "POST":
                data = request.get_json()
                info["humidity"] = data
                getData.post_request(URL+"humidity", {'data': data})
                return jsonify(error=False, msg="Success", code=200, data='')
        else:#get
                return jsonify(error=False, msg="Success", code=200, data=info["humidity"])

#percipitation
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

#temp
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

#window state
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

#command
@app.route("/data/command", methods=["POST"])
@cross_origin()
def sendCommand():
        if request.method == "POST":
                data = request.get_json()
                info["command"] = data['data']
                getData.post_request(URL+"command",{"data": info["command"]})
                return jsonify(error=False, msg="Success", code=200, data='')
                
#loop that runs the data collection and automatic/manual             
def getInfo():
        global info
        while True:
                info["temp"]["inside"] = getData.getTemp()
                info["humidity"]["inside"] = getData.getHumidity()
                info["precip"]= getData.getPercipitation()
                info["windowState"] = getData.getWindowState()
                info["settings"] = getData.getSettings()
                print(info)
                try:
                    info["temp"]["outside"], info["humidity"]["outside"] = webScraper.main(info["settings"]["city"], info["settings"]["country"])
                    manageData.main(info)
                except:
                    pass
                sleep(2)

if __name__ == "__main__":
       Thread(target=getInfo).start()
       app.run(debug=True, port=5000)
       #getInfo()

