#include "rocCurve.C"
#include "stackedBackground.C"

TGraph*  ROCwithStackedBkg(int mGluino=1025, int mLSP=25){

  THStack* bkgHist = stackedBackground("abs(dPhi)","HT>500&&MHT>200&&NJets>=3",18,0,3.1415);
  
  vector<TString> fileName;
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_25to550_8TeV.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_25to500_8TeV.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_525to875_8TeV.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_525to1000_8TeV_V2.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV.root");
  
  char treeName[256];
  char histName[256];
  
  sprintf(treeName,"massMom%i_massDau%i",mGluino ,mLSP);
  cout << treeName << endl;
  
  TFile* file;
  TTree* tree;
  
  for( unsigned int iFile = 0 ; iFile < fileName.size() ; iFile++ ){
    
    file = new TFile(fileName[iFile] , "READ" ) ;
    tree = (TTree*) file->Get(treeName);
    if ( tree != NULL )
      break;
    
  }
  
  if (tree == NULL){
    cout << "didn't find gluino!" << endl;
    file->Close();
    delete file;
    return 0; 
  }
  
  tree->SetAlias("dPhiRaw","JetsPhi[0]-JetsPhi[1]");
  tree->SetAlias("dPhi","(dPhiRaw<-3.1415)*(dPhiRaw+2*3.1415)+(dPhiRaw>3.1415)*(dPhiRaw-2*3.1415)+(dPhiRaw<=3.1415&&dPhiRaw>=-3.1415)*(dPhiRaw)");

  tree->Draw("abs(dPhi)>>sigHist(18,0,3.1415)","HT>500&&MHT>200&&NJets>=3&&DeltaPhi1>.5&&DeltaPhi2>.5&&DeltaPhi3>.3");
  TH1F* sigHist = (TH1F*) gDirectory->Get("sigHist");

  sigHist->Scale(1./sigHist->Integral());

  TList *histos = bkgHist->GetHists();
  TH1F *sum = new TH1F("sum","sum of histograms",18,0,3.1415);
  TIter next(histos);
  TH1F *hist;
  while ((hist =(TH1F*)next())) {
    sum->Add(hist);
  }

  sum->Scale(1./sum->Integral());

  ROCplotter* myROC = new ROCplotter();
  TGraph* ROC = myROC->make(sigHist,sum,1,1,2);
  ROC->GetXaxis()->SetRangeUser(0,1);
  ROC->GetYaxis()->SetRangeUser(0,1);

  file->Close();
  delete file;

  return ROC;

}
