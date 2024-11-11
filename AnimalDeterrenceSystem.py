# AnimalDeterrenceSystem.py
# Veg Group 2
# Run this to start the system. Currently in simulation mode.

# 11/11 TODO (Alex):
# Test flood light and strobe light with 3V relays. Test modulated, then combined.
# Test camera setup and implement deterrence into FSM.
# Become familiar with motion deterrence and detection code today.


import time
import random # used for simulation
from deterrence.sound_deterrence import *
from deterrence.light_deterrence import *
from deterrence.flood_light import *
from deterrence.beam_break import *

# TODO: connect speaker and trust to get mac addr
speaker_mac = "00:1A:7D:B0:57:39"

class AnimalDeterrenceSystem:

    
    # Initiate system.
    def __init__(self):

        

        # Set initial state to idle.
        self.cycle = 0
        self.state = 'idle'
        self.start_time = time.time()
        print("Starting system in idle...")

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
                print(f"Cycle Number: {self.cycle}")
                
                
                
                # TODO: turn off cameras and turn on motor and define audio path
                #run_sound_deterrence(speaker_mac, self.cycle) # make sure speaker is on!
                # Turn off flood light.
                #turn_off_flood_light()
                # Turn on strobe light.
                #turn_on_strobe_light()
               
                
               
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
            print(f"{elapsed_time}")
            if elapsed_time > 20:
                print("Deterrence completed. Returning to idle state")
                # TODO: stop audio, stop motor, repeat audio
                
                # update cycle number
                if self.cycle == 19:
                    self.cycle = 0
                else:
                    self.cycle = self.cycle + 1
                
                # Change strobe pattern.
                change_strobe_pattern()
                # Turn off strobe light.
                turn_off_strobe_light()
                self.state = 'idle'

    def run(self):
        while True:
            
            # Update beam and detection algorithm if in correct state.
            if self.state == 'idle': # IDLE STATE: update beam break ONLY
                beam_break_broken = get_beam_break_sensor_value()
                self.update(beam_break_broken, 0)
            elif self.state == 'detection': # DETECTION STATE: update camera ONLY
                animal_detected = get_animal_detection_sensor_value()
                self.update(0, animal_detected)
            else: # DETERRENCE STATE: update nothing (waits 20 seconds to return to idle)
                self.update(0,0)

            # REMOVE WHEN READY TO TEST BEAM BREAK/CAMERA
            #time.sleep(1)  # Delay to simulate real-time updates
            

# Function to simulate beam break sensor (replace this with real sensor input)
def get_beam_break_sensor_value():
    # TODO: code to read from the beam break sensor
    return monitor_beam() # Simulate beam break sensor (replace with real value)

# Function to simulate animal detection sensor (replace this with real sensor input)
def get_animal_detection_sensor_value():
    # TODO: code to read from the animal detection sensor
    return decision(.5)  # Simulate animal detection (replace with real value)

# function to generate decision with probability P
def decision(P):
    return random.random()<P


# Instantiate and run the system
system = AnimalDeterrenceSystem()
system.run()

