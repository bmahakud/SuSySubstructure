import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/QCD_Pt-3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/0256C739-B96B-E411-A571-3417EBE33927.root',
       '/store/mc/Phys14DR/QCD_Pt-3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/E48AEFFE-A06B-E411-9B9C-00266CF9BDFC.root',
       '/store/mc/Phys14DR/QCD_Pt-3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/58B35A7A-A56B-E411-88C1-00266CF2507C.root',
       '/store/mc/Phys14DR/QCD_Pt-3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/B4AAEFA4-0F6C-E411-8D6D-848F69FD2967.root',
       '/store/mc/Phys14DR/QCD_Pt-3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/F0C2FD08-9A6B-E411-A606-00266CF9B404.root' ] );


secFiles.extend( [
               ] )

