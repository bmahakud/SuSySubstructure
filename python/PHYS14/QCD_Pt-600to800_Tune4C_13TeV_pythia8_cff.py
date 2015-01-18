import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/04CA19AD-B673-E411-A42D-00266CF32E2C.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/0A1D2EB8-B673-E411-AE80-00266CFFA750.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/1EA65E5A-B073-E411-8DA2-003048D3739A.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/2E07644D-B073-E411-9692-002590DB91F0.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/32AFCEAD-B673-E411-8324-0025901D4C46.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/3A593EB9-B673-E411-883A-0025904B130E.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/3EAC7446-B073-E411-B4C8-002481E0DC4C.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/481C79A9-BA73-E411-9028-002590AC4BF6.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/5845C088-B073-E411-A392-002590494CC4.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/5E8961B1-BA73-E411-919D-003048F0E3AE.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/64302161-1B74-E411-8C75-0025907DC9DC.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/686D0A48-B073-E411-ACF7-003048F02CBE.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/72E9BF48-B073-E411-AAE6-00266CF32920.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/7CDB45B2-BA73-E411-B839-00266CFFA6F8.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/860DE7F6-B673-E411-B26D-002590AC500E.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/8A5148B8-BA73-E411-804A-0025901D4B06.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/92CEF747-B073-E411-BB3C-002481E94C56.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/A451D147-B073-E411-83C0-00266CFFB1F4.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/A6A95C69-D673-E411-A8D8-002590494C92.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/B226DA56-B073-E411-8F53-002481E0D6A6.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/D66ECE4E-1B74-E411-8BE8-0025901D4D76.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/DA631746-B073-E411-A993-003048F0E18C.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/E6A41E47-B073-E411-BD59-002590DB925E.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/E89E78AE-B673-E411-8553-002590AC5062.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/EA59B54C-B073-E411-950A-002590DB927A.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/00000/F49878E0-BF73-E411-830A-002590AC4FEC.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/0042434E-BE73-E411-A156-0025907DC9D2.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/022F720D-AF73-E411-BA49-002590DB917C.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/08F95204-B773-E411-9FD0-0025907FD24A.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/1820D9E7-B673-E411-ACAD-00266CFFA604.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/1CA1DA1D-AF73-E411-AA71-003048F02CB2.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/2AB34D0D-AF73-E411-B2CF-0025901D4C3E.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/42230818-B773-E411-B8A4-002590AC501A.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/4406B4FA-B673-E411-8B6B-00266CFFA604.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/5226E84F-AF73-E411-ACA8-0025907DC9BE.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/5ADF186D-AF73-E411-88FB-003048F0E3D0.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/6A7CAC1A-B773-E411-87FB-002590DB921A.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/8E9CEAFB-BC73-E411-98D8-0025907DC9B4.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/9A548129-B773-E411-AD46-0025907DC9F8.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/9E11441C-AF73-E411-A503-002590DBDFE0.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/A8AA57F2-B373-E411-A393-002590AC5066.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/AE3C43D4-BC73-E411-B4FA-002590494E38.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/B8C63646-AF73-E411-BEF8-00266CFFA604.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/CC48FDFF-B673-E411-A338-003048D43656.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/CC620F01-B773-E411-8CB2-002590AC4C72.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/D6ECC414-AF73-E411-8515-003048D437E4.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/D8AC52E3-B373-E411-85B1-00259074B2BE.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/DE5BB5E4-B373-E411-B175-002590AC5070.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/EC63722F-AF73-E411-9BBC-002481E1070E.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/F6041037-BE73-E411-B64A-002590AC539E.root',
       '/store/mc/Phys14DR/QCD_Pt-600to800_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v1/10000/F8EBF9F5-AE73-E411-A49E-0025901D42BC.root' ] );


secFiles.extend( [
               ] )

