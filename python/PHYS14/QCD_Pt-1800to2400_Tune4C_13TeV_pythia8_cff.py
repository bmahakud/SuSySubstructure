import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/QCD_Pt-1800to2400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v2/10000/7C6B4D11-AC7C-E411-8A5F-002590D0B0D8.root',
       '/store/mc/Phys14DR/QCD_Pt-1800to2400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v2/10000/C8C83950-C37C-E411-90F6-20CF305B0572.root',
       '/store/mc/Phys14DR/QCD_Pt-1800to2400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v2/10000/D89A3C72-C67C-E411-9BCF-00248C9BA537.root',
       '/store/mc/Phys14DR/QCD_Pt-1800to2400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v2/20000/085FCE99-877C-E411-900C-20CF3027A577.root',
       '/store/mc/Phys14DR/QCD_Pt-1800to2400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v2/20000/2A6589BB-A07C-E411-A137-00259074AE7A.root' ] );


secFiles.extend( [
               ] )

