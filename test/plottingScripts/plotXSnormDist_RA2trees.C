#include "stackedBackground.C"
#include "TFile.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "TROOT.h"

void plotXSnormDist(char* drawVar = "MHT", 
		    char* cutString = "HT>500&&NJets>=3&&NJets<=999&&DeltaPhi1>.5&&DeltaPhi2>.5&&DeltaPhi3>.3&&JetsPt[0]>75&&JetsPt[1]>75", 
		    int nBins = 40,
		    double lowBin = 0, 
		    double highBin = 1000,
		    int mLSP = 125){
	

  gROOT->ProcessLine(".L ~/tdrstyle.C");
  gROOT->ProcessLine("setTDRStyle()");

	const int nGluino = 7 ; 

	vector< TString > fileName;
	vector< TH1F* > sig;
	//vector< TChain* > tree;
	int color[nGluino] = { kRed-2, kRed , kOrange , kOrange+1 , kMagenta , kMagenta+1 } ;
	double xs[nGluino] = { 0.157399 , 0.060276 , 0.0243547 , 0.0101744 , 0.00440078 , 0.00194443 , 0.000871201} ;
	int mGluino[nGluino] = { 825 , 925 , 1025 , 1100 , 1200 , 1300 , 1400 } ;

	fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root");
	fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_25to550_8TeV.root");
	fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_25to500_8TeV.root");
	fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_525to875_8TeV.root");
	ileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV.root");
	fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_525to1000_8TeV_V2.root");
	fileName.push_back("~/eos/SuSySubstructureAnalysisNtuples_V5/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV.root");

	char treeName[256];
	char histName[256];

	for( int iGluino = 0 ; iGluino < nGluino ; iGluino++ ){

		cout << "iGluino: " << iGluino << endl;

		sprintf(treeName,"massMom%i_massDau%i",mGluino[iGluino] ,mLSP);
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
			assert(0);
		}

		cout << tree << endl;

		tree->SetAlias("dPhiRaw","JetsPhi[0]-JetsPhi[1]");
		tree->SetAlias("dPhi","(dPhiRaw<-3.1415)*(dPhiRaw+2*3.1415)+(dPhiRaw>3.1415)*(dPhiRaw-2*3.1415)+(dPhiRaw<=3.1415&&dPhiRaw>=-3.1415)*(dPhiRaw)");

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
	sprintf(legTitle,"T1tttt (mLSP=%i GeV)",mLSP) ;
	TLegend* leg = new TLegend(.6,.9,.95,.4,legTitle);
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
