import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/0023DCC2-2F1E-E411-B406-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/02FBDC46-301E-E411-84F9-00261894388A.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/04078207-301E-E411-AF49-003048FFD728.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/109BAD1E-2F1E-E411-A435-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/12AE5303-301E-E411-BB46-0025905B861C.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/1458ADA3-2F1E-E411-BFB2-0025905A60CA.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/146F8B6D-2F1E-E411-B65B-0025905B861C.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/16F9DBC2-2F1E-E411-8354-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/18863CD4-2E1E-E411-BEF5-0026189438DD.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/1AA87751-2F1E-E411-8B82-00248C0BE018.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/1EA6AD1E-2F1E-E411-A9E0-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/1EF5FB0D-2F1E-E411-AD53-00248C55CC97.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/20A9AD1E-2F1E-E411-9D87-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/244E1E05-2F1E-E411-A8D4-0026189438B4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2480D8C2-2F1E-E411-818D-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/26B2AD1E-2F1E-E411-BF7E-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/28A1AD1E-2F1E-E411-A35C-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/28BDD8C2-2F1E-E411-97C2-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2C418656-2F1E-E411-809D-002618FDA216.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2E2CDCC2-2F1E-E411-BFCA-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2E6C3ED1-2E1E-E411-A6F5-002354EF3BE3.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/2E72B5CC-2E1E-E411-B8F4-00248C55CC7F.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/305A18DF-2E1E-E411-AB5B-0026189438CE.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/30C9ECC2-2F1E-E411-BA74-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/328275B2-2E1E-E411-9872-00261894389A.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/32A1AD1E-2F1E-E411-8489-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/3441DAC2-2F1E-E411-8B21-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/36B13F78-2F1E-E411-BBFF-0026189438BF.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/384953CB-2E1E-E411-90D7-002618943862.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/385E9258-2F1E-E411-BE56-002618943856.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/3C707956-2F1E-E411-828D-00261894397B.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4274E4C2-2F1E-E411-B36A-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/44A0E8C2-2F1E-E411-AF9D-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/44D24E08-2F1E-E411-8321-002618943845.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/46215664-2F1E-E411-BC2C-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/46997978-2F1E-E411-B486-0026189438BF.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/46F7F3C2-2F1E-E411-8594-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4A2EAC39-2F1E-E411-BA32-003048FFD71E.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/4E8BA2C9-2E1E-E411-BA07-002618943876.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/54562F5C-2F1E-E411-BBAE-0025905A60F8.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/54B465A9-2F1E-E411-96D9-0025905B861C.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/54C5DBC2-2F1E-E411-816E-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/580BD363-2F1E-E411-8028-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5CA87ED1-2E1E-E411-B8C5-0025905A60F8.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/5E5BD263-2F1E-E411-872F-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/64CC305C-2F1E-E411-BF27-0025905A60F8.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6837E9B7-2E1E-E411-B09B-002618FDA250.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6CC4D8C2-2F1E-E411-A015-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6CD734CD-2E1E-E411-ADDD-0026189438B1.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/6E0EE2C2-2F1E-E411-BAF9-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/70D527FA-2F1E-E411-9EAD-002590596498.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/72764279-2F1E-E411-96BC-003048FF9AA6.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/729152BD-2E1E-E411-947B-00248C55CC7F.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/7496AD1E-2F1E-E411-A171-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/782661D2-2E1E-E411-8748-002618FDA204.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/7CC1DD47-2F1E-E411-BE04-00248C55CC7F.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/7CDB300D-2F1E-E411-A712-0026189438AA.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/823E895A-2F1E-E411-A223-00248C0BE01E.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/826928DC-2E1E-E411-B718-00259059391E.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/842DE4C2-2F1E-E411-A9A5-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/84FC5806-301E-E411-832A-0025905A48EC.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/86543DA5-2F1E-E411-B01F-002354EF3BE6.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/8672B3B7-2E1E-E411-8665-0026189438B4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/86C5F8D8-2E1E-E411-990F-0025905964BA.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/8CDF6613-2F1E-E411-B1F4-0025905964BA.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9273D811-2F1E-E411-B73B-0025905A60F8.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/92AD0DD0-2E1E-E411-B3E8-00261894389A.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/94BA1667-2F1E-E411-8F1F-00261894394D.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/94E4E0C2-2F1E-E411-B712-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/969883D9-2E1E-E411-88BE-0025905A6126.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9A0C9B58-2F1E-E411-9DFE-0026189438D7.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9A8BD4F9-2F1E-E411-9FC6-0025905A60F8.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9ABE39CC-2E1E-E411-9A88-002618FDA259.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/9ED8DDC2-2F1E-E411-9ED9-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/A0BD585C-2F1E-E411-A054-0025905A60F8.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/A8C8E8C2-2F1E-E411-A4CE-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/AA01A85A-2F1E-E411-AF6E-0026189438B8.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/AC1DB0DF-2E1E-E411-A9B2-002354EF3BE6.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B0169C1E-2F1E-E411-8B3E-0025905A6070.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B0264ECB-2E1E-E411-B2B4-00248C0BE018.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B0D4E8C2-2F1E-E411-B637-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B2B57F0C-301E-E411-AEE1-0025905A48D0.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B40A5216-2F1E-E411-B414-00261894388A.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B47190BC-2E1E-E411-BEA9-002618943986.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/B830F156-2F1E-E411-8203-002618943862.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/BA9AFAC2-2F1E-E411-8431-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/BEBB8ED8-2E1E-E411-B33D-003048FFCC2C.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C0180C4C-2F1E-E411-ADEB-00248C0BE01E.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C0CF2107-2F1E-E411-A9C8-002618943972.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C208665A-2F1E-E411-843C-00248C0BE01E.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C258BD12-2F1E-E411-9B4C-0025905A60F8.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C25AD8C2-2F1E-E411-877E-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C25AD8C2-2F1E-E411-A22A-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C273CCB6-2E1E-E411-B170-0025905B861C.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/C64D0BE5-2E1E-E411-9E00-00261894389A.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/CAC5C5CC-2E1E-E411-9745-00261894389A.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/CE464DCA-2E1E-E411-8E0B-00261894394F.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D08861DB-2E1E-E411-BC3D-002618943916.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D2E2885C-2F1E-E411-B5ED-0025905A60F8.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D45C0F09-301E-E411-95B7-00259059642A.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/D62B02C3-2F1E-E411-A6CF-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/DA3A7000-301E-E411-8993-0026189438AC.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/DE1E6560-2F1E-E411-BE90-0025905964BA.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/DE9FAD1E-2F1E-E411-A244-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E028479A-2F1E-E411-8B31-0025905A60F8.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E089A300-2F1E-E411-B0E6-002618943845.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E0B1AD1E-2F1E-E411-ADA4-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E0E2AE1E-2F1E-E411-926D-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E2E05964-2F1E-E411-90FA-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E46AA1AE-2F1E-E411-BAFD-0025905A60BC.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E6EC5864-2F1E-E411-A098-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E844DCC2-2F1E-E411-831B-0025905A6082.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/E8D8175D-2F1E-E411-A8FA-00261894386D.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/EED24278-2F1E-E411-984B-0026189438BF.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F0ABAD1E-2F1E-E411-8126-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/F4BBAD1E-2F1E-E411-B3D8-0025905938D4.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/FA32FBF4-2E1E-E411-AC21-002618FDA207.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/FAB84CD2-2E1E-E411-AF3D-002590596498.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/FCB30BFC-2F1E-E411-98AD-0025905A60AA.root',
       '/store/results/susy/StoreResults/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Spring14dr_PU_S14_POSTLS170_V6AN1_miniAOD706p1_814812ec83fce2f620905d2bb30e9100-v1/00000/FCFA2CD1-2E1E-E411-AFE5-0025905A60F8.root' ] );


secFiles.extend( [
               ] )
