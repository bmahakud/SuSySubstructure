from ROOT import TFile, TTree
from binning import *
from sumJetMassBinning import *
from datacard import *

def computeYields(  tree , 
					binning ,
					yields , 
					weight ) :

	for iBin in range( binning.nBins ): 

		passCuts = True
		cutString = "DeltaPhi1>.5 && DeltaPhi2>.5 && DeltaPhi3>.3 && Filter_PBNRFilter==1 && Filter_eeBadScFilter==1 && Filter_ecalLaserCorrFilter==1 && Filter_hcalLaserEventFilter==1 && Filter_ra2EcalBEFilter==1 && Filter_ra2EcalTPFilter==1 && Filter_eeNoiseFilter==1 && Filter_trackingFailureFilter==1 && Filter_inconsistentMuons==1 && Filter_greedyMuons==1 && PATMuonsPFIDIsoNum == 0 && PATElectronsIDIsoNum == 0"
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

def setAliases( tree ) : 

	tree.SetAlias("HT","Ht_patJetsAK5PFPt50Eta25")
	tree.SetAlias("MHT","Ht_patJetsAK5PFPt30")
	tree.SetAlias("NJets","nJets_patJetsAK5PFPt50Eta25")
	tree.SetAlias("sumJetMass","sumJetMass_fattenedJets")
	tree.SetAlias("DeltaPhi1","missHtPhi_patJetsAK5PFPt30[0]")
	tree.SetAlias("DeltaPhi2","missHtPhi_patJetsAK5PFPt30[1]")
	tree.SetAlias("DeltaPhi3","missHtPhi_patJetsAK5PFPt30[2]")

	#print "events:",tree.GetEntries()

	if tree == None : 
		raise InputError("datacardProduction - error grabbing tree: "+fileName)

####### end of getTreeSetAliases()

inputDir = "./"

### background trees
QCD500file = TFile( "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V4/QCD_500HT1000_LPCSUSYPAT_SLIM_SumJetMass_AnalysisTree.root" , "READ" )
QCD500tree = QCD500file.Get( "TreeFiller/AnalysisTree" )
setAliases( QCD500tree )
QCD1000file = TFile( "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V4/QCD_1000HTinf_LPCSUSYPAT_SLIM_SumJetMass_AnalysisTree.root" , "READ" )
QCD1000tree = QCD1000file.Get( "TreeFiller/AnalysisTree" )
setAliases( QCD1000tree )
Wjetsfile = TFile( "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V4/WJetsToLNu_HT-400ToInf_8TeV_LPCSUSYPAT_SLIM_SumJetMass_AnalysisTree.root" , "READ" )
Wjetstree = Wjetsfile.Get( "TreeFiller/AnalysisTree" )
setAliases( Wjetstree )
Zjetsfile = TFile( "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V4/ZJetsToNuNu_400_HT_inf_LPCSUSYPAT_SLIM_SumJetMass_AnalysisTree.root" , "READ" )
Zjetstree = Zjetsfile.Get( "TreeFiller/AnalysisTree" )
setAliases( Zjetstree )
TTjetsfile = TFile( "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V4/TTJets_SemiLeptMGDecays_8TeV_LPCSUSYPAT_SLIM_SumJetMass_AnalysisTree.root" , "READ" )
TTjetstree = TTjetsfile.Get( "TreeFiller/AnalysisTree" )
setAliases( TTjetstree )

#print TTjetstree.Draw("NJets","NJets>7")

### signal files for T1tttt trees
fileNames = []

sigDir = "/eos/uscms/store/user/awhitbe1/RA2nTupleExtension/divided/"

#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root")
#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_25to550_8TeV.root")
#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_25to500_8TeV.root")
#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_525to875_8TeV.root")
#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root")
#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_525to1000_8TeV_V2.root")
#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV.root")
fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_800to1400_mLSP_1_8TeV.root")

treeName = "massMom1100_massDau1"

T1tttt_datacard = datacard( SMJbins , ["T1tttt"] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )

computeYields( QCD500tree  , T1tttt_datacard.binning , T1tttt_datacard.bkgYields["QCD500"]         , 6.28   )
computeYields( QCD1000tree , T1tttt_datacard.binning , T1tttt_datacard.bkgYields["QCD1000"]        , 0.316  )
computeYields( Zjetstree   , T1tttt_datacard.binning , T1tttt_datacard.bkgYields["ZinvJets"]       , 0.040  )
computeYields( Wjetstree   , T1tttt_datacard.binning , T1tttt_datacard.bkgYields["WlvJets"]        , 0.126  )
computeYields( TTjetstree  , T1tttt_datacard.binning , T1tttt_datacard.bkgYields["TTsemiLeptJets"] , 0.082  )

for fileName in fileNames : 

	file = TFile( fileName , "READ" )
	sigTree = file.Get( treeName )

	if sigTree == None :
		continue

	computeYields( sigTree , T1tttt_datacard.binning , T1tttt_datacard.sigYields["T1tttt"] , 0.0101744*19500./sigTree.GetEntries() )
	
print T1tttt_datacard.binning.nBins

for i in range( T1tttt_datacard.binning.nBins ) :
	T1tttt_datacard.printDatacard("T1tttt_mGo1100_mLSP1_datacard_SMJ_bin{0}.txt".format(i),i)

#tree = file.Get( treeName )
#tree.Draw("sumJetMass","HT>500&&MHT>200&&NJets>7&&DeltaPhi1>.5&&DeltaPhi2>.5&&DeltaPhi3>.3")
