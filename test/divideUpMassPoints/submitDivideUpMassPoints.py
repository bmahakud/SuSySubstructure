###############

import os
from ROOT import TChain

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--sample", dest="sample",
		                    help="sample", metavar="SAMPLE")

(options, args) = parser.parse_args()

sample = options.sample
inputDir = "/eos/uscms/store/user/awhitbe1/RA2nTupleExtension/"+options.sample+"/"
dirList = os.listdir(inputDir)

ifile = 0

for f in dirList : 

	print f
	chain = TChain("RA2PreSelection")
	chain.Add( inputDir + f )
	print "events:",chain.GetEntries()
	if chain.GetEntries() <= 0 : 
		print "something wrong with this file!!!"
		print "{0}/{1}".format( inputDir , f )
		print chain.GetEntries()
		continue

	os.system( "sed -e 's|<DIR>|{0}|g' -e 's|<FILE>|{1}|g'< runDivideUpMassPoints.tpl > runDivideUpMassPoints_{2}_{3}.sh".format( inputDir , f , sample , ifile ) )
	os.system( "sed -e 's|<INDEX>|{0}|g' -e 's|<SAMPLE>|{1}|g' < divideUpMassPoints_condorSub.tpl > divideUpMassPoints_condorSub_{1}_{0}".format( ifile , sample ) )

	os.system("condor_submit divideUpMassPoints_condorSub_{0}_{1}".format( sample , ifile ) )

	ifile+=1
