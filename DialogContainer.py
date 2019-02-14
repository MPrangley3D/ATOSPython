# -*- coding: utf-8 -*-

"""Dialog Container
This is just separating the dialogs out into their own class to save space and make the main code more readable
Because ATOS dialogs are 200-some lines of garbage

Contains Functions:
---PopDialog - Popup for initial startup dialog
---PopErrorDialog - Popup for missing coded points dialog
"""

import gom

def PopDialog():
	STARTDIALOG_FIXTURE=gom.script.sys.create_user_defined_dialog (content='<dialog>' \
		' <title>Start Dialog</title>' \
		' <style>Touch</style>' \
		' <control id="Empty"/>' \
		' <position>left</position>' \
		' <embedding>embedded_in_kiosk</embedding>' \
		' <sizemode>automatic</sizemode>' \
		' <size width="430" height="527"/>' \
		' <content rows="15" columns="10">' \
		'  <widget rowspan="1" type="spacer::horizontal" row="0" column="0" columnspan="10">' \
		'   <name>spacer_width</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>386</minimum_size>' \
		'   <maximum_size>-1</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="1" column="0" columnspan="10">' \
		'   <name>spacer_1</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>30</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="image" row="2" column="0" columnspan="10">' \
		'   <name>image</name>' \
		'   <tooltip></tooltip>' \
		'   <use_system_image>false</use_system_image>' \
		'   <system_image>system_message_warning</system_image>' \
		'   <data><![CDATA[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]]></data>' \
		'   <file_name></file_name>' \
		'   <keep_original_size>true</keep_original_size>' \
		'   <keep_aspect>true</keep_aspect>' \
		'   <width>150</width>' \
		'   <height>90</height>' \
		'  </widget>' \
		'  <widget rowspan="1" type="label" row="3" column="0" columnspan="10">' \
		'   <name>label_title</name>' \
		'   <tooltip></tooltip>' \
		'   <text>Choose the purpose</text>' \
		'   <word_wrap>true</word_wrap>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="4" column="0" columnspan="1">' \
		'   <name>spacer_11</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>60</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="4" column="1" columnspan="1">' \
		'   <name>spacer_12</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>60</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="4" column="2" columnspan="1">' \
		'   <name>spacer_13</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>60</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="4" column="3" columnspan="1">' \
		'   <name>spacer_14</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>60</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="4" column="4" columnspan="1">' \
		'   <name>spacer_15</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>60</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="4" column="5" columnspan="1">' \
		'   <name>spacer_16</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>60</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="4" column="6" columnspan="1">' \
		'   <name>spacer_17</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>60</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="4" column="7" columnspan="1">' \
		'   <name>spacer_18</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>60</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="4" column="8" columnspan="1">' \
		'   <name>spacer_19</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>60</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="4" column="9" columnspan="1">' \
		'   <name>spacer_20</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>60</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="label" row="5" column="0" columnspan="2">' \
		'   <name>label_user</name>' \
		'   <tooltip></tooltip>' \
		'   <text>User:</text>' \
		'   <word_wrap>false</word_wrap>' \
		'  </widget>' \
		'  <widget rowspan="1" type="input::list" row="5" column="2" columnspan="8">' \
		'   <name>userlist</name>' \
		'   <tooltip></tooltip>' \
		'   <items>' \
		'    <item>John</item>' \
		'    <item>Jane</item>' \
		'    <item>Max</item>' \
		'   </items>' \
		'   <default>John</default>' \
		'  </widget>' \
		'  <widget rowspan="1" type="label" row="6" column="0" columnspan="2">' \
		'   <name>label_fixture</name>' \
		'   <tooltip></tooltip>' \
		'   <text>Fixture:</text>' \
		'   <word_wrap>false</word_wrap>' \
		'  </widget>' \
		'  <widget rowspan="1" type="input::string" row="6" column="2" columnspan="8">' \
		'   <name>inputFixture</name>' \
		'   <tooltip></tooltip>' \
		'   <value></value>' \
		'   <read_only>false</read_only>' \
		'  </widget>' \
		'  <widget rowspan="1" type="label" row="7" column="0" columnspan="2">' \
		'   <name>label_purpose</name>' \
		'   <tooltip></tooltip>' \
		'   <text>Purpose:</text>' \
		'   <word_wrap>false</word_wrap>' \
		'  </widget>' \
		'  <widget rowspan="1" type="input::list" row="7" column="2" columnspan="8">' \
		'   <name>input_purpose</name>' \
		'   <tooltip></tooltip>' \
		'   <items>' \
		'    <item>Production</item>' \
		'    <item>Training</item>' \
		'    <item>QC_Check</item>' \
		'    <item>Other</item>' \
		'   </items>' \
		'   <default>Production</default>' \
		'  </widget>' \
		'  <widget rowspan="1" type="label" row="8" column="0" columnspan="2">' \
		'   <name>label_template</name>' \
		'   <tooltip></tooltip>' \
		'   <text>Template:</text>' \
		'   <word_wrap>false</word_wrap>' \
		'  </widget>' \
		'  <widget rowspan="1" type="button::pushbutton" row="8" column="2" columnspan="8">' \
		'   <name>buttonTemplateChoose</name>' \
		'   <tooltip></tooltip>' \
		'   <text>Choose</text>' \
		'   <type>push</type>' \
		'   <icon_type>none</icon_type>' \
		'   <icon_size>icon</icon_size>' \
		'   <icon_system_type>ok</icon_system_type>' \
		'   <icon_system_size>default</icon_system_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="label" row="9" column="0" columnspan="2">' \
		'   <name>label_keyword_press</name>' \
		'   <tooltip></tooltip>' \
		'   <text>Press #:</text>' \
		'   <word_wrap>false</word_wrap>' \
		'  </widget>' \
		'  <widget rowspan="1" type="input::string" row="9" column="2" columnspan="8">' \
		'   <name>input_press</name>' \
		'   <tooltip></tooltip>' \
		'   <value></value>' \
		'   <read_only>false</read_only>' \
		'  </widget>' \
		'  <widget rowspan="1" type="label" row="10" column="0" columnspan="2">' \
		'   <name>label_keyword_Shift</name>' \
		'   <tooltip></tooltip>' \
		'   <text>Shift #:</text>' \
		'   <word_wrap>false</word_wrap>' \
		'  </widget>' \
		'  <widget rowspan="1" type="input::string" row="10" column="2" columnspan="8">' \
		'   <name>input_shift</name>' \
		'   <tooltip></tooltip>' \
		'   <value></value>' \
		'   <read_only>false</read_only>' \
		'  </widget>' \
		'  <widget rowspan="1" type="label" row="11" column="0" columnspan="2">' \
		'   <name>label</name>' \
		'   <tooltip></tooltip>' \
		'   <text>Mold Location</text>' \
		'   <word_wrap>false</word_wrap>' \
		'  </widget>' \
		'  <widget rowspan="1" type="input::list" row="11" column="2" columnspan="8">' \
		'   <name>input_moldloc</name>' \
		'   <tooltip></tooltip>' \
		'   <items>' \
		'    <item>Keating</item>' \
		'    <item>Port City</item>' \
		'    <item>36th Street</item>' \
		'   </items>' \
		'   <default>Keating</default>' \
		'  </widget>' \
		'  <widget rowspan="1" type="spacer::vertical" row="12" column="0" columnspan="10">' \
		'   <name>spacer</name>' \
		'   <tooltip></tooltip>' \
		'   <minimum_size>0</minimum_size>' \
		'   <maximum_size>-1</maximum_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="button::pushbutton" row="13" column="0" columnspan="10">' \
		'   <name>buttonNext</name>' \
		'   <tooltip></tooltip>' \
		'   <text>Start</text>' \
		'   <type>push</type>' \
		'   <icon_type>system</icon_type>' \
		'   <icon_size>icon</icon_size>' \
		'   <icon_system_type>ok</icon_system_type>' \
		'   <icon_system_size>default</icon_system_size>' \
		'  </widget>' \
		'  <widget rowspan="1" type="button::pushbutton" row="14" column="0" columnspan="10">' \
		'   <name>buttonExit</name>' \
		'   <tooltip></tooltip>' \
		'   <text>Exit</text>' \
		'   <type>push</type>' \
		'   <icon_type>system</icon_type>' \
		'   <icon_size>icon</icon_size>' \
		'   <icon_system_type>cancel</icon_system_type>' \
		'   <icon_system_size>default</icon_system_size>' \
		'  </widget>' \
		' </content>' \
		'</dialog>')
	return STARTDIALOG_FIXTURE

