########################################################################
# Script: CustomPatches
#
# PLEASE NOTE that this file is part of the GOM Inspect Professional software
# You are not allowed to distribute this file to a third party without written notice.
#
# Copyright (c) 2017 GOM GmbH
# Author: GOM Software Development Team (CustomPatchGenerator)
# All rights reserved.

# GOM-Script-Version: 2016
#
# ChangeLog:
#2017-SEPT-06: V1 Initial Creation
#2017-NOV-03 : V2 Revised Codeing for most templates to show new fixture 4B being added. Fixture 4B will be held most of the time at Keating.
#2018-APR-13 : V3 Major revision to configuration file storage
#		  	Config info now stores externally in a .CSV file, code should never need to be modified when adding new templates
#		  	Removed Catch-all "overflow template" and replaced with error.  All executions now require mandatory: correct Coded Points and existance of a Template config file
#		  	Added significant comments and searchable debug logs
#		  	Added WINSPC export capabilities
#		  	Refactored code to be less redundant, removed deprecated and commented-out bits of script
#		  	Commonized variable names and reinforced camelCase structure throughout  
#2018-MAY- 31: V4 Some Error/Bugfixing with export naming
#		  	Added Global Variables for Array storage across loops
#2018-NOV-06 : V5 Multi-Export
#		  	Added multiple folder exports
#2018-NOV-30 : V6 Overhaul and Finalization, OOP Improvements
#		  	Major refactoring to comment and clean up code flow
#			  Added DictBuilder - New function to store Config data in a dictionary instance
#			  Added CSV_Reader - New function to parse the CSV and store data in the config Dict
#			  Added FolderHandler - Broke those functions out for organization
#			  Added CubeCalc - Broke cube & polygonize calculations into their own class
#			  Added DialogContainer - Broke the Start Dialog into it's own class to keep the code clean - GOM's dialog script is gigantic and looks like hot garbage
#			  Deprecated all global variables
#			  Added RFID Functionality
#			  Added Manual Input Functionality
#2019-JAN-14 : V7 Fixed several bugs with report exporting
#			  Add more error boxes
#			  Improved the code flow for the export functionality
#			  Broke some complex methods up into simpler containers for ease of reading
#			  Finalized integration testing
#			  Now fully-functional with RFID, Manual entry, and Automatic Weight calls via RS232.  Error coding included.

import gom
import os
import math
import random
import time
import csv
import sys
	#Must append location for ADAC Utils.  
	#Run the ADAC_UTILS/whereAmI script if you are unsure of the proper filepath.
sys.path.append(r'E:/Kiosk_Share/2017/gom_scripts/KioskInterface/ADAC_UTILS')
from ADAC_UTILS import (CSV_Reader,CubeCalc,DialogContainer,DictBuilder,FileExport,
	FolderHandler,ManualDataEntry,RFID,RFID_Call,RFID_Dict,RS232)
from RFID import RFID_System
from DictBuilder import ConfigDict
from CubeCalc import Targets
from Base import Evaluate,Workflow,Dialogs
from Base.Misc import Globals, Utils, PersistentSettings

config = DictBuilder.ConfigDict()

