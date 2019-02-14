# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------
#        [+] C R E A T E   P A G E   I N   E V E R Y   S T A G E   R A N G E [+]
#------------------------------------------------------------------------------------------
#        This script is a utility to add stage range views to every selected report page
#		This is useful for revisiting old reports with larger sample sizes, as standard
#		reports don't show more than 8 samples well.
#
# Script by Matt Prangley - 07/10/18
#------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------
#                        [+] V E R S I O N   C O N T R O L  [+]
#------------------------------------------------------------------------------------------
#          1.0 (07/10/18) : Initial Release
#		  1.1 (07/20/18) : Numerous bugs fixed
#			Fixed "last page" error with index array - script now properly copies and positions last pages
#			Fixed error occuring when the Snapshot or Table view is not the primary element on a page
#			Added functionality to support multiple tabes on a single page
#------------------------------------------------------------------------------------------

import gom

#getSelected returns a list containing the currently selected reports, and a list containing all report pages
#This is used to determine which pages to copy, and where to insert them
def getSelected():
	selectedReports = []
	pageList = []
	for currentReport in gom.app.project.reports:
		pageList.append(currentReport)
		if currentReport.pages[0].get ('is_selected'):
			selectedReports.append(currentReport)
	return selectedReports,pageList

#refreshIndex is used after each copy to refresh the pageList list with the newly copied pages
def refreshIndex():	
	pageList = []
	for currentReport in gom.app.project.reports:
		pageList.append(currentReport)
	return pageList

#getRanges returns a list of stageRage gom elements, and a list of their names as strings
#The strings are used for title renaming, the gom elements are used for switching the report page 3d view
def getRanges():
	stageRanges = []
	rangeNameList = []			
	for range in gom.app.project.stage_markers:
		stageRanges.append(range)
		rangeNameList.append(range.name)	
	return(stageRanges,rangeNameList)

#rename takes in 3 arguments: the currently selected page we are copying, the stage range we are showing on the page, and the string list of range names
#Rename then uses the original page name, strips any element it finds that matches the stage range names, and then appends the current stage range name
#There is a bit of redundancy built in here, to allow for a range of potential user renaming oddities (or McCoy-proofing, as we call it)
def rename(currentPage,range,rangeNameList):		
	namePrefix = currentPage.get ('name')
	nameSuffix = range.name
	for name in rangeNameList:
		if name in namePrefix:
			namePrefix = namePrefix.replace(name,"")
	if " - " in namePrefix:
		namePrefix = namePrefix.replace(" - ","")
		
	newName = namePrefix + " - " + nameSuffix
	return newName

#copyPage takes in 5 arguments: The current page, the list of all pages, the indexed value of the current page in that list, the indexed value of the current stage range, and the new page name
#This bit is a clunky due to how GOM handles reports and copying
#The current page is copied then pasted, with the destination being the next page, plus the stage range's index value, which ensures the ranges paste out in order as 1, 2, 3, etc.
#Logic: pageIndex value will point to where the current page exists in the pageList.
#	pageList will be refreshed after copypage runs
#	rangeIndex starts counting at 0 for the first item in stageRanges
#	Therefore the second range adds +1 to the pageIndex, which results in pageList returning the location of the "next page", and so on
#	That newly copied page is assigned to newPage, which is then renamed newName
def copyPage(currentPage,pageList,pageIndex,rangeIndex,newName):
	gom.script.sys.copy_to_clipboard (elements=[currentPage])
	try: 
		newPage = gom.script.sys.paste_from_clipboard (destination=[pageList[pageIndex+rangeIndex]])
	except:
		newPage = gom.script.sys.paste_from_clipboard (append=True, destination=[pageList[pageIndex]])
		
	gom.script.report.edit_report (report=newPage, title=newName)
	return newPage	

#enableRanges takes in the current page as an argument
#This function is called if the page isn't currently a stage range.
#This is necessary because otherwise the "if rangeIndex == 0:" logic returns an error, due to having a null value for the stage range
def enableRanges(currentPage):
	FirstStageRNG = gom.app.project.stage_markers[0]
	gom.script.sys.open_stage_range (element=FirstStageRNG)
	gom.script.report.update_report_page (pages=currentPage, used_alignments='report',used_digits='report',used_legends='report',used_stages='current',used_units='report')

#incrementRanges takes a page and the current range, and refreshes the report page to display this range
def incrementRanges(page,range):
	gom.script.sys.open_stage_range (element=range)

	for e in page.pages[0].elements:	
		if 'table' in e.name:		
			gom.script.report.restore_3d_view_from_report_page (page=[page.pages[0].elements[e.name]])
			gom.script.sys.open_stage_range (element=range)
			gom.script.sys.switch_to_report_workspace ()
			gom.script.report.overwrite_report_page (target=[page.pages[0].elements[e.name]])

if __name__ == '__main__':
	selectedReports,pageList = getSelected()
	stageRanges,rangeNameList = getRanges()	
	for currentPage in selectedReports:
		pageIndex = pageList.index(currentPage)
		for range in stageRanges:
			rangeIndex = stageRanges.index(range)
			if currentPage.current_stage_range == "":
				enableRanges(currentPage)
			if rangeIndex == 0:
				newName = rename(currentPage,range,rangeNameList)
				gom.script.report.edit_report (report=currentPage, title=newName)
				incrementRanges(currentPage,range)
			else:
				newName = rename(currentPage,range,rangeNameList)
				newPage = copyPage(currentPage,pageList,pageIndex,rangeIndex,newName)
				incrementRanges(newPage[0],range)
				pageList = refreshIndex()