def PopErrorDialog(missing):
	ERROR=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
		' <title>CODED POINTS MISSING ERROR</title>' \
		' <style></style>' \
		' <control id="OkCancel"/>' \
		' <position></position>' \
		' <embedding></embedding>' \
		' <sizemode></sizemode>' \
		' <size height="282" width="308"/>' \
		' <content columns="1" rows="1">' \
		'  <widget column="0" columnspan="1" row="0" rowspan="1" type="display::text">' \
		'   <name>text</name>' \
		'   <tooltip></tooltip>' \
		'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
		'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
		'p, li { white-space: pre-wrap; }' \
		'&lt;/style>&lt;/head>&lt;body style="    ">' \
		'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">One or More Required Coded Point is Missing!&lt;/p>' \
		'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Verify Fixture is Correct for Template&lt;/li>' \
		'&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Attempt Running Inspection Again&lt;/li>' \
		'&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Visually Inspect Coded Points&lt;/li>' \
		'&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Contact ADAC Metrology if Issue Persists&lt;/li>&lt;/ul>' \
		'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Missing Points:&lt;/p>' \
		'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'+str(missing)+'\t&lt;/p>' \
		'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>&lt;/body>&lt;/html></text>' \
		'   <wordwrap>false</wordwrap>' \
		'  </widget>' \
		' </content>' \
		'</dialog>')
	return ERROR
	
