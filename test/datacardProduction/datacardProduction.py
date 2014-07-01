from ROOT import TFile, TTree, TChain
from binning import *
from datacard import *
from sumJetMassBinning import *
from gluinoXsec import *
from multiprocessing import Process
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--sample", dest="sample", default = "T1tttt",
		                      help="sample, must be either T1tttt, T1qqqq, T5VV", metavar="SAMPLE")

parser.add_option("--mGo", dest="mGluino", default = 1025,
		  help="mass of gluionos", metavar="MGLUINO")

parser.add_option("--mLSP", dest="mLSP", default = 25,
		  help="mass of LSP", metavar="MLSP")

parser.add_option("--useSMJ", dest="useSMJ", default=False, action = "store_true",
		  help="if selected the SMJ binning will be used", metavar="SMJ")

(options, args) = parser.parse_args()


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

def buildCards(sampleName = "T1tttt" ,  massMom = 1075 , massDau = 125 , useSMJ = False ) : 

	inputDir = "./"

	bkgDir = "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V5/"

	### background trees
	QCD500tree = TChain("RA2TreeFiller/AnalysisTree")
	QCD500tree.Add( bkgDir + "QCD_500HT1000_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )

	QCD1000tree = TChain( "RA2TreeFiller/AnalysisTree" )
	QCD1000tree.Add( bkgDir + "QCD_1000HTinf_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )

	Wjetstree = TChain( "RA2TreeFiller/AnalysisTree" )
	Wjetstree.Add( bkgDir + "WJetsToLNu_400HTInf_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )
	Wjetstree.Add( bkgDir + "WJetsToLNu_400HTInf_v2_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )

	Zjetstree = TChain( "RA2TreeFiller/AnalysisTree" )
	Zjetstree.Add( bkgDir + "ZJetsToNuNu_400HTinf_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )

	TTjetstree = TChain( "RA2TreeFiller/AnalysisTree" )
	TTjetstree.Add( bkgDir + "TTJets_SemiLeptMGDecays_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root" )
	

	#### load signal files
	fileNames = []

	sigDir = "/eos/uscms/store/user/awhitbe1/RA2nTupleExtension/"

	### signal files for T1tttt trees
	if sampleName == "T1tttt" :
		#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root")
		#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_25to550_8TeV.root")
		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_25to500_8TeV"))
		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_525to875_8TeV"))
		#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root")
		#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_525to1000_8TeV_V2.root")
		#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV.root")
		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_800to1400_mLSP_1_8TeV"))
		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_1_8TeV"))

	##### signal files for T5VV trees
	if sampleName == "T5VV" : 
		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_800to1100_mLSP_25to525_8TeV"))
		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_800to1100_mLSP_575to875_8TeV"))
		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_1150to1400_mLSP_25to525_8TeV"))
		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_400to750_mLSP_25to525_8TeV"))

	if sampleName == "T1qqqq" :
		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_1150to1400_mLSP_25to675_8TeV_V2"))
       		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_400to750_mLSP_25to725_8TeV_V2"))
      		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_800to1100_mLSP_25to625_8TeV_V2"))
		fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_800to1100_mLSP_675to1075_8TeV_V2"))

	### signal files for T5tttt trees
	if sampleName == "T5tttt" :
		fileNames.append(sigDir+"{0}/divided/scan*.root".format("29May2014_SignalTree_SMS_MG_T5tttt"))

	treeName = "massMom{0}_massDau{1}".format( massMom , massDau )
	#treeName = "RA2PreSelection"

	#myDatacard = datacard( njetBins , ["T1tttt"] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
	if useSMJ : 
		myDatacard = datacard( SMJbins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
	else :
		myDatacard = datacard( RA2bins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )

	#print "QCD500"
	computeYields( QCD500tree  , myDatacard.binning , myDatacard.bkgYields["QCD500"]         , 5.582   )
	#print "QCD1000"
	computeYields( QCD1000tree , myDatacard.binning , myDatacard.bkgYields["QCD1000"]        , 0.31  )
	#print "ZinvJets"
	computeYields( Zjetstree   , myDatacard.binning , myDatacard.bkgYields["ZinvJets"]       , 0.134  )
	#print "WlvJets"
	computeYields( Wjetstree   , myDatacard.binning , myDatacard.bkgYields["WlvJets"]        , 0.106  )
	#print "TTsemiLeptJets"
	computeYields( TTjetstree  , myDatacard.binning , myDatacard.bkgYields["TTsemiLeptJets"] , 0.082  )

	sigTree = TChain(treeName)
	for fileName in fileNames :
		sigTree.Add(fileName)

	if sigTree == None or sigTree.GetEntries() <= 0 :
		#raise InputError("Tree not found! Skipping this point")
		return 

	#print "T1tttt"
	computeYields( sigTree , myDatacard.binning , myDatacard.sigYields[sampleName] , xsec[int(massMom)]*19500./sigTree.GetEntries() , True )
	
	print myDatacard.binning.nBins

	for i in range( myDatacard.binning.nBins ) :
		if useSMJ : 
			myDatacard.printDatacard("{3}_mGo{1}_mLSP{2}_datacard_TEST_SMJ_bin{0}.txt".format( i , massMom , massDau , sampleName ),i)
		else :
			myDatacard.printDatacard("{3}_mGo{1}_mLSP{2}_datacard_TEST_Classic_bin{0}.txt".format( i , massMom , massDau , sampleName ),i)

#########
# main stuff
########
print "signal topology:",options.sample
print "gluino mass:",options.mGluino
print "LSP mass:",options.mLSP
print "using SMJ:",options.useSMJ

buildCards( options.sample , options.mGluino , options.mLSP , options.useSMJ )


