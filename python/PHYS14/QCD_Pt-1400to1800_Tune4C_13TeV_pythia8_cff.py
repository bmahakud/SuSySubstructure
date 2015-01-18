import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/3EA316C2-C76F-E411-9D79-0025905A60BC.root',
       '/store/mc/Phys14DR/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/582854DB-C76F-E411-BF08-0025905B85EE.root',
       '/store/mc/Phys14DR/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/B682ECB7-C76F-E411-8A6A-0025905A608A.root',
       '/store/mc/Phys14DR/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/D46F66BF-C76F-E411-A926-0025905A48F2.root',
       '/store/mc/Phys14DR/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/EE75CCBB-C76F-E411-B7C0-0025905A609E.root' ] );


secFiles.extend( [
               ] )

