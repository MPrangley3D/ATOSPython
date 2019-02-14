# -*- coding: utf-8 -*-

"""RFID Dict
Contains Functions:
---
---
"""

import gom

def FetchTemplate(RFID):
	
	if RFID == "4A55":
		filter = ['_02A']			
	
	elif RFID == "<NEW RFID TAG GOES HERE>":
		filter = ['*_04A*']
		
	elif RFID == "4A45":
		filter = ['*_09A*']
		#filter = ['*TST*']	

	#Fill these as needed
	elif RFID == "":
		filter = ['**']
		
	elif RFID == "":
		filter = ['**']
		
	elif RFID == "":
		filter = ['**']
	
	elif RFID == "":
		filter = ['**']
	
	elif RFID == "":		
		filter = ['**']
		
	elif RFID == "":
		filter = ['**']
		
	elif RFID == "":
		filter = ['**']
	
	elif RFID == "":
		filter = ['**']
		
	elif RFID == "":
		filter = ['**']
		
	elif RFID == "":
		filter = ['**']
	
	elif RFID == "":
		filter = ['**']
	
	else:	
		RESULT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
			' <title>Message</title>' \
			' <style></style>' \
			' <control id="OkCancel"/>' \
			' <position>automatic</position>' \
			' <embedding>always_toplevel</embedding>' \
			' <sizemode>automatic</sizemode>' \
			' <size height="126" width="315"/>' \
			' <content rows="1" columns="1">' \
			'  <widget rowspan="1" column="0" type="display::text" row="0" columnspan="1">' \
			'   <name>text</name>' \
			'   <tooltip></tooltip>' \
			'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
			'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
			'p, li { white-space: pre-wrap; }' \
			'&lt;/style>&lt;/head>&lt;body style="    ">' \
			'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-weight:600;">ERROR:  No suitable templates found for RFID&lt;/span>&lt;/p>&lt;/body>&lt;/html></text>' \
			'   <wordwrap>false</wordwrap>' \
			'  </widget>' \
			' </content>' \
			'</dialog>')
		workflow.exit_handler()
		
	return filter
