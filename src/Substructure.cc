// -*- C++ -*-
//
// Package:    SuSySubstructure
// Class:      SuSySubstructure
// 
/**\class Substructure Substructure.cc

 Description: Takes as cfg input a jet collection and
 a collection of PFCandidates.  PFCandidates within 
 each jet radius are reclustered for calculating 
 substructure variables. 

*/
//
// Original Author:  Andrew Whitbeck
//         Created:  Wed Dec 5, 2013
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TH1.h"
#include "TH2.h"
#include "TLorentzVector.h"
#include "TTree.h"

#include <DataFormats/PatCandidates/interface/Jet.h>
#include <DataFormats/PatCandidates/interface/Muon.h>
#include <DataFormats/PatCandidates/interface/CompositeCandidate.h>
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>

#include <fastjet/ClusterSequence.hh>
#include <fastjet/PseudoJet.hh>
#include <fastjet/JetDefinition.hh>

#include "SubjetCounting.hh"

#include <vector>


class Substructure : public edm::EDProducer {

public:
  explicit Substructure(const edm::ParameterSet&);
  ~Substructure();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  
  // ----------member data ---------------------------


  // ---------- configurable data ----------------
  // --------------- members ---------------------
  
  std::string jetCollection;    // name of jet collection
  std::string PFCandCollection; // name of PFCand collection
  double      clusterRadius;    // jet clustering radius
  bool        debug;
};


Substructure::Substructure(const edm::ParameterSet& iConfig):
  jetCollection(iConfig.getUntrackedParameter<std::string>("jetCollection","ak1p2GenJets")),
  PFCandCollection(iConfig.getUntrackedParameter<std::string>("PFCandCollection","genParticlesForJetsNoNu")),
  clusterRadius(iConfig.getUntrackedParameter<double>("clusterRadius",1.2)),
  debug(iConfig.getUntrackedParameter<bool>("debug",true))
{
  produces<double>(jetCollection+"nSubJets");
  produces<double>(jetCollection+"nSubJetsTEST");
  produces<double>(jetCollection+"sumJetMass");
  produces<double>(jetCollection+"sumJetMassTEST");
}


Substructure::~Substructure()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
Substructure::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // fill histograms for di-lepton system

  using namespace edm;

  Handle< View<reco::GenJet> > jetCands;
  iEvent.getByLabel(jetCollection,jetCands);

  Handle< View<reco::GenParticle> > PFCands;
  iEvent.getByLabel(PFCandCollection,PFCands);

  // get particles to cluster
  std::vector<fastjet::PseudoJet> constituents;      

  for(View<reco::GenParticle>::const_iterator iPFCand = PFCands->begin();
      iPFCand != PFCands->end();
      ++iPFCand){

    if( fabs( iPFCand->eta() ) > 5.0 ) continue;
	
    constituents.push_back( fastjet::PseudoJet( iPFCand->px(), 
						iPFCand->py(),
						iPFCand->pz(),
						iPFCand->energy() ) );
    
  }// end loop of PF candidates

  // testing .....

  std::vector<fastjet::PseudoJet> fatJets;

  fastjet::JetDefinition aktp12(fastjet::antikt_algorithm, clusterRadius);
  fastjet::ClusterSequence cs_aktp12(constituents, aktp12);
  fatJets = sorted_by_pt(cs_aktp12.inclusive_jets());

  for(View<reco::GenJet>::const_iterator iJet = jetCands->begin();
      iJet != jetCands->end();
      ++iJet){
   
    if( iJet->pt() > 20. )
      std::cout << "std jet pt: " << iJet->pt() << std::endl;
 
  }
  
  for(unsigned int iJet = 0 ; 
      iJet < fatJets.size();
      ++iJet){
   
    if( fatJets[iJet].pt() > 20. ) 
      std::cout << "hand jet pt: " << fatJets[iJet].pt() << std::endl;
 
  }  

  // ..... testing

  return; 
  
  // initialize object for counting subjets
  //               SubjetCountingCA(mass_cutoff,ycut,R_min,pt_cut);    
  fastjet::contrib::SubjetCountingCA subjetCounter_pt50(50.,0.15,0.15,50.);

  std::auto_ptr<double> sumJetMass ( new double(0.0) );
  std::auto_ptr<double> nSubJets   ( new double(0.0) );

  std::cout << "new events" << std::endl;
  std::cout << "===================" << std::endl;

  for(View<reco::GenJet>::const_iterator iJet = jetCands->begin();
      iJet != jetCands->end();
      ++iJet){

    std::vector<fastjet::PseudoJet> jetConst;    
    std::vector<fastjet::PseudoJet> fatJets;

    // kinematic selection for jets
    if ( iJet->pt() > 50. &&
	 fabs( iJet->eta() ) < 2.5 ){

      // recluster PFCandidates

      *sumJetMass = 0.0;
      *nSubJets   = 0.0;      

      // loop over all constituents
      for(unsigned int iConst = 0 ; 
	  iConst < constituents.size();
	  ++iConst){
	
	double dR = sqrt( 
			 pow( constituents[ iConst ].eta() - iJet->eta() , 2 ) + 
			 pow( constituents[ iConst ].phi() - iJet->phi() , 2 )
	                 );

	if( dR < 1.2 ){

	  jetConst.push_back( constituents[ iConst ] );
	  constituents.erase( constituents.begin() + iConst );

	} 

      }// end loop of PF candidates

      fastjet::JetDefinition aktp12(fastjet::antikt_algorithm, clusterRadius);
      fastjet::ClusterSequence cs_aktp12(jetConst, aktp12);
      fatJets = sorted_by_pt(cs_aktp12.inclusive_jets());

      if( fatJets.size() > 1 ) std::cout << "ERROR: " << fatJets.size() << " were clustered, but only 1 was expected. \n Only the first jet will be used." << std::endl;

      if( debug ){

	std::cout << "std Jet collection: " << iJet->pt() << std::endl;
	
	std::cout << "hand clustered jet: " << std::endl;
	for ( unsigned int k = 0 ; k < fatJets.size() ; k++){
	  std::cout << "pt: " << fatJets[ k ].pt() << std::endl;
	}
      }

      std::cout << "-----------------------" << std::endl;

      if( fatJets.size() > 0 ) {
	
	*sumJetMass += fatJets[ 0 ].m();
	*nSubJets   += subjetCounter_pt50.result( fatJets[ 0 ] );
      
      }

    }// end calculations for fat jets with pt > 50 GeV

  }// end loop over jets

  iEvent.put(sumJetMass, jetCollection+"sumJetMass" );
  iEvent.put(nSubJets,   jetCollection+"nSubJets"   );

}


// ------------ method called once each job just before starting event loop  ------------
void 

Substructure::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
Substructure::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
Substructure::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
Substructure::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
Substructure::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
Substructure::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
Substructure::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

}

//define this as a plug-in
DEFINE_FWK_MODULE(Substructure);
