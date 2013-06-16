from serialcom import Arduino
import time


class MorseCode:
	code = {
		'a':".-",
		'b':"-...",
		'c':"-.-.",
		'd':"-..",
		'e':".",
		'f':"..-.",
		'g':"--.",
		'h':"....",
		'i':"..",
		'j':".---",
		'k':"-.-",
		'l':".-..",
		'm':"--",
		'n':"-.",
		'o':"---",
		'p':".--.",
		'q':"--.-",
		'r':".-.",
		's':"...",
		't':"-",
		'u':"..-",
		'v':"...-",
		'w':".--",
		'x':"-..-",
		'y':"-.--",
		'z':"--..",
		'1':".----",
		'2':"..---",
		'3':"...--",
		'4':"....-",
		'5':".....",
		'6':"-....",
		'7':"--...",
		'8':"---..",
		'9':"----.",
		'0':"-----"
	}

	def __init__(self,arduino,speed=.15):
		self.arduino = arduino
		self.TIMEUNIT=speed

	def changeSpeed(self,speed):
		self.TIMEUNIT=speed

	def changeArduino(self,arduino):
		self.arduino=arduino

	def pause(self,numUnits=1):
		time.sleep(self.TIMEUNIT * numUnits)

	def dot(self):
		self.arduino.write('1')
		self.pause()
		self.arduino.write('0')

	def dash(self):
		self.arduino.write('1')
		self.pause(3)
		self.arduino.write('0')

	def writeLetter(self,char):
		char = char.lower()
		curCode = list(self.code[char])
		c = 0
		for symbol in curCode:
			if symbol == '.':
				self.dot()
			elif symbol == '-':
				self.dash()

			if c < len(curCode)-1:
				self.pause()
			c=c+1

	def writeWord(self,word):
		letters = list(word)
		c=0
		for letter in letters:
			#~ Gets rid of chars without morse translation:
			if letter.lower() in self.code:
				self.writeLetter(letter)
				if c < len(letters)-1:
					self.pause(3)
			c=c+1

	def writeString(self,string):
		words = string.split()
		c = 0
		for word in words:
			self.writeWord(word)
			if c < len(words)-1:
				self.pause(7)
			c=c+1

	def printMorse(self,string):
		string = string.lower()
		chars = list(string)
		morseString = ""
		for c in chars:
			if c in self.code:
				morseString = morseString + self.code[c] + " "
			elif c==" ":
				morseString = morseString + "   "
			else:
				morseString = morseString + c + " "
		return morseString


