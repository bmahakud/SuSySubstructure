// -*- C++ -*-
//
// Package:    AnalysisTreeFiller
// Class:      AnalysisTreeFiller
// 
/**\class AnalysisTreeFiller AnalysisTreeFiller.cc

 Description: Class which takes several types of jet collections
 and saves their kinematic properties to a TTree.  collections 
 that can be read and analyzed are either reco::Jet collections 
 and should be passed via the jetCollection argument or 
 std::vector< math::XYZTLorentzVector > collections (which 
 are built from the SubjetProducer, for example).   

 In both cases the string argument used to pass the collections
 can be used to pass a list of collections to be saved.  All
 collections should be deliniated used a ':'.  

 e.g.  for reading ak5PFJets and ak4PFJets collections, one 
 should pass "ak5PFJets:ak4PFJets" to jetCollections.

 NOTE:  current, the get handle does not catch exceptions 
 from collections not being found in the event and thus 
 will just seg fault... this will hopefully be fixed soon.

*/
//
// Original Author:  Andrew Whitbeck
//         Created:  Wed Dec 17 2013
//         Last updated: Feb 11, 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/ValueMap.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TLorentzVector.h"
#include "TTree.h"    


#include <DataFormats/PatCandidates/interface/Photon.h>
#include <DataFormats/PatCandidates/interface/Electron.h>
#include <DataFormats/EgammaCandidates/interface/GsfElectron.h>
#include <DataFormats/RecoCandidate/interface/IsoDeposit.h>
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "SandBox/Skims/plugins/ElectronEffectiveArea.h"

#include <DataFormats/PatCandidates/interface/MET.h>
#include <DataFormats/PatCandidates/interface/Jet.h>
#include <DataFormats/PatCandidates/interface/Muon.h>
#include <DataFormats/PatCandidates/interface/CompositeCandidate.h>
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include <SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h>

#include <fastjet/ClusterSequence.hh>
#include <fastjet/PseudoJet.hh>
#include <fastjet/JetDefinition.hh>

#include "SubjetCounting.hh"

#include "GSFelectronInterface.h"

#include <vector>


class AnalysisTreeFiller : public edm::EDAnalyzer {

public:
  explicit AnalysisTreeFiller(const edm::ParameterSet&);
  ~AnalysisTreeFiller();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:

  // ----------member data ---------------------------
  
  TTree* AnalysisTree;

  TH1F*  HT_histo;
  TH1F*  MHT_histo;
  TH1F*  sumJetMass_histo;

  TH2F*  HT_vs_MHT_histo;
  TH2F*  HT_vs_sumJetMass_histo;
  TH2F*  sumJetMass_vs_MHT_histo;
  TH2F*  HT_vs_met_histo;
  
  int event, run, lumi;

  double MET ; 
  double METsig ; 

  std::vector< double > muonPt;
  std::vector< double > muonEta;
  std::vector< double > muonPhi;
  std::vector< double > muonE;
  std::vector< double > muonRelIso;
  std::vector< bool >   muonPassID;

  int NMuons;

  std::vector< double > electronPt;
  std::vector< double > electronEta;
  std::vector< double > electronPhi;
  std::vector< double > electronE;
  std::vector< double > electronRelIso;
  std::vector< bool >   electronPassID;

  int NElectrons;

  std::vector< double > photonPt;
  std::vector< double > photonEta;
  std::vector< double > photonPhi;
  std::vector< double > photonE;

  int NPhotons;
 
  struct jetKinematics {

    std::vector< double > pt;
    std::vector< double > eta;
    std::vector< double > mass;
    std::vector< double > phi;  
    int NJets;
    double sumJetMass;
    double MHT;
    double MHTphi;
    double HT;
  
  };

  std::vector< jetKinematics* > jetKin ;
  std::vector< jetKinematics* > particleKin ;

  double eventWeight;

  // ---------- configurable data ----------------
  // --------------- members ---------------------
  
  std::string jetCollection;    // name of jet collection
  std::string pseudoParticleCollection;    // name of jet collection
  std::vector < std::string > jetCollectionList ; // parsed jet collections
  std::vector < std::string > pseudoParticleCollectionList ; // parsed jet collections
  edm::InputTag METcollection ; // MET collection
  edm::InputTag muonCollection ; // muon collection
  edm::InputTag photonCollection ; // photon collection
  edm::InputTag electronCollection ; // electron collection
  edm::InputTag conversionsSrc ; // conversions collection
  edm::InputTag vtxSrc ; // primary vertex collection
  edm::InputTag beamSpotSrc ; // beam spot collection
  edm::InputTag rhoIsoSrc ; // rho corrections
  std::vector< edm::InputTag > isoValsSrc ; // electrons isolations

