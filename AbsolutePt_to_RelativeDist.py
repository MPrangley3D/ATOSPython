# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------
#         [+] A B S O L U T E   P T   T O   R E L A T I V E   D I S T [+]
#------------------------------------------------------------------------------------------
#        This script converts a point absolute location into a relative distance
#		There is a Point-Direction Distance constructed from the selected point
#		Supports multiple selections
#
# Script by Matt Prangley - 10/10/17
#------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
#                        [+] V E R S I O N   C O N T R O L  [+]
#------------------------------------------------------------------------------------------
#        1.0 (2016) : Initial Release
#		2.0 (10/10/17) : Updated Methods, expanded to work with all name styles, and support multiple selections
#------------------------------------------------------------------------------------------

import gom

#-------------------FILTER----------------------#
#Builds an array of selected elements
myFilter = []
e0 = gom.app.project.inspection
selectedSeries = e0.filter("is_selected", True )
for i in selectedSeries:
	myFilter.append(i.get ('name'))
#-------------------/FILTER----------------------#


#-------------------TYPECHK----------------------#
def typeCHK():
	print(i)	
	myType = gom.app.project.inspection[str(i)].type
	print(myType)
	if myType == 'inspection_dimension_scalar':
		print('I am a Scalar! Yay!')
		myScalar = gom.app.project.inspection[str(i)].scalar_type
		print('My scalar type is: ',myScalar)
	else:
		myScalar = ''
		print('I am not! Boo!')
	return myScalar
#-------------------/TYPECHK---------------------#


#-------------------BUILDER----------------------#
#This builds a nom & actual, and links them.
def Builder(name,type):  
	
	UTL = 1.0
	LTL = 1.0
		
	#Create Nominal Distance
	myDir1 = gom.app.project.inspection[name]
	myName1 = 'Distance ' + name
	myPt1 = gom.app.project.inspection[name]
	myProj1 = {'projection_type': 'surface', 'target': gom.app.project.nominal_elements['all_cad_groups']}
	try:
		MCAD_ELEMENT=gom.script.inspection.create_distance_by_point_direction (direction=myDir1, name=myName1, point=myPt1, project_onto=myProj1)
	except:
		print('Error - Nominal Element already exists')
	
	#Create Actual Distance
	myDir2 = gom.app.project.inspection[name]
	myName2 = 'Distance ' + name
	myPt2 = gom.app.project.inspection[name]   #gom.ActualReference (gom.app.project.inspection[name])
	myProj2 = {'projection_type': 'surface', 'target': gom.app.project.actual_elements['actual_master']}
	try: 
		MCAD_ELEMENT=gom.script.inspection.create_distance_by_point_direction (direction=myDir2, name=myName2, point=myPt2, project_onto=myProj2)
	except:
		print('Error - Actual Element already exists')	
	
	#Link Elements
	myAct = gom.app.project.actual_elements[myName2]
	myEle = [gom.app.project.inspection[myName1]]
	try:
		gom.script.inspection.link_to_actual_element (actual_element=myAct, elements=myEle)
	except:
		print("Can't Link")
	
	if type == 'y':
		print(str(name))
		print('Type is Y')
		UTL = gom.app.project.inspection[name].get ('result_dimension.upper_tolerance_limit')
		LTL = gom.app.project.inspection[name].get ('result_dimension.lower_tolerance_limit')		
		MCAD_ELEMENT=gom.script.inspection.inspect_dimension (distance_restriction='y', elements=[gom.app.project.inspection['Distance ' + name]], nominal_value_source='from_nominal', tolerance={'lower': LTL, 'upper': UTL}, type='distance')
	
	if type == 'x':
		print(str(name))
		print('Type is X')
		UTL = gom.app.project.inspection[name].get ('result_dimension.upper_tolerance_limit')
		LTL = gom.app.project.inspection[name].get ('result_dimension.lower_tolerance_limit')		
		MCAD_ELEMENT=gom.script.inspection.inspect_dimension (distance_restriction='x', elements=[gom.app.project.inspection['Distance ' + name]], nominal_value_source='from_nominal', tolerance={'lower': LTL, 'upper': UTL}, type='distance')
		
	if type == 'z':
		print(str(name))
		print('Type is Z')
		UTL = gom.app.project.inspection[name].get ('result_dimension.upper_tolerance_limit')
		LTL = gom.app.project.inspection[name].get ('result_dimension.lower_tolerance_limit')		
		MCAD_ELEMENT=gom.script.inspection.inspect_dimension (distance_restriction='z', elements=[gom.app.project.inspection['Distance ' + name]], nominal_value_source='from_nominal', tolerance={'lower': LTL, 'upper': UTL}, type='distance')
		
	if type == 'xyz':
		print(str(name))
		print('Type is XYZ')
		UTL = gom.app.project.inspection[name].get ('result_dimension.upper_tolerance_limit')
		LTL = gom.app.project.inspection[name].get ('result_dimension.lower_tolerance_limit')		
		MCAD_ELEMENT=gom.script.inspection.inspect_dimension (distance_restriction='xyz', elements=[gom.app.project.inspection['Distance ' + name]], nominal_value_source='from_nominal', tolerance={'lower': LTL, 'upper': UTL}, type='distance')

	return
#-------------------/BUILDER---------------------#


#--------------------LOOPER----------------------#
# Loops once/item in the Array
# Runs the builder function
for i in myFilter:
	j = typeCHK()
	if j:
		Builder(i,j)
#-------------------/LOOPER----------------------#

gom.script.sys.recalculate_project ()


