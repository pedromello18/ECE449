# flood_light.py
# Veg Group 2

# Setup Instructions:
# install libraries:
# sudo apt-get update
# sudo apt-get install python3-rpi.gpio

# Replace code with correct pins (FLOOD_PIN)

import RPi.GPIO as GPIO
import time

# Define the GPIO pins
FLOOD_PIN = 38 # yellow

# Setup GPIO as outputs
GPIO.setmode(GPIO.BCM) # Use BCM numbering
GPIO.setup(FLOOD_PIN, GPIO.OUT)


def turn_on_flood_light():
    GPIO.output(FLOOD_PIN, GPIO.HIGH)
    print("Flood light turned ON.")

def turn_off_flood_light():
    GPIO.output(POWER_PIN, GPIO.HIGH)
    print("Flood light turned OFF.")