  bool debug;

  // ---------- private methods! -----------

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  void zeroJetKinematics( jetKinematics& jetKin );
  void addJetKinToTree( jetKinematics& jetKin, TString tag, TTree& tree );
  void parseString( std::vector< std::string > &container, std::string orig, size_t pos = 0, std::string delim = ":" );
  
};


AnalysisTreeFiller::AnalysisTreeFiller(const edm::ParameterSet& iConfig):
  jetCollection(iConfig.getUntrackedParameter<std::string>("jetCollection","patJetsAK5PFPt30")),
  pseudoParticleCollection(iConfig.getUntrackedParameter<std::string>("pseudoParticleCollection","fatjetSubjets")),
  METcollection(iConfig.getUntrackedParameter<edm::InputTag>("METcollection")),    // pfMet , patMETsPF, mhtPF
  muonCollection(iConfig.getUntrackedParameter<edm::InputTag>("muonCollection")),  //patMuonsPFID
  photonCollection(iConfig.getUntrackedParameter<edm::InputTag>("photonCollection")), //patPhotonsRA2
  electronCollection(iConfig.getUntrackedParameter<edm::InputTag>("electronCollection")), // gsfElectron or patElectronsID
  conversionsSrc(iConfig.getParameter<edm::InputTag>("ConversionsSource")), // allConversions
  vtxSrc(iConfig.getParameter<edm::InputTag>("VertexSource")),              // goodVertices
  beamSpotSrc(iConfig.getParameter<edm::InputTag>("BeamSpotSource")),       // offlineBeamSpot
  rhoIsoSrc(iConfig.getParameter<edm::InputTag>("RhoIsoSource")),           // kt6PFJets , rho
  isoValsSrc(iConfig.getParameter<std::vector<edm::InputTag> >("IsoValInputTags")),  //elPFIsoValueCharged03PFIdPFIso, elPFIsoValueGamma03PFIdPFIso, elPFIsoValueNeutral03PFIdPFIso
  debug(iConfig.getUntrackedParameter<bool>("debug",false))
{

  edm::Service<TFileService> fs;

  AnalysisTree            = fs->make<TTree>("AnalysisTree","AnalysisTree");

  // set branches
  // --------------------------

  AnalysisTree->Branch("event",&event);
  AnalysisTree->Branch("run",&run);
  AnalysisTree->Branch("lumi",&lumi);

  AnalysisTree->Branch("MET",&MET);
  AnalysisTree->Branch("METsig",&METsig);

  AnalysisTree->Branch("electronPt",&electronPt);
  AnalysisTree->Branch("electronEta",&electronEta);
  AnalysisTree->Branch("electronPhi",&electronPhi);
  AnalysisTree->Branch("electronE",&electronE);
  AnalysisTree->Branch("electronsRelIso",&electronRelIso);
  AnalysisTree->Branch("electronPassID",&electronPassID);
  AnalysisTree->Branch("NElectrons",&NElectrons);

  AnalysisTree->Branch("muonPt",&muonPt);
  AnalysisTree->Branch("muonEta",&muonEta);
  AnalysisTree->Branch("muonPhi",&muonPhi);
  AnalysisTree->Branch("muonE",&muonE);
  AnalysisTree->Branch("muonRelIso",&muonRelIso);
  AnalysisTree->Branch("muonPassID",&muonPassID);
  AnalysisTree->Branch("NMuons",&NMuons);

  AnalysisTree->Branch("photonPt",&photonPt);
  AnalysisTree->Branch("photonEta",&photonEta);
  AnalysisTree->Branch("photonPhi",&photonPhi);
  AnalysisTree->Branch("photonE",&photonE);

  // NOTE: histograms will only be filled for the last jet collection!
  // -----------------------------------------------------------------
  HT_histo                = fs->make<TH1F >("HT_histo","H_{T} [GeV]",400,0,2000);
  MHT_histo               = fs->make<TH1F >("MET_histo","missing H_{T} [GeV]",400,0,2000);
  sumJetMass_histo        = fs->make<TH1F >("sumJetMass_histo","#Sigma m_{j} [GeV]",400,0,2000);

  HT_vs_met_histo         = fs->make<TH2F >("HT_vs_MHT_histo",";H_{T} [GeV];missing H_{T} [GeV]",400,0,2000,400,0,2000);
  HT_vs_sumJetMass_histo  = fs->make<TH2F >("HT_vs_sumJetMass_histo",";H_{T} [GeV];#Sigma m_{j} [GeV]",400,0,2000,400,0,2000);
  sumJetMass_vs_MHT_histo = fs->make<TH2F >("sumJetMass_vs_MHT_histo",";#Sigma m_{j} [GeV];missing H_{T} [GeV]",400,0,2000,400,0,2000);
  
  // parse list of jet collections to analyze
  parseString( jetCollectionList, jetCollection ) ;
  // parse list of pseudo particle collections to analyze
  parseString( pseudoParticleCollectionList, pseudoParticleCollection ) ;

  if( debug ){

    for(unsigned int iJetColl = 0 ; iJetColl < jetCollectionList.size() ; iJetColl++ ){
      std::cout << "jets collection " << iJetColl << " " << jetCollectionList[ iJetColl ] << std::endl;
    }
    for(unsigned int iParticleColl = 0 ; iParticleColl < pseudoParticleCollectionList.size() ; iParticleColl++ ){
      std::cout << "pseudo particle collection " << iParticleColl << " " << pseudoParticleCollectionList[ iParticleColl ] << std::endl;
    }

  }

  // add branches for saving jets kinematics for each jet collection
  for( unsigned int iJetColl = 0 ; iJetColl < jetCollectionList.size() ; iJetColl++ ){
    jetKin.push_back( new jetKinematics() );
    addJetKinToTree( *jetKin[ iJetColl ], jetCollectionList[ iJetColl ], *AnalysisTree );

  }
 // add branches for saving particle kinematics for each pseudo particle collection
  for( unsigned int iParticleColl = 0 ; iParticleColl < pseudoParticleCollectionList.size() ; iParticleColl++ ){
    particleKin.push_back( new jetKinematics() );
    addJetKinToTree( *particleKin[ iParticleColl ], pseudoParticleCollectionList[ iParticleColl ], *AnalysisTree );
  
  }

  AnalysisTree->Branch("eventWeight",&eventWeight,"eventWeight/D");

  if( debug )
    std::cout << "done in constructor" << std::endl;

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

  if ( debug ) 
    std::cout << "AnalysisTreeFiller::analyze"  << std::endl;

  using namespace edm;

  // -- Monte Carlo Event Weight
  eventWeight = 1.0 ;
  edm::Handle< GenEventInfoProduct > genEventInfo;
  iEvent.getByLabel("generator", genEventInfo);
  
  if ( genEventInfo.isValid() ){
    
    if( debug )
      std::cout << genEventInfo->weight() << std::endl;

    eventWeight = genEventInfo->weight();

  }

  // MET
  // ===========================
  // for more information on MET stuff:
  // https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMetAnalysis
  // http://cmslxr.fnal.gov/lxr/source/DataFormats/PatCandidates/interface/MET.h
  // http://cmslxr.fnal.gov/lxr/source/DataFormats/METReco/interface/MET.h
  /*
  //scalar sum of transverse energy over all objects
  double sumEt() const { return sumet; }
  //MET Significance = MET / std::sqrt(SumET)
  double mEtSig() const { return ( sumet ? (this->et() / std::sqrt(sumet)) : (0.0) ); }
  //real MET significance
  double significance() const;
  //longitudinal component of the vector sum of energy over all object
  //(useful for data quality monitoring)
  double e_longitudinal() const {return elongit; }
  */
  // ---------------------------
  
  Handle< View< pat::MET > >  metCand;
  iEvent.getByLabel( METcollection , metCand );

  for( View<pat::MET>::const_iterator met = metCand->begin();
        met != metCand->end();
        ++met){

    if( debug ){
      std::cout << "MET:" << met->pt() << std::endl;
      std::cout << "MET significance: " << met->significance() << std::endl;
    }

    MET = met->pt();
    METsig = met->significance();

    break;

  }

  // Muons
  // ===========================
  // ---------------------------
  // should be using muon collection which has ID requirements 
  // already applied.
  // referencing the RA2 selector:
  // https://github.com/awhitbeck/RA2/blob/master/SandBox/Skims/plugins/GoodMuonSelector.cc

  Handle< View<pat::Muon> > muonCands;
  iEvent.getByLabel( muonCollection ,muonCands);

  muonPt.clear();
  muonEta.clear();
  muonPhi.clear();
  muonE.clear();
  muonPassID.clear();
  muonRelIso.clear();
  NMuons = 0;

  edm::Handle< std::vector<reco::Vertex> > vertices;
  iEvent.getByLabel(vtxSrc, vertices);
  reco::Vertex::Point vtxpos = (vertices->size() > 0 ? (*vertices)[0].position() : reco::Vertex::Point());

  for(View<pat::Muon>::const_iterator iMuon = muonCands->begin();
        iMuon != muonCands->end();
        ++iMuon){

    //if( iMuon->pt() < 10. || fabs( iMuon->eta() ) > 2.4 ) continue ;

    muonPt.push_back( iMuon->pt() );
    muonEta.push_back( iMuon->eta() ); 
    muonPhi.push_back( iMuon->phi() );
    muonE.push_back( iMuon->energy() );
    
    muonRelIso.push_back( (iMuon->pfIsolationR04().sumChargedHadronPt + std::max(0., iMuon->pfIsolationR04().sumNeutralHadronEt + iMuon->pfIsolationR04().sumPhotonEt - 0.5*iMuon->pfIsolationR04().sumPUPt) )/ iMuon->pt() );

    bool pass = false;

    if( !iMuon->isPFMuon() || 
        iMuon->globalTrack()->normalizedChi2() >= 10. ||
        iMuon->globalTrack()->hitPattern().numberOfValidMuonHits() <= 0 ||
        iMuon->numberOfMatchedStations() <=1 ||
        iMuon->innerTrack()->hitPattern().numberOfValidPixelHits() == 0 ||
        iMuon->innerTrack()->hitPattern().trackerLayersWithMeasurement() <=5 ||
        std::abs(iMuon->innerTrack()->dxy(vtxpos)) >= 0.2 && vertices->size() > 0 ||
        std::abs(iMuon->innerTrack()->dz(vtxpos))  >= 0.5 && vertices->size() > 0 ) pass = false;
    else pass = true;

    muonPassID.push_back(pass);

    NMuons++;
    
  }

  // Photon
  // ===========================
  // ---------------------------
  /*
  Handle< View<pat::Photon> > photonCands;
  iEvent.getByLabel( photonCollection ,photonCands);

  for(View<pat::Photon>::const_iterator iPhoton = photonCands->begin();
        iPhoton != photonCands->end();
        ++iPhoton){

    photonPt.push_back( iPhoton->pt() );
    photonEta.push_back( iPhoton->eta() ); 
    photonPhi.push_back( iPhoton->phi() );
    photonE.push_back( iPhoton->energy() );
    NPhotons++;
    
  }
  */

  // Electrons
  // ===========================
  // ---------------------------

  // get electrons
  Handle< std::vector< reco::GsfElectron> > electronCands;
  iEvent.getByLabel( electronCollection ,electronCands);

  GSFelectronInterface eleTool( electronCollection , conversionsSrc , vtxSrc , beamSpotSrc , rhoIsoSrc , isoValsSrc ) ; 

  electronPt.clear();
  electronEta.clear();
  electronPhi.clear();
  electronE.clear();
  electronRelIso.clear();
  electronPassID.clear();

  NElectrons = 0 ;

  for(unsigned int i = 0 ; i < electronCands->size(); ++i){
  
    electronData myEle = eleTool.passIDandISO( iEvent , i ) ;

   
    electronPt.push_back( myEle.pt );
    electronEta.push_back( myEle.eta ); 
    electronPhi.push_back( myEle.phi );
    electronE.push_back( myEle.e );
    electronRelIso.push_back( myEle.combIso );
    electronPassID.push_back( myEle.passID );
    NElectrons++;
    
  }

  // start section where jet collections will be looped over!!
  // ===================
  // -------------------
  for ( unsigned int iJetColl = 0 ; iJetColl < jetCollectionList.size() ; iJetColl++ ){

    if( debug ){

      std::cout << jetCollectionList[ iJetColl ] << std::endl;

    }

    Handle< View<reco::Jet> > jetCands;
    iEvent.getByLabel( jetCollectionList[ iJetColl ],jetCands);

    // set all variables in struct to zero or clear std::vectors
    zeroJetKinematics( *jetKin[ iJetColl ] );

    // for calculating missHt
    double negativePx_pt30 = 0.; 
    double negativePy_pt30 = 0.; 

    for(View<reco::Jet>::const_iterator iJet = jetCands->begin();
        iJet != jetCands->end();
        ++iJet){

      //std::cout  << "num. jets: " << jetCands->size() << std::endl;

      // kinematic selection for jets
      if ( iJet->pt() > 50. && fabs( iJet->eta() ) < 2.5 ){

        jetKin[ iJetColl ]->sumJetMass += iJet->mass() ;

      }// end if statement

      // kinematic selection for jets
      if ( iJet->pt() > 30. && fabs( iJet->eta() ) < 5. ){

        jetKin[ iJetColl ]->pt.push_back  (   iJet->pt()   );
        jetKin[ iJetColl ]->eta.push_back (   iJet->eta()  );
        jetKin[ iJetColl ]->phi.push_back (   iJet->phi()  );
        jetKin[ iJetColl ]->mass.push_back(   iJet->mass() );

        jetKin[ iJetColl ]->HT  += iJet->pt();

        negativePx_pt30        -= iJet->px();
        negativePy_pt30        -= iJet->py();

      }// end if statement

    } // end loop over iJet

    jetKin[ iJetColl ]->MHT   = sqrt( pow( negativePx_pt30 , 2 ) + pow( negativePy_pt30 , 2 ) ) ;

    jetKin[ iJetColl ]->MHTphi = acos( negativePx_pt30 / jetKin[ iJetColl ]->MHT ) ;

    jetKin[ iJetColl ]->NJets    = jetKin[ iJetColl ]->pt.size() ;

  } // end loop over jet collection list

    HT_histo->Fill( jetKin[ jetKin.size() - 1 ]->HT );
    MHT_histo->Fill( jetKin[ jetKin.size() - 1 ]->MHT );
    sumJetMass_histo->Fill( jetKin[ jetKin.size() - 1 ]->sumJetMass );

    HT_vs_met_histo->Fill( jetKin[ jetKin.size() - 1 ]->HT, jetKin[ jetKin.size() - 1 ]->MHT );
    HT_vs_sumJetMass_histo->Fill( jetKin[ jetKin.size() - 1 ]->HT, jetKin[ jetKin.size() - 1 ]->sumJetMass );
    sumJetMass_vs_MHT_histo->Fill( jetKin[ jetKin.size() - 1 ]->sumJetMass, jetKin[ jetKin.size() - 1 ]->MHT );

 for ( unsigned int iParticleColl = 0 ; iParticleColl < pseudoParticleCollectionList.size() ; iParticleColl++ ){

    if( debug ){

      std::cout << pseudoParticleCollectionList[ iParticleColl ] << std::endl;

    }

    Handle< std::vector < math::XYZTLorentzVector > > particleCands;
    iEvent.getByLabel( pseudoParticleCollectionList[ iParticleColl ],particleCands);

    // set all variables in struct to zero or clear std::vectors
    zeroJetKinematics( *particleKin[ iParticleColl ] );

    // for calculating missHt
    double negativePx_pt30 = 0.; 
    double negativePy_pt30 = 0.; 

    for( unsigned int iParticle = 0; iParticle < particleCands->size(); ++iParticle){

      math::XYZTLorentzVector p4 = (*particleCands)[iParticle] ; 

      // kinematic selection for pseudo particles
      if ( p4.pt() > 50. && fabs( p4.eta() ) < 2.5 ){

        particleKin[ iParticleColl ]->sumJetMass += p4.mass() ;

      }// end if statement

      // kinematic selection for jets
      if ( p4.pt() > 30. && fabs( p4.eta() ) < 5. ){

        particleKin[ iParticleColl ]->pt.push_back  (   p4.pt()   );
        particleKin[ iParticleColl ]->eta.push_back (   p4.eta()  );
        particleKin[ iParticleColl ]->phi.push_back (   p4.phi()  );
        particleKin[ iParticleColl ]->mass.push_back(   p4.mass() );

        particleKin[ iParticleColl ]->HT  += p4.pt();

        negativePx_pt30        -= p4.px();
        negativePy_pt30        -= p4.py();

      }// end if statement

    } // end loop over iParticle

    particleKin[ iParticleColl ]->MHT    = sqrt( pow( negativePx_pt30 , 2 ) + pow( negativePy_pt30 , 2 ) ) ;

    particleKin[ iParticleColl ]->MHTphi = acos( negativePx_pt30 / particleKin[ iParticleColl ]->MHT ) ;

    particleKin[ iParticleColl ]->NJets     = particleKin[ iParticleColl ]->pt.size();


  } // end loop over jet collection list

  AnalysisTree->Fill();    

}

