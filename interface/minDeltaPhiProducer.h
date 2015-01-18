#include <DataFormats/ParticleFlowCandidate/interface/PFCandidate.h>
#include "DataFormats/PatCandidates/interface/MET.h"

class minDeltaPhiProducer : public edm::EDProducer {

public:
  explicit minDeltaPhiProducer(const edm::ParameterSet&);
  ~minDeltaPhiProducer();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
  
private:
  virtual void beginJob() ;
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual void beginRun(edm::Run const&, edm::EventSetup const&);
  virtual void endRun(edm::Run const&, edm::EventSetup const&);
  virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
  
  // ----------member data ---------------------------


  // ---------- configurable data ----------------
  // --------------- members ---------------------  
  std::string jetCollection;     // name of jet collection
  std::string metCollection;     // name of met collection
  bool        debug;

};


