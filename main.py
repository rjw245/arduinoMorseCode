import morse
import serialcom
import time
import sys

arduino = serialcom.Arduino()
while not arduino.isReady():
	pass #Spin while arduino not ready

# arduino.turnOn()
# time.sleep(1)
# arduino.turnOff()

# time.sleep(2)

string = sys.argv[1]
morseGen = morse.MorseCode(arduino)
morseGen.writeString(string)