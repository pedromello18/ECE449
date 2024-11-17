import RPi.GPIO as GPIO
from picamera import PiCamera
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
RECEIVE_PIN = 17  # GPIO pin used to receive signal
GPIO.setup(RECEIVE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def capture_image():
    camera = PiCamera()
    camera.start_preview()
    time.sleep(2)  # Let the camera adjust
    camera.capture('test_pictures/picture.jpg')
    camera.stop_preview()
    print("Image captured and saved!")

def wait_for_signal():
    print("Waiting for trigger signal...")
    while True:
        if GPIO.input(RECEIVE_PIN) == GPIO.HIGH:  # Signal received
            print("Signal detected!")
            capture_image()
            time.sleep(1)  # Debounce, avoid multiple captures

wait_for_signal()