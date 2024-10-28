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
        #pygame.init()
        #pygame.mixer.music.load('./Pi_MP3/C_00.mp3')
        #pygame.mixer.music.play()
        subprocess.Popen(f"mpg321 {file_path}", shell=True)
        
    except subprocess.CalledProcessError:
        print(f"Failed to play audio file: {file_path}")

