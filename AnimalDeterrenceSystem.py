# AnimalDeterrenceSystem.py
# Veg Group 2
# Run this to start the system. Currently in simulation mode.


import time
import random # used for simulation

class AnimalDeterrenceSystem:
    def __init__(self):
        self.state = 'idle'
        self.start_time = time.time()
        print("Starting system in idle... (simulation /w 5% P each)")

    def update(self, beam_break_broken, animal_detected):
        print("Updating state...")
        current_time = time.time()

        # State transitions
        if self.state == 'idle':
            if beam_break_broken:
                print("Beam broken! Transitioning to detection state")
                self.state = 'detection'
                self.start_time = current_time
        
        elif self.state == 'detection':
            elapsed_time = current_time - self.start_time
            if animal_detected and elapsed_time <= 20:
                print("Animal detected! Transitioning to deterrence state")
                self.state = 'deterrence'
                self.start_time = current_time
            elif elapsed_time > 20:
                print("No animal detected within 20 seconds. Returning to idle state")
                self.state = 'idle'

        elif self.state == 'deterrence':
            elapsed_time = current_time - self.start_time
            if elapsed_time > 20:
                print("Deterrence completed. Returning to idle state")
                self.state = 'idle'

    def run(self):
        while True:
            # Replace these with your actual sensor inputs
            beam_break_broken = get_beam_break_sensor_value()
            animal_detected = get_animal_detection_sensor_value()

            self.update(beam_break_broken, animal_detected)
            time.sleep(1)  # Delay to simulate real-time updates

# Function to simulate beam break sensor (replace this with real sensor input)
def get_beam_break_sensor_value():
    # Your code to read from the beam break sensor
    return decision(0.1)  # Simulate beam break sensor (replace with real value)

# Function to simulate animal detection sensor (replace this with real sensor input)
def get_animal_detection_sensor_value():
    # Your code to read from the animal detection sensor
    return decision(.1)  # Simulate animal detection (replace with real value)

# function to generate decision with probability P
def decision(P):
    return random.random()<P


# Instantiate and run the system
system = AnimalDeterrenceSystem()
system.run()
