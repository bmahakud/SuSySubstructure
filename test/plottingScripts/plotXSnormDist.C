#include "stackedBackground.C"
#include "TFile.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TROOT.h"

void plotXSnormDist(char* drawVar = "MET", 
		    char* cutString = "HT>500&&NJets>=3&&NJets<=999&&DeltaPhi1>.5&&DeltaPhi2>.5&&DeltaPhi3>.3", 
		    int nBins = 40,
		    double lowBin = 0, 
		    double highBin = 1000
		    ){
	

  gROOT->ProcessLine(".L ~/tdrstyle.C");
  gROOT->ProcessLine("setTDRStyle()");

	const int nGluino = 1 ; 

	vector< TString > fileName;
	vector< TH1F* > sig;
	//vector< TChain* > tree;
	int color[nGluino] = { kRed-2 } ; //, kRed , kOrange , kOrange+1 , kMagenta , kMagenta+1 } ;
	//double xs[nGluino] = { 0.157399 , 0.060276 , 0.0243547 , 0.0101744 , 0.00440078 , 0.00194443 , 0.000871201} ;
	double xs[nGluino] = { 0.0101744 } ;
	//int mGluino[nGluino] = { 825 , 925 , 1025 , 1100 , 1200 , 1300 , 1400 } ;
	int mGluino[nGluino] = { 1100 } ;

	fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V7/SMS_T1tttt*root");

	char histName[256];

	for( int iGluino = 0 ; iGluino < nGluino ; iGluino++ ){

		cout << "iGluino: " << iGluino << endl;

		TChain* tree = new TChain("TreeFiller/AnalysisTree");
		tree->Add( fileName[ iGluino ] ) ;

		if ( tree->GetEntries() == 0 ){
			cout << "didn't find gluino files?!" << endl;
			assert(0);
		}

		cout << tree << endl;

		tree->SetAlias("JetsPt","pt_patJetsAK5PFPt50Eta25") ; 
		tree->SetAlias("JetsEta","eta_patJetsAK5PFPt50Eta25") ; 
		tree->SetAlias("JetsPhi","phi_patJetsAK5PFPt50Eta25") ; 

		tree->SetAlias("dPhiRaw","JetsPhi[0]-JetsPhi[1]");
		tree->SetAlias("dPhi","(dPhiRaw<-3.1415)*(dPhiRaw+2*3.1415)+(dPhiRaw>3.1415)*(dPhiRaw-2*3.1415)+(dPhiRaw<=3.1415&&dPhiRaw>=-3.1415)*(dPhiRaw)");

		tree->SetAlias("HT","HT_patJetsAK5PFPt50Eta25") ; 
		tree->SetAlias("MHT","MHT_patJetsAK5PFPt30") ; 
		tree->SetAlias("NJets","NJets_patJetsAK5PFPt50Eta25") ; 
		tree->SetAlias("sumJetMass","sumJetMass_fattenedJets") ; 
		tree->SetAlias("DeltaPhi1","abs(JetsPhi[0]-MHTphi_patJetsAK5PFPt30)");
		tree->SetAlias("DeltaPhi2","abs(JetsPhi[1]-MHTphi_patJetsAK5PFPt30)");
		tree->SetAlias("DeltaPhi3","abs(JetsPhi[2]-MHTphi_patJetsAK5PFPt30)");

		double noCuts = tree->Draw(drawVar,"") ;
		cout << "check" << endl;
		sprintf(histName,"%s>>sig_%i(%i,%f,%f)",drawVar,mGluino[iGluino],nBins,lowBin,highBin);
		double withCuts = tree->Draw(histName,cutString) ;
		cout << "check" << endl;

		sprintf(histName,"sig_%i",mGluino[iGluino]);
		cout << histName << endl;
		sig.push_back( (TH1F*) gDirectory->Get(histName) );

		sig[iGluino]->SetLineColor( color[iGluino] );
		sig[iGluino]->SetLineWidth( 2 ) ;
		cout << "xs: " << xs[iGluino] << endl;
		cout << "withCuts: " << withCuts << endl;
		cout << "nocuts: " << noCuts << endl;

		sig[iGluino]->Scale(19500*xs[iGluino]/noCuts) ;
		sig[iGluino]->GetXaxis()->SetTitle(drawVar);
		sig[iGluino]->GetYaxis()->SetTitle("Events");
		sig[iGluino]->GetYaxis()->SetRangeUser(0.1,100000);

	}

	cout << "test" << endl;

	TCanvas* can = new TCanvas("can","can",500,500);
	char legTitle[256];
	//legTitle="T1tttt (mLSP=25 GeV)" ;
	TLegend* leg = new TLegend(.6,.9,.95,.4,"T1tttt (mLSP=25 GeV)");
	leg->SetFillColor(0);
	leg->SetBorderSize(0);

	cout << "test" << endl;

	THStack* bkg = stackedBackground(drawVar,cutString,nBins,lowBin,highBin);

	cout << "bkg: " << bkg << endl;

	sig[0]->Draw();

	//bkg->GetXaxis()->SetTitle("MHT");
	//bkg->GetYaxis()->SetTitle("Events");
	//bkg->GetYaxis()->SetRangeUser(0.1,10000.);
	bkg->Draw("SAME");

	cout << "test" << endl;

	for( int iGluino = 0 ; iGluino<sig.size() ; iGluino++ ) {

		//if( iGluino == 0 )
			//sig[iGluino]->Draw();
		//else
	  sig[iGluino]->Draw("SAME");
	  sprintf(legTitle,"mGo=%i GeV",mGluino[iGluino]);
	  leg->AddEntry(sig[iGluino],legTitle,"l");

	}

	can->SetLogy();
	leg->Draw();

	char saveName[256];
	//sprintf(saveName,"bkgStack_sigScan_mLSP%i_HT.eps",mLSP);
	//can->SaveAs(saveName);

}	
