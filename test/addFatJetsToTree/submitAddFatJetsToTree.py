###############

import os
from ROOT import TChain

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--sample", dest="sample",
		                    help="sample", metavar="SAMPLE")

(options, args) = parser.parse_args()

sample = options.sample
inputDir = "/eos/uscms/store/user/awhitbe1/RA2nTuple/"+options.sample+"/"
dirList = os.listdir(inputDir)

ifile = 0

for f in dirList : 

	#print f

	#os.system( "sed -e 's|<DIR>|{0}|g' -e 's|<FILE>|{1}|g'< runAddFatJetsToTree.tpl > runAddFatJetsToTree_{2}_{3}.sh".format( inputDir , f , sample , ifile ) )
	os.system( "sed -e 's|<FILE>|{1}|g'< runAddFatJetsToTree.tpl > runAddFatJetsToTree_{2}_{3}.sh".format( inputDir , f , sample , ifile ) )
	os.system( "sed -e 's|<INDEX>|{0}|g' -e 's|<SAMPLE>|{1}|g' < addFatJetsToTree_condorSub.tpl > addFatJetsToTree_condorSub_{1}_{0}".format( ifile , sample ) )

	os.system("condor_submit addFatJetsToTree_condorSub_{0}_{1}".format( sample , ifile ) )

	ifile+=1
