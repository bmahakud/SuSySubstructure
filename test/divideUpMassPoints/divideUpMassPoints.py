from ROOT import TFile, TChain, TTree, AddressOf, gROOT
from array import array
import os
from optparse import OptionParser

debug = False

parser = OptionParser()
parser.add_option("-d", "--dir", dest="dirName",
                  help="read from DIR", metavar="INPUT_DIR")
parser.add_option("-o", "--outDir", dest="outputDir",
                  help="DIR for output files", metavar="OUTPUT_DIR")
parser.add_option("-n","--numEvents", dest="numEvents",
		    	  help="total number of events to process", metavar="NEVENT")
parser.add_option("-s","--startEvent", dest="startEvent",
		    	  help="first event to process", metavar="START_EVENT")
parser.add_option("-f","--file", dest="inputFile",
		    	  help="file to be loaded", metavar="FILE")

################################################
def divideUpMassPoints(	firstEvent = 0,
						lastEvent = 1000000 ) :

	if firstEvent > chain.GetEntries():
			print "not enough events"
			return 

	if lastEvent > chain.GetEntries():
		lastEvent = chain.GetEntries

	#loop over events in input TChain
	for i in range( firstEvent , lastEvent ) : 

		if ( i % 100000 == 0 ) :
			print "event:",i

		chain.GetEntry(i)

		if ( debug ):
			print "ht:",chain.HT
			print "mht:",chain.MHT
			print "nJets:",chain.NJets
			print "sumJetMass:",chain.sumJetMass
			print "massMom:",int(chain.massMom)
			print "massDau:",int(chain.massDau)
			print "treeName:","massMom{0}_massDau{1}".format(int(chain.massMom),int(chain.massDau))

		# format tree name base on gluino mass and LSP mass (or the analog of these)
		treeName = "massMom{0}_massDau{1}".format(int(chain.massMom),int(chain.massDau))


		# check if this mass point has been seen already:
		#     if yes, fill existing tree
		if treeName in tree :

			tree[treeName].Fill()

		#	if no, make new tree and fill that
		else: 
			print "making",treeName
			tree[treeName] = chain.CloneTree(0,"fast")
			tree[treeName].SetNameTitle(treeName,treeName)
			
			tree[treeName].Fill()

	# loop over new trees and write to outputFile
	for key in tree:
	
		if debug :
			print key
			print "entries:",tree[key].GetEntries()

		tree[key].Write()

	# close output file
	outputFile.Close()


##############################
##### start of main code #####
##############################

(options, args) = parser.parse_args()

tree = {}

#inputFiles="/eos/uscms/store/user/awhitbe1/RA2nTuple/"+options.dirName+"/*.root"
chain = TChain("RA2PreSelection")
chain.Add( options.dirName + "/" + options.inputFile )

#if options.startEvent + options.numEvents < chain.GetEntries() :
#	outputFile = TFile(options.outputDir+"/"+options.dirName+"_{0}.root".format(options.startEvent),"RECREATE")
#	divideUpMassPoints( options.startEvent , options.numEvents )
outputFile = TFile(options.outputDir+"/"+options.inputFile,"RECREATE")
divideUpMassPoints( 0 , chain.GetEntries() )
