import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
SEND_PIN = 17  # GPIO pin used for signaling
GPIO.setup(SEND_PIN, GPIO.OUT)

def send_signal():
    GPIO.output(SEND_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(SEND_PIN, GPIO.LOW)
    print("Signal sent to trigger image capture.")