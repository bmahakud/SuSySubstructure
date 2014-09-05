from ROOT import TFile, TTree, TChain
from binning import *
from datacard import *
from sumJetMassBinning import *
from extendedSumJetMassBinning import *
from gluinoXsec import *
from multiprocessing import Process
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--sample", dest="sample", default = "T1tttt",
		                      help="sample, must be either T1tttt, T1qqqq, T5VV", metavar="SAMPLE")

parser.add_option("--mGo", dest="mGluino", default = 1100,
		  help="mass of gluionos", metavar="MGLUINO")

parser.add_option("--mLSP", dest="mLSP", default = 25,
		  help="mass of LSP", metavar="MLSP")

parser.add_option("--binning", dest="binning", default="Classic",
		  help="Select binning to be used: Classic, SMJ, extSMJ", metavar="binning")

(options, args) = parser.parse_args()

def setAliases( tree ) : 

	tree.SetAlias("HT","HT_patJetsAK5PFPt50Eta25")
	tree.SetAlias("MHT","HT_patJetsAK5PFPt30")
	tree.SetAlias("NJets","NJets_patJetsAK5PFPt50Eta25")
	tree.SetAlias("sumJetMass","sumJetMass_fattenedJets")
	tree.SetAlias("DeltaPhi1","MHTPhi_patJetsAK5PFPt30[0]")
	tree.SetAlias("DeltaPhi2","MHTPhi_patJetsAK5PFPt30[1]")
	tree.SetAlias("DeltaPhi3","MHTPhi_patJetsAK5PFPt30[2]")

	#print "events:",tree.GetEntries()

	if tree == None : 
		raise InputError("datacardProduction - error grabbing tree: "+fileName)

def computeYields(  tree , 
		    binning ,
		    yields , 
		    weight ,
		    sig = False
		    ) :

	for iBin in range( binning.nBins ): 

		if sig : 
			cutString = "Filter_PBNRFilter==1 && Filter_eeBadScFilter==1 && Filter_ecalLaserCorrFilter==1 && Filter_hcalLaserEventFilter==1 && Filter_ra2EcalBEFilter==1 && Filter_ra2EcalTPFilter==1 && Filter_eeNoiseFilter==1 && Filter_trackingFailureFilter==1 && Filter_inconsistentMuons==1 && Filter_greedyMuons==1 && PATMuonsPFIDIsoNum == 0 && PATElectronsIDIsoNum==0 && DeltaPhi1>.5 && DeltaPhi2>.5 && DeltaPhi3>.3"
		else :
			setAliases( tree )
			cutString = "HT>0"


		for i in range( len( binning.branchNames ) ) : 

			branchName = binning.branchNames[i]
			cutString+="&&{0}>{1}&&{0}<{2}".format(branchName,binning.lowBinEdge[branchName][iBin],binning.highBinEdge[branchName][iBin])

		#print cutString
		
		yields[iBin] = tree.Draw(binning.branchNames[0],cutString)
		#print yields[iBin]

		yields[iBin] = float( yields[iBin] ) * weight		
		#print yields[iBin]

		if yields[iBin] == 0 :
			#print "ZERO!!"
			yields[iBin] = 0.000001

####### end of computeYields()

