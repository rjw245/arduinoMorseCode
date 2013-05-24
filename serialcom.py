import serial

class Arduino:
	def __init__(self):
		#Load from settings file
		settings = open('settings')
		settingsLines = settings.readlines()
		self.port = settingsLines[1].strip()
		self.baud = settingsLines[4].strip()

		#Open serial
		self.ser = serial.Serial(self.port,self.baud)
		self.ser.open()

	def turnOn(self):
		self.ser.write('1')

	def turnOff(self):
		self.ser.write('0')

	def isReady(self):
		return self.ser.read()
