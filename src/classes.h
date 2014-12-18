#include <vector>
#include "TLorentzVector.h"

namespace { 
  struct dictionary {

    std::vector<TLorentzVector> vt;
    edm::Wrapper<std::vector<TLorentzVector> > wvt;

    //std::vector<std::vector<TLorentzVector> > vtt;
    //edm::Wrapper<std::vector<std::vector<TLorentzVector> > > wvtt;

  };
}
