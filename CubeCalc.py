# -*- coding: utf-8 -*-

"""CubeCalc
Contains Classes:
---Targets
---   This class returns a dictionary of points 
Contains Functions:
---buildPointDict()
---	Leverages the targets class to produce and return a dictionary of coded points
---CubeGeometryCalc(codedPointsDict,fixturePoints,xOffset,yOffset,zOffset,lComp,wComp,hComp,j)
---	Using the data from the coded points, calculates a 3d cube to be used for selection and polygonization
---SelectCube(Midpoint,Length,Width,Height,j)
---	performs the cube selection based on the inputs
---Poly()
---	This calls the GOM polygonize function and returns the resultant element
"""

import gom
import math

	
class Targets():
	'''Targets Class
	This class parses the reference points in a project and contains a dictionary of them
	This instance is referenced by  to ID and pul that data for all the coded points
	'''	
	
	def __init__( self ):
		
		self.ScanList = []
		self.TargetDict = dict()
		self.CodedPoints = []
		
		# Create a few dictionaries for flexibility
		self.ScanOne = dict()
		self.ScanTwo = dict()
		self.ScanThree = dict()
		
		if not self.get_reference_points():
			print('Failed to get reference points.')

		if not self.parse_reference_points():
			print('Failed to get reference points.')
	
	def __str__( self ):
		
		String = ''
		
		String += 'Number of MS: {0}\n'.format( len(self.ScanList) )
		
		return String
	
	def get_reference_points( self ):
		''' Loop through each measurement series, then
			get the reference points with the ['results'] key.
		'''	
		
		try:
			for ms in gom.app.project.measurement_series:

				Name = ms.get('name')
				self.ScanList.append( ms )
				self.TargetDict[Name] = {'name'  : Name,
										'points': ms.results['points'],
										'total' : ms.results['points'].get('num_points') }

		except Exception as Err:
			print('get reference points error:', Err)
			return False
		
		return True

	def parse_reference_points( self ):
		''' Main function for identifing the characteristics
			of each refence point.
		'''
		
		try:
			for Name in sorted( self.TargetDict.keys() ):
				
				# Add the usable values to each dictionary
				print('Working on:', Name )
						
				Total = self.TargetDict[Name]['total']
				print('Points found:', Total)
				
				CodedList = dict()
				
				for i in range( Total ):
					Type = self.TargetDict[Name]['points'].get('point_type['+ str(i) +']')
					Coordinate = self.TargetDict[Name]['points'].get('coordinate['+ str(i) +']')
					Normal = self.TargetDict[Name]['points'].get('normal['+ str(i) +']')
					Diameter = self.TargetDict[Name]['points'].get('diameter['+ str(i) +']')
					Deviation = self.TargetDict[Name]['points'].get('residual['+ str(i) +']')
					Identification = self.TargetDict[Name]['points'].get('point_id['+ str(i) +']')

					TempDictionary = {'id':Identification,
									'center':Coordinate,
									'normal':Normal,
									'diameter':Diameter,
									'deviation':Deviation }										
					if 'coded' in Type:
						CodedList[Identification] = TempDictionary						
				self.TargetDict[Name]['coded'] = CodedList

		
		except Exception as Err:
			print('parse targets error:', Err)
			return False
		
		return True

def buildPointDict():
	'''Build Point Dictionary
	Creates an instance of the Targets class, and extracts just the coded points into a separate dictionary.
	Returns the dictionary of coded points with their ID, XYZ Center, and IJK Normal
	'''
	
	RefPoints = Targets()
	
	for MS in gom.ElementSelection ({'category': ['key', 'elements', 'explorer_category', 'actual', 'object_family', 'measurement_series']}):
			
		Name = MS.get('name')
		CodedPoints = RefPoints.TargetDict[Name].get( 'coded' )

		for Point in CodedPoints.keys():
			Number = CodedPoints[Point]['id']
			Center = CodedPoints[Point]['center']
			Normal = CodedPoints[Point]['normal']
					
		return(CodedPoints)

def CubeGeometryCalc(codedPointsDict,fixturePoints,xOffset,yOffset,zOffset,lengthCompensation,widthCompensation,heightCompensation,currentSample):
	'''Cube Geometry Calc
	Keyword arguments:
	codedPointsDict = A Dictionary of the coded points
	fixturePoints = A List of points on the specific fixture (derived from config)
	xOffset = A List - config value used to specify x location of the bounding box
	yOffset = A List - config value used to specify y location of the bounding box
	zOffset = A List - config value used to specify z location of the bounding box
	lengthCompensation = A Float - config value used to specify length of the bounding box
	widthCompensation = A Float - config value used to specify width of the bounding box
	heightCompensation = A Float - config value used to specify height of the bounding box
	currentSample = An integer - number used to iterate through sets of points 
	
	Stores the point locations of the XYZ centers of the 4 points
	Performs math to determine the center and the sized (Height/Length/Width) of the selection box
	
	Returns the Midpoint, Length, Width, and Height
	'''
	print(fixturePoints)
	print(xOffset,' ',yOffset,' ',zOffset)
	print(lengthCompensation,' ',widthCompensation,' ',heightCompensation)
	print(currentSample)

	ax = codedPointsDict[fixturePoints[currentSample*4+0]]['center'].x
	bx = codedPointsDict[fixturePoints[currentSample*4+1]]['center'].x
	cx = codedPointsDict[fixturePoints[currentSample*4+2]]['center'].x
	dx = codedPointsDict[fixturePoints[currentSample*4+3]]['center'].x
	ay = codedPointsDict[fixturePoints[currentSample*4+0]]['center'].y
	by = codedPointsDict[fixturePoints[currentSample*4+1]]['center'].y
	cy = codedPointsDict[fixturePoints[currentSample*4+2]]['center'].y
	dy = codedPointsDict[fixturePoints[currentSample*4+3]]['center'].y
	az = codedPointsDict[fixturePoints[currentSample*4+0]]['center'].z
	bz = codedPointsDict[fixturePoints[currentSample*4+1]]['center'].z
	cz = codedPointsDict[fixturePoints[currentSample*4+2]]['center'].z
	dz = codedPointsDict[fixturePoints[currentSample*4+3]]['center'].z
	midpoint = gom.Vec3d(((ax+cx)/2)+xOffset[currentSample],((ay+cy)/2)+yOffset[currentSample],((az+cz)/2)+zOffset[currentSample]) 
	width = (math.sqrt(((bx-dx)**2)+((by-dy)**2)))+widthCompensation
	length = (math.sqrt(((dx-cx)**2)+((dy-cy)**2)))+lengthCompensation
	height = (abs(az-bz))+heightCompensation
	return midpoint,length,width,height

def SelectCube(Midpoint,Length,Width,Height,currentSample,zRotArray):
	'''SelectCube
	
	Keyword arguments:
	Midpoint, Width, Height, and Length calculated by CubeGeometryCalc
	CurrentSample: Integer specifying iterable part #
	
	This is broken apart from the cube geometry calcualtion for neatness.
	
	'''
	gom.script.selection3d.select_inside_cube (center={'point': Midpoint},height=Height,length=Length,width=Width,rot_x=0,rot_y=0,rot_z=math.radians(zRotArray[currentSample]))
	
def Poly():
	MCAD_ELEMENT=gom.script.atos.polygonize_and_recalculate (fill_reference_points=True,polygonization_process='standard',polygonize_large_data_volumes=False)			
	return MCAD_ELEMENT.name

