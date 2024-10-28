# sound_deterrence.py
# Veg Group 2

# RPI4B Configuration:

# Install libraries:
# sudo apt-get update
# sudo apt-get install pulseaudio pulseaudio-module-bluetooth mpg321

# Run bluetoothct1: bluetoothct1
# Turn on the agent: agent on
# Scan for speaker: scan on

# Look for the speaker's MAC addresses
# pair: pair XX:XX:XX:XX:XX:XX
# trust: trust XX:XX:XX:XX:XX:XX
# connect: connect XX:XX:XX:XX:XX:XX
# exit: exit

import os
import subprocess
import time
import pygame

def run_sound_deterrence(speaker_mac, cycle):
    # Attempt to connect to speaker.
    if (connect_bluetooth_speaker(speaker_mac)):
        print("Connected to speaker.")
        # Play audio.
        if cycle < 10:
            file_path = f"./Pi_MP3/C_0{cycle}.mp3"
        else:
            last_digit = cycle - 10
            file_path = f"./Pi_MP3/C_1{last_digit}.mp3"
                     
        print(f"Playing audio file: {file_path}")
        play_audio(file_path)
    else:
        print("Failed to connect to speaker.")
                    

# speaker_mac (str): "XX:XX:XX:XX:XX:XX"
def connect_bluetooth_speaker(speaker_mac):
    # restart bluetooth service
    subprocess.run("sudo systemctl stop bluetooth", shell=True) 
    subprocess.run("sudo systemctl start bluetooth", shell=True)
    subprocess.run(f"bluetoothctl info {speaker_mac}", shell = True)

    # attempt to connect to speaker
    try:
        subprocess.run(f"bluetoothctl connect {speaker_mac}", shell=True, check=True)
        print(f"Connected to bluetooth speaker {speaker_mac}")
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to connect to bluetooth speaker {speaker_mac}")
        return False

# file_path (str): "CXX.mp3"
def play_audio(file_path):
    # play the MP3 file using mpg321

    try:
        subprocess.Popen(f"mpg321 {file_path}", shell=True)
        
    except subprocess.CalledProcessError:
        print(f"Failed to play audio file: {file_path}")

