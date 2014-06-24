"""
class intended to organize all the relevant information
for building a multi-binned cut & count datacard.

A. Whitbeck - June 3, 2014

The binning object (as defined in binning.py), a list
of signal channel labels, and a list of background channel 
labels should all be passed to the constructor.
"""

from binning import *

class datacard:

	def __init__( self , binning = RA2bins , sigLabels = [ "T1tttt" ] , bkgLabels = [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] ) :

		self.binning = binning
		
		self.sigLabels = sigLabels
		self.bkgLabels = bkgLabels

		self.sigYields = {}
		self.bkgYields = {}

		for label in sigLabels :
			self.sigYields[ label ] = [0.]*self.binning.nBins

		for label in bkgLabels :
			self.bkgYields[ label ] = [0.]*self.binning.nBins		

		self.header = ["imax 1  #number of channels \n" , 
					   "jmax {0}  #number of backgrounds \n".format(len(self.bkgLabels)),
					   "kmax 0  #number of nuisance parameters \n",
					   "#------------ \n",
					   "Observation 1 \n",
					   "#------------ \n",
					   "bin"+" ch1"*(len(self.sigLabels)+len(self.bkgLabels))+"\n" ]

		processString = "process "
		for process in self.sigYields : 
			processString=processString+" "+process

		for process in self.bkgYields : 
			processString=processString+" "+process

		processString=processString+" \n"
		self.header.append(processString)

		processString = "process "

		for i in range( 1 - len(self.sigLabels) , 1 , 1 ) :
			processString=processString+" "+str(i)

		for i in range( 1 , len(self.bkgLabels) + 1 , 1 ) :
			processString=processString+" "+str(i)

		processString=processString+" \n"
		self.header.append(processString)

	def printDatacard( self , fileName = "exampleCard.txt" , bin = 0 ) :

		#for var in self.binning.lowBinEdge :
			#print self.binning.lowBinEdge[var][bin]

		outputFile = open( fileName , 'w' )

		for line in self.header : 
			outputFile.write( line )

		rateString = "rate "
		for process in self.sigYields :
			#print process,self.sigYields[process][bin]
			rateString = rateString+" {0:.6f}".format(self.sigYields[process][bin])
		for process in self.bkgYields :
			#print process,self.bkgYields[process][bin]
			rateString = rateString+" {0:.6f}".format(self.bkgYields[process][bin])

		outputFile.write( rateString + " \n" )
		outputFile.close()

exampleCard = datacard()
exampleCard.sigYields["T1tttt"][0] = 10.
exampleCard.bkgYields["QCD500"][0] = 2.
exampleCard.bkgYields["QCD1000"][0] = 2.
exampleCard.bkgYields["ZinvJets"][0] = 2.
exampleCard.bkgYields["WlvJets"][0] = 2.
exampleCard.bkgYields["TTsemiLeptJets"][0] = 2.
#exampleCard.printDatacard()
