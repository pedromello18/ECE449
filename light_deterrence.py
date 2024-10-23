# light_deterrence.py
# Veg Group 2

# Setup Instructions:
# install libraries:
# sudo apt-get update
# sudo apt-get install python3-rpi.gpio

# Replace code with correct pins (Power and Signal)

import RPi.GPIO as GPIO
import time

# Define the GPIO pins
POWER_PIN = 17
SIGNAL_PIN = 27

# Setup GPIO as outputs
GPIO.setmode(GPIO.BCM) # Use BCM numbering
GPIO.setup(POWER_PIN, GPIO.OUT)
GPIO.setup(SIGNAL_PIN, GPIO.OUT)

def turn_on_strobe_light():
    GPIO.output(POWER_PIN, GPIO.HIGH)
    print("Strobe light turned ON.")

def turn_off_strobe_light():
    GPIO.output(POWER_PIN, GPIO.HIGH)
    print("Strobe light turned OFF.")

# sleeps for 1 second to change
def change_strobe_pattern():
    GPIO.output(SIGNAL_PIN, GPIO.HIGH)
    print("Signal HIGH - changing strobe pattern...")
    time.sleep(1)
    GPIO.output(SIGNAL_PIN, GPIO.LOW)
    print("Signal LOW - pattern changed.")
    


