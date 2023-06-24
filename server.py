# housekeeping
import main as main # Import main.py
import flask as flask
from flask import Flask, render_template, request, jsonify, Response, json
from flask.views import View
# sesnor data class 
class SensorData(View):
    def get(self, request):
        soilMoisture = main.getSoilMoisture()
        light = main.getLight()
        tempHumid = main.getTempHumid()
        data = {
            "Soil Moisture: " : soilMoisture,
            "Light: " : light,
            "Temperature: " : tempHumid
        }
        return json(data)
    
# video class
class Video(View):
    def get(self, request):
        video = main.getVideo()
        data = {
            "Video: " : video
        }
        return json(data)