def PopWeightDialog(sample):
	SCALEDIALOG=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
		' <title>SCALE INSTRUCTIONS</title>' \
		' <style></style>' \
		' <control id="OkCancel"/>' \
		' <position>automatic</position>' \
		' <embedding>always_toplevel</embedding>' \
		' <sizemode>automatic</sizemode>' \
		' <size height="263" width="456"/>' \
		' <content columns="1" rows="1">' \
		'  <widget row="0" columnspan="1" column="0" type="display::text" rowspan="1">' \
		'   <name>text</name>' \
		'   <tooltip></tooltip>' \
		'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
		'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
		'p, li { white-space: pre-wrap; }' \
		'&lt;/style>&lt;/head>&lt;body style="    ">' \
		'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:11pt; font-weight:600; text-decoration: underline;">SCALE INSTRUCTIONS:&lt;/span>&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; text-decoration: underline;">&lt;br />&lt;/p>' \
		'&lt;ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">&lt;li style=" font-weight:600; text-decoration: underline;" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-weight:400; text-decoration:none;">Place the sample onto the scale&lt;/span>&lt;/li>' \
		'&lt;ul style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">&lt;li style=" font-weight:600; text-decoration: underline;" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-weight:400; text-decoration:none;">Ensure Scale is stable&lt;/span>&lt;/li>&lt;/ul>' \
		'&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Press the OK button to close this dialog and continue&lt;/li>' \
		'&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Press the &amp;quot;Print&amp;quot; Button on the Scale&lt;/li>' \
		'&lt;li style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">This will repeat for every sample&lt;/li>&lt;/ul>' \
		'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:12pt; font-weight:600;">PLACE CAVITY '+str(sample)+' SAMPLE ONTO SCALE AND PROCEED&lt;/span>&lt;/p>' \
		'&lt;p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;">&lt;br />&lt;/p>&lt;/body>&lt;/html></text>' \
		'   <wordwrap>false</wordwrap>' \
		'  </widget>' \
		' </content>' \
		'</dialog>')
	return SCALEDIALOG
	
def PopScaleError():
	SCALE_ERROR=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
		' <title>ERROR!</title>' \
		' <style></style>' \
		' <control id="OkCancel"/>' \
		' <position></position>' \
		' <embedding></embedding>' \
		' <sizemode></sizemode>' \
		' <size height="222" width="350"/>' \
		' <content columns="1" rows="1">' \
		'  <widget row="0" columnspan="1" column="0" type="display::text" rowspan="1">' \
		'   <name>text</name>' \
		'   <tooltip></tooltip>' \
		'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
		'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
		'p, li { white-space: pre-wrap; }' \
		'&lt;/style>&lt;/head>&lt;body style="    ">' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-weight:600; text-decoration: underline;">ERROR - NO RESPONSE FROM SCALE&lt;/span>&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Press &amp;quot;OK&amp;quot; to return to the previous dialog and try again.&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Review the instructions.&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">If the issue persists, contact ADAC Metrology&lt;/p>&lt;/body>&lt;/html></text>' \
		'   <wordwrap>false</wordwrap>' \
		'  </widget>' \
		' </content>' \
		'</dialog>')
	return SCALE_ERROR		
		
