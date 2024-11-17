import RPi.GPIO as GPIO
import time

def send_signal():
    GPIO.setmode(GPIO.BCM)
    SEND_PIN = 17 # TODO make sure it's not being used
    GPIO.setup(SEND_PIN, GPIO.OUT)
    GPIO.output(SEND_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(SEND_PIN, GPIO.LOW)
    print("Signal sent to trigger image capture.")