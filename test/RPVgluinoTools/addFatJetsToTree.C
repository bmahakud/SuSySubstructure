#ifndef __addFatJetsToTree__
#define __addFatJetsToTree__

/*
Script for reading RA2nTuples (as defined in ../src/RA2nTuple.h) 
calculated sum-jet-mass from fattened ak5 jets in event, and storing
this information into the ntuples again and saving the new 
tree in a new file.
Original Author: Andrew Whitbeck - May 5, 2014

Should be compiled with:

g++ `root-config --cflags` RA2nTuple.cc addFatJetsToTree.C `root-config --glibs` -l$PWD/fastjet-3.0.6/src/.libs/libfastjet.so.0.0.0 -Ifastjet-3.0.6/include/ -o addFatJetsToTree.exe -Wall

should be run with:

./addFatJetsToTree.exe <input-file-name> <input-tree-name>

output files will be save to dirName and the filename will be the 
input file name appended with '_withFatJets'.  The tree name will
be the same as the input tree name.

*/


#include "TString.h"
#include <iostream>
#include "RA2nTuple.h"
#include "JetFattening.cc"
#include "TH1F.h" 
#include "TFile.h"

using namespace std;

int main( int argc , char* argv[] ){

  TString inputDirName ; //"/eos/uscms/store/user/lpcsusyhad/SusyRA2Analysis2012/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV/"
  TString outputDirName ; //"/eos/uscms/store/user/awhitbe1/RA2nTupleExtension/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV/"
  TString FileName ; //"scanTree_T1tttt_323_1_fTO.root"
  TString TreeName ; //"RA2TreeMaker/RA2PreSelection"

  if( argc == 5 ){
    inputDirName = argv[1];
    outputDirName = argv[2];
    FileName =  argv[3];
    TreeName =  argv[4];
  }else{
    cout << "ERROR: you only passed " << argc - 1 << " arguments! Three arguments must be provided! " << endl;
    cout << "first:  input directory " << endl;
    cout << "second: output directory " << endl;
    cout << "third:  input file name" << endl;
    cout << "fourth: input treename" << endl;
    return 1;
  }

  // overriding using input!!!!
  //inputDirName = "/eos/uscms/store/user/lpcsusyhad/SusyRA2Analysis2012/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV/" ;  

  bool debug = true ;

  RA2nTuple RA2tree( inputDirName + FileName , TreeName ) ;

  float sumJetMass = 0.0 ;

  TH1F* fatJetPt = new TH1F("fatJetPt", "fatJetPt", 40, 0, 1000 );

  //TString outputDirName  = "/eos/uscms/store/user/awhitbe1/RA2nTupleExtension/19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV/" ;

  FileName.ReplaceAll( ".root" , "_withFatJets.root" ) ;
  TFile *outputFile = new TFile( outputDirName + FileName , "RECREATE" ) ;
  TTree* extendedTree = (TTree*)  RA2tree.tree->CloneTree(0,"fast") ;

  int   FatJetsNum;
  float FatJetPt[100]  ;
  float FatJetEta[100] ;
  float FatJetPhi[100] ;
  float FatJetE[100]   ;

  //[FatJetsNum]

  extendedTree->Branch("FatJetsNum",&FatJetsNum,"FatJetsNum/I") ;
  extendedTree->Branch("FatJetPt",&FatJetPt,"FatJetPt[FatJetsNum]/F") ;
  extendedTree->Branch("FatJetEta",&FatJetEta,"FatJetEta[FatJetsNum]/F") ;
  extendedTree->Branch("FatJetPhi",&FatJetPhi,"FatJetPhi[FatJetsNum]/F") ;
  extendedTree->Branch("FatJetE",&FatJetE,"FatJetE[FatJetsNum]/F") ;
  extendedTree->Branch("sumJetMass",&sumJetMass,"sumJetMass/F") ;
  // ^^^^^^^^^^^^^^^
  // loop over each event
  for( int iEvt = 0 ; iEvt < RA2tree.getEvents() ; iEvt++){

    RA2tree.getEvent( iEvt ) ;

    vector< TLorentzVector > ak5Jet4Vec ;

    //if ( RA2tree.massMom < 700 ) continue;
    
    // !!!!!!!!!!!
    // loop over ak5 jets to recluster into ak1.2 jets
    for( int iJet = 0 ; iJet < RA2tree.JetsNum ; iJet++ ){

      TLorentzVector temp;

      if( debug ){
      	cout << RA2tree.JetsPt[iJet] << " " << RA2tree.JetsEta[iJet] << " " << RA2tree.JetsPhi[iJet] << " " << RA2tree.JetsE[iJet] << endl;
      }

      temp.SetPtEtaPhiE(
                  RA2tree.JetsPt[iJet],
                  RA2tree.JetsEta[iJet],
                  RA2tree.JetsPhi[iJet],
                  RA2tree.JetsE[iJet]);

      ak5Jet4Vec.push_back( temp ) ;


    } // loop over jet in event
    // !!!!!!!!!!!

    if ( ak5Jet4Vec.size() == 0 ){
      cout << "ERROR: there are no ak5Jets!!!" << endl;
      continue;
    }

    vector< TLorentzVector > fatJet4Vec = JetFattening( ak5Jet4Vec ) ;

    if ( fatJet4Vec.size() == 0 ){
      cout << "ERROR: zero jets received from JetFattening function! " << endl;
      continue;
    } 

    sumJetMass = 0.0 ;

    // ################
    // loop over fat jets, fill vectors for tree, calc. sumJetMass

    FatJetsNum = fatJet4Vec.size() ; 

    for( unsigned int iJet = 0 ; iJet < fatJet4Vec.size() ; iJet++ ){

      sumJetMass += fatJet4Vec[ iJet ].M() ;

      FatJetPt[ iJet ] = fatJet4Vec[ iJet ].Pt() ;
      FatJetEta[ iJet ] = fatJet4Vec[ iJet ].Eta() ;
      FatJetPhi[ iJet ] = fatJet4Vec[ iJet ].Phi() ;
      FatJetE[ iJet ] = fatJet4Vec[ iJet ].E() ;

     } // end loop over fat jets
    // ################

    //cout << sumJetMass << endl;
    fatJetPt->Fill( sumJetMass ) ;
    extendedTree->Fill();

  } // loop over events in tree
  // ^^^^^^^^^^^^^^^

  //fatJetPt->Draw();
  outputFile->cd();
  extendedTree->Write();
  outputFile->Close();

  return 0;
}

#endif
