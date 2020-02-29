from flask import Flask, request, jsonify

app = Flask(__name__)

def writeFile(file, data):
    with open(file, "w") as f:
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
        temp = readFile("temp")
        return jsonify(error=False, msg="Success", code=200, data=temp)

@app.route('/data/humidity', methods=["GET", "POST"])
def sendHumidity():
    if request.method == "POST":
        writeFile("humidity", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        humidity = readFile("humidity")
        return jsonify(error=False, msg="Success", code=200, data=humidity)

@app.route('/data/smoke', methods=["GET", "POST"])
def sendSmoke():
    if request.method == "POST":
        writeFile("smoke", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        smoke = readFile("smoke")
        return jsonify(error=False, msg="Success", code=200, data=smoke)

@app.route('/data/precip', methods=["GET", "POST"])
def sendPrecip():
    if request.method == "POST":
        writeFile("precip", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        precip = readFile("precip")
        return jsonify(error=False, msg="Success", code=200, data=precip)

@app.route('/data/settings', methods=["GET", "POST"])
def sendSettings():
    if request.method == "POST":
        writeFile("settings", request.form['data'])
        return jsonify(error=False, msg="Success", code=200, data='')
    else:
        settings = readFile("settings")
        return jsonify(error=False, msg="Success", code=200, data=settings)

if __name__ == "__main__":
    app.run(debug=True)