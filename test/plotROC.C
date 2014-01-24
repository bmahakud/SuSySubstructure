


void plotROC(TString sigFileName = "T1tttt_mLSP-200_mGo-1000_condorSub/T1tttt_mG1000_mLSP200_LPCSUSYPAT_SumJetMass_AnalysisTree.root", //"T1tttt_mLSP-200_mGo-1000_condorSub/T1tttt_mG1000_mLSP200_LPCSUSYPAT_RECO_SumJetMass_AnalysisTree.root",
	     TString bkgFileName = "QCD_condorSub/QCDsample_LPCSUSYPAT_ALL_SumJetMass_AnalysisTree.root",//"QCD_condorSub/QCDsample_LPCSUSYPAT_RECO_SumJetMass_AnalysisTree.root"
	     ){

  gROOT->ProcessLine(".L ~/tdrstyle.C");
  setTDRStyle();

  gROOT->ProcessLine(".L rocCurve.C++");

  TFile* sigFile = new TFile(sigFileName);  
  TFile* bkgFile = new TFile(bkgFileName);

  ROCplotter* myROC = new ROCplotter((TTree*)sigFile->Get("TreeFiller/AnalysisTree"),(TTree*)bkgFile->Get("TreeFiller/AnalysisTree"));

  TGraph* sjm = myROC.make("sumJetMass_pt50",
			   100,0.,1500.,
			   4,2,2,
			   "(nJets_pt50>3)*eventWeight");

  TGraph* ht = myROC.make("Ht_pt50",
			  100,0.,2500.,
			  1,1,2,
			  "(nJets_pt50>3)*eventWeight");

  TCanvas* can = new TCanvas("can","can",500,500);

  ht->Draw("AC");
  sjm->Draw("same");    
  
}
