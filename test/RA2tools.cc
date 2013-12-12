#include "RA2tools.h"

TH1F* RA2tools::initHisto(JetMult jetBin, HtRegion Htbin){

  int nBins;
  double bins[5];  // note this sets the max... which is currently 5

  switch ( jetBin ){
    
  case kLow :

    switch ( Htbin ){
      
    case k1250_1500 :

      nBins = 4;
      bins[0]=200; bins[1]=300; bins[2]=450; bins[3]=600; bins[4]=1000;

    case k1500On :
      
      nBins = 2;
      bins[0]=200; bins[1]=300; bins[2]=1000;
				
    default : 
      
      nBins = 4;
      bins[0]=200; bins[1]=300; bins[2]=450; bins[3]=600; bins[4]=1000;
    
    }

  case kMed : 

    switch ( Htbin ){

    case k1500On :
      
      nBins = 2;
      bins[0]=200; bins[1]=300; bins[2]=1000;

    default : 
      
      nBins = 3; 
      bins[0]=200; bins[1]=300; bins[2]=450; bins[3]=1000;
      
    }
    
  case kHigh : 

    // special case where bins are Ht instead of MET
    nBins = 5; 
    bins[0]=500; bins[1]=800; bins[2]=1000; bins[3]=1250; bins[4]=1500; bins[5]=2000;

  }

  return new TH1F("test","test",nBins,bins);

}
