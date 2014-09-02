#include "TH1.h"
#include "TGraph.h"
#include "TTree.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TString.h"
#include "TDirectory.h"

#include <vector>
#include <iostream>

using namespace std;

class ROCplotter {

private:

  TTree* SIGtree, *BKGtree;
  vector<TString> branchName;
  vector<int> bins;
  vector<double> start;
  vector<double> end;
  
  vector<int> lineColor;
  vector<int> lineStyle;
  vector<int> lineWidth;


  vector<TGraph*> ROC;

public:

  vector<TH1F*> SIGhisto;
  vector<TH1F*> BKGhisto;
  
  ROCplotter(TString sigFileName, 
	     TString bkgFileName,
	     TString sigTreeName="SelectedTree", 
	     TString bkgTreeName="SelectedTree"
	     ){

    TFile* sigFile = new TFile(sigFileName);
    SIGtree = (TTree*) sigFile->Get(sigTreeName);
    
    TFile* bkgFile = new TFile(bkgFileName);
    BKGtree = (TTree*) bkgFile->Get(bkgTreeName);

  }

  ROCplotter(TTree* sigTree = NULL , 
	     TTree* bkgTree = NULL ){

    SIGtree = sigTree;
    BKGtree = bkgTree;

  }


  ~ROCplotter(){

    delete SIGtree;
    delete BKGtree;
    
    for( int i = 0 ; i < SIGhisto.size() ; i++ ){

      delete SIGhisto[i];
      delete BKGhisto[i];
      
      delete ROC[i];

    }

  }

  TGraph* make(TH1F* SIGhisto_, TH1F* BKGhisto_,
	       int lineColor_=1, int lineStyle_=1, int lineWidth_=2){

    int bins_ = SIGhisto_->GetNbinsX();

    branchName.push_back( "" );
    bins.push_back      ( bins_ );
    start.push_back     ( -99 );
    end.push_back       ( -99 );
    lineColor.push_back (lineColor_ );
    lineStyle.push_back (lineStyle_ );
    lineWidth.push_back (lineWidth_ );

    double effSIG[bins_],effBKG[bins_];

    for(int i=0; i<bins_; i++){

      effSIG[i] = SIGhisto_->Integral(i, bins_+1);
      effBKG[i] = BKGhisto_->Integral(i, bins_+1);

    }

    cout << "making ROC curve" << endl;
    
    TGraph* ROC_ = new TGraph(bins_,effSIG,effBKG) ;

    ROC_->SetLineColor(lineColor_);
    ROC_->SetLineStyle(lineStyle_);
    ROC_->SetLineWidth(lineWidth_);
    ROC_->GetXaxis()->SetTitle("#epsilon_{SIG}");
    ROC_->GetYaxis()->SetTitle("#epsilon_{BKG}");

    ROC.push_back(ROC_);

    return ROC_;    

  }

  TGraph* make(TString branchName_="ZZpseudoLD",
	       const int bins_=30, double start_=0., double end_=1.,
	       int lineColor_=1, int lineStyle_=1, int lineWidth_=2,
	       TString cutString=""
	       ){

    branchName.push_back(branchName_);
    bins.push_back      (bins_      );
    start.push_back     (start_     ); 
    end.push_back       (end_       );
    lineColor.push_back (lineColor_ );
    lineStyle.push_back (lineStyle_ );
    lineWidth.push_back (lineWidth_ );

    /*
    if( SIGtree->GetBranch(branchName_ ) == NULL ){
	  cout << "ERROR ROCplotter::make() - signal tree does not have the branch you want..." << endl;
	  return 0;
	}
    if( BKGtree->GetBranch(branchName_ ) == NULL ){
      cout << "ERROR ROCplotter::make() - background tree does not have the branch you want..." << endl;
      return 0;
    }
    */

    char drawString[150];
    
    sprintf(drawString,"%s>>SIGhisto(%i,%f,%f)",branchName_.Data(),bins_,start_,end_);
    SIGtree->Draw(drawString,cutString);
    
    sprintf(drawString,"%s>>BKGhisto(%i,%f,%f)",branchName_.Data(),bins_,start_,end_);
    BKGtree->Draw(drawString,cutString);
    
    cout << "making histograms" << endl;

    TH1F* SIGhisto_ = (TH1F*) gDirectory->Get("SIGhisto");
    cout << SIGhisto_ << endl;
	
    SIGhisto_->Scale(1/SIGhisto_->Integral(0,SIGhisto_->GetNbinsX()+1));
    SIGhisto.push_back( SIGhisto_ );

    TH1F* BKGhisto_ = (TH1F*) gDirectory->Get("BKGhisto");
    BKGhisto_->Scale(1/BKGhisto_->Integral(0,BKGhisto_->GetNbinsX()+1));
    BKGhisto.push_back( BKGhisto_ );

    SIGhisto_->Draw();
    BKGhisto_->Draw("SAME");

    cout << "calculating efficiencies" << endl;

    double effSIG[bins_],effBKG[bins_];

    for(int i=0; i<bins_; i++){

      effSIG[i] = SIGhisto_->Integral(i, bins_+1);
      effBKG[i] = BKGhisto_->Integral(i, bins_+1);

    }

    cout << "making ROC curve" << endl;
    
    TGraph* ROC_ = new TGraph(bins_,effSIG,effBKG) ;

    ROC_->SetLineColor(lineColor_);
    ROC_->SetLineStyle(lineStyle_);
    ROC_->SetLineWidth(lineWidth_);
    ROC_->GetXaxis()->SetTitle("#epsilon_{SIG}");
    ROC_->GetYaxis()->SetTitle("#epsilon_{BKG}");

    ROC.push_back(ROC_);

    return ROC_;
    
  }  
  
  /*
  TH1F* fillHisto(TTree* tree,
		  const int bins_,
		  const double start_,
		  const double end_
		  ){

    TH1F* histo;
    
    
    
    tree->Set

    for ( int iEvt ; 
	  iEvt < tree->GetEntries  ;
	  iEvt++){

      histo
      
    }



  }
  */

};
