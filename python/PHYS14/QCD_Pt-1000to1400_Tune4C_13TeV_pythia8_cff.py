import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/5EF1A5AC-B76F-E411-93FC-0025905A48F2.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/9075AAA6-B76F-E411-A3A5-0025905A6126.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/B82C3CA4-B76F-E411-A430-003048FF9AA6.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/000937E1-AB6F-E411-9EDF-0025905A6092.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/4241DED8-AB6F-E411-A43B-0026189438A0.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/7C262BE5-AB6F-E411-BD47-0025905B8582.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/A44B9FDD-AB6F-E411-800A-0025905A48D6.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/B0EF19DB-AB6F-E411-9AE3-002618943810.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/B85DF3F4-AB6F-E411-87A2-0025905A613C.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/CE9373E7-AB6F-E411-AA69-003048FFD71E.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/D8B487DF-AB6F-E411-8FEC-0025905A48BC.root',
       '/store/mc/Phys14DR/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/EA62CAEB-AB6F-E411-9170-0025905A48B2.root' ] );


secFiles.extend( [
               ] )

