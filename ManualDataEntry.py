# -*- coding: utf-8 -*-

"""Manual Data Entry
Contains Functions:
---manualEntry
------This controls the manual entry popup dialog
"""
import gom

def dataEntry(sampleCount,dialogTitle,dialogText,dialogType):
	'''manualEntry
	
	Takes Arguments:
	---sampleCount
	------
	---manualDialogTitleArray
	------
	---manualDialogTextArray
	------
	---manualDialogTypeArray
	------
	'''

	label1 = 'No Sample'
	container1 = '<widget rowspan="1" columnspan="1" row="1" column="1" type="separator"><name>input_1</name><tooltip></tooltip><title></title></widget>'
	if 1 in sampleCount:
		label1 = 'Cavity #1'
		if dialogType == 'var':
			container1 = '<widget rowspan="1" columnspan="1" row="1" column="1" type="input::number"><name>input_1</name><tooltip></tooltip><value>0</value><minimum>0</minimum><maximum>1000</maximum><precision>2</precision><background_style></background_style></widget>'
		elif dialogType == 'bool':
			container1 = '<widget rowspan="1" columnspan="1" row="1" column="1" type="input::list"><name>input_1</name><tooltip></tooltip><items><item>Pass</item><item>Fail</item></items><default>Pass</default></widget>'
	label2 = 'No Sample'
	container2 = '<widget rowspan="1" columnspan="1" row="2" column="1" type="separator"><name>input_2</name><tooltip></tooltip><title></title></widget>'
	if 2 in sampleCount:
		label2 = 'Cavity #2'
		if dialogType == 'var':
			container2 = '<widget rowspan="1" columnspan="1" row="2" column="1" type="input::number"><name>input_2</name><tooltip></tooltip><value>0</value><minimum>0</minimum><maximum>1000</maximum><precision>2</precision><background_style></background_style></widget>'
		elif dialogType == 'bool':
			container2 = '<widget rowspan="1" columnspan="1" row="2" column="1" type="input::list"><name>input_2</name><tooltip></tooltip><items><item>Pass</item><item>Fail</item></items><default>Pass</default></widget>'
	label3 = 'No Sample'
	container3 = '<widget rowspan="1" columnspan="1" row="3" column="1" type="separator"><name>input_3</name><tooltip></tooltip><title></title></widget>'
	if 3 in sampleCount:
		label3 = 'Cavity #3'
		if dialogType == 'var':
			container3 = '<widget rowspan="1" columnspan="1" row="3" column="1" type="input::number"><name>input_3</name><tooltip></tooltip><value>0</value><minimum>0</minimum><maximum>1000</maximum><precision>2</precision><background_style></background_style></widget>'
		elif dialogType == 'bool':
			container3 = '<widget rowspan="1" columnspan="1" row="3" column="1" type="input::list"><name>input_3</name><tooltip></tooltip><items><item>Pass</item><item>Fail</item></items><default>Pass</default></widget>'
	label4 = 'No Sample'
	container4 = '<widget rowspan="1" columnspan="1" row="4" column="1" type="separator"><name>input_4</name><tooltip></tooltip><title></title></widget>'
	if 4 in sampleCount:
		label4 = 'Cavity #4'
		if dialogType == 'var':
			container4 = '<widget rowspan="1" columnspan="1" row="4" column="1" type="input::number"><name>input_4</name><tooltip></tooltip><value>0</value><minimum>0</minimum><maximum>1000</maximum><precision>2</precision><background_style></background_style></widget>'
		elif dialogType == 'bool':
			container4 = '<widget rowspan="1" columnspan="1" row="4" column="1" type="input::list"><name>input_4</name><tooltip></tooltip><items><item>Pass</item><item>Fail</item></items><default>Pass</default></widget>'
	label5 = 'No Sample'
	container5 = '<widget rowspan="1" columnspan="1" row="5" column="1" type="separator"><name>input_5</name><tooltip></tooltip><title></title></widget>'
	if 5 in sampleCount:
		label5 = 'Cavity #5'
		if dialogType == 'var':
			container5 = '<widget rowspan="1" columnspan="1" row="5" column="1" type="input::number"><name>input_5</name><tooltip></tooltip><value>0</value><minimum>0</minimum><maximum>1000</maximum><precision>2</precision><background_style></background_style></widget>'
		elif dialogType == 'bool':
			container5 = '<widget rowspan="1" columnspan="1" row="5" column="1" type="input::list"><name>input_5</name><tooltip></tooltip><items><item>Pass</item><item>Fail</item></items><default>Pass</default></widget>'
	label6 = 'No Sample'
	container6 = '<widget rowspan="1" columnspan="1" row="6" column="1" type="separator"><name>input_6</name><tooltip></tooltip><title></title></widget>'
	if 6 in sampleCount:
		label6 = 'Cavity #6'
		if dialogType == 'var':
			container6 = '<widget rowspan="1" columnspan="1" row="6" column="1" type="input::number"><name>input_6</name><tooltip></tooltip><value>0</value><minimum>0</minimum><maximum>1000</maximum><precision>2</precision><background_style></background_style></widget>'
		elif dialogType == 'bool':
			container6 = '<widget rowspan="1" columnspan="1" row="6" column="1" type="input::list"><name>input_6</name><tooltip></tooltip><items><item>Pass</item><item>Fail</item></items><default>Pass</default></widget>'
	label7 = 'No Sample'
	container7 = '<widget rowspan="1" columnspan="1" row="7" column="1" type="separator"><name>input_7</name><tooltip></tooltip><title></title></widget>'
	if 7 in sampleCount:
		label7 = 'Cavity #7'
		if dialogType == 'var':
			container7 = '<widget rowspan="1" columnspan="1" row="7" column="1" type="input::number"><name>input_7</name><tooltip></tooltip><value>0</value><minimum>0</minimum><maximum>1000</maximum><precision>2</precision><background_style></background_style></widget>'
		elif dialogType == 'bool':
			container7 = '<widget rowspan="1" columnspan="1" row="7" column="1" type="input::list"><name>input_7</name><tooltip></tooltip><items><item>Pass</item><item>Fail</item></items><default>Pass</default></widget>'
	label8 = 'No Sample'
	container8 = '<widget rowspan="1" columnspan="1" row="8" column="1" type="separator"><name>input_8</name><tooltip></tooltip><title></title></widget>'
	if 8 in sampleCount:
		label8 = 'Cavity #8'
		if dialogType == 'var':
			container8 = '<widget rowspan="1" columnspan="1" row="8" column="1" type="input::number"><name>input_8</name><tooltip></tooltip><value>0</value><minimum>0</minimum><maximum>1000</maximum><precision>2</precision><background_style></background_style></widget>'
		elif dialogType == 'bool':
			container8 = '<widget rowspan="1" columnspan="1" row="8" column="1" type="input::list"><name>input_8</name><tooltip></tooltip><items><item>Pass</item><item>Fail</item></items><default>Pass</default></widget>'
	
	MANUAL_INPUT=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
	' <title>'+dialogTitle+'</title>' \
	' <style></style>' \
	' <control id="OkCancel"/>' \
	' <position>center</position>' \
	' <embedding></embedding>' \
	' <sizemode>fixed</sizemode>' \
	' <size height="396" width="398"/>' \
	' <content rows="9" columns="2">' \
	'  <widget rowspan="1" columnspan="2" row="0" column="0" type="display::text">' \
	'   <name>text</name>' \
	'   <tooltip></tooltip>' \
	'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
	'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
	'p, li { white-space: pre-wrap; }' \
	'&lt;/style>&lt;/head>&lt;body style="    ">' \
	'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:16pt; font-weight:600;">'+dialogText+'&lt;/span>&lt;/p>&lt;/body>&lt;/html></text>' \
	'   <wordwrap>false</wordwrap>' \
	'  </widget>' \
	'  <widget rowspan="1" columnspan="1" row="1" column="0" type="label">' \
	'   <name>label_1</name>' \
	'   <tooltip></tooltip>' \
	'   <text>'+label1+'</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	' '+container1+''\
	'  <widget rowspan="1" columnspan="1" row="2" column="0" type="label">' \
	'   <name>label_2</name>' \
	'   <tooltip></tooltip>' \
	'   <text>'+label2+'</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	' '+container2+''\
	'  <widget rowspan="1" columnspan="1" row="3" column="0" type="label">' \
	'   <name>label_3</name>' \
	'   <tooltip></tooltip>' \
	'   <text>'+label3+'</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	' '+container3+''\
	'  <widget rowspan="1" columnspan="1" row="4" column="0" type="label">' \
	'   <name>label_4</name>' \
	'   <tooltip></tooltip>' \
	'   <text>'+label4+'</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	' '+container4+''\
	'  <widget rowspan="1" columnspan="1" row="5" column="0" type="label">' \
	'   <name>label_5</name>' \
	'   <tooltip></tooltip>' \
	'   <text>'+label5+'</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	' '+container5+''\
	'  <widget rowspan="1" columnspan="1" row="6" column="0" type="label">' \
	'   <name>label_6</name>' \
	'   <tooltip></tooltip>' \
	'   <text>'+label6+'</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	' '+container6+''\
	'  <widget rowspan="1" columnspan="1" row="7" column="0" type="label">' \
	'   <name>label_7</name>' \
	'   <tooltip></tooltip>' \
	'   <text>'+label7+'</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	' '+container7+''\
	'  <widget rowspan="1" columnspan="1" row="8" column="0" type="label">' \
	'   <name>label_8</name>' \
	'   <tooltip></tooltip>' \
	'   <text>'+label8+'</text>' \
	'   <word_wrap>false</word_wrap>' \
	'  </widget>' \
	' '+container8+''\
	' </content>' \
	'</dialog>')
	
	data = []
	if MANUAL_INPUT.input_1:
		data.append(MANUAL_INPUT.input_1)
	if MANUAL_INPUT.input_2:
		data.append(MANUAL_INPUT.input_2)
	if MANUAL_INPUT.input_3:
		data.append(MANUAL_INPUT.input_3)
	if MANUAL_INPUT.input_4:
		data.append(MANUAL_INPUT.input_4)
	if MANUAL_INPUT.input_5:
		data.append(MANUAL_INPUT.input_5)
	if MANUAL_INPUT.input_6:
		data.append(MANUAL_INPUT.input_6)
	if MANUAL_INPUT.input_7:
		data.append(MANUAL_INPUT.input_7)
	if MANUAL_INPUT.input_8:
		data.append(MANUAL_INPUT.input_8)
		
	return data
	
	
	
	
