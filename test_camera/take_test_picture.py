import RPi.GPIO as GPIO
from picamera import PiCamera
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
RECEIVE_PIN = 17  # GPIO pin used to receive signal
GPIO.setup(RECEIVE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize the camera (you can move this outside the callback if preferred)
camera = PiCamera()

def capture_image():
    """Capture and save an image when the positive edge is detected."""
    camera.start_preview()
    time.sleep(2)  # Let the camera adjust
    camera.capture('test_pictures/picture.jpg')
    camera.stop_preview()
    print("Image captured and saved!")

# Callback function that gets triggered on a rising edge
def positive_edge_callback(channel):
    print("Positive edge detected! GPIO pin transitioned from LOW to HIGH.")
    capture_image()  # Capture image when positive edge is detected

# Set up event detection for the positive edge (LOW to HIGH)
GPIO.add_event_detect(RECEIVE_PIN, GPIO.RISING, callback=positive_edge_callback)


while True:
    time.sleep(1)  # Sleep to keep the program alive and responsive