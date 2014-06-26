from ROOT import TFile, TTree, TChain
from binning import *
from datacard import *
from sumJetMassBinning import *
from gluinoXsec import *
from multiprocessing import Process

def computeYields(tree , 
		  binning ,
		  yields , 
		  weight ,
		  sig = False
		  ):

	for iEvt in range( tree.GetEntries() ) : 

		tree.GetEntry( iEvt )

		if sig : 
			if tree.Filter_PBNRFilter!=1 and tree.Filter_eeBadScFilter!=1 and tree.Filter_ecalLaserCorrFilter!=1 and tree.Filter_hcalLaserEventFilter!=1 and tree.Filter_ra2EcalBEFilter!=1 and tree.Filter_ra2EcalTPFilter!=1 and tree.Filter_eeNoiseFilter!=1 and tree.Filter_trackingFailureFilter!=1 and tree.Filter_inconsistentMuons!=1 and tree.Filter_greedyMuons!=1 and tree.PATMuonsPFIDIsoNum!=0 and tree.PATElectronsIDIsoNum!=0 and tree.DeltaPhi1>.5 and tree.DeltaPhi2>.5 and tree.DeltaPhi3>.3 :
				continue

		for iBin in range( binning.nBins ): 
			
			for branch in binning.branchNames : 

				var = getattr( tree , branch )

				if var > binning.lowBinEdge[branch][iBin] and var < binning.highBinEdge[branch][iBin] : 
					yields[iBin] += 1

			# #################################
			# end loop over cuts
		# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		# end loop over bins
	# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	# end loop over events

	print yields

	## apply weights
	for iBin in range( binning.nBins ): 
		
		if yields[iBin] == 0 :
			#print "ZERO!!"
			yields[iBin] = 0.000001
		else : 
			yields[iBin] = float( yields[iBin] ) * weight

	print yields

####### end of getTreeSetAliases()

def buildCards( massMom , massDau , datacard ) :

	fileNames = []

	sigDir = "/eos/uscms/store/user/awhitbe1/RA2nTupleExtension/"

	### signal files for T1tttt trees
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
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_800to1100_mLSP_25to525_8TeV"))
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_800to1100_mLSP_575to875_8TeV"))
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_1150to1400_mLSP_25to525_8TeV"))
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_400to750_mLSP_25to525_8TeV"))

	### signal files for T5tttt trees
	#fileNames.append(sigDir+"{0}/divided/scan*.root".format(""))

	#print TTjetstree.Draw("NJets","NJets>7")

	treeName = "massMom{0}_massDau{1}".format( massMom , massDau )
	#treeName = "RA2PreSelection"

	sigTree = TChain(treeName)
	for fileName in fileNames :
		sigTree.Add(fileName)

	if sigTree == None or sigTree.GetEntries() <= 0 :
		#raise InputError("Tree not found! Skipping this point")
		return myDatacard

	#print "T1tttt"
	computeYields( sigTree , datacard.binning , datacard.sigYields[sampleName] , xsec[massMom]*19500./sigTree.GetEntries() , True )

	for i in range( datacard.binning.nBins ) :
		datacard.printDatacard("{3}_mGo{1}_mLSP{2}_datacard_TEST_SMJ_bin{0}.txt".format( i , massMom , massDau , sampleName ),i)

#### -- background stuff -- ####

sampleName = "T1tttt"

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

referenceCardSMJ = datacard( SMJbins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
referenceCard = datacard( RA2bins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )

#print "QCD500"                                                                                                                                                            
#computeYields( QCD500tree  , referenceCard.binning , referenceCard.bkgYields["QCD500"]         , 5.582   )
QCD500yields = []
QCD500yieldsSMJ = []
QCD500proc = Process( target=computeYields , args=( QCD500tree  , referenceCard.binning , QCD500yields         , 5.582   ) )
QCD500procSMJ = Process( target=computeYields , args=( QCD500tree  , referenceCardSMJ.binning , QCD500yieldsSMJ         , 5.582   ) )
#print "QCD1000"                                                                                                                                                           
#computeYields( QCD1000tree , myDatacard.binning , myDatacard.bkgYields["QCD1000"]        , 0.31    )
QCD1000proc = Process( target=computeYields , args=( QCD1000tree , referenceCard.binning , referenceCard.bkgYields["QCD1000"]        , 0.31    ) )
QCD1000procSMJ = Process( target=computeYields , args=( QCD1000tree , referenceCardSMJ.binning , referenceCardSMJ.bkgYields["QCD1000"]        , 0.31    ) )
#print "ZinvJets"                                                                                                                                                          
#computeYields( Zjetstree   , myDatacard.binning , myDatacard.bkgYields["ZinvJets"]       , 0.134   )
ZjetProc = Process( target=computeYields , args=( Zjetstree   , referenceCard.binning , referenceCard.bkgYields["ZinvJets"]       , 0.134   ) )
ZjetProcSMJ = Process( target=computeYields , args=( Zjetstree   , referenceCardSMJ.binning , referenceCardSMJ.bkgYields["ZinvJets"]       , 0.134   ) )
#print "WlvJets"                                                                                                                                                           
#computeYields( Wjetstree   , myDatacard.binning , myDatacard.bkgYields["WlvJets"]        , 0.106   )
WjetProc = Process( target=computeYields , args=( Wjetstree   , referenceCard.binning , referenceCard.bkgYields["WlvJets"]        , 0.106   ) )
WjetProcSMJ = Process( target=computeYields , args=( Wjetstree   , referenceCardSMJ.binning , referenceCardSMJ.bkgYields["WlvJets"]        , 0.106   ) )
#print "TTsemiLeptJets"                                                                                                                                                    
#computeYields( TTjetstree  , myDatacard.binning , myDatacard.bkgYields["TTsemiLeptJets"] , 0.082   )
TTjetProc = Process( target=computeYields , args=( TTjetstree  , referenceCard.binning , referenceCard.bkgYields["TTsemiLeptJets"] , 0.082   ) )
TTjetProcSMJ = Process( target=computeYields , args=( TTjetstree  , referenceCardSMJ.binning , referenceCardSMJ.bkgYields["TTsemiLeptJets"] , 0.082   ) )

QCD500proc.start() ; 
#QCD1000proc.start() ; ZjetProc.start() ; WjetProc.start() ; TTjetProc.start()                                                      
#QCD500procSMJ.start() ; QCD1000procSMJ.start() ; ZjetProcSMJ.start() ; WjetProcSMJ.start() ; TTjetProcSMJ.start()                                                      
print "Waiting for all background processes to finish..."                                                                                                                            
QCD500proc.join() ; 
#QCD1000proc.join() ; ZjetProc.join() ; WjetProc.join() ; TTjetProc.join()                                                           
#QCD500procSMJ.join() ; QCD1000procSMJ.join() ; ZjetProcSMJ.join() ; WjetProcSMJ.join() ; TTjetProcSMJ.join()                                                           

print referenceCard.bkgYields["QCD500"]

sigProcess = []
for m in range(25,875,100) :	

	myDatacard = datacard( RA2bins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
	myDatacard.bkgYields = referenceCard.bkgYields
	sigProcess.append( Process( target=buildCards , args=( 1025 , m , myDatacard ) ) )
	#sigProcess[-1].start()
	
	myDatacard = datacard( SMJbins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
	myDatacard.bkgYields = referenceCardSMJ.bkgYields
	sigProcess.append( Process( target=buildCards , args=( 1025 , m , myDatacard ) ) )
	#sigProcess[-1].start()
	
#print "Waiting for all signal processes to finish..."
#for p in sigProcess : 
#	p[-1].join()
