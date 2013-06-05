import morse
import serialcom
import time
import sys
import traceback

try:
	#Load from settings file
	settings = open('settings')
	settingsLines = settings.readlines()
	port = settingsLines[1].strip()
	baud = settingsLines[4].strip()

	print "Readying arduino..."
	myArduino = serialcom.Arduino(port,baud)
	myArduino.init() #Delays until ready

	morseGen = morse.MorseCode(myArduino,.15)

	while 1:
		string = raw_input("Enter text: ")
		print morseGen.printMorse(string)
		morseGen.writeString(string)

except serialcom.serial.SerialException:
	print "Unable to connect to Arduino."
	print "Port: " + port
	print "Baud: " + baud

except KeyboardInterrupt:
	print "Shutdown requested...exiting"

except Exception:
	traceback.print_exc(file=sys.stdout)
sys.exit(0)