class StartUpV8( Workflow.StartUpV8, metaclass = Utils.MetaClassPatch ):	
	@property	
	def Template_filter( self ):			
		return RFID_Call.Scan()
	
	def set_additional_project_keywords ( self ):
		Globals.ADDITIONAL_PROJECTKEYWORDS = [('press', 'Press #', 'input_press', False),
												('shift', 'Shift #', 'input_shift', False),
												('purpose', 'Purpose', 'input_purpose', False),
												('loc', 'Mold Loc', 'input_moldloc', False)]

	def open_template( self, startup = False ):
		'''
		create a project from template
		if startup is given directly opens last used template
		'''
		if not startup:
			# if the filter is unique (only one template would match)
			# directly open the project template
			unique_template = self.is_template_filter_unique()
			if unique_template is not None and unique_template == Globals.SETTINGS.CurrentTemplate:
				self.log.debug( 'already open' )
				self._after_template_opened( opened_template = {'template_name':unique_template} )
				return
			elif unique_template is not None:
				gom.script.sys.close_project ()
				template = gom.script.sys.create_project_from_template ( 
					config_level = Globals.SETTINGS.TemplateConfigLevel,
					template_name = unique_template )
				self.log.debug( 'opened automatically {}'.format( unique_template ) )
				template['template_name'] = unique_template
				self._after_template_opened( template )
				return
			elif Globals.SETTINGS.Inline:
				opened_template = {'template_name':None}
				self._after_template_opened( opened_template )
				return

		gom.script.sys.close_project ()
		opened_template = {'template_name':None}
		try:
			# called directly after dialog show
			if startup:
				template = gom.script.sys.create_project_from_template ( 
					config_level = Globals.SETTINGS.TemplateConfigLevel,
					template_name = Globals.SETTINGS.CurrentTemplate )
				opened_template['template_name'] = Globals.SETTINGS.CurrentTemplate
			# show the template dialog
			elif Globals.SETTINGS.ShowTemplateDialog:
				filter = self.Template_filter  # first get the filter before deactivating the dialog
				self.dialog.enabled = False
				opened_template = gom.interactive.sys.create_project_from_template ( 
					config_levels = [Globals.SETTINGS.TemplateConfigLevel],
					template_name = Globals.SETTINGS.TemplateName,
					filters = filter )
			# dont show the template dialog
			else:
				template = gom.script.sys.create_project_from_template ( 
					config_level = Globals.SETTINGS.TemplateConfigLevel,
					template_name = Globals.SETTINGS.TemplateName )
				opened_template['template_name'] = Globals.SETTINGS.TemplateName
		except Globals.EXIT_EXCEPTIONS:
			raise
		except Exception as error:
			self.log.exception( str( error ) )
		finally:
			self.dialog.enabled = True

		self._after_template_opened( opened_template )
		self.log.info( 'opened template "{}"'.format( Globals.SETTINGS.CurrentTemplate ) )
		
		
class PatchedDialogs(Dialogs.Dialogs, metaclass = Utils.MetaClassPatch):
	STARTDIALOG_FIXTURE=DialogContainer.PopDialog()
	
class PatchedPersistentSettings( PersistentSettings.PersistentSettings, metaclass = Utils.MetaClassPatch ):
	def __init__( self, savepath ):
		self.CFG_NAME = os.path.join( savepath+'/Kiosk_Share/', 'KioskInterface_persistantsettings.cfg' )
		print(self.CFG_NAME)
		self.read_settings()

