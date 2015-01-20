//Author
//Bibhuprasad Mahakud
//email: bmahakud@cern.ch

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

#include "AWhitbeck/SuSySubstructure/interface/NsubjettinessProducer.h"

#include "TH1.h"
#include "TH2.h"
#include "TLorentzVector.h"
#include "TTree.h"

#include <DataFormats/JetReco/interface/Jet.h>
#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include <fastjet/ClusterSequence.hh>
#include <fastjet/PseudoJet.hh>
#include <fastjet/JetDefinition.hh>
#include <fastjet/tools/Filter.hh>

#include "SubjetCounting.hh"
#include "Nsubjettiness.hh"
#include "Njettiness.hh"
#include "NjettinessPlugin.hh"

#include <vector>

NsubjettinessProducer::NsubjettinessProducer(const edm::ParameterSet& iConfig):
  jetCollection(iConfig.getUntrackedParameter<std::string>("jetCollection","ak12Jets")),
  particleCollection(iConfig.getUntrackedParameter<std::string>("particleCollection","packedPFCandidates")),
  clusterRadius(iConfig.getUntrackedParameter<double>("clusterRadius",1.2)),
  trimPtFracMin(iConfig.getUntrackedParameter<double>("trimPtFracMin",0.05)),
  trimJets(iConfig.getUntrackedParameter<bool>("trimJets",true)),
  subjetPtCut(iConfig.getUntrackedParameter<double>("subjetPtCut",30.)),
  subjetMassCut(iConfig.getUntrackedParameter<double>("subjetMassCut",30.)),
  subjetRcut(iConfig.getUntrackedParameter<double>("subjetRcut",0.15)),
  subjetPtImbalance(iConfig.getUntrackedParameter<double>("subjetPtImbalance",.15)),
  debug(iConfig.getUntrackedParameter<bool>("debug",true))

{
  //produces< std::vector< reco::Jet > >(jetCollection+"-Subjets");
  produces< std::vector< math::XYZTLorentzVector > >(""); //(jetCollection+"-Subjets"); 
  
  //produces< std::vector< math::XYZTLorentzVector > >("ak12JetsTlzv");
  produces< std::vector< double > >("tau1");
  produces< std::vector< double > >("tau2");
  produces< std::vector< double > >("tau3");
  produces< std::vector< double > >("tau4");
  produces< std::vector< double > >("ak12Px");
  produces< std::vector< double > >("ak12Py");
  produces< std::vector< double > >("ak12Pz");
  produces< std::vector< double > >("ak12E"); 
  
 produces< std::vector< int > >("NumSubjets");
 







}


