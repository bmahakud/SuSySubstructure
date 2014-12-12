import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/0224C2EF-0118-E411-97AC-0025905A48EC.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/06142FE9-0118-E411-AE51-0025905A613C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/0CEECEF0-0118-E411-BB70-0025905A607A.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/1E37A537-0218-E411-8B61-002618943849.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/3C849E0A-0218-E411-9091-00261894385D.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/42393540-0218-E411-B474-002618943985.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/5882E1F8-0118-E411-9482-0026189438B3.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/5EFCAA4A-0218-E411-90A6-0025905A60F8.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/621AF227-0218-E411-BA84-00261894393C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/621BB3C9-0218-E411-B99D-0025905A60B2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/6CA6F835-0218-E411-9740-0026189438DE.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/70167112-0218-E411-A801-0025905B85E8.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/70F3E141-0218-E411-ACCF-0025905A60AA.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/74A44849-0218-E411-9A6A-00261894382D.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/7E976BE3-0118-E411-B127-00261894398B.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/80A9D037-0218-E411-8C50-0026189438DE.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/828C2E18-0218-E411-ACA3-0025905A6132.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/82D84F05-0218-E411-BE98-0025905A60BC.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/8EC1BC25-0218-E411-BC0D-0025905A611E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/9EC16A4E-0218-E411-B0B8-0025905A48C0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/9EFADAFA-0118-E411-AA5E-0025905A6060.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/AC7B23FB-0118-E411-8B9D-002618943962.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/ACC177E3-0118-E411-832F-0025905B860C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/B49B7602-0218-E411-9A4C-0026189438BC.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/B8B2353C-0218-E411-AA07-0025905A48EC.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/BCCEB00A-0218-E411-B338-0026189438B3.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/D0F3B2C9-0218-E411-B393-0025905A60B2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/D26273DF-0118-E411-9993-0025905A60F4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/D473C907-0218-E411-A5D9-0026189438A5.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/D6DBAF39-0218-E411-984F-0025905A6082.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/DE5EB102-0218-E411-9BBC-0025905B858E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/E6017CD8-0118-E411-A63A-00261894385D.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/E8DFDDF5-0118-E411-B587-0025905A60F2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/EA1AA60E-0218-E411-AAF2-0025905B85D8.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/EAC624FD-0118-E411-ADAF-002590593876.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/EEE0DD20-0218-E411-A588-002618943948.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/F49553E6-0118-E411-816A-002354EF3BDB.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-470to600_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v2/00000/F67D78E1-0118-E411-B329-002590596486.root' ] );


secFiles.extend( [
               ] )