class PatchedEvaluationAnalysis( Evaluate.EvaluationAnalysis, metaclass = Utils.MetaClassPatch ):
	
	def polygonize(self):	
		global config
		gom.script.cad.show_element_exclusively (elements=gom.ElementSelection ({'category': ['key', 'elements', 'explorer_category', 'actual', 'object_family', 'measurement_series']}))
		gom.script.selection3d.deselect_all ()

																				#THE SCANBOX VMR TEMPLATE NAME MUST FOLLOW THE [XXXX-XXXX.XXX_XXX]... FORMAT WHERE THE XXXX SPACES CONTAIN THE 11-DIGIT PART # AND 3 DIGIT FIXTURE ID
																				#THIS IS A LIST, SO EXACT SPACING IS CRITICAL.  ELEMENTS 1-17 ARE KEY.  ELEMENT 0 SHOULD BE A '['.  THE REST IS IRRELEVANT.
		myPart = str(gom.app.project.get('template.relative_path')[0][1:14])    #Pulls part number from template name	
		myFixt = str(gom.app.project.get('template.relative_path')[0][15:18])   #Pulls fixture ID from template name	
		root = Globals.SETTINGS.SavePath 							 		  #SavePath is defined in the Kiosk Configuration Settings.  KioskShare > Year > KioskInterfaceSettings.CFG File, First line should be Drive Letter without slash EG  'E:' 	
		setupFolder = 'Kiosk_Share' 								 	  	 #Defined in ATOS as the Shared Folder in settings menu	
		configLoc = root+'/'+setupFolder+'/'+'template_config.csv'   	   	#The location for our Config CSV, intentionally explicit location.
				
		config = CSV_Reader.ReadCSV(configLoc,myPart,myFixt,config)
		config.add([('purpose',gom.app.project.get ('user_purpose'))])
		config.add([('press',gom.app.project.get ('user_press'))])
		config.add([('shift',gom.app.project.get ('user_shift'))])
		config.add([('moldLoc',gom.app.project.get ('user_loc'))])
		config.add([('inspector',gom.app.project.get ('user_inspector'))])
		config.add([('myTime',time.localtime(time.time()))])
		
		exportPathProject,exportPathReport,exportPathSPC = FolderHandler.getFolderLocations(root,config.read('myTime')[0],config.read('directory')[0],config.read('purpose')[0])
		config.add([('export_path_project',exportPathProject)])
		config.add([('export_path_report',exportPathReport)])
		config.add([('export_path_spc',exportPathSPC)])

		codedPointsDict = CubeCalc.buildPointDict()	
		codedPointsVisible = set()
		expectedCodedPoints = set()		
		for point in codedPointsDict:
			codedPointsVisible.add(str(point))	
		for point in config.read('fixturePoints'):
			expectedCodedPoints.add(str(point))
			
		#This ensures the inspection will only proceed if all the expected coded points are visible in the scanned data.	
		if (expectedCodedPoints <= codedPointsVisible):
			#Determine the total # of parts by summing the # of each type
			totalParts = 0
			for samplePerType in config.read('numParts'):
				totalParts = totalParts+int(samplePerType)
				
			currentSample = 0
			while currentSample < totalParts: 
				codedPointsDict = CubeCalc.buildPointDict()

				fixturePoints = config.read('fixturePoints')
				xOffset = config.read('xOffset')
				yOffset = config.read('yOffset')
				zOffset = config.read('zOffset')	
				lengthCompensation = config.read('lComp')[0]
				widthCompensation = config.read('wComp')[0]
				heightCompensation = config.read('hComp')[0]

				midpoint, length, width, height = CubeCalc.CubeGeometryCalc(codedPointsDict,fixturePoints,xOffset,yOffset,zOffset,lengthCompensation,widthCompensation,heightCompensation,currentSample)
				CubeCalc.SelectCube(midpoint, length, width, height,currentSample,config.read('zRotArray'))
				
				print("=============================================================")
				print('Working on Station: ',currentSample+1)
				print('MP:',midpoint)
				print('L/X:',length)
				print('W/Y:',width)
				print('H/Z:',height)
				print('Rotation:',config.read('zRotArray'))
				print("=============================================================")
								
				newMesh = CubeCalc.Poly()
				rename = 'CAV '+str(currentSample+1)
				gom.script.sys.edit_properties (data=[gom.app.project.actual_elements[newMesh]],elem_name=rename)						
				gom.script.selection3d.deselect_all ()
				gom.script.cad.show_element_exclusively (elements=gom.ElementSelection ({'category': ['key', 'elements', 'explorer_category', 'actual', 'object_family', 'measurement_series']}))	
				if gom.app.project.actual_elements[rename].area < config.read('meshArea')[0]:
					gom.script.cad.delete_element (elements=[gom.app.project.actual_elements[rename]])
				currentSample+=1
				
			gom.script.cad.show_element_exclusively (elements=gom.ElementSelection ({'category': ['key', 'elements', 'explorer_category', 'actual', 'object_family', 'mesh']}))
			
			stlArray = []
			Meshes = []
			currentMesh = 0
			allMeshes = gom.ElementSelection ({'category': ['key', 'elements', 'explorer_category', 'actual', 'object_family', 'mesh']})
			
			for mesh in allMeshes:				
				gom.script.sys.export_stl (
					bgr_coding=False, 
					binary=True, 
					color=False, 
					elements=[mesh], 
					export_in_one_file=True,  
					file=(config.read('export_path_project')[0]+'STLS/'+mesh.name+'.stl'), 
					length_unit='default', 
					set_stl_color_bit=True)
				
				myFile = (config.read('export_path_project')[0]+'STLS/'+mesh.name+'.stl')
				stlArray.append(myFile)
				Meshes.append(currentMesh)
				currentMesh+=1
			
			config.add([('MeshNameArray',Meshes)])
			
			file_name = os.path.basename( gom.app.project.get( 'project_file' ))
			for stl in stlArray:
				config.add([('stlArray',stl)])
			print('STL Array Debugging: ',stlArray)
			print('STL Array Debugging: ',config.read('stlArray'))								
		else:
			missing = expectedCodedPoints - codedPointsVisible	
			print('$$$ --DEBUG-- Missing coded Points:',missing)		
			ERROR=DialogContainer.PopErrorDialog(missing)
																						
	@staticmethod
	def export_results( result ):
		global config
		
		fileTimeStamp = str(config.read('myTime')[0][1])+'_'+str(config.read('myTime')[0][2])+'_'+str(config.read('myTime')[0][0])+'_'+str(config.read('myTime')[0][3])+'_'+str(config.read('myTime')[0][4])	
		index = config.read('globalIndex')[0]
		
		if result == True:
			approval = "Evaluation Approved"	
		elif result == False:
			approval = "Evaluation Rejected"	
		gom.script.sys.set_project_keywords (keywords={'approval':approval},keywords_description={'approval': 'Approval'})
		
		saveName = config.read('saveName')[index]
		projectPath = config.read('export_path_project')[0]
		print('debug - project and save name: ',projectPath,' && ',saveName)		
		FileExport.exportCSV(projectPath+saveName,fileTimeStamp)
		FileExport.exportPDF(projectPath+saveName,fileTimeStamp)
		FileExport.exportATOS(projectPath+saveName,fileTimeStamp)
		
		reportPath = config.read('export_path_report')[0]
		print(reportPath+saveName)
		FileExport.exportCSV(reportPath+saveName,fileTimeStamp)
		FileExport.exportPDF(reportPath+saveName,fileTimeStamp)
		
		csvPath = config.read('export_path_spc')[0]
		print(csvPath+saveName)
		FileExport.exportCSV(csvPath+saveName,fileTimeStamp)
		
		config.get().pop('globalIndex')
					
