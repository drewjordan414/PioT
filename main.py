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

# get video 
def getVideo():
    videoCapture = cv.VideoCapture(0)
    videoCapture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    videoCapture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    videoCapture.set(cv.CAP_PROP_FPS, 30)
    # videoCapture.set(cv.CAP_PROP_BRIGHTNESS, 0.5)
    # videoCapture.set(cv.CAP_PROP_CONTRAST, 0.5)
    # videoCapture.set(cv.CAP_PROP_SATURATION, 0.5)
    # videoCapture.set(cv.CAP_PROP_HUE, 0.5)
    # videoCapture.set(cv.CAP_PROP_EXPOSURE, 0.5)
    # videoCapture.set(cv.CAP_PROP_GAIN, 0.5)
    # videoCapture.set(cv.CAP_PROP_AUTO_EXPOSURE, 0.5)
    # videoCapture.set(cv.CAP_PROP_AUTOFOCUS, 0.5)
    # videoCapture.set(cv.CAP_PROP_AUTO_WB, 0.5)
    # videoCapture.set(cv.CAP_PROP_SHARPNESS, 0.5)
    # videoCapture.set(cv.CAP_PROP_BACKLIGHT, 0.5)
    # videoCapture.set(cv.CAP_PROP_ZOOM, 0.5)
    # videoCapture.set(cv.CAP_PROP_FOCUS, 0.5)
    # videoCapture.set(cv.CAP_PROP_WB_TEMPERATURE, 0.5)
    # videoCapture.set(cv.CAP_PROP_GAMMA, 0.5)
    # videoCapture.set(cv.CAP_PROP_TEMPERATURE, 0.5)
    # videoCapture.set(cv.CAP_PROP_TRIGGER, 0.5)
    # videoCapture.set(cv.CAP_PROP_TRIGGER_DELAY, 0.5)
    # videoCapture.set(cv.CAP_PROP_WHITE_BALANCE_BLUE_U, 0.5)
    # videoCapture.set(cv.CAP_PROP_WHITE_BALANCE_RED_V, 0.5)
    # videoCapture.set(cv.CAP_PROP_OPENNI_OUTPUT_MODE, 0.5)
    # videoCapture.set(cv.CAP_PROP_OPENNI_FRAME_MAX_DEPTH, 0.5)
    # videoCapture.set(cv.CAP_PROP_OPENNI_BASELINE, 0.5)
    # videoCapture.set(cv.CAP_PROP_OPENNI_FOCAL_LENGTH, 0.5)
    return videoCapture
