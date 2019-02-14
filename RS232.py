# -*- coding: utf-8 -*-

'''
This takes an RS232 byte-encoded signal and converts it to a string of the values

Baud Rate, Port, Parity, and Timeout can be changed
Currently set for the AND GF-2000 RS232 format
Adjust Timeout as needed
'''

import gom
import serial
import DialogContainer

ser = serial.Serial()

ser.baudrate = 1200
ser.port = 'COM6'
ser.parity = 'E'
ser.timeout = 20 #Wait time in Seconds

def ReadPort():	
	ser.open()
	byte = ser.readline(100)
	if not byte:
		DialogContainer.PopScaleError()
	ser.close()
	return byte

def decoderRing(encodedByte):
	x = str(encodedByte).split("\\")
	decoded = ''
	for i in x:
		for j in i:
			if j.isnumeric() == True:
				decoded = decoded + j
			elif '.' in j:
				decoded = decoded + j
	decoded = decoded[0:8]
	return decoded
	
def stripLeadingZeros(decodedByte):
	currentCharacter = 0
	zeroCount = 0
	
	for character in decodedByte:
		currentCharacter = character
		if currentCharacter == '0':
			zeroCount += 1
		else:
			trimmedByte = decodedByte[zeroCount:]
			return trimmedByte	

def parseByte():
	byte = ReadPort()
	decodedByte = decoderRing(byte)
	trimmedByte = stripLeadingZeros(decodedByte)
	try:
		if float(trimmedByte) < 1:
			DialogContainer.PopNoSample()
			return None
	except:
		return None
	return trimmedByte


		




	

			


