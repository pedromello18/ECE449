# sound_deterrence.py
# Veg Group 2
# Alex Penne

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

# speaker_mac (str): "XX:XX:XX:XX:XX:XX"
def connect_bluetooth_speaker(speaker_mac):
    # turn on bluetooth service
    subprocess.run("sudo systemct1 start bluetooth", shell=True)

    # attempt to connect to speaker
    try:
        subprocess.run(f"bluetoothct1 connect {speaker_mac}", shell=True, check=True)
        print(f"Connected to bluetooth speaker {speaker_mac}")
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to connect to bluetooth speaker {speaker_mac}")
        return False

# file_path (str): "CXX.mp3"
def play_audio(file_path):
    # play the MP3 file using mpg321

    try:
        subprocess.run(f"mpg321 {file_path}", shell=True, check=True)
        print(f"Playing audio file: {file_path}")
    except: subprocess.CalledProcessError:
        print(f"Failed to play audio file: {file_path}")

