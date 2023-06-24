# housekeeping
import main as main # Import main.py
import flask as flask
from flask import Flask, render_template, request, jsonify, Response, json
from flask.views import View

# flask app
app = Flask(__name__)

# routes for the soil sensor
@app.route('/soil-moisture' , methods=['GET'])
def getSoilMoisture():
    getSoilMoisture = main.getSoilMoisture()
    return jsonify(getSoilMoisture)

# routes for the light sensor
@app.route('/light' , methods=['GET'])
def getLight():
    getLight = main.getLight()
    return jsonify(getLight)

# routes for the temperature and humidity sensor
@app.route('/temp-humid' , methods=['GET'])
def getTempHumid():
    getTempHumid = main.getTempHumid()
    return jsonify(getTempHumid)

# routes for the video
@app.route('/video' , methods=['GET'])
def getVideo():
    getVideo = main.getVideo()
    return jsonify(getVideo)

if __name__ == '__main__':
    app.run()