#include <vector>

double computeEff(TTree* tree , double PT1, double PT2, double MHT , double dPhi , double HT ){

  double baseline = tree->Draw("JetsPt[0]","HT>500&&MHT>200&&NJets>=3&&DeltaPhi1>.5&&DeltaPhi2>.5&&DeltaPhi3>.3");
  char cutString[256];
  sprintf(cutString,"HT>%f&&MHT>%f&&NJets>=3&&DeltaPhi1>.5&&DeltaPhi2>.5&&DeltaPhi3>.3&&JetsPt[0]>%f&&JetsPt[1]>%f&&dPhi<%f",HT,MHT,PT1,PT2,dPhi);
  double withPtCuts = tree->Draw("JetsPt[0]",cutString);

  cout << "relative efficiency: " << withPtCuts / baseline << endl;

  return withPtCuts/baseline ;

}

void setAlias( TTree* tree ){

  tree->SetAlias("dPhiRaw","JetsPhi[0]-JetsPhi[1]");
  tree->SetAlias("dPhi","(dPhiRaw<-3.1415)*(dPhiRaw+2*3.1415)+(dPhiRaw>3.1415)*(dPhiRaw-2*3.1415)+(dPhiRaw<=3.1415&&dPhiRaw>=-3.1415)*(dPhiRaw)");

}

void scanEfficiencies( double PT1 = 75. , double PT2 = 75. , double MHT = 200 , double dPhi = 3.3 , double HT = 550. ){

  gROOT->ProcessLine(".L ~/tdrstyle.C");
  setTDRStyle();

  vector<TString> fileName ; 

  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_25to550_8TeV.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_25to500_8TeV.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_525to875_8TeV.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_525to1000_8TeV_V2.root");
  fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV.root");
  

  char treeName[256];
  
  TFile* file;
  TTree* tree;

  TH2F* effHisto = new TH2F("effHisto","effHisto",22,375,1425,28,12.5,1212.5);

  for( int mGluino = 400 ; mGluino <= 700 ; mGluino+=100){
    file = new TFile( fileName[0] , "READ" ) ;
    for( int mLSP = 25 ; mLSP <= mGluino-200 ; mLSP+=50 ){
      sprintf(treeName,"massMom%i_massDau%i",mGluino ,mLSP);
      cout << treeName << endl;
      tree = (TTree*) file->Get(treeName) ; 
      if( tree == NULL ) continue;
      setAlias(tree);
      effHisto->SetBinContent( effHisto.FindBin(mGluino,mLSP) , computeEff(tree,PT1,PT2,MHT,dPhi,HT) ) ;
    }
    file->Close();
    delete file;

  }
  
  for( int mGluino = 775 ; mGluino <= 1075 ; mGluino+=100){
    
    file = new TFile( fileName[1] , "READ" ) ;
    for( int mLSP = 25 ; mLSP <= 500 ; mLSP+=50 ){
      sprintf(treeName,"massMom%i_massDau%i",mGluino ,mLSP);
      cout << treeName << endl;
      tree = (TTree*) file->Get(treeName) ; 
      if( tree == NULL ) continue;
      setAlias(tree);
      cout << "gluino: " << mGluino << "LSP: " << mLSP << endl;
      effHisto->SetBinContent( effHisto.FindBin(mGluino,mLSP) , computeEff(tree,PT1,PT2,MHT,dPhi,HT) ) ;
    }
    file->Close();
    delete file;

    file = new TFile( fileName[2] , "READ" ) ;
    for( int mLSP = 525 ; mLSP <= 875 ; mLSP+=50 ){
      sprintf(treeName,"massMom%i_massDau%i",mGluino ,mLSP);
      cout << treeName << endl;
      tree = (TTree*) file->Get(treeName) ;
      if( tree == NULL ) continue;
      cout << tree->GetEntries() << endl;
      setAlias(tree);
      cout << "gluino: " << mGluino << "LSP: " << mLSP << endl;
      effHisto->SetBinContent( effHisto.FindBin(mGluino,mLSP) , computeEff(tree,PT1,PT2,MHT,dPhi,HT) ) ;
    }
    file->Close();
    delete file;

  }

  for( int mGluino = 1100 ; mGluino <= 1400 ; mGluino+=100){

    file = new TFile( fileName[3] , "READ" ) ;
    for( int mLSP = 25 ; mLSP <= 500 ; mLSP+=50 ){
      sprintf(treeName,"massMom%i_massDau%i",mGluino ,mLSP);
      cout << treeName << endl;
      tree = (TTree*) file->Get(treeName) ; 
      if( tree == NULL ) continue;
      setAlias(tree);
      cout << "gluino: " << mGluino << "LSP: " << mLSP << endl;
      effHisto->SetBinContent( effHisto.FindBin(mGluino,mLSP) , computeEff(tree,PT1,PT2,MHT,dPhi,HT) ) ;
    }
    file->Close();
    delete file;

    file = new TFile( fileName[4] , "READ" ) ;
    for( int mLSP = 525 ; mLSP <= 1000 ; mLSP+=50 ){
      sprintf(treeName,"massMom%i_massDau%i",mGluino ,mLSP);
      cout << treeName << endl;
      tree = (TTree*) file->Get(treeName) ; 
      if( tree == NULL ) continue;
      setAlias(tree);
      cout << "gluino: " << mGluino << "LSP: " << mLSP << endl;
      effHisto->SetBinContent( effHisto.FindBin(mGluino,mLSP) , computeEff(tree,PT1,PT2,MHT,dPhi,HT) ) ;
    }
    file->Close();
    delete file;

    file = new TFile( fileName[5] , "READ" ) ;
    for( int mLSP = 1025 ; mLSP <= 1200 ; mLSP+=50 ){
      sprintf(treeName,"massMom%i_massDau%i",mGluino ,mLSP);
      cout << treeName << endl;
      tree = (TTree*) file->Get(treeName) ; 
      if( tree == NULL ) continue;
      setAlias(tree);
      cout << "gluino: " << mGluino << "LSP: " << mLSP << endl;
      effHisto->SetBinContent( effHisto.FindBin(mGluino,mLSP) , computeEff(tree,PT1,PT2,MHT,dPhi,HT) ) ;
    }
    file->Close();
    delete file;

  }

  TCanvas* c = new TCanvas("c","c",600,600);

  //c->SetCanvasSize(500,540);

  c->SetMargin(0.15,.15,0.15,0.05);

  //TPaletteAxis* palette = (TPaletteAxis*) effHisto->GetListOfFunctions()->FindObject("palette");

  //palette->SetX1NDC(0.86);
  //palette->SetX2NDC(0.91);
  //palette->SetY2NDC(0.95);
  //palette->SetY1NDC(0.15);

  effHisto->GetXaxis()->SetTitle("m_{gluino}");
  effHisto->GetYaxis()->SetTitle("m_{LSP}");
  effHisto->GetZaxis()->SetRangeUser(0.,1.);
  
  effHisto->Draw("colz");

}
