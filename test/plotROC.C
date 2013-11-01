


void plotROC(TString sigFileName = "T1tttt_SumJetMass_AnalysisTree.root",
	    TString bkgFileName = "Zjets_SumJetMass_AnalysisTree.root"){

  gROOT->ProcessLine(".L ~/tdrstyle.C");
  setTDRStyle();

  gROOT->ProcessLine(".L rocCurve.C+");

  TFile* sigFile = new TFile(sigFileName);  
  TFile* bkgFile = new TFile(bkgFileName);

  ROCplotter myROC((TTree*)sigFile->Get("SumJetMassTreeFiller/GenJetTree"),(TTree*)bkgFile->Get("SumJetMassTreeFiller/GenJetTree"));

  TGraph* ht = myROC.make("Ht_pt50",
			  500,0.,4500.,
			  1,1,2,
			  "nJets_pt50>3&&Ht_pt50>500");
			  
  TGraph* sjm = myROC.make("sumJetMass_pt50",
			   500,0.,2000.,
			   4,2,2,
			   "nJets_pt50>3&&Ht_pt50>500");

  ht->Draw("AC");
  sjm->Draw("same");    

}
