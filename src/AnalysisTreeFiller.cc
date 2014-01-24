// -*- C++ -*-
//
// Package:    AnalysisTreeFiller
// Class:      AnalysisTreeFiller
// 
/**\class AnalysisTreeFiller AnalysisTreeFiller.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Andrew Whitbeck
//         Created:  Wed Dec 17 2013
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

#include "TH1.h"
#include "TH2.h"
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


class AnalysisTreeFiller : public edm::EDAnalyzer {

public:
  explicit AnalysisTreeFiller(const edm::ParameterSet&);
  ~AnalysisTreeFiller();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  
  // ----------member data ---------------------------

  TTree* AnalysisTree;

  struct treeStructure {

    std::vector<double> jetPt_min30;
    std::vector<double> jetPt_min50;

    std::vector<double> jetMass_pt30;
    std::vector<double> jetMass_pt50;

    double sumJetMass_pt50;
    double sumJetMass_pt30;
    int nSubJets_pt50;
    int nSubJets_pt30;
    double Ht_pt30;
    double Ht_pt50;
    double met_pt30;    
    double met_pt50;

    int nJets_pt30;
    int nJets_pt50;

    double eventWeight;

  };
  
  treeStructure myTree;

  // ---------- configurable data ----------------
  // --------------- members ---------------------
  
  std::string stdJetCollection;    // name of jet collection
  std::string fatJetCollection;      // name of jet collection with large R

  bool debug;
};


AnalysisTreeFiller::AnalysisTreeFiller(const edm::ParameterSet& iConfig):
  stdJetCollection(iConfig.getUntrackedParameter<std::string>("stdJetCollection","ak5PFJets")),
  fatJetCollection(iConfig.getUntrackedParameter<std::string>("fatJetCollection","ak1p2PFJets")),
  debug(iConfig.getUntrackedParameter<bool>("debug",false))
{

  //now do what ever initialization is needed
  edm::Service<TFileService> fs;

  AnalysisTree = fs->make<TTree>("AnalysisTree","AnalysisTree");

  AnalysisTree->Branch("jetPt_min30",&myTree.jetPt_min30);
  AnalysisTree->Branch("jetPt_min50",&myTree.jetPt_min50);
  AnalysisTree->Branch("jetMass_pt30",&myTree.jetMass_pt30);
  AnalysisTree->Branch("jetMass_pt50",&myTree.jetMass_pt50);
  AnalysisTree->Branch("sumJetMass_pt30",&myTree.sumJetMass_pt30,"sumJetMass_pt30/D");
  AnalysisTree->Branch("sumJetMass_pt50",&myTree.sumJetMass_pt50,"sumJetMass_pt50/D");
  AnalysisTree->Branch("nSubJets_pt30",&myTree.nSubJets_pt30,"nSubJets_pt30/I");
  AnalysisTree->Branch("nSubJets_pt50",&myTree.nSubJets_pt50,"nSubJets_pt50/I");
  AnalysisTree->Branch("Ht_pt30",&myTree.Ht_pt30,"Ht_pt30/D");
  AnalysisTree->Branch("Ht_pt50",&myTree.Ht_pt50,"Ht_pt50/D");
  AnalysisTree->Branch("met_pt30",&myTree.met_pt30,"met_pt30/D");
  AnalysisTree->Branch("met_pt50",&myTree.met_pt50,"met_pt50/D");
  AnalysisTree->Branch("nJets_pt30",&myTree.nJets_pt30,"nJets_pt30/I");
  AnalysisTree->Branch("nJets_pt50",&myTree.nJets_pt50,"nJets_pt50/I");
  AnalysisTree->Branch("eventWeight",&myTree.eventWeight,"eventWeight/D");

}


AnalysisTreeFiller::~AnalysisTreeFiller()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
AnalysisTreeFiller::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // fill histograms for di-lepton system

  using namespace edm;

  // -- Monte Carlo Event Weight
  double eventWeight = 1.0 ;
  edm::Handle< GenEventInfoProduct > genEventInfo;
  iEvent.getByLabel("generator", genEventInfo);
  
  if ( genEventInfo.isValid() ){
    
    if( debug )
      std::cout << genEventInfo->weight() << std::endl;

    eventWeight = genEventInfo->weight();

  }

  myTree.eventWeight = eventWeight;
  // ---------------------------

  Handle< View<reco::Jet> > jetCands;
  iEvent.getByLabel(stdJetCollection,jetCands);

  Handle< View<reco::Jet> > fatJetCands;
  iEvent.getByLabel(fatJetCollection,fatJetCands);

  myTree.jetPt_min30.clear();
  myTree.jetMass_pt30.clear();

  myTree.jetPt_min50.clear();
  myTree.jetMass_pt50.clear();

  myTree.sumJetMass_pt30 = 0.;
  myTree.sumJetMass_pt50 = 0.;

  myTree.nSubJets_pt50   = 0.;
  myTree.nSubJets_pt30   = 0.;

  myTree.Ht_pt30         = 0.;
  myTree.Ht_pt50         = 0.;

  myTree.met_pt30        = 0.; 
  myTree.met_pt50        = 0.; 

  double negativePx_pt30 = 0.; 
  double negativePy_pt30 = 0.; 

  double negativePx_pt50 = 0.; 
  double negativePy_pt50 = 0.; 

  for(View<reco::Jet>::const_iterator iJet = jetCands->begin();
      iJet != jetCands->end();
      ++iJet){

    //std::cout  << "num. jets: " << jetCands->size() << std::endl;

    // kinematic selection for jets
    if ( iJet->pt() > 50. &&
	 fabs( iJet->eta() ) < 2.5 ){
      
      // set variables for tree
      myTree.jetPt_min50.push_back  (   iJet->pt() );
      myTree.jetMass_pt50.push_back (   iJet->mass()    );

      myTree.Ht_pt50         += iJet->pt();

      negativePx_pt50        -= iJet->px();
      negativePy_pt50        -= iJet->py();

    }// end if statement

    // kinematic selection for jets
    if ( iJet->pt() > 30. && 
	 fabs( iJet->eta() ) < 5. ){

      myTree.jetPt_min30.push_back  (   iJet->pt() );
      myTree.jetMass_pt30.push_back (   iJet->mass()    );

      myTree.Ht_pt30         += iJet->pt();

      negativePx_pt30        -= iJet->px();
      negativePy_pt30        -= iJet->py();

    }// end if statement

  } // end loop over iJet

  myTree.met_pt30   = sqrt( pow( negativePx_pt30 , 2 ) + pow( negativePy_pt30 , 2 ) ) ;
  myTree.met_pt50   = sqrt( pow( negativePx_pt50 , 2 ) + pow( negativePy_pt50 , 2 ) ) ;

  myTree.nJets_pt30 = myTree.jetPt_min30.size();
  myTree.nJets_pt50 = myTree.jetPt_min50.size();
  
  // grab substructure variables from the event
  // ..........................................
  Handle< double > sumJetMass;
  iEvent.getByLabel("Substructure","ak1p2Jets-sumJetMass",sumJetMass);

  myTree.sumJetMass_pt30 = *sumJetMass;
  myTree.sumJetMass_pt50 = *sumJetMass;

  Handle< double > nSubJets;
  iEvent.getByLabel("Substructure","ak1p2Jets-nSubJets",nSubJets);

  myTree.nSubJets_pt30 = *nSubJets;
  myTree.nSubJets_pt50 = *nSubJets;
  // ..........................................

  AnalysisTree->Fill();    

}


// ------------ method called once each job just before starting event loop  ------------
void 

AnalysisTreeFiller::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
AnalysisTreeFiller::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
AnalysisTreeFiller::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
AnalysisTreeFiller::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
AnalysisTreeFiller::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
AnalysisTreeFiller::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
AnalysisTreeFiller::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

}

//define this as a plug-in
DEFINE_FWK_MODULE(AnalysisTreeFiller);
