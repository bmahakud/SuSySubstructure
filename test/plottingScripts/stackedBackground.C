#include <vector>
#include "TChain.h"
#include "TH1F.h"
#include "THStack.h"
#include "TString.h"
#include "TDirectory.h"
#include <iostream>
#include <vector>

THStack* stackedBackground(char* darVar = "MET",
			   char* cutString = "HT>500&&MHT>200&&NJets>2",
			   int binning = 20 , 
			   double lowBin = 0 , 
			   double highBin = 4500 
			   ){
	
	char drawString[256] ; 
	char getString[256] ;
	vector< TChain* > trees;
	vector< TH1F* > histo;

	const int nBkgSamples = 5 ; 

	int color[ nBkgSamples ] = { kGray+1 , kBlue+1 , kBlue-7, kCyan+1 , kGreen-3 } ;
	double weight[ nBkgSamples ] = { 0.307 , 5.582 , 0.122 , 0.125 , 0.082 } ;

	TString	backgroundFileNames[ nBkgSamples ] = {"/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V7/QCD_1000HTinf_LPCSUSYPAT_SLIM_*_SumJetMass_AnalysisTree.root" , 
						      "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V7/QCD_500HT1000_LPCSUSYPAT_SLIM_*_SumJetMass_AnalysisTree.root" , 
						      "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V7/WJetsToLNu_400HTInf_v2_LPCSUSYPAT_SLIM_*_SumJetMass_AnalysisTree.root" , 
						      "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V7/ZJetsToNuNu_400HTinf_LPCSUSYPAT_SLIM_*_SumJetMass_AnalysisTree.root" , 
						      "/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V7/TTJets_SemiLeptMGDecays_LPCSUSYPAT_SLIM_*_SumJetMass_AnalysisTree.root" } ; 
	
	for( int iSample = 0 ; iSample < nBkgSamples ; iSample++ ){

		trees.push_back( new TChain("TreeFiller/AnalysisTree" ) ) ;
		trees[ iSample ]->Add( backgroundFileNames[ iSample ] ) ;

		trees[ iSample ]->SetAlias("JetsPt","pt_patJetsAK5PFPt50Eta25") ; 
		trees[ iSample ]->SetAlias("JetsEta","eta_patJetsAK5PFPt50Eta25") ; 
		trees[ iSample ]->SetAlias("JetsPhi","phi_patJetsAK5PFPt50Eta25") ; 
		trees[ iSample ]->SetAlias("dPhiRaw","JetsPhi[0]-JetsPhi[1]");
		trees[ iSample ]->SetAlias("dPhi","(dPhiRaw<-3.1415)*(dPhiRaw+2*3.1415)+(dPhiRaw>3.1415)*(dPhiRaw-2*3.1415)+(dPhiRaw<=3.1415&&dPhiRaw>=-3.1415)*(dPhiRaw)");		
		trees[ iSample ]->SetAlias("dPhiRaw","JetsPhi[0] - JetsPhi[1]") ; 
		trees[ iSample ]->SetAlias("HT","HT_patJetsAK5PFPt50Eta25") ; 
		trees[ iSample ]->SetAlias("MHT","MHT_patJetsAK5PFPt30") ; 
		trees[ iSample ]->SetAlias("NJets","NJets_patJetsAK5PFPt50Eta25") ; 
		trees[ iSample ]->SetAlias("sumJetMass","sumJetMass_fattenedJets") ; 
		trees[ iSample ]->SetAlias("DeltaPhi1","abs(JetsPhi[0]-MHTphi_patJetsAK5PFPt30)");
		trees[ iSample ]->SetAlias("DeltaPhi2","abs(JetsPhi[1]-MHTphi_patJetsAK5PFPt30)");
		trees[ iSample ]->SetAlias("DeltaPhi3","abs(JetsPhi[2]-MHTphi_patJetsAK5PFPt30)");

		sprintf(drawString,"%s>>histo_%i(%i,%f,%f)",darVar,iSample,binning,lowBin,highBin) ;
		 
		sprintf(getString,"histo_%i",iSample) ;

		cout << drawString << endl;
		cout << cutString << endl;

		cout << trees[ iSample ]->Draw(drawString,cutString) <<endl ;
		histo.push_back( (TH1F*) gDirectory->Get( getString ) ) ;
		histo[ iSample ]->Scale( weight[ iSample ] ) ;
		histo[ iSample ]->SetFillColor( color[ iSample ] ) ;
		histo[ iSample ]->GetYaxis()->SetRangeUser(0.1,10000) ;

	}

	cout << "stack test" << endl;

	THStack* stack = new THStack() ;
	
	for( int iSample = 0 ; iSample < nBkgSamples ; iSample++ ){

		stack->Add( histo[ iSample ] ) ;

	}

	return stack ;

}