class PatchedWorkflow( Workflow.WorkFlow, metaclass = Utils.MetaClassPatch ):

	def after_successful_evaluation( self ):
		global config
		#=================================Cleanup=================================
		tempfile = gom.app.project.get( 'project_file' )
		gom.script.sys.close_project()
		if ( os.path.exists( os.path.join( Globals.SETTINGS.SavePath, os.path.basename( tempfile ) ) ) ):
			os.unlink( os.path.join( Globals.SETTINGS.SavePath, os.path.basename( tempfile) ) )		
		#=================================Cleanup=================================	
	
		def inspectionSetup(file,myIndx):
			global config
			gom.script.sys.load_project (file=file)						
			
			#Container Variables to pull config data and keep the set_project_keywords method cleaner
			_print = config.read('key_Print')[myIndx]
			version = 'ATOS Professional '+str(gom.app.application_build_information.version)
			matl = config.read('key_Material')[myIndx]
			date = gom.Date(config.read('myTime')[0].tm_mday, config.read('myTime')[0].tm_mon, config.read('myTime')[0].tm_year) 
			part_nr = config.read('partNR')[myIndx]
			inspector = config.read('inspector')
			timestamp = time.strftime('%I:%M:%S',config.read('myTime')[0])
			press = config.read('press')
			shift = config.read('shift')
			purpose = config.read('purpose')
			system = config.read('key_System')
			part = config.read('key_PartName')[myIndx]
			loc = config.read('moldLoc')
			
			#Set keywords
			try:			
				gom.script.sys.set_project_keywords (
					keywords={'print': _print, 'version': version, 'matl': matl, 'date': date, 'part_nr': part_nr, 
						'inspector': inspector, 'timestamp': timestamp, 'press': press, 'shift': shift, 
						'purpose': purpose ,'system': system ,'part': part, 'loc': loc
					}, 
					keywords_description={'print':'Print','version':'Version','matl':'Material','date': 'Date', 
						'part_nr': 'Part no.','inspector': 'Inspector','timestamp': 'Time Stamp', 'press':'Press #',
						'shift':'Shift #', 'purpose':'Purpose:', 'system':'System','part':'Part','loc':'Mold Location'
					})
				print('Keywords updated properly! Yay! :D')
			except:
				print('Keywords not set, deal with it.')
			try:
				firstStage = gom.app.project.stages[0]
				lastStage = gom.app.project.stages[len(gom.app.project.stages)-1]
				gom.script.sys.delete_stage (stages=gom.StageSelection (first=firstStage, last=lastStage))
			except:
				print('No Stages to Delete!')	
		
		def loadMeshes(file,myIndx):
			#Build list of STL file paths for the given set of cavities
			myImports = []
			stlArray = config.read('stlArray')
			meshIDs = config.read('nestID')[myIndx]
			for cavity in meshIDs:
				try:
					myImports.append(stlArray[cavity-1])
				except:
					print('EXPECTED STL MISSING!')
			
			#Import all meshes
			for stl in myImports: 
				gom.script.sys.import_stl (
					bgr_coding=True, 
					files=[stl], 
					import_mode='new_stage', 
					length_unit='mm', 
					stl_color_bit_set=False, 
					target_type='mesh')

			gom.script.sys.switch_to_report_workspace ()
			
		def manualCheck(currentNests,manualChecks,checkTypes):
			#Builds an array of data for the manual checks
			#This is deiven by the number of checks specified in the config CSV
			#This expects the inspection template to have the correct containers for data prepared and named properly
			
			tempList = []
			for check,type in zip(manualChecks,checkTypes):
				index = manualChecks.index(check)
				if type == 'var' or type == 'bool':
					expected = len(currentNests)
					recieved = 0
					while recieved < expected:
						dialogText = config.read('manualDialogTextArray')[index]
						data = ManualDataEntry.dataEntry(currentNests,check,dialogText,type)
						recieved = len(data)
						if recieved < expected:
							DialogContainer.PopNullVariable()
					tempList.append(data)
						
				elif type == 'weight':
					weights = []
					for sample in currentNests:
						sampleWeight = None
						while sampleWeight == None:
							SCALEDIALOG = DialogContainer.PopWeightDialog(sample)
							sampleWeight = RS232.parseByte()
						weights.append(sampleWeight)
					tempList.append(weights)						
				else:
					DialogContainer.PopGenericError()
					
			return tempList

		def updateValues(manualChecks,actualValues,currentNests):
			#This parses the actual data matrix creaed by manualCheck() and then applies it to the inspection features
			
			for dimension in manualChecks:
				index = manualChecks.index(dimension)
				tempDict={}
				for sample in currentNests:
					sampleIndex = currentNests.index(sample)
					try:
						tempDict.update({'CAV '+str(sample):actualValues[index][sampleIndex]})
					except:
						print('Missing Expected Data')
				gom.script.sys.edit_creation_parameters (auto_apply=True, element=gom.app.project.actual_elements[dimension],stage_values=tempDict)
		
		def buildSaveName():
			#Builds a list of the save names per set of samples.
			
			for name in config.read('winSPCname'):
				saveName = name[0:9]
				config.add([('saveName',name[0:9])])	
			return saveName
		
		for template in config.read('inspectionTemplate'):
			#Loads the Inspection Templates, performs the manual entry, and triggers the export of the reports
			
			templateIndex = config.read('inspectionTemplate').index(template)
			config.add([('globalIndex',templateIndex)])
			
			buildSaveName()
			inspectionSetup(template,templateIndex)
			loadMeshes(template,templateIndex)
			
			#Pull config info the manual checks require
			currentNests = config.read('nestID')[templateIndex]
			manualChecks = config.read('manualDialogTitleArray')
			checkTypes = config.read('manualDialogTypeArray')
			
			#Runs the manual data input and weight components, if necessary
			if not len(manualChecks[0]) < 1:
				actualValues = manualCheck(currentNests,manualChecks,checkTypes)
				updateValues(manualChecks,actualValues,currentNests)
			gom.script.sys.recalculate_project ()	
			
			self.confirm.execute()		
			



