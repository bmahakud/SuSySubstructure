#ifndef __JetFattening__
#define __JetFattening__

/*

 Description: Calculates fat jets from ak5 std jets.  
 Users can either retrieve a vector of fat jet 4vec
 or simply the sum jet mass variable for a given set
 of input jets. 

*/
//
// Original Author:  Andrew Whitbeck
//         Created:  Thursday May 1, 2014
// 

#include "TTree.h"
#include "TLorentzVector.h"

#include <fastjet/ClusterSequence.hh>
#include <fastjet/PseudoJet.hh>
#include <fastjet/JetDefinition.hh>

#include <vector>

using namespace std;
using namespace fastjet;

vector< TLorentzVector > JetFattening( vector< TLorentzVector > jets , 
				       double clusterRadius = 1.2 ,
				       bool debug = false 
				       ){

  if( debug ) 
    cout << "JetFattening: begin" << endl;

  // initialize objects needed for fastjet 
  // -------------------------------------
  vector< PseudoJet > fatJets;
  vector< PseudoJet > constituents;      
  JetDefinition aktp12(antikt_algorithm, clusterRadius);  

  vector < TLorentzVector > fatJet4Vec_ ; 
  // -------------------------------------

  if( debug ){
    cout << "new events" << endl;
    cout << "===================" << endl;
  }

  for(unsigned int iJet = 0 ; iJet < jets.size() ; iJet++ ){
      
    if ( debug ) {

      cout << "std jet pt: " << jets[ iJet].Pt() << endl;

    }// end debug

    if ( jets[ iJet ].Pt() < 30.0 ) continue ;
    if ( fabs( jets[ iJet ].Eta() ) > 5.0 )  continue ;

    constituents.push_back( PseudoJet( jets[ iJet ].Px(),
				       jets[ iJet ].Py(),
				       jets[ iJet ].Pz(),
				       jets[ iJet ].E()
				       )
			    ) ; 

    if( debug ) {
	       cout << "input jets p_{mu}: " 
		      << jets[ iJet ].Px() << " " 
		      << jets[ iJet ].Py() << " " 
		      << jets[ iJet ].Pz() << " " 
		      << jets[ iJet ].E() << endl;
    }// end debug
     
  }// end loop over jets

  // recluster 
  ClusterSequence cs_aktp12(constituents, aktp12);
  fatJets = sorted_by_pt(cs_aktp12.inclusive_jets());
  
  if( debug ){
    
    cout << "hand clustered jet: " << endl;
    for ( unsigned int k = 0 ; k < fatJets.size() ; k++){
      cout << "pt: " << fatJets[ k ].pt() << endl;
    }
    cout << "-----------------------" << endl;
  }
  // ..............................
  
  
  // fill vector of XYZTLorentzVector for putting in event
  for( unsigned int iFatJet = 0 ; iFatJet < fatJets.size() ; iFatJet++ ){
    
    TLorentzVector p4( fatJets[iFatJet].px(), 
		       fatJets[iFatJet].py(), 
		       fatJets[iFatJet].pz(), 
		       fatJets[iFatJet].e() ) ;
    
    fatJet4Vec_.push_back( p4 ) ; 
    
  }// done filling XYZTLorentzVector vector
 
  if( debug ) 
    cout << "JetFattening: end" << endl;

  return fatJet4Vec_ ; 

}

double sumJetMass(vector< TLorentzVector > jets , 
               double clusterRadius = 1.2 ,
               bool debug = false ){

  vector< TLorentzVector > myFatJets = JetFattening( jets , clusterRadius , debug ) ;

  double SMJ = 0.0;

  for( unsigned int i = 0 ; i < myFatJets.size() ; i++){

    SMJ += myFatJets[i].M();

  }

  return SMJ ;

}

#endif
