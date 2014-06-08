#ifndef __RA2nTuple__
#define __RA2nTuple__

#include "TChain.h"	
#include "TString.h"
#include <iostream>
#include "TString.h"

using namespace std;

class RA2nTuple  {


public:
	
	TChain* tree;

	int	RunNum ; 
 	int LumiBlockNum ;
	int EvtNum ;

 	int NVtx ; 
 	
 	float HT ;
	float MHT ;
 	int NJets ;
 	
 	float Jet1Pt ;
 	float Jet2Pt ;
 	float Jet3Pt ;
 	float Jet1Eta ;  
 	float Jet2Eta ;
  	float Jet3Eta ;
	float DeltaPhi1 ;
	float DeltaPhi2 ;
	float DeltaPhi3 ;
	int NumPUInteractions ; 
	float rho ;

	int	JetsNum ;
 	float JetsPt[100] ;
	float JetsEta[100] ; 
	float JetsPhi[100] ; 
	float JetsE[100] ;

	float JetArea[100] ; 
	float JetNeutHadF[100] ;
	float JetNeutEmF[100] ; 
	float BTagCSV[100] ; 

	int PATMuonsPFIDIsoNum ;
	int PATElectronsIDIsoNum ;
 	int PATMETsPFNum ;
 	float PATMETsPFPt ;
 	float PATMETsPFEta ;
 	float PATMETsPFPhi ;
 	float PATMETsPFE ;

	int massMom ;
 	int massDau ;
 	int procID  ;

	int Filter_eeNoiseFilter ;
	int Filter_trackingFailureFilter ;
	int Filter_inconsistentMuons ;
	int Filter_greedyMuons ;
	int Filter_ra2EcalTPFilter ;
	int Filter_ra2EcalBEFilter ;
	int Filter_hcalLaserEventFilter ;
	int Filter_ecalLaserCorrFilter ;
	int Filter_eeBadScFilter ;
	int Filter_PBNRFilter ;

	RA2nTuple( TString FileName="" , TString TreeName="" ) ; 
	~RA2nTuple(){};

	void initBranches() ;
	void addFile( TString FileName ) ; 
	void getEvent( unsigned int iEvt ) ;
	int getEvents( ) ; 

};

#endif