def PopNoSample():
	SCALE_ERROR=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
		' <title>ERROR!</title>' \
		' <style></style>' \
		' <control id="OkCancel"/>' \
		' <position></position>' \
		' <embedding></embedding>' \
		' <sizemode></sizemode>' \
		' <size height="299" width="350"/>' \
		' <content columns="1" rows="1">' \
		'  <widget row="0" columnspan="1" column="0" type="display::text" rowspan="1">' \
		'   <name>text</name>' \
		'   <tooltip></tooltip>' \
		'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
		'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
		'p, li { white-space: pre-wrap; }' \
		'&lt;/style>&lt;/head>&lt;body style="    ">' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-weight:600; text-decoration: underline;">ERROR - NO SAMPLE ON SCALE&lt;/span>&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Signal is present but weight is below set limits&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Verify scale is zeroed correctly before proceeding.&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-size:10pt; font-weight:600; text-decoration: underline;">TO ZERO:&lt;/span>&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Remove all items from scale.&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Allow scale value to stabilize.&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Press the orange &amp;quot;RE-ZERO&amp;quot; button&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Press &amp;quot;OK&amp;quot; to return to the previous dialog and try again.&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Review the instructions on the page.&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">If the issue persists, contact ADAC Metrology&lt;/p>&lt;/body>&lt;/html></text>' \
		'   <wordwrap>false</wordwrap>' \
		'  </widget>' \
		' </content>' \
		'</dialog>')
	return SCALE_ERROR	
			
def PopGenericError():
	GENERIC_ERROR=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
		' <title>ERROR!</title>' \
		' <style></style>' \
		' <control id="OkCancel"/>' \
		' <position></position>' \
		' <embedding></embedding>' \
		' <sizemode></sizemode>' \
		' <size height="207" width="363"/>' \
		' <content columns="1" rows="1">' \
		'  <widget row="0" columnspan="1" column="0" type="display::text" rowspan="1">' \
		'   <name>text</name>' \
		'   <tooltip></tooltip>' \
		'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
		'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
		'p, li { white-space: pre-wrap; }' \
		'&lt;/style>&lt;/head>&lt;body style="    ">' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-weight:600; text-decoration: underline;">ERROR - RESTART EVALUATION&lt;/span>&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Press &amp;quot;OK&amp;quot; to return to cancel this inspection and try again.&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">If the issue persists, contact ADAC Metrology.&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Reference Error Code:  01&lt;/p>&lt;/body>&lt;/html></text>' \
		'   <wordwrap>false</wordwrap>' \
		'  </widget>' \
		' </content>' \
		'</dialog>')
	return GENERIC_ERROR		
	
def PopNullVariable():
	NULL_VAR=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
		' <title>ERROR!</title>' \
		' <style></style>' \
		' <control id="OkCancel"/>' \
		' <position></position>' \
		' <embedding></embedding>' \
		' <sizemode></sizemode>' \
		' <size height="207" width="369"/>' \
		' <content columns="1" rows="1">' \
		'  <widget row="0" columnspan="1" column="0" type="display::text" rowspan="1">' \
		'   <name>text</name>' \
		'   <tooltip></tooltip>' \
		'   <text>&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">' \
		'&lt;html>&lt;head>&lt;meta name="qrichtext" content="1" />&lt;style type="text/css">' \
		'p, li { white-space: pre-wrap; }' \
		'&lt;/style>&lt;/head>&lt;body style="    ">' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;span style=" font-weight:600; text-decoration: underline;">ERROR - Variable Value Left Empty&lt;/span>&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">It looks like you forgot to enter an expected measured value.&lt;/p>' \
		'&lt;p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">&lt;br />&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Press &amp;quot;OK&amp;quot; to return to the previous dialog and try again.&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Review the instructions on the page.&lt;/p>' \
		'&lt;p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">If the issue persists, contact ADAC Metrology&lt;/p>&lt;/body>&lt;/html></text>' \
		'   <wordwrap>false</wordwrap>' \
		'  </widget>' \
		' </content>' \
		'</dialog>')
	return NULL_VAR		
	
	
	
	
	
	
	
	
	
