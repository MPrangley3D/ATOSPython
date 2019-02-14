# -*- coding: utf-8 -*-

"""File Export
Contains Functions:
---exportCSV:
------Exports the .CSV file for WINSPC data collection
---exportPDF:
------Exports the standard PDF report
---exportATOS:
------Stores the ATOS project
"""

import gom

def exportCSV(location,fileTimeStamp):
	'''exportCSV
		Arguments:
		---Location:
		------A sys file location provided as a string
		---fileTimeStamp:
		------A string that details the timestamp used for the filename
	'''	
	csvElements = []
	for i in gom.ElementSelection ({'category': ['key', 'elements', 'explorer_category', 'inspection', 'object_family', 'dimension']}):
		csvElements.append(i)
	for j in gom.ElementSelection ({'category': ['key', 'elements', 'explorer_category', 'inspection', 'object_family', 'gdat']}):
		csvElements.append(j)
	for k in gom.ElementSelection ({'category': ['key', 'elements', 'explorer_category', 'inspection', 'object_family', 'deviation_label', 'type', 'deviation_label_gdat']}):
		csvElements.append(k)	
		
	try:
		gom.script.table.export_table_contents (
			cell_separator=',', 
			codec='iso 8859-1', 
			decimal_separator='.', 
			elements=csvElements, 
			file=(location+'_Data_'+fileTimeStamp+'.csv'), 
			header_export=True, 
			line_feed='\n', 
			sort_column=0, 
			sort_order='ascending', 
			template_name='WIN_SPC_EXPORT', 
			text_quoting='', 
			write_one_line_per_element=False)
	except:
		print('Missing WIN_SPC_EXPORT template')
		
def exportPDF(location,fileTimeStamp):
	'''exportPDF
		Arguments:
		---Location:
		------A sys file location provided as a string
		---fileTimeStamp:
		------A string that details the timestamp used for the filename
	'''	
	try:
		gom.script.report.export_pdf ( 
			export_all_reports = True,
			file = (location+'_Inspection Report_'+fileTimeStamp+'.pdf'),
			jpeg_quality_in_percent = 70,
			reports = gom.app.project.reports )
	except:
		pass
		
def exportATOS(location,fileTimeStamp):
	'''exportATOS
		Arguments:
		---Location:
		------A sys file location provided as a string
		---fileTimeStamp:
		------A string that details the timestamp used for the filename
	'''	
	gom.script.sys.save_project_as( file_name = location+'_Inspection Project_'+fileTimeStamp+'.atos')		
	

