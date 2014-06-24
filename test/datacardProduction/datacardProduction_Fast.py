def setAliases( tree ) : 

	tree.SetAlias("HT","Ht_patJetsAK5PFPt50Eta25")
	tree.SetAlias("MHT","missHt_patJetsAK5PFPt30")
	tree.SetAlias("NJets","nJets_patJetsAK5PFPt50Eta25")
	tree.SetAlias("sumJetMass","sumJetMass_fattenedJets")
	tree.SetAlias("DeltaPhi1","missHtPhi_patJetsAK5PFPt30[0]")
	tree.SetAlias("DeltaPhi2","missHtPhi_patJetsAK5PFPt30[1]")
	tree.SetAlias("DeltaPhi3","missHtPhi_patJetsAK5PFPt30[2]")

	#print "events:",tree.GetEntries()

	if tree == None : 
		raise InputError("datacardProduction - error grabbing tree: "+fileName)

####### end of getTreeSetAliases()

def buildCards( massMom = 1075 , massDau = 125 , useSMJ = False ) : 

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

	sampleName = "T5VV"

	fileNames = []

	sigDir = "/eos/uscms/store/user/awhitbe1/RA2nTupleExtension/"

	### signal files for T1tttt trees
	#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root")
	#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_25to550_8TeV.root")
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_25to500_8TeV"))
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_525to875_8TeV"))
	#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root")
	#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_525to1000_8TeV_V2.root")
	#fileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV.root")
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_800to1400_mLSP_1_8TeV"))
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_1_8TeV"))

	##### signal files for T5VV trees
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_800to1100_mLSP_25to525_8TeV"))
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_800to1100_mLSP_575to875_8TeV"))
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_1150to1400_mLSP_25to525_8TeV"))
	#fileNames.append(sigDir+"{0}/divided/{0}.root".format("19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_400to750_mLSP_25to525_8TeV"))

	### signal files for T5tttt trees
	fileNames.append(sigDir+"{0}/divided/scan*.root".format(""))

	treeName = "massMom{0}_massDau{1}".format( massMom , massDau )
	#treeName = "RA2PreSelection"

	njetBins = binning(["NJets"])
	njetBins.addBin( [(2,6)] )
	njetBins.addBin( [(5,8)] ) 
	njetBins.addBin( [(7,999 )] )

	#myDatacard = datacard( njetBins , ["T1tttt"] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
	if useSMJ : 
		myDatacard = datacard( SMJbins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )
	else :
		myDatacard = datacard( RA2bins , [sampleName] , [ "QCD500" , "QCD1000" , "ZinvJets" , "WlvJets" , "TTsemiLeptJets" ] )

	#print "QCD500"
	computeYields( QCD500tree  , myDatacard.binning , myDatacard.bkgYields["QCD500"]         , 6.28   )
	#print "QCD1000"
	computeYields( QCD1000tree , myDatacard.binning , myDatacard.bkgYields["QCD1000"]        , 0.316  )
	#print "ZinvJets"
	computeYields( Zjetstree   , myDatacard.binning , myDatacard.bkgYields["ZinvJets"]       , 0.040  )
	#print "WlvJets"
	computeYields( Wjetstree   , myDatacard.binning , myDatacard.bkgYields["WlvJets"]        , 0.126  )
	#print "TTsemiLeptJets"
	computeYields( TTjetstree  , myDatacard.binning , myDatacard.bkgYields["TTsemiLeptJets"] , 0.082  )

	sigTree = TChain(treeName)
	for fileName in fileNames :
		sigTree.Add(fileName)

	if sigTree == None or sigTree.GetEntries() <= 0 :
		#raise InputError("Tree not found! Skipping this point")
		return 

	#print "T1tttt"
	computeYields( sigTree , myDatacard.binning , myDatacard.sigYields[sampleName] , xsec[massMom]*19500./sigTree.GetEntries() , True )
	
	print myDatacard.binning.nBins

	for i in range( myDatacard.binning.nBins ) :
		if useSMJ : 
			myDatacard.printDatacard("{3}_mGo{1}_mSt{2}_datacard_TEST_SMJ_bin{0}.txt".format( i , massMom , massDau , sampleName ),i)
		else :
			myDatacard.printDatacard("{3}_mGo{1}_mSt{2}_datacard_TEST_Classic_bin{0}.txt".format( i , massMom , massDau , sampleName ),i)

#for m in range(800,1400,100) :

	#buildCards( m , 1 , True)
	#buildCards( m , 1 , False)

for m in range(1200,1425,100) :

	buildCards( m , 25 , True)
	buildCards( m , 25 , False)


