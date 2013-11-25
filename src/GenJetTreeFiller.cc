// -*- C++ -*-
//
// Package:    GenJetTreeFiller
// Class:      GenJetTreeFiller
// 
/**\class GenJetTreeFiller GenJetTreeFiller.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Andrew Whitbeck
//         Created:  Wed Oct 25 2013
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

#include <fastjet/ClusterSequence.hh>
#include <fastjet/PseudoJet.hh>
#include <fastjet/JetDefinition.hh>

#include "SubjetCounting.hh"

#include <vector>



class GenJetTreeFiller : public edm::EDAnalyzer {

public:
  explicit GenJetTreeFiller(const edm::ParameterSet&);
  ~GenJetTreeFiller();
  
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

  TTree* GenJetTree;

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

  };
  
  treeStructure myTree;

  // ---------- configurable data ----------------
  // --------------- members ---------------------
  
  std::string stdJetCollection;    // name of jet collection
  std::string fatJetCollection;      // name of jet collection with large R

};


GenJetTreeFiller::GenJetTreeFiller(const edm::ParameterSet& iConfig):
  stdJetCollection(iConfig.getUntrackedParameter<std::string>("stdJetCollection","ak5GenJets")),
  fatJetCollection(iConfig.getUntrackedParameter<std::string>("fatJetCollection","ak1p2GenJets"))
{
   //now do what ever initialization is needed
  edm::Service<TFileService> fs;

  GenJetTree = fs->make<TTree>("GenJetTree","GenJetTree");

  GenJetTree->Branch("jetPt_min30",&myTree.jetPt_min30);
  GenJetTree->Branch("jetPt_min50",&myTree.jetPt_min50);
  GenJetTree->Branch("jetMass_pt30",&myTree.jetMass_pt30);
  GenJetTree->Branch("jetMass_pt50",&myTree.jetMass_pt50);
  GenJetTree->Branch("sumJetMass_pt30",&myTree.sumJetMass_pt30,"sumJetMass_pt30/D");
  GenJetTree->Branch("sumJetMass_pt50",&myTree.sumJetMass_pt50,"sumJetMass_pt50/D");
  GenJetTree->Branch("nSubJets_pt30",&myTree.nSubJets_pt30,"nSubJets_pt30/I");
  GenJetTree->Branch("nSubJets_pt50",&myTree.nSubJets_pt50,"nSubJets_pt50/I");
  GenJetTree->Branch("Ht_pt30",&myTree.Ht_pt30,"Ht_pt30/D");
  GenJetTree->Branch("Ht_pt50",&myTree.Ht_pt50,"Ht_pt50/D");
  GenJetTree->Branch("met_pt30",&myTree.met_pt30,"met_pt30/D");
  GenJetTree->Branch("met_pt50",&myTree.met_pt50,"met_pt50/D");
  GenJetTree->Branch("nJets_pt30",&myTree.nJets_pt30,"nJets_pt30/I");
  GenJetTree->Branch("nJets_pt50",&myTree.nJets_pt50,"nJets_pt50/I");

}


GenJetTreeFiller::~GenJetTreeFiller()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
GenJetTreeFiller::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // fill histograms for di-lepton system

  using namespace edm;

  Handle< View<reco::GenJet> > jetCands;
  iEvent.getByLabel(stdJetCollection,jetCands);

  Handle< View<reco::GenJet> > fatJetCands;
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

  for(View<reco::GenJet>::const_iterator iJet = jetCands->begin();
      iJet != jetCands->end();
      ++iJet){

    // kinematic selection for jets
    if ( iJet->pt() > 50. &&
	 fabs( iJet->eta() ) < 2.5 ){
      
      // set variables for tree
      myTree.jetPt_min50.push_back  (   iJet->pt() );
      myTree.jetMass_pt50.push_back (   iJet->mass()    );

      myTree.Ht_pt50         += iJet->pt();

      negativePx_pt50        -= iJet->px();
      negativePy_pt50        -= iJet->py();

    }

    // kinematic selection for jets
    if ( iJet->pt() > 30. && 
	 fabs( iJet->eta() ) < 5. ){

      myTree.jetPt_min30.push_back  (   iJet->pt() );
      myTree.jetMass_pt30.push_back (   iJet->mass()    );

      myTree.Ht_pt30         += iJet->pt();

      negativePx_pt30        -= iJet->px();
      negativePy_pt30        -= iJet->py();

    }

  }
  
  // need to recluster fatjets inorder to pass fastjet::pseudojet collection
  // to fastjet::contrib::SubjetCountingCA because reco::jets doesn't
  // save information about constituents

  Handle< View<reco::GenParticle> > genCands;
  iEvent.getByLabel("genParticlesForJetsNoNu",genCands);

  std::vector<fastjet::PseudoJet> fatJetConst;

  for(View<reco::GenParticle>::const_iterator iCand = genCands->begin();
      iCand != genCands->end();
      ++iCand){
    
    fatJetConst.push_back( fastjet::PseudoJet( iCand->px(), 
					       iCand->py(),
					       iCand->pz(),
					       iCand->energy() ) );

  }
    
  //std::cout << "n jet constituents: " << fatJetConst.size() << std::endl;

  fastjet::JetDefinition aktp12(fastjet::antikt_algorithm, 1.2);
  fastjet::ClusterSequence cs_aktp12(fatJetConst, aktp12);
  std::vector<fastjet::PseudoJet> fatJets = sorted_by_pt(cs_aktp12.inclusive_jets());
  
  // initialize object for counting subjets
  //               SubjetCountingCA(mass_cutoff,ycut,R_min,pt_cut);
                                    
  fastjet::contrib::SubjetCountingCA subjetCounter_pt50(50.,0.15,0.15,50.);
  fastjet::contrib::SubjetCountingCA subjetCounter_pt30(30.,0.10,0.15,40.);

  //std::cout << "N fat jets: " << fatJets.size() << std::endl;

  for( unsigned int iFatJet = 0 ; iFatJet < fatJets.size() ; iFatJet++ ){

    //std::cout << "fat jet pt : " << fatJets[ iFatJet ].pt() << std::endl;
    //std::cout << "fat jet eta: " << fatJets[ iFatJet ].eta() << std::endl;

    if( fatJets[ iFatJet ].pt() > 50. &&
	fabs( fatJets[ iFatJet ].eta() < 2.5 ) ){
      
        myTree.sumJetMass_pt50 += fatJets[ iFatJet ].m();
	
	//std::cout << "jet mass: " << fatJets[ iFatJet ].m() << std::endl;

	myTree.nSubJets_pt50 = subjetCounter_pt50.result( fatJets[ iFatJet ] );
      
    }

    if( fatJets[ iFatJet ].pt() > 30. &&
	fabs( fatJets[ iFatJet ].eta() < 2.5 ) ){

	myTree.sumJetMass_pt30 += fatJets[ iFatJet ].m();

	//std::cout << "jet mass: " << fatJets[ iFatJet ].m() << std::endl;

	myTree.nSubJets_pt30 = subjetCounter_pt30.result( fatJets[ iFatJet ] );

    }

  }


  myTree.met_pt30   = sqrt( pow( negativePx_pt30 , 2 ) + pow( negativePy_pt30 , 2 ) ) ;
  myTree.met_pt50   = sqrt( pow( negativePx_pt50 , 2 ) + pow( negativePy_pt50 , 2 ) ) ;

  myTree.nJets_pt30 = myTree.jetPt_min30.size();
  myTree.nJets_pt50 = myTree.jetPt_min50.size();

  GenJetTree->Fill();    

}


// ------------ method called once each job just before starting event loop  ------------
void 

GenJetTreeFiller::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenJetTreeFiller::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
GenJetTreeFiller::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
GenJetTreeFiller::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
GenJetTreeFiller::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
GenJetTreeFiller::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenJetTreeFiller::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

}

//define this as a plug-in
DEFINE_FWK_MODULE(GenJetTreeFiller);
