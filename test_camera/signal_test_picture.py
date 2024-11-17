import RPi.GPIO as GPIO

def send_signal(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    print("Positive Edge on Test Camera Singal.")

def turn_off_signal(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    print("Negative Edge on Test Camera Singal.")