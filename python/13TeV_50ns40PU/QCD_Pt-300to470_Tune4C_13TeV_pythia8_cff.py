import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0044DCD0-BC1B-E411-9F97-003048FFCBFC.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/00F1C6D4-BC1B-E411-937B-003048FFD7A2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/08080ADC-BC1B-E411-A711-0025905A60B0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0A516ED7-BC1B-E411-A89C-0025905A6066.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0A6BB1D9-BC1B-E411-ACE5-0025905A60B8.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0A8150D9-BC1B-E411-9A20-0025905A6068.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/109822D6-BC1B-E411-A3ED-0025905A60DA.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/140E33CE-BC1B-E411-98AD-0026189438F5.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/1AB98FDE-BC1B-E411-8BC5-0025905A60CE.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2658B332-BD1B-E411-A993-0025905A60C6.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/301FA3D1-BC1B-E411-8DB4-0025905A608E.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/32E9A2D3-BC1B-E411-ADF1-0025905B8590.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/3E27EABA-BC1B-E411-9C4A-0026189438F2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/42C0D8BB-BC1B-E411-966C-00261894397B.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/441915D4-BC1B-E411-8258-0026189438DF.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4CD6B4E7-BC1B-E411-A30E-0025905A6056.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4E7D46DA-BC1B-E411-BC44-0025905B860C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5060D4C1-BC1B-E411-B7C7-00261894380B.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/54245FBF-BC1B-E411-8F71-002618943849.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5ABB5332-BD1B-E411-AE5B-0025905A608A.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5CA5D717-BD1B-E411-B873-00261894385A.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6A071AD9-BC1B-E411-9D7C-0025905A608C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6C25CCBB-BC1B-E411-A2B5-003048FFD754.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6C8DB5BA-BC1B-E411-962C-0026189438B3.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/70811BDF-BC1B-E411-A71C-0025905AA9F0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/74F35CE6-BC1B-E411-8129-0025905964C0.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/80547DD1-BC1B-E411-BA7B-003048FFCBA4.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/8E5A56BC-BC1B-E411-9B60-0025905A60DE.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/94727CD7-BC1B-E411-9AB7-002590596484.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/96448531-BD1B-E411-9843-002354EF3BE6.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/96FFFD0C-BD1B-E411-A6DF-0025905A6136.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9C31ABE1-BC1B-E411-AF06-0025905B8610.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/AAC0A1D0-BC1B-E411-8958-0025905B857C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B28C34BA-BC1B-E411-B3E4-0026189438FD.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C0A5B5CB-BC1B-E411-AD94-0025905A6138.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C2743CD3-BC1B-E411-91A2-0025905A6060.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C47A8D33-BD1B-E411-9713-0025905A60D2.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/EA1D15D4-BC1B-E411-A442-0026189438DF.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/EC2FC1B9-BC1B-E411-85FB-00261894390C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F20D9ED0-BC1B-E411-99D5-0025905B857C.root',
       '/store/results/b_tagging/StoreResults/QCD_Pt-300to470_Tune4C_13TeV_pythia8/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F4A743DA-BC1B-E411-84F9-0025905B860C.root' ] );


secFiles.extend( [
               ] )

