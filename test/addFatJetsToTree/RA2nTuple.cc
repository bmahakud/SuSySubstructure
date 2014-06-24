#include "RA2nTuple.h"

RA2nTuple::RA2nTuple( TString FileName, TString TreeName ){
	
	tree = new TChain( TreeName ) ;
	tree->Add( FileName ) ; 

	initBranches();

}

void RA2nTuple::initBranches(){

	tree->SetBranchAddress( "RunNum" , &RunNum ) ;
	tree->SetBranchAddress( "LumiBlockNum" , &LumiBlockNum ) ;
	tree->SetBranchAddress( "EvtNum" , &EvtNum ) ;

	tree->SetBranchAddress( "NVtx" , &NVtx ) ;

	tree->SetBranchAddress( "HT" , &HT ) ;
	tree->SetBranchAddress( "MHT" , &MHT ) ;
	tree->SetBranchAddress( "NJets" , &NJets ) ;

	tree->SetBranchAddress( "Jet1Pt" , &Jet1Pt ) ;
	tree->SetBranchAddress( "Jet2Pt" , &Jet2Pt ) ;
	tree->SetBranchAddress( "Jet3Pt" , &Jet3Pt ) ;
	tree->SetBranchAddress( "Jet1Eta" , &Jet1Eta ) ;
	tree->SetBranchAddress( "Jet2Eta" , &Jet2Eta ) ;
	tree->SetBranchAddress( "Jet3Eta" , &Jet3Eta ) ;
	tree->SetBranchAddress( "DeltaPhi1" , &DeltaPhi1 ) ;
	tree->SetBranchAddress( "DeltaPhi2" , &DeltaPhi2 ) ;
	tree->SetBranchAddress( "DeltaPhi3" , &DeltaPhi3 ) ;
	tree->SetBranchAddress( "NumPUInteractions" , &NumPUInteractions ) ;
	tree->SetBranchAddress( "rho" , &rho ) ;

	//maxJetsNum = 100 ;

	tree->SetBranchAddress( "JetsNum" , &JetsNum ) ;
	tree->SetBranchAddress( "JetsPt" , JetsPt ) ;
	tree->SetBranchAddress( "JetsEta" , JetsEta ) ;
	tree->SetBranchAddress( "JetsPhi" , JetsPhi ) ;
	tree->SetBranchAddress( "JetsE" , JetsE ) ;

	tree->SetBranchAddress( "JetArea" , &JetArea ) ;
	tree->SetBranchAddress( "JetNeutHadF" , &JetNeutHadF ) ;
	tree->SetBranchAddress( "JetNeutEmF" , &JetNeutEmF ) ;
	tree->SetBranchAddress( "BTagCSV" , &BTagCSV ) ;

	tree->SetBranchAddress( "PATMuonsPFIDIsoNum" , &PATMuonsPFIDIsoNum ) ;
	tree->SetBranchAddress( "PATElectronsIDIsoNum" , &PATElectronsIDIsoNum ) ;
	tree->SetBranchAddress( "PATMETsPFNum" , &PATMETsPFNum ) ;
	tree->SetBranchAddress( "PATMETsPFPt" , &PATMETsPFPt ) ;
	tree->SetBranchAddress( "PATMETsPFEta" , &PATMETsPFEta ) ;
	tree->SetBranchAddress( "PATMETsPFPhi" , &PATMETsPFPhi ) ;
	tree->SetBranchAddress( "PATMETsPFE" , &PATMETsPFE ) ;

	tree->SetBranchAddress( "massMom" , &massMom ) ;
	tree->SetBranchAddress( "massDau" , &massDau ) ;
	tree->SetBranchAddress( "procID" , &procID ) ;

	tree->SetBranchAddress( "Filter_eeNoiseFilter" , &Filter_eeNoiseFilter ) ;
	tree->SetBranchAddress( "Filter_trackingFailureFilter" , &Filter_trackingFailureFilter ) ;
	tree->SetBranchAddress( "Filter_inconsistentMuons" , &Filter_inconsistentMuons ) ;
	tree->SetBranchAddress( "Filter_greedyMuons" , &Filter_greedyMuons ) ;
	tree->SetBranchAddress( "Filter_ra2EcalTPFilter" , &Filter_ra2EcalTPFilter ) ;
	tree->SetBranchAddress( "Filter_ra2EcalBEFilter" , &Filter_ra2EcalBEFilter ) ;
	tree->SetBranchAddress( "Filter_hcalLaserEventFilter" , &Filter_hcalLaserEventFilter ) ;
	tree->SetBranchAddress( "Filter_ecalLaserCorrFilter" , &Filter_ecalLaserCorrFilter ) ;
	tree->SetBranchAddress( "Filter_eeBadScFilter" , &Filter_eeBadScFilter ) ;
	tree->SetBranchAddress( "Filter_PBNRFilter" , &Filter_PBNRFilter ) ;

}

void RA2nTuple::addFile( TString FileName ){

	tree->Add( FileName ) ; 

}

void RA2nTuple::getEvent( unsigned int iEvt ){

	tree->GetEntry( iEvt ) ;

}	
	
int RA2nTuple::getEvents( ){

	return tree->GetEntries( ) ;

}	

