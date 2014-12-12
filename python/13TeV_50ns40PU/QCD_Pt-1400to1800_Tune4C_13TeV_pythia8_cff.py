import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/08198D67-D218-E411-B114-00248C55CC3C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0A03687C-D318-E411-939B-0025905A48EC.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/1207276C-D218-E411-BB72-0025905938D4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/143578B4-D118-E411-97F1-0025905A60D2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2042BA67-D218-E411-89C0-00261894394A.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/249078B2-D118-E411-B040-0025905938D4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2E30E3A1-D218-E411-9B49-0025905A6118.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/3885B8AF-D118-E411-8E1E-0026189438F4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/3A5C00F8-D118-E411-8401-0025905A609E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4814B06D-D218-E411-9943-0025905A60F8.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4E9E6FBA-D118-E411-8913-002590593878.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/58CF5868-D218-E411-95DD-00261894389A.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/621BC4BB-D118-E411-95CD-0025905A4964.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6C973695-D218-E411-A379-003048FFD744.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/76E2E1AE-D118-E411-B84C-00261894391C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/8644813C-D318-E411-B390-0025905A6138.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/8878A966-D218-E411-9047-00261894395F.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/8AB9A1CB-D218-E411-A947-0025905A60DA.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/8EFE4DB4-D118-E411-9F21-003048FFD7C2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/90C52EC4-D118-E411-84D5-002590596498.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/94033378-D218-E411-9BE2-0025905A607E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/98C0B665-D218-E411-856F-002354EF3BE0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9CA3FBDF-D118-E411-B5DC-0025905A60CA.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/A226F7E1-D218-E411-A1C8-0025905A48C0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/A83E6A6F-D218-E411-98CF-0025905A6094.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B077E369-D218-E411-B0F8-00248C55CC9D.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B69C6B6B-D218-E411-9AE5-0025905A6090.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C643E2A1-D218-E411-B883-0025905A6118.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C8181DAF-D118-E411-A13C-0026189438D7.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D2424FDF-D118-E411-A326-0025905A6090.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D2AB1CBD-D118-E411-A761-00259059649C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D610DFE1-D118-E411-9F21-0025905A60BE.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E0D6A9CD-D218-E411-96B0-0025905A48D6.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E2F6813C-D318-E411-97B7-0025905A6138.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E6426271-D218-E411-ACE2-002590596468.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/EC10FDDF-D118-E411-8470-0025905A60CA.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F29810DA-D118-E411-8E61-0025905B860C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F46B8DF0-D218-E411-812C-0025905A60A8.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1400to1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F82F6ACB-CB18-E411-A66F-003048FFD770.root' ] );


secFiles.extend( [
               ] )

