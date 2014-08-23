#ifndef GSFELECTRONINTERFACE
#define GSFELECTRONINTERFACE

#include <memory>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
//#include "DataFormats/Common/interface/View.h"
//#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
#include "DataFormats/RecoCandidate/interface/IsoDeposit.h"
//#include "EGamma/EGammaAnalysisTools/interface/EGammaCutBasedEleId.h"
#include "SandBox/Skims/plugins/ElectronEffectiveArea.h"

typedef std::vector< edm::Handle< edm::ValueMap<double> > >             IsoDepositVals;

struct electronData{
  double pt ; 
  double eta ; 
  double phi ; 
  double e ; 
  double iso_ch ;
  double iso_em ;
  double iso_nh ;
  double combIso ;
  double effA ;
  double rho ;
  bool passISO ;
  bool passID ; 
  bool isEB ; 
};

class GSFelectronInterface {

  public:

  GSFelectronInterface( edm::InputTag electronSrc_ , 
			edm::InputTag conversionsSrc_ , 
			edm::InputTag vtxSrc_ , 
			edm::InputTag beamSpotSrc_ , 
			edm::InputTag rhoIsoSrc_ , 
			std::vector< edm::InputTag > isoValsSrc_ , 
			double minElePt = 10. , 
			double maxEleEta = 2.4 , 
			bool debug_ = false
			);
    
  ~GSFelectronInterface();
  
  electronData passIDandISO(const edm::Event & iEvent, unsigned int i );

  private:
  
  edm::InputTag electronSrc;
  edm::InputTag conversionsSrc;
  edm::InputTag vtxSrc;
  edm::InputTag beamSpotSrc;
  edm::InputTag rhoIsoSrc;
  std::vector<edm::InputTag>  isoValsSrc;
  double minElePt, maxEleEta;
  bool debug;

};

GSFelectronInterface::GSFelectronInterface( edm::InputTag electronSrc_ , 
		      edm::InputTag conversionsSrc_ , 
		      edm::InputTag vtxSrc_ , 
		      edm::InputTag beamSpotSrc_ , 
		      edm::InputTag rhoIsoSrc_ , 
		      std::vector< edm::InputTag > isoValsSrc_ , 
		      double minElePt_ , 
		      double maxEleEta_ , 
		      bool debug_
		      ){
  
  beamSpotSrc = beamSpotSrc_;
  vtxSrc = vtxSrc_;
  rhoIsoSrc = rhoIsoSrc_;
  conversionsSrc = conversionsSrc_;
  isoValsSrc = isoValsSrc_;
  electronSrc = electronSrc_;
  minElePt = minElePt_ ; 
  maxEleEta = maxEleEta_ ; 
  debug = debug_ ;

}


GSFelectronInterface::~GSFelectronInterface() {
}


