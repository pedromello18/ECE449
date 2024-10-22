**sound_deterrence.py:** Comments in the beginning include instructions for setting up the speaker on the RPI before running.
* connect_bluetooth_speaker(speaker_mac): connects to speaker with mac format of "XX:XX:XX:XX:XX:XX"
* play_audio(file_path): plays mp3 file with path of "CXX.mp3"
* to run: if (connect_bluetooth_speaker): play_audio(file_path)...

**light_deterrence.py:** Comments in the beginning include instructions for setting up the RPI.
* turn_on_strobe_light(): turns on strobe with previous pattern
* turn_off_strobe_light()
* change_strobe_pattern(): turns high and sleeps for 1s to change pattern
