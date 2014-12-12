import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/082A147A-CD18-E411-90DB-003048FFCBA8.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0A7900A1-CD18-E411-A734-0025905A60D0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0AFC0AFA-CD18-E411-8B34-0025905A608C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/14AF7A38-CC18-E411-A85C-0025905A608C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/16D50584-CD18-E411-912C-002618943906.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2056A897-CD18-E411-87A1-002590596468.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2A669996-CD18-E411-8DF4-0025905A60E0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2C06D4A5-CD18-E411-8535-0025905964BE.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/464D7F3A-CD18-E411-BC5E-0026189438D9.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/506DB4FD-CD18-E411-9E5F-0025905A60E4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5C0B10E9-CD18-E411-85E0-003048FFD7C2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5EE89039-CD18-E411-AB1C-002618FDA237.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/647F7B57-CD18-E411-B3BC-003048FFD7C2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6C54C9DB-CD18-E411-A567-0025905A605E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6CBFBCB9-CD18-E411-910A-0025905964C0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6E4CA79A-CD18-E411-862A-0025905938D4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/7E561CF9-CB18-E411-86FA-0025905A609E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/7E8B9A8F-CD18-E411-949A-0025905A6090.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/80AF3BA5-CD18-E411-BAE3-0026189438F2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/900355DC-CD18-E411-B25E-003048D15DE0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/94C92D8A-CD18-E411-97A8-002618943918.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/96B0ABE1-CD18-E411-8B75-002618943982.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/A87F6939-CD18-E411-B63D-00248C55CC7F.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/AC81BCFD-CD18-E411-9C4C-0025905A60E4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B289D0A4-CD18-E411-B697-0025905964BA.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B6E6F969-CE18-E411-8813-0025905A60D6.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B8EA215B-CD18-E411-9C16-0025905B8562.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/BE1FE7E8-CB18-E411-96C3-0025905A60F2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C4C7B8FD-CD18-E411-B55F-0025905A60E4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C622F488-CD18-E411-B741-00248C0BE018.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D2C58A84-CD18-E411-8B2E-0025905A48C0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E222EFAD-CD18-E411-9FA5-0025905A60D2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E25034D6-CD18-E411-AC2F-0025905A606A.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E2FF7B9E-CD18-E411-86F4-0025905A607E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E435E7E8-CB18-E411-8DFC-0025905A60F2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E83F11E1-CD18-E411-950F-0025905B85EE.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F2D2604A-CD18-E411-8771-003048FFD7D4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/FCAD75E8-CB18-E411-A4F4-0025905B85A2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1800_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/FE0990E1-CD18-E411-B26F-002618943862.root' ] );


secFiles.extend( [
               ] )

