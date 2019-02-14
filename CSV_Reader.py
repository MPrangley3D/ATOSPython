# -*- coding: utf-8 -*-

"""CSV Reader

Contains Functions:
---ReadCSV(configLoc,myPart,myFixt,config)
---	Returns the provided config dictionary instance, filled with the parsed CSV data
"""
	
import gom
import DictBuilder
from collections import defaultdict
import csv 

def ReadCSV(configLoc,myPart,myFixt,config):
	"""Read CSV
	
	Keyword arguments:
	configLoc -- File location of the Config .CSV
	myPart -- string: 4 Digit Part #
	myFixt -- string: 3 Character Fixture ID
	config -- Object: instance of the config dictionary class
	
	Returns the provided config dictionary instance, filled with the parsed CSV data
	"""
	found = False
	
	with open(configLoc,'r') as csvfile:
		reader = csv.reader(csvfile,delimiter=',')
		for row in reader:
			if myPart in row[1] and myFixt in row[0]:                      
				found = True
				_fixturePoints = row[13].split(',')
				fixturePoints = []
				for f in _fixturePoints:
					fixturePoints.append(int(f))
				_numParts = row[3].split(',')	
				numParts = []
				for np in _numParts:
					numParts.append(np)
				_iTemplate = row[7].split(',')
				inspectionTemplate = []
				for it in _iTemplate:
					inspectionTemplate.append(row[6]+it)
				_xOffset = row[14].split(',')
				xOffset = []
				for x in _xOffset:
					xOffset.append(int(x))
				_yOffset = row[15].split(',')
				yOffset = []
				for y in _yOffset:
					yOffset.append(int(y))
				_zOffset = row[16].split(',')
				zOffset = []
				for z in _zOffset:
					zOffset.append(int(z))
				_zRotArray = row[17].split(',')
				zRotArray = []
				for zr in _zRotArray:
					zRotArray.append(int(zr))			
				lComp = int(row[18])
				wComp = int(row[19])
				hComp = int(row[20])
				directory = row[2]
				meshArea = int(row[21])
				_winSPCname = row[8].split(',')
				winSPCname = []
				partNR = []
				for name in _winSPCname:
					winSPCname.append(name)
					partNR.append(name[0:13])
				key_Location = row[5]
				_key_Material = row[9].split(',')
				key_Material = []
				for km in _key_Material:
					key_Material.append(km)
				_key_Print = row[10].split(',')
				key_Print = []
				for kp in _key_Print:
					key_Print.append(kp)
				_key_PartName = row[11].split(',')
				key_PartName = []
				for kpn in _key_PartName:
					key_PartName.append(kpn)
				key_System = str(row[12])
				_nestID = row[4].split(',')
				nestID = []
				for n in _nestID:
					splitter = n.split(';')
					nestID.append(splitter)
				nestID = [list(map(int, x)) for x in nestID]
				_manualDialogTitleArray = row[22].split(',')
				manualDialogTitleArray = []
				for title in _manualDialogTitleArray:
					manualDialogTitleArray.append(title)
				_manualDialogTextArray = row[23].split(',')
				manualDialogTextArray = []
				for text in _manualDialogTextArray:
					manualDialogTextArray.append(text)
				_manualDialogTypeArray = row[24].split(',')
				manualDialogTypeArray = []
				for type in _manualDialogTypeArray:
					manualDialogTypeArray.append(type)
				
		if found == False:
			print('$$$ DEBUG : CANNOT LOCATE TEMPLATE FOR VMR: '+myPart+myFixt)
			NOTMP=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
				' <title>Message</title>' \
				' <style></style>' \
				' <control id="OkCancel"/>' \
				' <position>automatic</position>' \
				' <embedding>always_toplevel</embedding>' \
				' <sizemode>automatic</sizemode>' \
				' <size height="184" width="322"/>' \
				' <content rows="2" columns="2">' \
				'  <widget row="0" column="0" columnspan="2" type="display::text" rowspan="1">' \
				'   <name>text</name>' \
				'   <tooltip></tooltip>' \
				'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
				'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
				'p, li { white-space: pre-wrap; }' \
				'&lt;/style>&lt;/head>&lt;body style="    ">' \
				'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-weight:600;">ERROR: NO CONFIGURATION TEMPLATE FOUND&lt;/span>&lt;/p>&lt;/body>&lt;/html></text>' \
				'   <wordwrap>false</wordwrap>' \
				'  </widget>' \
				'  <widget row="1" column="0" columnspan="1" type="label" rowspan="1">' \
				'   <name>label</name>' \
				'   <tooltip></tooltip>' \
				'   <text>'+myPart+'</text>' \
				'   <word_wrap>false</word_wrap>' \
				'  </widget>' \
				'  <widget row="1" column="1" columnspan="1" type="label" rowspan="1">' \
				'   <name>label_1</name>' \
				'   <tooltip></tooltip>' \
				'   <text>'+myFixt+'</text>' \
				'   <word_wrap>false</word_wrap>' \
				'  </widget>' \
				' </content>' \
				'</dialog>')	
		
	globalArrayLists = [fixturePoints, numParts, inspectionTemplate, xOffset, yOffset, zOffset, zRotArray, winSPCname, key_Material, key_Print, key_PartName, nestID, partNR, manualDialogTitleArray, manualDialogTextArray, manualDialogTypeArray]
	globalArrayKeys = ['fixturePoints', 'numParts', 'inspectionTemplate', 'xOffset', 'yOffset', 'zOffset', 'zRotArray', 'winSPCname', 'key_Material', 'key_Print', 'key_PartName', 'nestID', 'partNR', 'manualDialogTitleArray', 'manualDialogTextArray', 'manualDialogTypeArray']
	
	arrayPosition = 0
	if len(globalArrayKeys) == len(globalArrayLists):
		for array in globalArrayLists:
			#print('Array Start: ',array)
			
			for item in array:
				#print('Subitem: ',item)
				#print('Array: ',array)
				config.add([(globalArrayKeys[arrayPosition],item)])
				
			#print (arrayPosition)
			arrayPosition+=1
	else:
		print('ERROR: Mismatch in Keys & Lists')


	globalVariableList = [lComp, wComp, hComp, directory, meshArea,key_Location, key_System]
	globalVariableKeys = ['lComp', 'wComp', 'hComp', 'directory', 'meshArea', 'key_Location', 'key_System']
	
	arrayPosition = 0
	if len(globalVariableKeys) == len(globalVariableList):
		for var in globalVariableList:
			#print('Var Start: ',var)
			config.add([(globalVariableKeys[arrayPosition],var)])
			arrayPosition+=1
		
	else:
		print('ERROR: Mismatch in Keys & Lists')
		
	return config
	

	
