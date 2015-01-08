// -*- C++ -*-
//
// Package:    SuSySubstructure
// Class:      sumJetMassProducer
// 
/*

 Description: Takes as cfg input a jet collection 
 and clusters the jets into large-R anti-kt jets.
 A collection of 4-vectors corresponding to these 
 jets is saved to the event.

*/
//
// Original Author:  Andrew Whitbeck
//         Created:  Wed March 7, 2014
// 

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "AWhitbeck/SuSySubstructure/interface/sumJetMassProducer.h"

#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>

#include <vector>

sumJetMassProducer::sumJetMassProducer(const edm::ParameterSet& iConfig):
  jetCollection(iConfig.getUntrackedParameter<std::string>("jetCollection","patJetsAK5PFPt30")),
  ptCut(iConfig.getUntrackedParameter<double>("ptCut",50.)),
  debug(iConfig.getUntrackedParameter<bool>("debug",true))
{
  produces< double >("");
}


sumJetMassProducer::~sumJetMassProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
sumJetMassProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // fill histograms for di-lepton system

  using namespace edm;

  // get jet collection
  Handle< View<reco::Candidate> > jetCands;
  iEvent.getByLabel(jetCollection,jetCands);

  std::auto_ptr< double > sumJetMass ( new double (0.0) );

  if( debug ){
    std::cout << "new events" << std::endl;
    std::cout << "===================" << std::endl;
  }

  for(View<reco::Candidate>::const_iterator iJet = jetCands->begin(); iJet != jetCands->end(); ++iJet){
      
    if( debug ) {
	       std::cout << "input jets p_{mu}: " 
		      << iJet->px() << " " 
		      << iJet->py() << " " 
		      << iJet->pz() << " " 
		      << iJet->energy() << std::endl;
    }// end debug
    if( iJet->pt() > ptCut )
      *sumJetMass += iJet->mass();
     

  }// end loop over jets

  iEvent.put(sumJetMass);
 
}


// ------------ method called once each job just before starting event loop  ------------
void 

sumJetMassProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
sumJetMassProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
sumJetMassProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
sumJetMassProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
sumJetMassProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
sumJetMassProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
sumJetMassProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  /*
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
  */

}


#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(sumJetMassProducer);
