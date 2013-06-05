import serial
import time
#Must be running the .ino in this package for
#Arduino to function.

class ArduinoError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class Arduino:
	def __init__(self,port='/dev/ttyUSB0',baud=9600):
		#Open serial
		self.port = port
		self.baud = baud
		self.ser = serial.Serial(port=self.port,baudrate=self.baud,timeout=0)
		self.ser.open()

	def turnOn(self):
		self.ser.write('1')

	def turnOff(self):
		self.ser.write('0')

	#Asks for ready signal, delays up to two secs until received
	def init(self):
		self.ser.write('r')
		lastChar = self.ser.read()
		end_time = time.time() + 2
		while (not lastChar) and time.time() < end_time:
			self.ser.write('r')
			lastChar = self.ser.read()
		if not lastChar:
			raise ArduinoError("Arduino timed out.")