# import libraries
import adafruit_seesaw as ss
import os 
import RPI.GPIO as GPIO
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

