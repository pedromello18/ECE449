import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1115 ADC instance
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

# Gain setting for the ADC (adjust if needed)
GAIN = 1  # Gain of 1 corresponds to a full-scale range of +/- 4.096V

# Number of samples to take
NUM_SAMPLES = 10  # Take 10 samples over a short period
SAMPLE_INTERVAL = 0.01  # 10 milliseconds between samples

# Function to monitor the beam with square wave sampling logic
def monitor_beam():
    while True:
        unbroken_count = 0
        broken_count = 0
        
        # Take multiple samples over a short time period
        for _ in range(NUM_SAMPLES):
            # Read analog value from channel 0 (AIN0)
            # value = adc.read_adc(0, gain=GAIN)
            voltage = chan.voltage         

            # Convert the ADC value to voltage (assuming 16-bit resolution and 4.096V full scale)
            # voltage = value * 4.096 / 32767.0
            
            # Set the thresholds for detecting beam status
            if voltage > 3.0:  # Adjust threshold as needed
                broken_count += 1  # Beam intact
            else:
                unbroken_count += 1  # Beam broken
                
            time.sleep(SAMPLE_INTERVAL)
        
        # Determine the beam status based on the majority of samples
        if unbroken_count > broken_count:
            print("Beam intact")
            return -1
        else:
            print("Beam broken")
            return 1
        # Sleep before the next detection cycle
        time.sleep(0.5)

# Main loop
try:
    monitor_beam()
except KeyboardInterrupt:
    print("Stopping the program")


