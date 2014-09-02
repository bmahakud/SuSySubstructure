
void plotROC(//TString bkgFileName = "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V5/TTJets_SemiLeptMGDecays_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root",
	     TString bkgFileName = "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V5/QCD_1000HTinf_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root",
	     //TString bkgFileName = "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V5/QCD_500HT1000_LPCSUSYPAT_SLIM_ALL_SumJetMass_AnalysisTree.root",
	     TString sigFileName = "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_25to500_8TeV.root"
	     ){

  TFile* sigFile = new TFile(sigFileName);  
  TFile* bkgFile = new TFile(bkgFileName);

  TTree* sigTree = (TTree*)sigFile->Get("massMom1025_massDau825");
  TTree* bkgTree = (TTree*)bkgFile->Get("TreeFiller/AnalysisTree");
  
  bkgTree->SetAlias("JetsPt","pt_patJetsAK5PFPt50Eta25") ; 
  bkgTree->SetAlias("JetsPhi","phi_patJetsAK5PFPt50Eta25") ; 
  bkgTree->SetAlias("HT","Ht_patJetsAK5PFPt50Eta25") ; 
  bkgTree->SetAlias("MHT","missHt_patJetsAK5PFPt30") ; 
  bkgTree->SetAlias("NJets","nJets_patJetsAK5PFPt50Eta25") ; 
  bkgTree->SetAlias("sumJetMass","sumJetMass_fattenedJets") ; 

  gROOT->ProcessLine(".L rocCurve.C+");

  ROCplotter* myROC = new ROCplotter(sigTree,bkgTree);

  TGraph* sjm = myROC->make("abs(JetsPhi[0]-JetsPhi[1])",
			   100,0.,6.3,
			   2,1,2,
			   "(NJets>3&&HT>500&&MHT>200)");
  /*
  TGraph* ht = myROC.make("abs(JetsPhi[0]-JetsPhi[1])",
			  100,0.,6.3,
			  4,2,2,
			  "(NJets>3&&HT>500&&MHT>200)");
  */

  TCanvas* can = new TCanvas("can","can",500,500);

  smj->GetYaxis()->SetRangeUser(0.00001,1);

  smj->GetXaxis()->SetTitle("#epsilon_{sig}");
  smj->GetYaxis()->SetTitle("#epsilon_{bkg}");

  //ht->Draw("AC");
  sjm->Draw("AC");    
  
}
