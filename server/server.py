from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

def writeFile(file, data):
    with open(file, "w+") as f:
        f.write(data)

def readFile(file):
    with open(file, "r") as f:
        content = f.read()
    return content

@app.route('/data/temp', methods=["GET", "POST"])
def sendTemp():
    if request.method == "POST":
        writeFile("temp", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        try:
            temp = readFile("temp")
        except:
            return jsonify(error=True, msg="Not found", code=404, data='')
        return jsonify(error=False, msg="Success", code=200, data=temp)

@app.route('/data/humidity', methods=["GET", "POST"])
def sendHumidity():
    if request.method == "POST":
        writeFile("humidity", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        try:
            humidity = readFile("humidity")
        except:
            return jsonify(error=True, msg="Not found", code=404, data='')
        return jsonify(error=False, msg="Success", code=200, data=humidity)

@app.route('/data/smoke', methods=["GET", "POST"])
def sendSmoke():
    if request.method == "POST":
        writeFile("smoke", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        try:
            smoke = readFile("smoke")
        except:
            return jsonify(error=True, msg="Not found", code=404, data='')
        return jsonify(error=False, msg="Success", code=200, data=smoke)

@app.route('/data/precip', methods=["GET", "POST"])
def sendPrecip():
    if request.method == "POST":
        writeFile("precip", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        try:
            precip = readFile("precip")
        except:
            return jsonify(error=True, msg="Not found", code=404, data='')
        return jsonify(error=False, msg="Success", code=200, data=precip)

@app.route('/data/settings', methods=["GET", "POST"])
def sendSettings():
    if request.method == "POST":
        try:
            req_data = json.loads(request.form['data'])
            file_data = json.loads(readFile("settings"))
            for key in req_data.keys():
                file_data[key] = req_data[key]
            writeFile("settings", json.dumps(file_data))
        except:
            writeFile("settings", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        try:
            settings = readFile("settings")
        except:
            return jsonify(error=True, msg="Not found", code=404, data='')
        return jsonify(error=False, msg="Success", code=200, data=json.loads(settings))

@app.route('/data/windowState', methods=["GET", "POST"])
def sendWindowState():
    if request.method == "POST":
        writeFile("windowState", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        try:
            windowState = readFile("windowState")
        except:
            return jsonify(error=True, msg="Not found", code=404, data='')
        return jsonify(error=False, msg="Success", code=200, data=windowState)

@app.route('/data/command', methods=["GET", "POST"])
def sendCommand():
    if request.method == "POST":
        writeFile("command", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        try:
            command = readFile("command")
            os.remove("command")
        except:
            return jsonify(error=True, msg="Not found", code=404, data='')
        return jsonify(error=False, msg="Success", code=200, data=command)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
