# AnimalDeterrenceSystem.py
# Veg Group 2
# Run this to start the system. Currently in simulation mode.


import time
import random # used for simulation
from sound_deterrence import *
from light_deterrence import *
from flood_light import *

# TODO: connect speaker and trust to get mac addr
speaker_mac = "XX:XX:XX:XX:XX:XX"

class AnimalDeterrenceSystem:

    
    # Initiate system.
    def __init__(self):

        # Attempt to connect to speaker.
        if (connect_bluetooth_speaker(speaker_mac)):
            print("Connected to speaker.")
        else:
            print("Failed to connect to speaker.")

        # Set initial state to idle.
        self.state = 'idle'
        self.start_time = time.time()
        print("Starting system in idle... (simulation /w 5% P each)")

    # Update the state.
    def update(self, beam_break_broken, animal_detected):
        print("Updating state...")
        current_time = time.time()

        # State transitions
        if self.state == 'idle':
            if beam_break_broken:
                print("Beam broken! Transitioning to detection state")
                # TODO: need to turn on cameras

                # Turn on flood light.
                turn_on_flood_light()

                # Change state to Detection.
                self.state = 'detection'
                self.start_time = current_time
        
        elif self.state == 'detection':
            elapsed_time = current_time - self.start_time
            if animal_detected and elapsed_time <= 20:
                print("Animal detected! Transitioning to deterrence state")
                # TODO: turn off cameras and turn on motor and define audio path

                # TUrn off flood light.
                turn_off_flood_light()
                # Turn on strobe light.
                turn_on_strobe_light()
                # Play audio.
                play_audio(file_path)
                self.state = 'deterrence'
                self.start_time = current_time
            elif elapsed_time > 20:
                print("No animal detected within 20 seconds. Returning to idle state")
                # TODO: turn off cameras

                # Turn off flood light.
                turn_off_flood_light()
                self.state = 'idle'

        elif self.state == 'deterrence':
            elapsed_time = current_time - self.start_time
            if elapsed_time > 20:
                print("Deterrence completed. Returning to idle state")
                # TODO: stop audio, stop motor, repeat audio

                # Change strobe pattern.
                change_strobe_pattern()
                # Turn off strobe light.
                turn_off_strobe_light()
                self.state = 'idle'

    def run(self):
        while True:
            
            # Update beam and detection algorithm if in correct state.
            if state.self == 'idle':
                beam_break_broken = get_beam_break_sensor_value()
            elif state.self == 'detection':
                animal_detected = get_animal_detection_sensor_value()

            self.update(beam_break_broken, animal_detected)
            time.sleep(1)  # Delay to simulate real-time updates

# Function to simulate beam break sensor (replace this with real sensor input)
def get_beam_break_sensor_value():
    # TODO: code to read from the beam break sensor
    return decision(0.1)  # Simulate beam break sensor (replace with real value)

# Function to simulate animal detection sensor (replace this with real sensor input)
def get_animal_detection_sensor_value():
    # TODO: code to read from the animal detection sensor
    return decision(.1)  # Simulate animal detection (replace with real value)

# function to generate decision with probability P
def decision(P):
    return random.random()<P


# Instantiate and run the system
system = AnimalDeterrenceSystem()
system.run()
