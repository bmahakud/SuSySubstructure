// -*- C++ -*-
//
// Package:    SuSySubstructure
// Class:      RA2TreeFiller
// 
/**\class RA2TreeFiller RA2TreeFiller.cc

 Description: 

*/
//
// Original Author:  Andrew Whitbeck
//         Created:  Tues June 24, 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TLorentzVector.h"
#include "TTree.h"    

#include <DataFormats/PatCandidates/interface/Jet.h>
#include <DataFormats/PatCandidates/interface/Muon.h>
#include <DataFormats/PatCandidates/interface/CompositeCandidate.h>
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>

#include <SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h>

#include <fastjet/ClusterSequence.hh>
#include <fastjet/PseudoJet.hh>
#include <fastjet/JetDefinition.hh>

#include "SubjetCounting.hh"

#include <vector>


class RA2TreeFiller : public edm::EDAnalyzer {

public:
  explicit RA2TreeFiller(const edm::ParameterSet&);
  ~RA2TreeFiller();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:

  // ----------member data ---------------------------
  
  TTree* AnalysisTree;

  int NJets;
  double sumJetMass;
  double MHT;
  double DeltaPhi1, DeltaPhi2, DeltaPhi3;
  double HT;

  // ---------- configurable data ----------------
  // --------------- members ---------------------
  
  std::string HTjetCollection;    // name of jet collection
  std::string MHTjetCollection;    // name of jet collection
  std::string pseudoParticleCollection;    // name of jet collection
  bool debug;

  // ---------- private methods! -----------

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  
};


RA2TreeFiller::RA2TreeFiller(const edm::ParameterSet& iConfig):
  HTjetCollection(iConfig.getUntrackedParameter<std::string>("HTjetCollection","patJetsAK5PFPt50Eta25")),
  MHTjetCollection(iConfig.getUntrackedParameter<std::string>("MHTjetCollection","patJetsAK5PFPt30")),
  pseudoParticleCollection(iConfig.getUntrackedParameter<std::string>("pseudoParticleCollection","fatjetSubjets")),
  debug(iConfig.getUntrackedParameter<bool>("debug",false))
{

  edm::Service<TFileService> fs;

  AnalysisTree = fs->make<TTree>("AnalysisTree","AnalysisTree");

  AnalysisTree->Branch("HT",&HT,"HT/D");
  AnalysisTree->Branch("MHT",&MHT,"MHT/D");
  AnalysisTree->Branch("DeltaPhi1",&DeltaPhi1,"DeltaPhi1/D");
  AnalysisTree->Branch("DeltaPhi2",&DeltaPhi2,"DeltaPhi2/D");
  AnalysisTree->Branch("DeltaPhi3",&DeltaPhi3,"DeltaPhi3/D");
  AnalysisTree->Branch("sumJetMass",&sumJetMass,"sumJetMass/D");
  AnalysisTree->Branch("nJets",&NJets,"nJets/I");

  if( debug ){

    std::cout << "HT jets collection " << HTjetCollection << std::endl;
    std::cout << "MHT jets collection " << MHTjetCollection << std::endl;
    std::cout << "pseudo particle collection "  << pseudoParticleCollection << std::endl;
    std::cout << "-------------------" << std::endl;
    std::cout << "done in constructor" << std::endl;

  }

}

RA2TreeFiller::~RA2TreeFiller()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
RA2TreeFiller::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  if ( debug ) 
    std::cout << "RA2TreeFiller::analyze"  << std::endl;

  using namespace edm;

  // start section where jet collections will be looped over!!
  // ===================
  // -------------------

  Handle< View<reco::Jet> > HTjetCands;
  iEvent.getByLabel( HTjetCollection,HTjetCands);

  Handle< View<reco::Jet> > MHTjetCands;
  iEvent.getByLabel( MHTjetCollection,MHTjetCands);

  // set all variables in struct to zero or clear std::vectors
  HT = MHT = sumJetMass = 0. ;
  DeltaPhi1 = DeltaPhi2 = DeltaPhi3 = -99. ;
  NJets = 0 ;

  // for calculating missHt
  double negativePx_MHTjets = 0.; 
  double negativePy_MHTjets = 0.; 

  // $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  // HT calculation
  for(View<reco::Jet>::const_iterator iJet = HTjetCands->begin();
      iJet != HTjetCands->end();
      ++iJet){

    if ( debug ) std::cout  << "num. jets: " << HTjetCands->size() << std::endl;

    HT += iJet->pt();

  } // end loop over iJet
  // $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

  // ##############################
  // MHT calculation
  for(View<reco::Jet>::const_iterator iJet = MHTjetCands->begin();
      iJet != MHTjetCands->end();
      ++iJet){

    if ( debug ) std::cout  << "num. jets: " << MHTjetCands->size() << std::endl;

    negativePx_MHTjets -= iJet->px();
    negativePy_MHTjets -= iJet->py();

  } // end loop over iJet
  // ##############################

  MHT = sqrt( pow( negativePx_MHTjets , 2 ) + pow( negativePy_MHTjets , 2 ) ) ;
  double MHTphi = acos( negativePx_MHTjets / MHT ) ;

  // ******************************
  // DeltaPhi calculation
  View<reco::Jet>::const_iterator iJet = MHTjetCands->begin();
  DeltaPhi1 = abs( MHTphi - iJet.phi() ) ; 
  if( iJet != HTjetCands->end() ){
    ++iJet ;
    DeltaPhi2 = abs( MHTphi - iJet.phi() ) ;
    if( iJet != HTjetCands->end() ){
      ++iJet ; 
      DeltaPhi3 = abs( MHTphi - iJet.phi() ) ;
    }
  }
  // ******************************

  NJets = HTjetCands->size() ;

  // @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  // sum jet mass calculation

  if( debug ){
    std::cout << pseudoParticleCollection<< std::endl;
  }

  Handle< std::vector < math::XYZTLorentzVector > > particleCands;
  iEvent.getByLabel( pseudoParticleCollection,particleCands);

  for( unsigned int iParticle = 0; iParticle < particleCands->size(); ++iParticle){

    math::XYZTLorentzVector p4 = (*particleCands)[iParticle] ; 

    sumJetMass += p4.M() ;

  } // end loop over iParticle

  AnalysisTree->Fill();    

}

// ------------ method called once each job just before starting event loop  ------------
void RA2TreeFiller::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void RA2TreeFiller::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void RA2TreeFiller::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void RA2TreeFiller::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void RA2TreeFiller::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void RA2TreeFiller::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void RA2TreeFiller::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

}

//define this as a plug-in
DEFINE_FWK_MODULE(RA2TreeFiller);
