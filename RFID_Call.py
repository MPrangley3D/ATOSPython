# -*- coding: utf-8 -*-

"""RFID Call
Contains Functions:
---
---
"""

import gom
import RFID 
import RFID_Dict
from RFID import RFID_System


def Scan():

	RFID_container = RFID.RFID_System(RFID_System.IP, RFID_System.PORT_DIAG) 

	try:
		tag_value = RFID_container.read_IO()  
		print('Tag Read: ',tag_value)  
	except:
		tag_value = ''
		print('No RFID Found')
	
	myTags = RFID_container.multiple_tags(tag_value)
	print(myTags)
	
	if len(myTags) == 1:
		filter = RFID_Dict.FetchTemplate(myTags[0])
		
	elif len(myTags) > 1:
		print('TOO MANY COOKS!')
		RESULT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
			' <title>ERROR</title>' \
			' <style></style>' \
			' <control id="OkCancel"/>' \
			' <position>automatic</position>' \
			' <embedding>always_toplevel</embedding>' \
			' <sizemode>automatic</sizemode>' \
			' <size height="162" width="304"/>' \
			' <content rows="1" columns="1">' \
			'  <widget rowspan="1" column="0" type="display::text" row="0" columnspan="1">' \
			'   <name>text</name>' \
			'   <tooltip></tooltip>' \
			'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
			'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
			'p, li { white-space: pre-wrap; }' \
			'&lt;/style>&lt;/head>&lt;body style="    ">' \
			'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-weight:600;">ERROR:  TOO MANY RFID SIGNALS FOUND!!!!&lt;/span>&lt;/p>' \
			'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;">&lt;br />&lt;/p>' \
			'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-weight:600;">Remove Multiple Fixtures Before Continuing.&lt;/span>&lt;/p>' \
			'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>&lt;/body>&lt;/html></text>' \
			'   <wordwrap>false</wordwrap>' \
			'  </widget>' \
			' </content>' \
			'</dialog>')
		workflow.exit_handler()

	return filter	


	