electronData GSFelectronInterface::passIDandISO(const edm::Event& iEvent, unsigned int i){

  electronData myEle;

  myEle.pt     = -99. ; 
  myEle.eta    = -99. ; 
  myEle.phi    = -99. ; 
  myEle.e      = -99. ; 
  myEle.iso_ch = -99. ;
  myEle.iso_em = -99. ;
  myEle.iso_nh = -99. ;
  myEle.combIso= -99. ;
  myEle.effA   = -99. ;
  myEle.rho    = -99. ;
  myEle.passISO = false ;
  myEle.passID  = false ; 
  myEle.isEB  = false ; 

  // electrons
  edm::Handle< std::vector<reco::GsfElectron> > electrons;   
  iEvent.getByLabel(electronSrc, electrons);

  // conversions
  edm::Handle< std::vector<reco::Conversion> > conversions;
  iEvent.getByLabel(conversionsSrc, conversions);

  // iso deposits
  IsoDepositVals isoVals(isoValsSrc.size());
  for (size_t j = 0; j < isoValsSrc.size(); ++j) {
    iEvent.getByLabel(isoValsSrc[j], isoVals[j]);
  }
  
  // beam spot
  edm::Handle<reco::BeamSpot> beamspot;
  iEvent.getByLabel(beamSpotSrc, beamspot);
  const reco::BeamSpot &beamSpot = *(beamspot.product());
  
  // vertices
  edm::Handle< std::vector<reco::Vertex> > vertices;
  iEvent.getByLabel(vtxSrc, vertices);

  // rho for isolation                                                                                                
  edm::Handle<double> rhoIsoH;
  iEvent.getByLabel(rhoIsoSrc, rhoIsoH);
  double rhoIso = *(rhoIsoH.product());

  float cut_dEtaIn[2]         = {999.9, 999.9};
  float cut_dPhiIn[2]         = {999.9, 999.9};
  float cut_sigmaIEtaIEta[2]  = {999.9, 999.9};
  float cut_hoe[2]            = {999.9, 999.9};
  float cut_ooemoop[2]        = {999.9, 999.9};
  float cut_d0vtx[2]          = {999.9, 999.9};
  float cut_dzvtx[2]          = {999.9, 999.9};
  float cut_iso[2]            = {999.9, 999.9};
  bool cut_vtxFit[2]          = {false, false};
  unsigned int cut_mHits[2]   = {999, 999};
    
  cut_dEtaIn[0]        = 0.007; cut_dEtaIn[1]        = 0.010;
  cut_dPhiIn[0]        = 0.800; cut_dPhiIn[1]        = 0.700;
  cut_sigmaIEtaIEta[0] = 0.010; cut_sigmaIEtaIEta[1] = 0.030;
  cut_hoe[0]           = 0.150; cut_hoe[1]           = 999.9;
  cut_ooemoop[0]       = 999.9; cut_ooemoop[1]       = 999.9;
  cut_d0vtx[0]         = 0.040; cut_d0vtx[1]         = 0.040;
  cut_dzvtx[0]         = 0.200; cut_dzvtx[1]         = 0.200;
  cut_vtxFit[0]        = false; cut_vtxFit[1]        = false;
  cut_mHits[0]         = 999  ; cut_mHits[1]         = 999;
  cut_iso[0]           = 0.150; cut_iso[1]           = 0.150;
  
  // check which ones to keep
  std::auto_ptr<std::vector<reco::GsfElectron> > prod(new std::vector<reco::GsfElectron>());


  // get reference to electron
  reco::GsfElectronRef ele(electrons, i);

  double pt = ele->pt();
  if (ele->pt() < minElePt ) return myEle;

  myEle.pt = ele->pt();
  myEle.eta = ele->eta();
  myEle.phi = ele->phi();
  myEle.e = ele->energy();

  // get particle flow isolation
  double iso_ch = (*(isoVals)[0])[ele];
  double iso_em = (*(isoVals)[1])[ele];
  double iso_nh = (*(isoVals)[2])[ele];
  
  // working points
  //bool veto       = EgammaCutBasedEleId::PassWP(EgammaCutBasedEleId::VETO, ele, conversions, beamSpot, vertices, iso_ch, iso_em, iso_nh, rhoIso);

  // get the ID variables from the electron object
  // kinematic variables
  bool isEB           = ele->isEB() ? true : false;
  myEle.isEB = isEB ; 
  float eta           = ele->superCluster()->eta();

  // id variables
  float dEtaIn        = ele->deltaEtaSuperClusterTrackAtVtx();
  float dPhiIn        = ele->deltaPhiSuperClusterTrackAtVtx();
  float sigmaIEtaIEta = ele->sigmaIetaIeta();
  float hoe           = ele->hadronicOverEm();
  float ooemoop       = (1.0/ele->ecalEnergy() - ele->eSuperClusterOverP()/ele->ecalEnergy());

  // impact parameter variables
  float d0vtx         = 0.0;
  float dzvtx         = 0.0;
  if (vertices->size() > 0) {
    reco::VertexRef vtx(vertices, 0);    
    d0vtx = ele->gsfTrack()->dxy(vtx->position());
    dzvtx = ele->gsfTrack()->dz(vtx->position());
  } else {
    d0vtx = ele->gsfTrack()->dxy();
    dzvtx = ele->gsfTrack()->dz();
  }

  // conversion rejection variables
  bool vtxFitConversion = ConversionTools::hasMatchedConversion( *ele, conversions, beamSpot.position());
  float mHits = ele->gsfTrack()->trackerExpectedHitsInner().numberOfHits(); 
  
  // choose cut if barrel or endcap
  unsigned int idx = isEB ? 0 : 1;

  // test cuts
  if (fabs(dEtaIn) > cut_dEtaIn[idx] ||
      fabs(dPhiIn) > cut_dPhiIn[idx] ||
      sigmaIEtaIEta > cut_sigmaIEtaIEta[idx] ||
      hoe > cut_hoe[idx] ||
      fabs(ooemoop) > cut_ooemoop[idx] ||
      fabs(d0vtx) > cut_d0vtx[idx] ||
      fabs(dzvtx) > cut_dzvtx[idx] ||  
      //( !cut_vtxFit[idx] || !vtxFitConversion)  &&
      mHits > cut_mHits[idx]) myEle.passID = false;
  else 
    myEle.passID = true ;

  if(debug) {
    reco::VertexRef vtx(vertices, 0);
    std::cout << "iEle " << i << ": "
	<< " (pt,eta,phi) "<<ele->pt()<<", "<<ele->eta()<<", "<<ele->phi() << " "
	<< ", isEB " << ele->isEB() << ", isEE " << ele->isEE() << "\n"
	<< ", dEtaIn " << ele->deltaEtaSuperClusterTrackAtVtx()
	<< ", dPhiIn " << ele->deltaPhiSuperClusterTrackAtVtx()
	<< ", sigmaIEtaIEta "<< ele->sigmaIetaIeta()
	<< ", hoe " << ele->hadronicOverEm()
	<< ", d0vtx " << ele->gsfTrack()->dxy(vtx->position())
	<< ", dzvtx " << ele->gsfTrack()->dz(vtx->position())
	<< ", passSelection " 
	<< std::endl;
  }


  // isolation cuts                                                                                                                                        
  // effective area for isolation
  float AEff = ElectronEffectiveArea::GetElectronEffectiveArea(ElectronEffectiveArea::kEleGammaAndNeutralHadronIso03, eta, ElectronEffectiveArea::kEleEAData2012);

  // apply to neutrals
  double rhoPrime = std::max(rhoIso, 0.0);
  double iso_n = std::max(iso_nh + iso_em - rhoPrime * AEff, 0.0);

  // compute final isolation
  myEle.combIso = (iso_n + iso_ch)/pt;

  myEle.iso_ch = iso_ch ;
  myEle.iso_em = iso_em ;
  myEle.iso_nh = iso_nh ;
  myEle.effA   = AEff ;
  myEle.rho    = rhoPrime ;

  if(myEle.combIso > cut_iso[idx]) myEle.passISO = false ;

  return myEle;
  
}

#endif
