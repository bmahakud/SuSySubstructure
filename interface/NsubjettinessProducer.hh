#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include "TTree.h"
#include <fastjet/ClusterSequence.hh>
#include <fastjet/PseudoJet.hh>
#include <fastjet/JetDefinition.hh>
#include <fastjet/tools/Filter.hh>

#include "AWhitbeck/SuSySubstructure/src/SubjetCounting.hh"

#include <vector>


class NsubjettinessProducer : public edm::EDProducer {

public:
  explicit NsubjettinessProducer(const edm::ParameterSet&);
  ~NsubjettinessProducer();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:


   // struct jetKinematics {


   // std::vector< double > pt;
   // std::vector< double > eta;
   // std::vector< double > mass;
   // std::vector< double > phi;



  // } 



  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
 // void addJetKinToTree( jetKinematics& jetKin, TString tag, TTree& tree );
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  
  // ----------member data ---------------------------


  // ---------- configurable data ----------------
  // --------------- members ---------------------
  
  std::string jetCollection;     // name of jet collection
  double      clusterRadius;     // jet clustering radius
  double      trimPtFracMin;     // %pt for trimming
  bool        trimJets;          // apply trimming
  double      subjetPtCut;       // min pt of subjets
  double      subjetMassCut;     // min mass of subjets
  double      subjetRcut;        // min delta R between subjets
  double      subjetPtImbalance; // maximum imbalance between jet and subjet 
  bool        debug;
  TTree* NsubjettinessTree;











 






};
