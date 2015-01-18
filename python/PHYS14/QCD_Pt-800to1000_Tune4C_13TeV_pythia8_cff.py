import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/1437E878-5E78-E411-A33F-0025905964CC.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/2A9C8623-5E78-E411-AAA5-0025905A60A8.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/44982569-5E78-E411-9E44-002618943821.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/5270797A-5E78-E411-9DEB-0025905A6110.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/7C97CD5C-5E78-E411-B966-002618943926.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/82967C07-FF78-E411-9FD5-0025905A48D8.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/8ED3A25C-5E78-E411-9507-0025905A612C.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/A23B076B-6578-E411-9769-003048FFCC2C.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/AA034D4D-5E78-E411-B2EA-002618943959.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/22E6A2F6-4677-E411-BEF6-0026189437F9.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/384E48FB-4677-E411-AE08-0025905A7786.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/7E7C466B-EA78-E411-9D2F-0025905A6064.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/80CF5BEF-4377-E411-9549-002618943935.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/A6567AF8-4677-E411-9499-0025905A6104.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/B4A5EBF7-4677-E411-9D67-0025905A60B4.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/C823DA71-1478-E411-A43B-002618943836.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/CA441271-1478-E411-B5C3-00261894394A.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/CEB075F8-4677-E411-B9F8-0025905B85D8.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/DE2C9EFD-4677-E411-B149-0025905964C0.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/E66128FA-4677-E411-A3D0-0025905B860C.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/F4C19EF7-4677-E411-8721-0025905A60B2.root',
       '/store/mc/Phys14DR/QCD_Pt-800to1000_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/FA6E6FF6-4677-E411-8AA5-0026189437F9.root' ] );


secFiles.extend( [
               ] )

