# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------
#             [+] M A N U A L   V A L U E   E L E M E N T   B U I L D E R [+]
#------------------------------------------------------------------------------------------
#     This script creates a custom label for reporting hand-measured items
#		like Weight, Pin gage, Caliper, etc.
#           
#   Script by Matt Prangley || Original 04/28/17
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#                        [+] V E R S I O N   C O N T R O L  [+]
#------------------------------------------------------------------------------------------
#        1.0 (04/28/17) : Initial Release
#		2.0 (08/21/08) : Expanded from a pin gage script to manage all things manual imput
#------------------------------------------------------------------------------------------



import gom

CONFIG=gom.script.sys.execute_user_defined_dialog (content='<dialog>' \
' <title>Manual Entry Element Creation</title>' \
' <style></style>' \
' <control id="OkCancel"/>' \
' <position></position>' \
' <embedding></embedding>' \
' <sizemode></sizemode>' \
' <size width="497" height="278"/>' \
' <content rows="6" columns="7">' \
'  <widget columnspan="1" column="0" rowspan="1" row="0" type="label">' \
'   <name>label</name>' \
'   <tooltip></tooltip>' \
'   <text>Feature Name</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget columnspan="6" column="1" rowspan="1" row="0" type="input::string">' \
'   <name>name</name>' \
'   <tooltip></tooltip>' \
'   <value></value>' \
'   <read_only>false</read_only>' \
'  </widget>' \
'  <widget columnspan="1" column="0" rowspan="1" row="1" type="label">' \
'   <name>label_8</name>' \
'   <tooltip></tooltip>' \
'   <text>Tool</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget columnspan="6" column="1" rowspan="1" row="1" type="input::string">' \
'   <name>tool</name>' \
'   <tooltip></tooltip>' \
'   <value></value>' \
'   <read_only>false</read_only>' \
'  </widget>' \
'  <widget columnspan="1" column="0" rowspan="1" row="2" type="label">' \
'   <name>label_1</name>' \
'   <tooltip></tooltip>' \
'   <text>Tolerance</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget columnspan="1" column="1" rowspan="1" row="2" type="label">' \
'   <name>label_2</name>' \
'   <tooltip></tooltip>' \
'   <text>+</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget columnspan="1" column="2" rowspan="1" row="2" type="input::number">' \
'   <name>posTol</name>' \
'   <tooltip></tooltip>' \
'   <value>0</value>' \
'   <minimum>0</minimum>' \
'   <maximum>1000</maximum>' \
'   <precision>2</precision>' \
'   <background_style></background_style>' \
'  </widget>' \
'  <widget columnspan="1" column="3" rowspan="1" row="2" type="label">' \
'   <name>label_5</name>' \
'   <tooltip></tooltip>' \
'   <text>Unequal:</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget columnspan="1" column="4" rowspan="1" row="2" type="input::checkbox">' \
'   <name>checkbox</name>' \
'   <tooltip></tooltip>' \
'   <value>false</value>' \
'   <title>Unequal Tol</title>' \
'  </widget>' \
'  <widget columnspan="1" column="5" rowspan="1" row="2" type="label">' \
'   <name>label_3</name>' \
'   <tooltip></tooltip>' \
'   <text>-</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget columnspan="1" column="6" rowspan="1" row="2" type="input::number">' \
'   <name>negTol</name>' \
'   <tooltip></tooltip>' \
'   <value>0</value>' \
'   <minimum>0</minimum>' \
'   <maximum>1000</maximum>' \
'   <precision>2</precision>' \
'   <background_style></background_style>' \
'  </widget>' \
'  <widget columnspan="1" column="0" rowspan="1" row="3" type="label">' \
'   <name>label_4</name>' \
'   <tooltip></tooltip>' \
'   <text>Nominal</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget columnspan="6" column="1" rowspan="1" row="3" type="input::number">' \
'   <name>nom</name>' \
'   <tooltip></tooltip>' \
'   <value>0</value>' \
'   <minimum>0</minimum>' \
'   <maximum>1000</maximum>' \
'   <precision>2</precision>' \
'   <background_style></background_style>' \
'  </widget>' \
'  <widget columnspan="1" column="0" rowspan="1" row="4" type="label">' \
'   <name>label_6</name>' \
'   <tooltip></tooltip>' \
'   <text>Unit</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget columnspan="6" column="1" rowspan="1" row="4" type="input::list">' \
'   <name>list</name>' \
'   <tooltip></tooltip>' \
'   <items>' \
'    <item>Length (mm)</item>' \
'    <item>Weight (g)</item>' \
'   </items>' \
'   <default>Length (mm)</default>' \
'  </widget>' \
'  <widget columnspan="6" column="0" rowspan="1" row="5" type="label">' \
'   <name>label_7</name>' \
'   <tooltip></tooltip>' \
'   <text>Add Actual Data Now (Uncheck for Templates Creation)</text>' \
'   <word_wrap>false</word_wrap>' \
'  </widget>' \
'  <widget columnspan="1" column="6" rowspan="1" row="5" type="input::checkbox">' \
'   <name>checkbox_1</name>' \
'   <tooltip></tooltip>' \
'   <value>true</value>' \
'   <title>Actual Data Ready</title>' \
'  </widget>' \
' </content>' \
'</dialog>')

name = CONFIG.name
posTol = CONFIG.posTol
negTol = CONFIG.negTol
nominal = CONFIG.nom
unit = CONFIG.list
tool = CONFIG.tool
actualReady = CONFIG.checkbox_1

if unit == 'Length (mm)':
	unit = 'LENGTH'

if unit == 'Weight (g)':
	unit = 'UNIT_NONE'

NOM_MCAD_ELEMENT=gom.script.inspection.create_constant_value_element (description='', name=name, type='float', unit=unit, value=nominal)

ACT_MCAD_ELEMENT=gom.script.inspection.create_value_element (conversion_factor=1, stage_values={}, offset=0, name=name, type='float', unit=unit)

gom.script.inspection.link_to_actual_element (actual_element=ACT_MCAD_ELEMENT, elements=NOM_MCAD_ELEMENT)

MCAD_ELEMENT=gom.script.inspection.inspect_dimension ( 
	elements=[NOM_MCAD_ELEMENT], 
	expression_arguments={'A': gom.ActualReference (ACT_MCAD_ELEMENT)}, 
	nominal_value_source='from_nominal', 
	properties=gom.Binary ('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'), 
	tolerance={'lower': negTol, 'upper': posTol}, 
	type={'abbreviation': tool, 'actual_expression': 'actual.value', 'base_type': 'construct_user_defined', 'geometry': 'scalar', 'inputs': [{'configuration': {}, 'description': 'A', 'name': 'A', 'trait_type': 'gom.ObjectReference'}], 'nominal_expression': nominal, 'reduce_to_scalar': False, 'type_name': tool, 'unit': unit})


if actualReady == True:
	gom.script.sys.edit_creation_parameters (element=ACT_MCAD_ELEMENT)
	

	
