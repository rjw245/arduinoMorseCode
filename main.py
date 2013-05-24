import morse
import serialcom
import time
import sys

arduino = serialcom.Arduino()
while not arduino.isReady():
	pass #Spin while arduino not ready

string = sys.argv[1]
morseGen = morse.MorseCode(arduino)
morseGen.writeString(string)
