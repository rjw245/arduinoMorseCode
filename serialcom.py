import serial
#Must be running the .ino in this package for
#Arduino to function.

class Arduino:
	def __init__(self,port='/dev/ttyUSB0',baud=9600):
		#Open serial
		self.port = port
		self.baud = baud
		self.ser = serial.Serial(self.port,self.baud)
		self.ser.open()

	def turnOn(self):
		self.ser.write('1')

	def turnOff(self):
		self.ser.write('0')

	def isReady(self):
		return self.ser.read()
