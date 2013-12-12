
#include "TH1F.h"

// enumerators for classification

enum JetMult { kLow, // 3<=njets<=5
	       kMed, // 6<=njets<=7
	       kHigh,// njets>8
             };

enum HtRegion { k500_800, 
		k800_1000,
		k1000_1250,
		k1250_1500,
		k1500On
              };

using namespace std;

class RA2tools {

public:

  RA2tools(){};
  ~RA2tools(){};

  void setJetMult(JetMult jetBin){ jetMult = jetBin ; };
  TH1F* initHisto(JetMult jetBin, HtRegion Htbin);

private:
  
  JetMult jetMult;

};
