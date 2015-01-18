// -*- C++ -*-
//
// Package:    SuSySubstructure
// Class:      minDeltaPhiProducer
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

#include "AWhitbeck/SuSySubstructure/interface/minDeltaPhiProducer.h"

#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>

#include <vector>
#include "TMath.h"

minDeltaPhiProducer::minDeltaPhiProducer(const edm::ParameterSet& iConfig):
  jetCollection(iConfig.getUntrackedParameter<std::string>("jetCollection","randomString")),
  metCollection(iConfig.getUntrackedParameter<std::string>("metCollection","moreRandomString")),
  debug(iConfig.getUntrackedParameter<bool>("debug",true))
{
  produces< double >("");
  produces< std::vector<double> >("deltaPhiN");
}


minDeltaPhiProducer::~minDeltaPhiProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
minDeltaPhiProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // fill histograms for di-lepton system

  using namespace edm;

  // get jet collection
  Handle< View<reco::Candidate> > jetCands;
  iEvent.getByLabel(jetCollection,jetCands);

  // get met collection
  edm::Handle< edm::View<reco::MET> > MET;
  iEvent.getByLabel(metCollection,MET); 

  std::auto_ptr< std::vector<double> > deltaPhi ( new std::vector<double> () ) ;
  std::auto_ptr< double > minDeltaPhi ( new double (999999.999999) );

  int maxJets = 0 ;

  for(View<reco::Candidate>::const_iterator iJet = jetCands->begin(); iJet != jetCands->end(); ++iJet){

    if( debug ) {
	       std::cout << "input jets p_{mu}: " 
		      << iJet->px() << " " 
		      << iJet->py() << " " 
		      << iJet->pz() << " " 
		      << iJet->energy() << std::endl;
    }// end debug

    // = = = = = = = = = = = = = = = = = = = 
    // following code from by Jack B.F. 
    // https://github.com/jbradmil/csa14/blob/master/src/event_handler.cpp#L2849-L2893
    // = = = = = = = = = = = = = = = = = = = 
    // ================ compute DELTA-T =================
    double sum = 0.;
    deltaPhi->push_back(999999.999999);

    // loop of all other jets
    for(View<reco::Candidate>::const_iterator jJet = jetCands->begin(); jJet != jetCands->end(); ++jJet){

      if( iJet == jJet ) continue; 
      sum += pow( 0.1 * ( iJet->px() * jJet->py() - iJet->py() * jJet->px() ) , 2 ) ;

    }
    
    double deltaT = sqrt( sum ) / iJet->pt() ;
    
    if( debug ){
      std::cout << "deltaT: " << deltaT << std::endl;
      std::cout << "phi_i: " << iJet->phi() << std::endl;
      std::cout << "phi_MET: " << MET->at(0).phi() << std::endl;
      std::cout << "fabs( iJet->phi() - MET->at(0).phi() )" << fabs( iJet->phi() - MET->at(0).phi() ) << std::endl;
      std::cout << "fmod( fabs( iJet->phi() - MET->at(0).phi() ) + TMath::Pi() , 2.0 * TMath::Pi() ): " << fmod( fabs( iJet->phi() - MET->at(0).phi() ) + TMath::Pi() , 2.0 * TMath::Pi() ) << std::endl;
    }
    // compute deltaPhi-hat
    // dphi taken from: https://github.com/manuelfs/ucsb_code/blob/master/src/math.cpp
    double dphi = fabs( fmod( fabs( iJet->phi() - MET->at(0).phi() ) + TMath::Pi() , 2.0 * TMath::Pi() ) - TMath::Pi() ) ;

    if( debug ){
      std::cout << "dPhi: " << dphi << std::endl;
      std::cout << "MET: " << MET->at(0).pt() << std::endl;
      std::cout << "dT/MET: " << deltaT / MET->at(0).pt() << std::endl;
      std::cout << "asin(dT/MET): " << asin( deltaT / MET->at(0).pt() ) << std::endl;
    }

    if( deltaT / MET->at(0).pt() >= 1.0 ) dphi = dphi / ( TMath::Pi() / 2.0 );
    else dphi = dphi / asin( deltaT / MET->at(0).pt() ) ;

    if( debug ) 
      std::cout << "Normalized dPhi: " << dphi << std::endl;

    deltaPhi->push_back( dphi );

    // minimize...
    //if( dphi < deltaPhi->back() ) minDeltaPhi->back() = dphi ;
    if( dphi < *minDeltaPhi && maxJets < 3 ) *minDeltaPhi = dphi ;

    if( debug ){
      std::cout << "minDeltaPhi: " << *minDeltaPhi << std::endl;
      std::cout << "last deltaPhi: " << deltaPhi->back() << std::endl; 
    }

    maxJets ++;
      
  }// end loop over jets

  

  iEvent.put(minDeltaPhi);
  iEvent.put(deltaPhi,"deltaPhiN");
}


// ------------ method called once each job just before starting event loop  ------------
void 

minDeltaPhiProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
minDeltaPhiProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
minDeltaPhiProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
minDeltaPhiProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
minDeltaPhiProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
minDeltaPhiProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}


// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
minDeltaPhiProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  /*
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
  */

}


#include "FWCore/Framework/interface/MakerMacros.h"

//define this as a plug-in
DEFINE_FWK_MODULE(minDeltaPhiProducer);