// ------------ method to zero information in jetKinematics structs ---------------------
void AnalysisTreeFiller::zeroJetKinematics(jetKinematics& jetKin){

  if( debug ){

    std::cout << "AnalysisTreeFiller::zeroJetKinematics" << std::endl;

  }

  if( jetKin.pt.size() > 0 )
    jetKin.pt.clear();
  if( jetKin.eta.size() > 0 )
    jetKin.eta.clear();
  if( jetKin.mass.size() > 0 )
    jetKin.mass.clear();
  if( jetKin.phi.size() > 0 )
    jetKin.phi.clear();

  jetKin.NJets      = 0. ;
  jetKin.sumJetMass = 0. ;
  jetKin.MHT     = 0. ;
  jetKin.MHTphi  = 0. ;
  jetKin.HT         = 0. ;

  if( debug ){

    std::cout << "AnalysisTreeFiller::zeroJetKinematics -- done!" << std::endl;

  }

}

//------------ method for mapping jetKinematics structs to tree branches ------------
void AnalysisTreeFiller::addJetKinToTree(jetKinematics& jetKin, TString tag, TTree& tree){

  if( debug )
    std::cout << "AnalysisTreeFiller::addJetKinToTree" << std::endl;
  tree.Branch( "pt_" + tag,   &jetKin.pt);
  tree.Branch( "eta_" + tag,  &jetKin.eta);
  tree.Branch( "mass_" + tag, &jetKin.mass);
  tree.Branch( "phi_" + tag,  &jetKin.phi);
  
  TString branchName  = "NJets_" + tag ; 
  TString branchTitle = "NJets_" + tag + "/I" ;   
  tree.Branch( branchName.Data() ,      &jetKin.NJets , branchTitle.Data() );
  
  branchName  = "sumJetMass_" + tag ; 
  branchTitle = "sumJetMass_" + tag + "/D" ;   
  tree.Branch( branchName.Data() , &jetKin.sumJetMass , branchTitle.Data() );
  
  branchName  = "MHT_" + tag ; 
  branchTitle = "MHT_" + tag + "/D" ;   
  tree.Branch( branchName.Data() ,     &jetKin.MHT , branchTitle.Data() );
  
  branchName  = "MHTphi_" + tag ;
  branchTitle = "MHTphi_" + tag + "/D" ;   
  tree.Branch( branchName.Data() ,     &jetKin.MHTphi , branchTitle.Data() );
  
  branchName  = "HT_" + tag ;
  branchTitle = "HT_" + tag + "/D" ;   
  tree.Branch( branchName.Data() ,         &jetKin.HT , branchTitle.Data() );

  if( debug )
    std::cout << "AnalysisTreeFiller::addJetKinToTree - done " << std::endl;

}

//------------ method for parsing string passed from configuration file -------------
// ......... NOTE:  this aspect of the code is still in development .................
// This is intended to be used for passing multiple jet collections which are of 
// interest to the user to study.  
void AnalysisTreeFiller::parseString( std::vector< std::string > &container, std::string orig, size_t pos, std::string delim ){

  if ( orig.find( delim ) == std::string::npos ){
    container.push_back( orig );
    return;
  }

  container.push_back( orig.substr( 0, orig.find( delim ) ) ) ;
  parseString( container, orig.substr( orig.find( delim, pos ) + 1 ), orig.find( delim, pos ) ) ;

}

// ------------ method called once each job just before starting event loop  ------------
void AnalysisTreeFiller::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void AnalysisTreeFiller::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void AnalysisTreeFiller::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void AnalysisTreeFiller::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void AnalysisTreeFiller::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void AnalysisTreeFiller::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void AnalysisTreeFiller::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

}

//define this as a plug-in
DEFINE_FWK_MODULE(AnalysisTreeFiller);
