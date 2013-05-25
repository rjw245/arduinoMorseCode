arduinoMorseCode
================

Python interfaced with Arduino serial to allow Python to light LED to speak in morse code

"settings" contains the settings for this program, which are very simple. On one line is the port for the Arduino you'd like to communicate with via serial. On another is the baud rate for this Arduino. Do not move these settings onto different lines, as Python expects them to be on the current line numbers.

"main.py" is the Python script you'll run to execute the program. Will ready the arduino and then prompt the user for input. Prints the corresponding morse code to the terminal at the same time that it bleeps the code on the arduino.

"serialcom.py" contains the necessary functionality to send serial commands to the Arduino to turn its LED on and off.

"morse.py" uses the serialcom.py library to bleep morse code on the Arduino.

"arduinoMorseCode.ino" is the code that runs on the Arduino. The LED pin is 7 by default, but can be changed easily at the top of the code.

NOTE:
This code has only been tested on an Ubuntu 12.04 Linux install. I have reason to believe this will not work properly on a Windows machine as serial ports work differently on that OS.

