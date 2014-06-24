info = """
class which should be used to define binning to 
be used for statistical interpretations.  

A. Whitbeck - June 3, 2014

The constructor takes a list of variable names. 
if these variables truely correspond tree branch
names, it can be used as an iterable list so that
yields for each bin can be computed automatically.

addBin method also one to build up a list of relevant bins
so that the binning for a whole analysis can be 
defined within one single object.  The structure 
of the bin definitions is such that the low edge of 
each cut used for a given bin is store in a dictionary
where the key correspond to the variable of the cut, these
will correspond to the list of variables passed to the construct.
a similar dictionary also exists for the high edge of each
cut to be applied for a given bin.  Note, each element of the 
dict are lists of doubles - one for each bin.
"""

class binning : 
	def __init__( self , branchNameList = [ "HT" , "MHT" , "NJets" ] ) :

		self.branchNames = branchNameList
		self.lowBinEdge = {}
		self.highBinEdge ={}
		self.nBins = 0

		for branchName in branchNameList :
			self.lowBinEdge[ branchName ]  = []
			self.highBinEdge[ branchName ] = []

	def addBin( self , binEdges = [] ) : 

		if len( binEdges ) != len( self.branchNames ) :
			raise InputError("binning::addBin - number of entries in binEdges doesn't match number of branches passed to constructor")
			return 

		for i in range( len( self.branchNames ) ): 
			self.lowBinEdge[ self.branchNames[i] ].append( binEdges[i][0] ) 
			self.highBinEdge[ self.branchNames[i] ].append( binEdges[i][1] ) 

		self.nBins+=1

## binning used for the RA2 analysis
RA2bins = binning() # [ "HT" , "MHT" , "NJets" ] )

################ HT cuts #### MHT cuts #### NJet cuts ###

## low jet binning
RA2bins.addBin( [ (500 , 800) , (200 , 300)  , (2 , 6) ] )
RA2bins.addBin( [ (500 , 800) , (300 , 450)  , (2 , 6) ] )
RA2bins.addBin( [ (500 , 800) , (450 , 600)  , (2 , 6 ) ] )
RA2bins.addBin( [ (500 , 800) , (600 , 9999) , (2 , 6 ) ] )

RA2bins.addBin( [ (800 , 1000) , (200 , 300)  , (2 , 6 ) ] )
RA2bins.addBin( [ (800 , 1000) , (300 , 450)  , (2 , 6 ) ] )
RA2bins.addBin( [ (800 , 1000) , (450 , 600)  , (2 , 6 ) ] )
RA2bins.addBin( [ (800 , 1000) , (600 , 9999) , (2 , 6 ) ] )

RA2bins.addBin( [ (1000 , 1250) , (200 , 300)  , (2 , 6 ) ] )
RA2bins.addBin( [ (1000 , 1250) , (300 , 450)  , (2 , 6 ) ] )
RA2bins.addBin( [ (1000 , 1250) , (450 , 600)  , (2 , 6 ) ] )
RA2bins.addBin( [ (1000 , 1250) , (600 , 9999) , (2 , 6 ) ] )

RA2bins.addBin( [ (1250 , 1500) , (200 , 300)  , (2 , 6 ) ] )
RA2bins.addBin( [ (1250 , 1500) , (300 , 450)  , (2 , 6 ) ] )
RA2bins.addBin( [ (1250 , 1500) , (450 , 9999) , (2 , 6 ) ] )

RA2bins.addBin( [ (1500 , 9999) , (200 , 300)  , (2 , 6 ) ] )
RA2bins.addBin( [ (1500 , 9999) , (300 , 9999) , (2 , 6 ) ] )

## medium jet binning
RA2bins.addBin( [ (500 , 800) , (200 , 300)  , (5 , 8) ] )
RA2bins.addBin( [ (500 , 800) , (300 , 450)  , (5 , 8) ] )
RA2bins.addBin( [ (500 , 800) , (450 , 9999)  , (5 , 8) ] )

RA2bins.addBin( [ (800 , 1000) , (200 , 300)  , (5 , 8) ] )
RA2bins.addBin( [ (800 , 1000) , (300 , 450)  , (5 , 8) ] )
RA2bins.addBin( [ (800 , 1000) , (450 , 9999)  , (5 , 8) ] )

RA2bins.addBin( [ (1000 , 1250) , (200 , 300)  , (5 , 8) ] )
RA2bins.addBin( [ (1000 , 1250) , (300 , 450)  , (5 , 8) ] )
RA2bins.addBin( [ (1000 , 1250) , (450 , 9999)  , (5 , 8) ] )

RA2bins.addBin( [ (1250 , 1500) , (200 , 300)  , (5 , 8) ] )
RA2bins.addBin( [ (1250 , 1500) , (300 , 450)  , (5 , 8) ] )
RA2bins.addBin( [ (1250 , 1500) , (450 , 9999) , (5 , 8) ] )

RA2bins.addBin( [ (1500 , 9999) , (200 , 300)  , (5 , 8) ] )
RA2bins.addBin( [ (1500 , 9999) , (300 , 9999) , (5 , 8) ] )

## high jet binning
RA2bins.addBin( [ (500 , 800) , (200 , 9999)  , (7 , 9999) ] )
RA2bins.addBin( [ (800 , 1000) , (200 , 9999)  , (7 , 9999) ] )
RA2bins.addBin( [ (1000 , 1250) , (200 , 9999)  , (7 , 9999) ] )
RA2bins.addBin( [ (1250 , 1500) , (200 , 9999)  , (7 , 9999) ] )
RA2bins.addBin( [ (1500 , 9999) , (200 , 9999)  , (7 , 9999) ] )

	