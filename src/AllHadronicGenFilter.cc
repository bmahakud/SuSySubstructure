// -*- C++ -*-
//
// Package:    AllHadronicGenFilter
// Class:      AllHadronicGenFilter
// 
/**\class AllHadronicGenFilter AllHadronicGenFilter.cc 

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Andrew Whitbeck
//         Created:  Wed Oct 16 10:10:37 CDT 2013
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TH1.h"
#include "TH2.h"
#include "TLorentzVector.h"
#include "TTree.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>

#include <fastjet/ClusterSequence.hh>
#include <fastjet/PseudoJet.hh>
#include <fastjet/JetDefinition.hh>

#include <vector>



class AllHadronicGenFilter : public edm::EDFilter {

public:
  explicit AllHadronicGenFilter(const edm::ParameterSet&);
  ~AllHadronicGenFilter();
  
private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  // ---------- configurable data ----------------
  // --------------- members ---------------------
  
  bool debug;                  

};


AllHadronicGenFilter::AllHadronicGenFilter(const edm::ParameterSet& iConfig):
  debug(iConfig.getUntrackedParameter<bool>("debug",false))
{

}


AllHadronicGenFilter::~AllHadronicGenFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
bool
AllHadronicGenFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // fill histograms for di-lepton system

  using namespace edm;

  Handle< View<reco::GenParticle> > genCands;
  iEvent.getByLabel("genParticles",genCands);

  if(debug)
    std::cout << "New Event" << std::endl;
  
  for(View<reco::GenParticle>::const_iterator iCand = genCands->begin();
      iCand != genCands->end();
      ++iCand){

    if ( abs(iCand->pdgId()) == 6 ) {
      
      // find which top daughter is the 
      int bosonicDaughter;
    
      if ( abs(iCand->daughter(0)->pdgId()) == 24 ) bosonicDaughter = 0;
      else if ( abs(iCand->daughter(1)->pdgId()) == 24 ) bosonicDaughter = 1;
      else continue;
        
      if(debug){
	std::cout << "top quark found: " << std::endl;
	std::cout << "        W decay: " 
		  << iCand->daughter(bosonicDaughter)->daughter(0)->pdgId() 
		  << ", " 
		  << iCand->daughter(bosonicDaughter)->daughter(1)->pdgId() 
		  << std::endl;
      }

      // check for leptonic W decay
      if( abs(iCand->daughter(bosonicDaughter)->daughter(0)->pdgId()) > 6 ) return false; 

    }

  }

  return true;

}


// ------------ method called once each job just before starting event loop  ------------
void 

AllHadronicGenFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
AllHadronicGenFilter::endJob() 
{
}


//define this as a plug-in
DEFINE_FWK_MODULE(AllHadronicGenFilter);