NsubjettinessProducer::~NsubjettinessProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
NsubjettinessProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{

  // fill histograms for di-lepton system
  //std::cout<<"testing .."<<std::endl;
  using namespace edm;
  using namespace std;  


  edm::EventID eventId = iEvent.id();
  cout<<"Event no = "<<eventId<<endl;

 
  edm::Handle<edm::View<pat::PackedCandidate> > PFCands;
  iEvent.getByLabel(particleCollection,PFCands);

   
  std::vector<fastjet::PseudoJet> ak12Jets;
  std::vector<fastjet::PseudoJet> particles; particles.clear();
  fastjet::JetDefinition Jetdefak12(fastjet::antikt_algorithm, 1.2);


  //PFcandidates are stored for reclustering   
  for(edm::View<pat::PackedCandidate>::const_iterator iPFcand = PFCands->begin(); iPFcand != PFCands->end(); ++iPFcand){
    
 // cout<<"px = "<<iPFcand->px()<<endl; 

   particles.push_back( fastjet::PseudoJet( iPFcand->px(),
                                                  iPFcand->py(),
                                                  iPFcand->pz(),
                                                  iPFcand->energy() ) ); 

   }


    std::auto_ptr< std::vector< math::XYZTLorentzVector > > ak12JetsTlzv ( new std::vector< math::XYZTLorentzVector > () );
    std::auto_ptr < std::vector<double> > tau1(new std::vector<double>());
    std::auto_ptr < std::vector<double> > tau2(new std::vector<double>());
    std::auto_ptr < std::vector<double> > tau3(new std::vector<double>());
    std::auto_ptr < std::vector<double> > tau4(new std::vector<double>());
  

    std::auto_ptr < std::vector<double> > ak12Px(new std::vector<double>());
    std::auto_ptr < std::vector<double> > ak12Py(new std::vector<double>());
    std::auto_ptr < std::vector<double> > ak12Pz(new std::vector<double>());
    std::auto_ptr < std::vector<double> > ak12E(new std::vector<double>());
    
    std::auto_ptr < std::vector<int> > NumSubjets(new std::vector<int>());


    fastjet::contrib::Nsubjettiness nSub1_b1KT(1, fastjet::contrib::Njettiness::kt_axes, 1.0, 1.2, 1.2);
    fastjet::contrib::Nsubjettiness nSub2_b1KT(2, fastjet::contrib::Njettiness::kt_axes, 1.0, 1.2, 1.2);
    fastjet::contrib::Nsubjettiness nSub3_b1KT(3, fastjet::contrib::Njettiness::kt_axes, 1.0, 1.2, 1.2);
    fastjet::contrib::Nsubjettiness nSub4_b1KT(4, fastjet::contrib::Njettiness::kt_axes, 1.0, 1.2, 1.2);



    //defines cluster sequence for reclustring on the  k12 Jets  
    fastjet::ClusterSequence cs_ak12(particles, Jetdefak12);
    ak12Jets = sorted_by_pt(cs_ak12.inclusive_jets());
//    cout<<"number of clusterd ak12 Jets untrimmed= "<<ak12Jets.size()<<endl;



  
   fastjet::Filter trimmer1(fastjet::Filter(fastjet::JetDefinition(fastjet::kt_algorithm,0.2),fastjet::SelectorPtFractionMin(0.05)));

   fastjet::contrib::SubjetCountingCA subjetCounter(subjetMassCut,subjetPtImbalance,subjetRcut,subjetPtCut);  




        std::vector<fastjet::Transformer const *> transformers;
        transformers.push_back(&trimmer1);
     for(unsigned int j1=0;j1<ak12Jets.size();j1++){//jet loop

            int transctr = 0;
        for ( std::vector<fastjet::Transformer const *>::const_iterator
       itransf = transformers.begin(), itransfEnd = transformers.end();
       itransf != itransfEnd; ++itransf ) {//transformed jet

           fastjet::PseudoJet transformedJet = ak12Jets.at(j1);
           transformedJet = (**itransf)(transformedJet);


        if (transctr == 0){//12 Trimmer1
    TLorentzVector jet_tr_corr(transformedJet.px(),transformedJet.py(),transformedJet.pz(),transformedJet.e());

       if(jet_tr_corr.Pt() > 3.0){

        std::vector<fastjet::PseudoJet> ak12pseudoSubjets ;

        ak12pseudoSubjets = subjetCounter.getSubjets(transformedJet) ;


       cout<<"no of subjets = "<<ak12pseudoSubjets.size()<<endl;
        NumSubjets->push_back(ak12pseudoSubjets.size());
        tau1->push_back( nSub1_b1KT(transformedJet) );
        tau2->push_back( nSub2_b1KT(transformedJet) );
        tau3->push_back( nSub3_b1KT(transformedJet) );
        tau4->push_back( nSub4_b1KT(transformedJet) );
        
        ak12Px->push_back(transformedJet.px());
        ak12Py->push_back(transformedJet.py());
        ak12Pz->push_back(transformedJet.pz());
        ak12E->push_back(transformedJet.e());



       // math::XYZTLorentzVector ak12Jet4v(  transformedJet.px(),
        //                                    transformedJet.py(),
        //                                    transformedJet.pz(),
         //                                   transformedJet.e() ) ;


      
       
        }


                    }//12


     else{ std::cout << "error in number of transformers" << std::endl;}

        transctr++;



             }//transformed jet
       }//jet loop








 // cout<<"Default ak12 num jets trimmed ="<<ak12_default<<endl;

 // iEvent.put(Subjets) ; //,   jetCollection+"-Subjets"   );

  iEvent.put(NumSubjets,"NumSubjets");
  iEvent.put(ak12Px,"ak12Px");
  iEvent.put(ak12Py,"ak12Py");
  iEvent.put(ak12Pz,"ak12Pz");
  iEvent.put(ak12E,"ak12E");



  iEvent.put(tau1, "tau1");
  iEvent.put(tau2, "tau2");
  iEvent.put(tau3, "tau3");
  iEvent.put(tau4, "tau4");
  


}










// ------------ method called once each job just before starting event loop  ------------
void 

NsubjettinessProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
NsubjettinessProducer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
NsubjettinessProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
NsubjettinessProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
NsubjettinessProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
NsubjettinessProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
NsubjettinessProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {

  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

}

//define this as a plug-in
DEFINE_FWK_MODULE(NsubjettinessProducer);
