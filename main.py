# import libraries
import adafruit_seesaw as ss
import os 
import RPi.GPIO as GPIO
import board
import busio
import adafruit_sht4x
import adafruit_tsl2591
import cv2 as cv
import smbus2
import json 

# gpio warnings off
GPIO.setwarnings(False)

# gpio pins for the realy
GPIO.setmode(GPIO.BCM)
pinlist = [17, 22, 27, 10]
for i in pinlist:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# create i2c bus
i2c_bus = busio.I2C(board.SCL, board.SDA)
i2c = busio.I2C(3,2)

# soil moisture sensor 
soilMoisture = ss.Seesaw(i2c_bus, addr=0x36)
print("Sensors initialized")
# light sensor
lightSensor = adafruit_tsl2591.TSL2591(i2c)
print("Sensors initialized")
# temperature and humidity sensor
sht = adafruit_sht4x.SHT4x(i2c, address=0x44)
print("Sensors initialized")

# get the soil moisture
def getSoilMoisture():
    soilMoistureData = soilMoisture.moisture_read()
    return{
        "Soil Moisture: " : soilMoistureData
    }

# get the light
def getLight():
    lightData = lightSensor.lux
    return{
        "Light: " : lightData
    }

# get the temperature and humidity
def getTempHumid():
    temp, relative_humidity = sht.measurements
    return{
        "Temperature: " : temp * 1.8 + 32, # will convert to fahrenheit
        "Humidity: " : relative_humidity
    }
