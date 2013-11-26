#include "TString.h"
#include "TChain.h"
#include "TH1F.h"
#include "TLegend.h"

using namespace std;

TString dcache = "dcap://cmsgridftp.fnal.gov:24125/pnfs/fnal.gov/usr/cms/WAX/11/store/user/awhitbe1/" ; 

enum files { kQCD, kWjets, kZjets, kTop, kT1tttt, kNumFiles };

TString fileNames[kNumFiles] = {"QCD_SumJetsMass_AnalysisTree_ALL.root",    //QCD 
				"WJets_SumJetsMass_AnalysisTree_ALL.root",  //wjets 
				"ZJets_SumJetsMass_AnalysisTree_ALL.root",  //zjets 
				"Top_SumJetsMass_AnalysisTree_ALL.root",    //top   
				"T1tttt_SumJetMass_AnalysisTree.root"};     // T1tttt

TString sampleNames[kNumFiles] = {"QCD",       //QCD 
				  "WJets",     //wjets 
				  "ZJets",     //zjets 
				  "Top",       //top   
				  "T1tttt" };  // T1tttt

void plotDist(char* drawVar="nSubJets_pt50",char* binning="(10,0,10)"){

  gROOT->ProcessLine(".L ~/tdrstyle.C");
  setTDRStyle();

  // fill signal tree and draw
  ///////////////////////////////////////
  TChain* sigTree = new TChain("SumJetMassTreeFiller/GenJetTree");
  cout << sampleNames[ kT1tttt ] << " " << sigTree->Add( fileNames[ kT1tttt ] ) << endl;

  char drawString[150];
  sprintf(drawString,"%s>>sig%s",drawVar,binning);

  sigTree->Draw(drawString);

  TH1F* sig = (TH1F*) gDirectory->Get("sig");
  sig->SetLineWidth(2);
  sig->SetLineColor(kT1tttt+1);
  
  TLegend* leg = new TLegend(.9,.9,.7,.7);
  leg->SetFillColor(0);
  
  leg->AddEntry(sig,sampleNames[ kT1tttt ],"l");

  // Fill background tree and draw
  //////////////////////////////////////
  const int numBkg = 4;

  TChain* bkgTree[numBkg];
  TH1F* bkg[numBkg];
			
  for( unsigned int iBkg = 0 ; iBkg < numBkg ; iBkg++){
    
    bkgTree[iBkg] = new TChain("SumJetMassTreeFiller/GenJetTree");
    cout << sampleNames[ iBkg ] << " " << bkgTree[iBkg]->Add( fileNames[ iBkg ] ) << endl;

    sprintf(drawString,"%s>>bkg%i%s",drawVar,iBkg,binning);

    bkgTree[iBkg]->Draw(drawString);

    char histoName[150];
    sprintf(histoName,"bkg%i",iBkg);

    bkg[iBkg] = (TH1F*) gDirectory->Get(histoName);
    bkg[iBkg]->SetLineWidth(2);
    bkg[iBkg]->SetLineColor(iBkg+1);

    leg->AddEntry(bkg[iBkg],sampleNames[ iBkg ],"l");

  }

  sig->DrawNormalized();
  for( unsigned int iBkg = 0 ; iBkg < numBkg ; iBkg++){
    bkg[iBkg]->DrawNormalized("SAME");
  }


  leg->Draw();

}

