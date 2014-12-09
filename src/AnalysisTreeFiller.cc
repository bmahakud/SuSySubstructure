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
//#include "SandBox/Skims/plugins/ElectronEffectiveArea.h"

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

//#include "GSFelectronInterface.h"

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
  
  double fixedGridRhoFastjetAll, fixedGridRhoFastjetAllCalo, fixedGridRhoFastjetCentralCalo, fixedGridRhoFastjetCentralChargedPileUp, fixedGridRhoFastjetCentralNeutral;

  int nVrtx ; 

  double MET ; 
  double METsig ; 

  std::vector< double > genMuonPt;
  std::vector< double > genMuonEta;
  std::vector< double > genMuonPhi;
  std::vector< double > genMuonE;

  std::vector< double > muonPt;
  std::vector< double > muonEta;
  std::vector< double > muonPhi;
  std::vector< double > muonE;
  std::vector< double > muonRelIso;
  std::vector< bool >   muonPassID;

  int NMuons;

  std::vector< double > genElectronPt;
  std::vector< double > genElectronEta;
  std::vector< double > genElectronPhi;
  std::vector< double > genElectronE;

  std::vector< double > genParPt;
  std::vector< double > genParEta;
  std::vector< double > genParPhi;
  std::vector< double > genParE;
  std::vector< double > genParPDGid;
  std::vector< double > genParStatus;
  
  std::vector< double > electronPt;
  std::vector< double > electronEta;
  std::vector< double > electronPhi;
  std::vector< double > electronE;
  std::vector< double > electronNeutralIso;
  std::vector< double > electronChargedIso;
  std::vector< double > electronPhotonIso;

  int NElectrons;

  std::vector< double > genPhotonPt;
  std::vector< double > genPhotonEta;
  std::vector< double > genPhotonPhi;
  std::vector< double > genPhotonE;

  std::vector< double > photonPt;
  std::vector< double > photonEta;
  std::vector< double > photonPhi;
  std::vector< double > photonE;
  std::vector< double > photon_isEB;
  std::vector< double > photon_genMatched;
  std::vector< double > photon_hadTowOverEm;
  std::vector< double > photon_sigmaIetaIeta;
  std::vector< double > photon_pfChargedIso;
  std::vector< double > photon_pfNeutralIso;
  std::vector< double > photon_pfGammaIso;
  std::vector< double > photon_ConeDR03ecalEtIso;
  std::vector< double > photon_ConeDR03hcalEtIso;
  std::vector< double > photon_ConeDR03trkPtIso;
  std::vector< bool >   photon_passElectronConvVeto;
  std::vector< bool >   photon_hasPixelSeed;
  
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
  std::vector< edm::InputTag > elIsoValsSrc ; // electrons isolations
  std::vector< edm::InputTag > phIsoValsSrc ; // photon isolations

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
  elIsoValsSrc(iConfig.getParameter<std::vector<edm::InputTag> >("EleIsoValInputTags")),  //elPFIsoValueCharged03PFIdPFIso, elPFIsoValueGamma03PFIdPFIso, elPFIsoValueNeutral03PFIdPFIso
  phIsoValsSrc(iConfig.getParameter<std::vector<edm::InputTag> >("PhotonIsoValInputTags")),  //phPFIsoValueCharged03PFIdPFIso, phPFIsoValueGamma03PFIdPFIso, phPFIsoValueNeutral03PFIdPFIso
  debug(iConfig.getUntrackedParameter<bool>("debug",false))
{

  edm::Service<TFileService> fs;

  AnalysisTree            = fs->make<TTree>("AnalysisTree","AnalysisTree");

  // set branches
  // --------------------------

  AnalysisTree->Branch("event",&event);
  AnalysisTree->Branch("run",&run);
  AnalysisTree->Branch("lumi",&lumi);

  AnalysisTree->Branch( "fixedGridRhoFastjetAll", &fixedGridRhoFastjetAll ) ;
  AnalysisTree->Branch( "fixedGridRhoFastjetAllCalo", &fixedGridRhoFastjetAllCalo ) ;
  AnalysisTree->Branch( "fixedGridRhoFastjetCentralCalo", &fixedGridRhoFastjetCentralCalo ) ;
  AnalysisTree->Branch( "fixedGridRhoFastjetCentralChargedPileUp", &fixedGridRhoFastjetCentralChargedPileUp ) ;
  AnalysisTree->Branch( "fixedGridRhoFastjetCentralNeutral", &fixedGridRhoFastjetCentralNeutral ) ;

  AnalysisTree->Branch( "nVrtx" , &nVrtx ) ;
  
  AnalysisTree->Branch("MET",&MET);
  AnalysisTree->Branch("METsig",&METsig);

  AnalysisTree->Branch("genElectronPt",&genElectronPt);
  AnalysisTree->Branch("genElectronEta",&genElectronEta);
  AnalysisTree->Branch("genElectronPhi",&genElectronPhi);
  AnalysisTree->Branch("genElectronE",&genElectronE);

  AnalysisTree->Branch("electronPt",&electronPt);
  AnalysisTree->Branch("electronEta",&electronEta);
  AnalysisTree->Branch("electronPhi",&electronPhi);
  AnalysisTree->Branch("electronE",&electronE);
  AnalysisTree->Branch("electronNeutralIso",&electronNeutralIso);
  AnalysisTree->Branch("electronChargedIso",&electronChargedIso);
  AnalysisTree->Branch("electronPhotonIso",&electronPhotonIso);
  AnalysisTree->Branch("NElectrons",&NElectrons);

  AnalysisTree->Branch("genMuonPt",&genMuonPt);
  AnalysisTree->Branch("genMuonEta",&genMuonEta);
  AnalysisTree->Branch("genMuonPhi",&genMuonPhi);
  AnalysisTree->Branch("genMuonE",&genMuonE);

  AnalysisTree->Branch("muonPt",&muonPt);
  AnalysisTree->Branch("muonEta",&muonEta);
  AnalysisTree->Branch("muonPhi",&muonPhi);
  AnalysisTree->Branch("muonE",&muonE);
  AnalysisTree->Branch("muonRelIso",&muonRelIso);
  AnalysisTree->Branch("muonPassID",&muonPassID);
  AnalysisTree->Branch("NMuons",&NMuons);

  AnalysisTree->Branch("genPhotonPt",&genPhotonPt);
  AnalysisTree->Branch("genPhotonEta",&genPhotonEta);
  AnalysisTree->Branch("genPhotonPhi",&genPhotonPhi);
  AnalysisTree->Branch("genPhotonE",&genPhotonE);

  AnalysisTree->Branch("genParPt",&genParPt);
  AnalysisTree->Branch("genParEta",&genParEta);
  AnalysisTree->Branch("genParPhi",&genParPhi);
  AnalysisTree->Branch("genParE",&genParE);
  AnalysisTree->Branch("genParPDGid",&genParPDGid);
  AnalysisTree->Branch("genParStatus",&genParStatus);

  AnalysisTree->Branch("photonPt",&photonPt);
  AnalysisTree->Branch("photonEta",&photonEta);
  AnalysisTree->Branch("photonPhi",&photonPhi);
  AnalysisTree->Branch("photonE",&photonE);
  AnalysisTree->Branch("photon_isEB",&photon_isEB);
  AnalysisTree->Branch("photon_genMatched",&photon_genMatched);
  AnalysisTree->Branch("photon_hadTowOverEm",&photon_hadTowOverEm);  
  AnalysisTree->Branch("photon_sigmaIetaIeta",&photon_sigmaIetaIeta);
  AnalysisTree->Branch("photon_pfChargedIso",&photon_pfChargedIso);
  AnalysisTree->Branch("photon_pfNeutralIso",&photon_pfNeutralIso);
  AnalysisTree->Branch("photon_pfGammaIso",&photon_pfGammaIso);
  AnalysisTree->Branch("photon_ConeDR03ecalEtIso",&photon_ConeDR03ecalEtIso);
  AnalysisTree->Branch("photon_ConeDR03hcalEtIso",&photon_ConeDR03hcalEtIso);
  AnalysisTree->Branch("photon_ConeDR03trkPtIso" ,&photon_ConeDR03trkPtIso );
  AnalysisTree->Branch("photon_passElectronConvVeto",&photon_passElectronConvVeto);
  AnalysisTree->Branch("photon_hasPixelSeed",&photon_hasPixelSeed);

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

  genMuonPt.clear();
  genMuonEta.clear();
  genMuonPhi.clear();
  genMuonE.clear();

  genElectronPt.clear();
  genElectronEta.clear();
  genElectronPhi.clear();
  genElectronE.clear();

  genPhotonPt.clear();
  genPhotonEta.clear();
  genPhotonPhi.clear();
  genPhotonE.clear();

  genParPt.clear();
  genParEta.clear();
  genParPhi.clear();
  genParE.clear();
  genParPDGid.clear();
  genParStatus.clear();

  std::vector<int> pdgIdOfInterest;
  pdgIdOfInterest.push_back(21);
  pdgIdOfInterest.push_back(22);
  pdgIdOfInterest.push_back(23);
  pdgIdOfInterest.push_back(24);
  pdgIdOfInterest.push_back(25);

  pdgIdOfInterest.push_back(1);
  pdgIdOfInterest.push_back(2);
  pdgIdOfInterest.push_back(3);
  pdgIdOfInterest.push_back(4);
  pdgIdOfInterest.push_back(5);
  pdgIdOfInterest.push_back(6);

  pdgIdOfInterest.push_back(11);
  pdgIdOfInterest.push_back(12);
  pdgIdOfInterest.push_back(13);
  pdgIdOfInterest.push_back(14);
  pdgIdOfInterest.push_back(15);
  pdgIdOfInterest.push_back(16);

  pdgIdOfInterest.push_back(1000021);
  pdgIdOfInterest.push_back(1000022);
  pdgIdOfInterest.push_back(1000023);
  pdgIdOfInterest.push_back(1000025);
  pdgIdOfInterest.push_back(1000035);

  pdgIdOfInterest.push_back(1000001);
  pdgIdOfInterest.push_back(1000002);
  pdgIdOfInterest.push_back(1000003);
  pdgIdOfInterest.push_back(1000004);
  pdgIdOfInterest.push_back(1000005);
  pdgIdOfInterest.push_back(1000006);

  pdgIdOfInterest.push_back(2000001);
  pdgIdOfInterest.push_back(2000002);
  pdgIdOfInterest.push_back(2000003);
  pdgIdOfInterest.push_back(2000004);
  pdgIdOfInterest.push_back(2000005);
  pdgIdOfInterest.push_back(2000006);

  Handle< View<reco::Candidate> > genPartCands;
  iEvent.getByLabel( "packedGenParticles" ,genPartCands);

  for(View<reco::Candidate>::const_iterator iPart = genPartCands->begin();
        iPart != genPartCands->end();
        ++iPart){

    if( iPart->pdgId() == 1000022 ){
   
      //cout << "gen particle: " << iPart->pdgId() << " status: " << iPart->status() << endl;
      //cout << "pt: " << iPart->pt() << " eta: " << iPart->eta() << " phi: " << iPart->phi() << " energy: " << iPart->energy() << endl;

      genParPt.push_back( iPart->pt() );
      genParEta.push_back( iPart->eta() );
      genParPhi.push_back( iPart->phi() );
      genParE.push_back( iPart->energy() );

      genParPDGid.push_back( iPart->pdgId() );
      genParStatus.push_back( iPart->status() );

    }

  }

  iEvent.getByLabel( "prunedGenParticles" ,genPartCands);

  for(View<reco::Candidate>::const_iterator iPart = genPartCands->begin();
        iPart != genPartCands->end();
        ++iPart){

    if( std::find( pdgIdOfInterest.begin(), pdgIdOfInterest.end(), abs(iPart->pdgId()) ) != pdgIdOfInterest.end() && abs( iPart->status() ) >20 && abs( iPart->status() ) <30 ){
            
      genParPt.push_back( iPart->pt() );
      genParEta.push_back( iPart->eta() );
      genParPhi.push_back( iPart->phi() );
      genParE.push_back( iPart->energy() );

      genParPDGid.push_back( iPart->pdgId() );
      genParStatus.push_back( iPart->status() );

    }
    
    if( abs( iPart->pdgId() ) == 23 && abs(iPart->status()) > 20 && abs(iPart->status()) < 30){ 

      if( debug )
	std::cout << "found Z, status: " << iPart->status() << std::endl;

      // check to see that Z decays to muons
      if( abs( iPart->daughter(0)->pdgId() ) == 13 &&
	  abs( iPart->daughter(1)->pdgId() ) == 13 ){

	genMuonPt.push_back( iPart->daughter(0)->pt() );
	genMuonEta.push_back( iPart->daughter(0)->eta() );
	genMuonPhi.push_back( iPart->daughter(0)->phi() );
	genMuonE.push_back( iPart->daughter(0)->energy() );
	
	genMuonPt.push_back( iPart->daughter(1)->pt() );
	genMuonEta.push_back( iPart->daughter(1)->eta() );
	genMuonPhi.push_back( iPart->daughter(1)->phi() );
	genMuonE.push_back( iPart->daughter(1)->energy() );
	
      }// end of muonic z decay...

      // check to see that Z decays to muons
      if( abs( iPart->daughter(0)->pdgId() ) == 11 &&
	  abs( iPart->daughter(1)->pdgId() ) == 11 ){

	genElectronPt.push_back( iPart->daughter(0)->pt() );
	genElectronEta.push_back( iPart->daughter(0)->eta() );
	genElectronPhi.push_back( iPart->daughter(0)->phi() );
	genElectronE.push_back( iPart->daughter(0)->energy() );
	
	genElectronPt.push_back( iPart->daughter(1)->pt() );
	genElectronEta.push_back( iPart->daughter(1)->eta() );
	genElectronPhi.push_back( iPart->daughter(1)->phi() );
	genElectronE.push_back( iPart->daughter(1)->energy() );
	
      }// end of electronic z decay...

    }// end Z stuff

    if( abs( iPart->pdgId() ) == 22 && abs(iPart->status()) > 20 && abs(iPart->status()) < 30 ){

      if( debug ){
	std::cout << "-------" << std::endl;
	std::cout << "found photon, status: " << iPart->status() << std::endl;
	std::cout << "pt: " << iPart->pt() << " eta: " << iPart->eta() << " phi: " << iPart->phi() << " e: " << iPart->energy() << std::endl;
      }
      
      genPhotonPt.push_back( iPart->pt() );
      genPhotonEta.push_back( iPart->eta() );
      genPhotonPhi.push_back( iPart->phi() );
      genPhotonE.push_back( iPart->energy() );
      
    }// end photon stuff

  }// end of loop over gen-particles

  // -- Monte Carlo Event Weight
  eventWeight = 1.0 ;
  edm::Handle< GenEventInfoProduct > genEventInfo;
  iEvent.getByLabel("generator", genEventInfo);
  
  if ( genEventInfo.isValid() ){
    
    if( debug )
      std::cout << genEventInfo->weight() << std::endl;

    eventWeight = genEventInfo->weight();

  }

  edm::Handle< std::vector<reco::Vertex> > vertices;
  iEvent.getByLabel(vtxSrc, vertices);
  nVrtx = vertices->size() ;

  reco::Vertex::Point vtxpos = (vertices->size() > 0 ? (*vertices)[0].position() : reco::Vertex::Point());

  // rho variables &&&&&&&&&&&&&&&&

  edm::Handle< double > rho;
  iEvent.getByLabel("fixedGridRhoFastjetAll",rho);
  fixedGridRhoFastjetAll = *rho;
  iEvent.getByLabel("fixedGridRhoFastjetAllCalo",rho);
  fixedGridRhoFastjetAllCalo = *rho;
  iEvent.getByLabel("fixedGridRhoFastjetCentralCalo",rho);
  fixedGridRhoFastjetCentralCalo = *rho;
  iEvent.getByLabel("fixedGridRhoFastjetCentralChargedPileUp",rho);
  fixedGridRhoFastjetCentralChargedPileUp = *rho;
  iEvent.getByLabel("fixedGridRhoFastjetCentralNeutral",rho);
  fixedGridRhoFastjetCentralNeutral = *rho;

  // &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

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

  if( debug ) std::cout << "got muon collection" << std::endl;
  

  muonPt.clear();
  muonEta.clear();
  muonPhi.clear();
  muonE.clear();
  muonPassID.clear();
  muonRelIso.clear();
  NMuons = 0;


  for(View<pat::Muon>::const_iterator iMuon = muonCands->begin();
        iMuon != muonCands->end();
        ++iMuon){

    //if( iMuon->pt() < 10. || fabs( iMuon->eta() ) > 2.4 ) continue ;

    if( debug ){
      std::cout << "muon pt: " << iMuon->pt() << std::endl;
      std::cout << "muon eta: " << iMuon->eta() << std::endl;
      std::cout << "muon phi: " << iMuon->phi() << std::endl;
    }

    muonPt.push_back( iMuon->pt() );
    muonEta.push_back( iMuon->eta() ); 
    muonPhi.push_back( iMuon->phi() );
    muonE.push_back( iMuon->energy() );
    
    if( debug ) std::cout << "muon isolation" << std::endl;

    muonRelIso.push_back( (iMuon->pfIsolationR04().sumChargedHadronPt + std::max(0., iMuon->pfIsolationR04().sumNeutralHadronEt + iMuon->pfIsolationR04().sumPhotonEt - 0.5*iMuon->pfIsolationR04().sumPUPt) )/ iMuon->pt() );

    bool pass = false;
    
    if( debug ) std::cout << "muon ID" << std::endl;

    if( iMuon->globalTrack().isNonnull() ){

      if( !iMuon->isPFMuon()  || 
	  iMuon->globalTrack()->normalizedChi2() >= 10. ||
	  iMuon->globalTrack()->hitPattern().numberOfValidMuonHits() <= 0 ||
	  iMuon->numberOfMatchedStations() <=1 ||
	  iMuon->innerTrack()->hitPattern().numberOfValidPixelHits() == 0 ||
	  iMuon->innerTrack()->hitPattern().trackerLayersWithMeasurement() <=5 ||
	  std::abs(iMuon->innerTrack()->dxy(vtxpos)) >= 0.2 && vertices->size() > 0 ||
	  std::abs(iMuon->innerTrack()->dz(vtxpos))  >= 0.5 && vertices->size() > 0 ) pass = false;
      else pass = true;
      
    }

    muonPassID.push_back(pass);
    
    NMuons++;
    
  }

  // Photon
  // ===========================
  // ---------------------------

  /*
  std::vector< double > photonPt;		    
  std::vector< double > photonEta;		    
  std::vector< double > photonPhi;		    
  std::vector< double > photonE;		    
  std::vector< double > photon_hadTowOverEm;	    
  std::vector< double > photon_sigmaIetaIeta;	    
  std::vector< double > photon_pfChargedIso;	    
  std::vector< double > photon_pfNeutralIso;	    
  std::vector< double > photon_pfGammaIso;	    
  std::vector< double > photon_ConeDR03ecalEtIso;   
  std::vector< double > photon_ConeDR03hcalEtIso;   
  std::vector< double > photon_ConeDR03trkPtIso;    
  std::vector< bool >   photon_passElectronConvVeto;
  std::vector< bool >   photon_hasPixelSeed;        
  
  int NPhotons;
 
  */

  Handle< View< pat::Photon> > photonCands;
  iEvent.getByLabel( photonCollection ,photonCands);

  if( debug ) std::cout << "got photon collection" << std::endl;

  NPhotons=0;
  photonPt.clear();		    
  photonEta.clear();		    
  photonPhi.clear();		    
  photonE.clear();		    
  photon_isEB.clear();
  photon_genMatched.clear();
  photon_hadTowOverEm.clear();	    
  photon_sigmaIetaIeta.clear();	    
  photon_pfChargedIso.clear();	    
  photon_pfNeutralIso.clear();	    
  photon_pfGammaIso.clear();	    
  photon_ConeDR03ecalEtIso.clear();   
  photon_ConeDR03hcalEtIso.clear();   
  photon_ConeDR03trkPtIso.clear();    
  photon_passElectronConvVeto.clear();
  photon_hasPixelSeed.clear();        

  for( View< pat::Photon >::const_iterator iPhoton = photonCands->begin();
        iPhoton != photonCands->end();
        ++iPhoton){

    if( debug ) {
      std::cout << "photon pt: " << iPhoton->pt() << std::endl;
      std::cout << "photon eta: " << iPhoton->eta() << std::endl;
      std::cout << "photon phi: " << iPhoton->phi() << std::endl;
    }

    photonPt.push_back( iPhoton->pt() );
    photonEta.push_back( iPhoton->eta() ); 
    photonPhi.push_back( iPhoton->phi() );
    photonE.push_back( iPhoton->energy() );

    photon_isEB.push_back( iPhoton->isEB() );
    photon_genMatched.push_back( iPhoton->genPhoton() != NULL );
    photon_hadTowOverEm.push_back( iPhoton->hadTowOverEm() ) ;
    photon_sigmaIetaIeta.push_back( iPhoton->sigmaIetaIeta() ) ;
    
    photon_pfChargedIso.push_back(      iPhoton->chargedHadronIso() );
    photon_pfGammaIso.push_back(        iPhoton->photonIso() );
    photon_pfNeutralIso.push_back(      iPhoton->neutralHadronIso() );
    photon_ConeDR03ecalEtIso.push_back( iPhoton->ecalRecHitSumEtConeDR03() );
    photon_ConeDR03hcalEtIso.push_back( iPhoton->hcalTowerSumEtConeDR03() );
    photon_ConeDR03trkPtIso.push_back(  iPhoton->trkSumPtSolidConeDR03() );

    photon_passElectronConvVeto.push_back( iPhoton->userFloat("passElectronConvVeto") ) ;    
    photon_hasPixelSeed.push_back( iPhoton->hasPixelSeed() );
    NPhotons++;

  }

  // Electrons
  // ===========================
  // ---------------------------

  // get electrons
  Handle< View< pat::Electron > > electronCands;
  iEvent.getByLabel( electronCollection ,electronCands);

  if( debug ) std::cout << "got electron collection" << std::endl;

  //GSFelectronInterface eleTool( electronCollection , conversionsSrc , vtxSrc , beamSpotSrc , rhoIsoSrc , elIsoValsSrc ) ; 

  electronPt.clear();
  electronEta.clear();
  electronPhi.clear();
  electronE.clear();
  electronNeutralIso.clear();
  electronChargedIso.clear();
  electronPhotonIso.clear();

  NElectrons = 0 ;

  for( View< pat::Electron >::const_iterator iEle = electronCands->begin();
        iEle != electronCands->end();
        ++iEle){

    //for(unsigned int i = 0 ; i < electronCands->size(); ++i){
  
    //electronData myEle = eleTool.passIDandISO( iEvent , i ) ;
   
    if( debug ) {
      std::cout << "electron pt: " << iEle->pt() << std::endl;
      std::cout << "electron eta: " << iEle->eta() << std::endl;
      std::cout << "electron phi: " << iEle->phi() << std::endl;
    }

    electronPt.push_back( iEle->pt() );
    electronEta.push_back( iEle->eta() ); 
    electronPhi.push_back( iEle->phi() );
    electronE.push_back( iEle->energy() );
    electronNeutralIso.push_back( iEle->pfIsolationVariables().sumNeutralHadronEt );
    electronChargedIso.push_back( iEle->pfIsolationVariables().sumChargedHadronPt );
    electronPhotonIso.push_back( iEle->pfIsolationVariables().sumPhotonEt );
    NElectrons++;
    
  }

  // start section where jet collections will be looped over!!
  // ===================
  // -------------------
  for ( unsigned int iJetColl = 0 ; iJetColl < jetCollectionList.size() ; iJetColl++ ){

    if( debug ) std::cout << jetCollectionList[ iJetColl ] << std::endl;

    Handle< View<reco::Candidate> > jetCands;
    iEvent.getByLabel( jetCollectionList[ iJetColl ],jetCands);
    if( debug ) std::cout << "got jet collection" << std::endl;

    // set all variables in struct to zero or clear std::vectors
    zeroJetKinematics( *jetKin[ iJetColl ] );
    if( debug ) std::cout << "reset jet kin struct" << std::endl;

    // for calculating missHt
    double negativePx_pt30 = 0.; 
    double negativePy_pt30 = 0.; 

    for(View<reco::Candidate>::const_iterator iJet = jetCands->begin();
        iJet != jetCands->end();
        ++iJet){

      if( debug ){
	std::cout << "jet pt: " << iJet->pt() << std::endl;
	std::cout << "jet eta: " << iJet->eta() << std::endl;
	std::cout << "jet phi: " << iJet->phi() << std::endl;
	std::cout << "jet mass: " << iJet->mass() << std::endl;
      }

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

   if( pseudoParticleCollectionList[ iParticleColl ] == "" ) continue;

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
     
     particleKin[ iParticleColl ]->sumJetMass += p4.mass() ;
       
     particleKin[ iParticleColl ]->pt.push_back  (   p4.pt()   );
     particleKin[ iParticleColl ]->eta.push_back (   p4.eta()  );
     particleKin[ iParticleColl ]->phi.push_back (   p4.phi()  );
     particleKin[ iParticleColl ]->mass.push_back(   p4.mass() );
     
     particleKin[ iParticleColl ]->HT  += p4.pt();
     
     negativePx_pt30        -= p4.px();
     negativePy_pt30        -= p4.py();
     
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
