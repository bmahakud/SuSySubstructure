#include <vector>

TString dcache = "dcap://cmsgridftp.fnal.gov:24125/pnfs/fnal.gov/usr/cms/WAX/11/store/user/awhitbe1/" ; 

vector<TString> fileNames;


fileNames->push_back("");
fileNames->push_back("");
fileNames->push_back("");
fileNames->push_back("");


TString SigFiles = "RPVstop_SumJetMass_AnalysisTree.root" ; 

void plotDist(){

  gROOT->ProcessLine(".L ~/tdrstyle.C");
  setTDRStyle();

  TChain* sigTree = new TChain("SumJetMassTreeFiller/GenJetTree");
  cout << sigTree->Add(SigFiles) << endl;

  TChain* QCDTree = new TChain("SumJetMassTreeFiller/GenJetTree");
  cout << QCDTree->Add(dcache+QCDfiles) << endl;;
  //cout << QCDTree->GetEntries() << endl;

  TChain* QCDTree = new TChain("SumJetMassTreeFiller/GenJetTree");

  sigTree->Draw("sumJetMass_pt50>>sig");
  bkgTree->Draw("sumJetMass_pt50>>bkg","","SAME");

  TH1F* sig = (TH1F*) gDirectory->Get("sig");
  TH1F* bkg = (TH1F*) gDirectory->Get("bkg"); 

  bkg->DrawNormalized();
  sig->DrawNormalized("SAME");
  
}
