import morse
import serialcom
import time
import sys

import sys, traceback

def main():
	try:
		print "Readying arduino..."
		arduino = serialcom.Arduino()
		while not arduino.isReady():
			pass #Spin while arduino not ready

		morseGen = morse.MorseCode(arduino,.15)

		while 1:
			string = raw_input("Enter text: ")
			print morseGen.printMorse(string)
			morseGen.writeString(string)

	except KeyboardInterrupt:
		print "Shutdown requested...exiting"
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
	main()
