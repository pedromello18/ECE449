# sound_deterrence.py
# Veg Group 2

# RPI4B Configuration:

# Install libraries:
# sudo apt-get update
# sudo apt-get install pulseaudio pulseaudio-module-bluetooth mpg321

import os
import subprocess
import time
import pygame

def run_sound_deterrence(cycle):
    print("Connected to speaker.")
    # Play audio.
    if cycle < 10:
        file_path = f"./Pi_MP3/C_0{cycle}.mp3"
    else:
        last_digit = cycle - 10
        file_path = f"./Pi_MP3/C_1{last_digit}.mp3"
                    
    print(f"Playing audio file: {file_path}")
    play_audio(file_path)

# file_path (str): "CXX.mp3"
def play_audio(file_path):
    # play the MP3 file using mpg321
    try:
        subprocess.Popen(f"mpg321 {file_path}", shell=True)
        
    except subprocess.CalledProcessError:
        print(f"Failed to play audio file: {file_path}")