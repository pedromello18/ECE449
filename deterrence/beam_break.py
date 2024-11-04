import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin where the sensor output is connected
SENSOR_PIN = 17 # Example GPIO pin

# Setup the pin as an input
GPIO.setup(SENSOR_PIN, GPIO.IN)

# Number of samples to take                                                                                                                                                               
NUM_SAMPLES = 10 # Take 10 samples over a short period
SAMPLE_INTERVAL = 0.01 # 10 milliseconds between samples

# Function to monitor the beam with square wave sampling logic
def monitor_beam():
    unbroken_count = 0
    broken_count = 0
    # Take multiple samples over a short time period
    for _ in range(NUM_SAMPLES):
        if GPIO.input(SENSOR_PIN):
            unbroken_count += 1
        else:
            broken_count += 1

        time.sleep(SAMPLE_INTERVAL)

    # Determine the beam status based on the majority of samples
    if unbroken_count > broken_count:
        print("Beam intact (majority of HIGH signals detected)")
        return 1
    else:
        print("Beam broken (majority of LOW signals detected)")
        return -1

def test_beam_break():
    print(monitor_beam())
    
test_beam_break()
        
            

