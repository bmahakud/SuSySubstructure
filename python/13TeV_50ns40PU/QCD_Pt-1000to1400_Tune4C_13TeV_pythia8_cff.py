import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/029BF965-D218-E411-A3DA-0025905A60F8.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/06B8B952-D218-E411-ADBB-0025905A60B4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0ADC46CF-D218-E411-A65E-003048FFCB74.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0E4F3EAD-CC18-E411-A04C-0025905A612A.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/22D5AD7F-D218-E411-B127-00259059649C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/26FB84C4-D218-E411-BEBF-0025905A607E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/28041DE0-D218-E411-9268-0025905A6094.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/324B916B-D218-E411-8F02-0025905A60D6.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/36EBB133-D218-E411-94B1-0025905A6066.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/3A64DFAD-CB18-E411-AFFF-002618943906.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/3AEE9E80-D218-E411-83D9-0026189438D6.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/44DFFE1F-D318-E411-9322-0025905A608E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4860F072-D218-E411-9AE6-0025905A60B4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4E45F4E7-D218-E411-A5C9-0025905B858C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5A46C0AF-D218-E411-AA3D-0025905B85F6.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5E232231-D218-E411-A585-003048FFD7C2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/62FDE27D-D218-E411-B4C6-0025905964C0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/64B7324F-D218-E411-979C-0025905A6088.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/68563E37-D218-E411-AF6C-002590593878.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6C4072DD-D218-E411-BCE1-0025905A608C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/7024DD99-D218-E411-8072-0025905A6080.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/78258CF0-D218-E411-8972-0025905A60A8.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/78706E87-D218-E411-A596-0025905A60FE.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/881A3868-D218-E411-AFD1-003048FFD7BE.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/88E2CAD5-D218-E411-87A4-003048FFD730.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/8EB9D287-D218-E411-9DD5-0025905964BC.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/A0BDC4B6-D218-E411-B942-0025905A6094.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/AA7DC884-D218-E411-A537-003048FFD752.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B200F257-D218-E411-BB61-0025905A60B4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C44A624F-D218-E411-9861-00261894390A.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/CA3E583C-D218-E411-AF32-003048FFD756.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D24E1B61-D218-E411-A479-0025905A6090.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E6A03883-D218-E411-A281-003048FFD71E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F414B6E7-D218-E411-A57B-0025905A60F4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F4B5A633-D218-E411-BF54-003048FFCBA8.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/FA629A31-D318-E411-A7B3-0025905A60BE.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-1000to1400_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/FCC235EE-D218-E411-BC8E-0025905A612A.root' ] );


secFiles.extend( [
               ] )

