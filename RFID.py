# -*- coding: utf-8 -*-

"""RFID
Contains Functions:
---
---
"""

# Script: RFID
#
# Script-Version: 1.1.0
#
# ChangeLog:

# v1.1.1: Changed Dialog Box and implemented changes
# v1.1.0: Added check for signal strength, displays Right/Left depedning on signal strength 
# v1.0.0: Initial version


import gom
import time
import socket 

class RFID_System(object):
	"""
		A class that defines a complete RFID system
		
	"""
	IP = '169.254.11.210'
	PORT_IO = 2111
	PORT_DIAG = 2112

	MSG_START = b'\x02sMN '
	MSG_END = b'\x03'	

	def __init__(self, ip, port_io = 2111, port_diag=2112, timeout = 4):
		"""
			Initializes the class representation of an RFID system
			ip = The ipv-4 address of the RFID device, as a string. Ex: "192.168.1.1"
			port_io = The IO port of the RFID device (if it has one) as an integer
			port_diag = The diagnostic port of the RFID device (if it has one) as an integer
		"""
		self.IP = ip
		self.PORT_IO = port_io
		self.PORT_DIAG = port_diag
		self.TIMEOUT = timeout
		self.IO_SOCK = self.setup_socket(self.IP, self.PORT_IO, self.TIMEOUT)
		self.DIAG_SOCK = self.setup_socket(self.IP, self.PORT_DIAG, self.TIMEOUT)  
		
	def __del__(self):
		"""
			Ensures all used sockets are safely shut down
		"""
		if self.IO_SOCK is not None:
			self.IO_SOCK.shutdown(0)
			self.IO_SOCK.close()
		
		if self.DIAG_SOCK is not None:
			self.DIAG_SOCK.shutdown(0)
			self.DIAG_SOCK.close()
	
	def close_IO(self):
		"""
			Disconnects the IO socket
		"""
		if self.IO_SOCK is not None:
			self.IO_SOCK.shutdown(0)
			self.IO_SOCK.close()
			
	def close_DIAG(self):
		"""
			Disconnects the diagnostic socket
		"""
		if self.DIAG_SOCK is not None:
			self.DIAG_SOCK.shutdown(0)
			self.DIAG_SOCK.close()
	
	def extract_message(self, input_rfid):
		"""
			Removes the start/end signals from an RFID message
			Returns a byte array
		"""
		return str(input_rfid)[30:34]
	
	def compose_message(self, utf_message):
		"""
			Creates a byte message to send to RFID
		"""
		return self.MSG_START + utf_message.encode('utf-8') + self.RMSG_END
		
	def setup_socket(self, ip, port, timeout = 4):
		"""
			Creates the sockets to communicate with the RFID system
		""" 
		print('RFID.setup_socket_I.O._IP:  ',ip) 
		s = socket.socket()
		s.connect(( ip, port ))
		s.settimeout( timeout )
		return s
		
	def send_IO(self, msg):
		"""
			Sends a message via the IO socket
		"""
		self.IO_SOCK.send(msg)
		
	def send_DIAG(self, msg):
		"""
			Sends a message via the DIAGNOSTIC socket
		"""
		self.DIAG_SOCK.send(msg)
		
	def read_IO(self, bytes = 1028):
		mydata = self.IO_SOCK.send(b'K')
		print('RFID.read_IO: message sent: {}'.format(mydata))
		
		recieved_data = self.IO_SOCK.recv(bytes)
		return recieved_data 
		
	def multiple_tags(self, tag_value): 
		count = 0
		new_value = tag_value
		new_value = str(new_value)
		new_value = new_value.strip("b'")
		tags = new_value.split('\\') 
		print(tags)
		new_tags = [] 
		tag_ids = []
		for i in tags:
			if len(i)> 7: 
				tag_ids.append(i[23:27]) 
		for i in tag_ids: 
			print("RFID.multiple_tags: ",i) 
		return tag_ids		
		
