from collections import defaultdict

"""Dict Builder
This is a lifehack to store lists against a key in a dictionary
---
"""

class ConfigDict(object):
	'''ConfigDict
	Initializes a Config Dictionary Class Instance
	Function: add
	---Accepts a list of keys as string, and associated lists
	---Example: dict.add() ([('key1',1),('key2',2),('key3',1),('key1',3))])
	---Results in:  dict.items() [('key1',[1,3]),('key2',[2]),('key3',[1])]
	---The Reason for the added convolution is to allow storing of a list of lists
	---This allows for our mixed lot of parts capabilities for operate
	Function: Read
	---Returns the values stored for the given key (taken as a string)
	'''
	def __init__(self):
		self.dict = defaultdict(list)
	def add(self,configList):
		'''add
		Arguments:
		---ConfigList:  A list of key and value pairs.  The value can be another list.
		------Ex:  ConfigList = [('example',[1,2,3])]  OR [('example',[1,2,3]),('example2',[1,2,3]),('example3',[1,2,3])...]		
		'''	
		for key, item in configList:
			self.dict[key].append(item)
	def read(self,key):
		'''read
		Arguments:
		---key: Accepts a string pointing to the key of the dictionary
		---Returns the list associated with that key.  This list may contain multiple lists.		
		'''	
		return self.dict[key]
	def get(self):
		return self.dict
		
		
		
