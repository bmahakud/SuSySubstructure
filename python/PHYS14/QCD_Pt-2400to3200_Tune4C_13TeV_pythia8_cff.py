import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/QCD_Pt-2400to3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/38C42CBA-C273-E411-93BB-002590494E38.root',
       '/store/mc/Phys14DR/QCD_Pt-2400to3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/5AF48710-0B73-E411-92B7-002590DB9296.root',
       '/store/mc/Phys14DR/QCD_Pt-2400to3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/6E7B6EB3-C273-E411-8026-003048D47912.root',
       '/store/mc/Phys14DR/QCD_Pt-2400to3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/EC04EF3F-0473-E411-AA2A-002590DBDFE0.root',
       '/store/mc/Phys14DR/QCD_Pt-2400to3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/F069219D-BA73-E411-B146-002590AC504A.root',
       '/store/mc/Phys14DR/QCD_Pt-2400to3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/829871F8-BC73-E411-AE9B-00266CF32F18.root',
       '/store/mc/Phys14DR/QCD_Pt-2400to3200_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/10000/8E6C9B07-BD73-E411-82E0-003048D43838.root' ] );


secFiles.extend( [
               ] )

