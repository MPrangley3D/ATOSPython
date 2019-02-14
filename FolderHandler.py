# -*- coding: utf-8 -*-

"""Folder Handler
Contains Functions:
---ensureDir - Ensures a directory exists.  Creates one if it's not found
---getFolderLocations - generates the sys file location strings for the 3 output file locations (Project Files, Scan Results, and WInSPCExport)
"""
import gom
import os
import time

def ensureDir(directory,boolSaveSTL):
	'''ensureDir(directory,b)
		Arguments:
		---directory:
		------A sys file location provided as a string
		---b:
		------A string that details the timestamp used for the filename
		
		Returns the sys file path created
	'''	
	initialDirectory = directory+'_#1/'
	if not os.path.exists(initialDirectory):
		os.makedirs(initialDirectory)
		if boolSaveSTL:
			os.makedirs(initialDirectory+'/STLS/')
		return initialDirectory
		
	elif os.path.exists(initialDirectory):
		i = 2
		while True:
			newDirectory = directory+'_#'+str(i)+'/'
			if os.path.exists(newDirectory):
				i += 1
				continue
			elif not os.path.exists(newDirectory):
				os.makedirs(newDirectory)
				if boolSaveSTL:
					os.makedirs(newDirectory+'/STLS/')
				return newDirectory
				break
	
def getFolderLocations(root,time,directory,purpose):
	'''getFolderLocations(root,time,directory,purpose)
		Arguments:
		---Location:
		------A sys file location provided as a string
		---fileTimeStamp:
		------A string that details the timestamp used for the filename
		
		Returns three sys file locations
	'''	
	print(type(root),type(time),type(directory),type(purpose))
	def monthName(m):          
		monthNames = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
		myMonth = monthNames[m-1]
		return myMonth
	year = str(time.tm_year)
	mName = monthName(time.tm_mon)
	if len(str(time.tm_mday)) == 1:
		day = '0'+str(time.tm_mday)
	else:
		day = str(time.tm_mday)
	if len(str(time.tm_mon)) == 1:
		month = '0'+str(time.tm_mon)
	else:
		month = str(time.tm_mon)
	
	suffix = directory[0:2]+'XX-ARCHIVE/'+directory+'/'+year+'_'+month+'_'+mName+'/'+mName+'_'+day+'_'+purpose
	
	print('root',root)
	print('suff',suffix)
	
	loc1 = ensureDir(root+'/Project Files/'+suffix,True)
	loc2 = ensureDir(root+'/Scan Results/'+suffix,False)	
	loc3 = ensureDir(root+'/WinSpc Export/'+suffix,False)
					
	return os.path.join(loc1),os.path.join(loc2),os.path.join(loc3)