def buildCards(sampleName = "T1qqqq_HV" ,  massMom = 1000 , massDau = 25 , binning = "Classic" ) : 

        #myDatacard = datacard( njetBins , ["T1tttt"] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
	if binning == "SMJ" : 
		myDatacard = datacard( SMJbins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
	elif binning == "Classic" :
		myDatacard = datacard( RA2bins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
	elif binning == "extSMJ" :
		myDatacard = datacard( extRA2bins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
	else :
		raise NameError(binning)
	        return 


	inputDir = "./"

	accessProtocol = "root://cmsxrootd-site.fnal.gov//store/user/"
	bkgDir = "awhitbe1/SuSySubstructureAnalysisNtuples_V8/"

	### background trees
	QCD500tree = TChain("RA2TreeFiller/AnalysisTree")
	QCD500tree.Add( accessProtocol + bkgDir + "QCD_500HT1000_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )
	#print QCD500tree.GetEntries()

	QCD1000tree = TChain( "RA2TreeFiller/AnalysisTree" )
	QCD1000tree.Add( accessProtocol + bkgDir + "QCD_1000HTinf_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )
	#print QCD1000tree.GetEntries()

	Wjetstree = TChain( "RA2TreeFiller/AnalysisTree" )
	Wjetstree.Add( accessProtocol + bkgDir + "WJetsToLNu_400HTInf_v2_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )
	#print Wjetstree.GetEntries()

	Zjetstree = TChain( "RA2TreeFiller/AnalysisTree" )
	Zjetstree.Add( accessProtocol + bkgDir + "ZJetsToNuNu_400HTinf_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )
	#print Zjetstree.GetEntries()
	
	TTjetstree = TChain( "RA2TreeFiller/AnalysisTree" )
	TTjetstree.Add( accessProtocol + bkgDir + "TTJets_SemiLeptMGDecays_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )
	#print TTjetstree.GetEntries()
		
	#### load signal files
	fileNames = []

	sigDir = "awhitbe1/SuSySubstructureAnalysisNtuples_V8/"

	### signal files for T1tttt trees
	#fileNames.append(accessProtocol + "{0}/T1qqqq_HiddenValley_SumJetMass_AnalysisTree.root".format( sigDir ) )
	fileNames.append(accessProtocol + "{0}/SMS_T1tttt_mGo1100_mLSP25_ALL_SumJetMass_AnalysisTree.root".format( sigDir ) )

	treeName = "TreeFiller/AnalysisTree"
	#treeName = "RA2PreSelection"

	#print "QCD500"
	computeYields( QCD500tree  , myDatacard.binning , myDatacard.bkgYields["QCD500"]         , 5.7398   )
	#print "QCD1000"
	computeYields( QCD1000tree , myDatacard.binning , myDatacard.bkgYields["QCD1000"]        , 0.3179  )
	#print "ZinvJets"
	computeYields( Zjetstree   , myDatacard.binning , myDatacard.bkgYields["ZinvJets"]       , 0.1237 )
	#print "WlvJets"
	computeYields( Wjetstree   , myDatacard.binning , myDatacard.bkgYields["WlvJets"]        , 0.1222  )
	#print "TTsemiLeptJets"
	computeYields( TTjetstree  , myDatacard.binning , myDatacard.bkgYields["TTsemiLeptJets"] , 0.0816  )

	sigTree = TChain(treeName)
	for fileName in fileNames :
		sigTree.Add(fileName)

	if sigTree == None or sigTree.GetEntries() <= 0 :
		#raise InputError("Tree not found! Skipping this point")
		return 

	print "Signal"
	computeYields( sigTree , myDatacard.binning , myDatacard.sigYields[sampleName] , xsec[int(massMom)]*19500./sigTree.GetEntries() )
	
	print myDatacard.binning.nBins

	for i in range( myDatacard.binning.nBins ) :
		if binning == "SMJ" : 
			myDatacard.printDatacard("{3}_mGo{1}_mLSP{2}_datacard_TEST_SMJ_bin{0}.txt".format( i , massMom , massDau , sampleName ),i)
		elif binning == "Classic" :
			myDatacard.printDatacard("{3}_mGo{1}_mLSP{2}_datacard_TEST_Classic_bin{0}.txt".format( i , massMom , massDau , sampleName ),i)
		elif binning == "extSMJ" :
			myDatacard.printDatacard("{3}_mGo{1}_mLSP{2}_datacard_TEST_extRA2_bin{0}.txt".format( i , massMom , massDau , sampleName ),i)

#########
# main stuff
########
print "signal topology:",options.sample
print "gluino mass:",options.mGluino
print "LSP mass:",options.mLSP
print "binning:",options.binning

buildCards( options.sample , options.mGluino , options.mLSP , options.binning )


