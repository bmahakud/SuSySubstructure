import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/02C1987C-9727-E411-94B6-0025905B85A2.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/02DE11CB-9927-E411-9F60-00261894394B.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/061017E1-9827-E411-8514-00261894382D.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/080C54C9-9827-E411-B8A0-002618943950.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/08BA0633-9727-E411-9CF4-0026189438AE.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/0AC24CAE-9927-E411-8AF0-0025905A60E0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/0AF75EA5-9727-E411-8D8D-0025905A60E0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/0C824E88-9727-E411-A351-00248C55CC9D.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/109C9F82-9727-E411-8B57-00261894398D.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/12164B88-9727-E411-9EC4-0025905A6092.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/14221FEB-9827-E411-A6EA-0025905A611C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/163BF4FF-9827-E411-95A6-0025905A6092.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/180C8683-9727-E411-A3F5-0026189438F7.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/1A8D51AB-9927-E411-96D6-0025905A6132.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/1E806381-9727-E411-A255-002618943858.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/20DCA58A-9827-E411-8B43-0026189437FD.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/22529B82-9727-E411-BD1C-0026189437FD.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/261A569C-9727-E411-88D0-0025905B85AE.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/28FF48BB-9927-E411-BDFC-0025905A608C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/2E157845-9727-E411-B47C-002618943982.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/306CF9D1-9927-E411-A921-0026189438CE.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/30E4F486-9927-E411-A88C-0025905B858C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/30F842EE-9827-E411-88BD-003048FFD730.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/3449E6EB-9827-E411-BE7C-002618943954.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/347245AF-9827-E411-8969-002618943831.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/347EA684-9727-E411-B702-0025905A610C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/38C02509-9927-E411-9446-0025905A612A.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/3A052AA4-9927-E411-97F7-0025905B858A.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/3A501E35-9727-E411-80A6-0025905A6094.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/3AEB0F19-9A27-E411-ACD3-0025905B855C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/3C65494D-9727-E411-9237-003048FFD71E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/3CD6A5E2-9827-E411-9682-002618943843.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/3E2160A5-9727-E411-B054-0025905A60E0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/447309E9-9827-E411-852C-00261894385A.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/4487F8DF-9927-E411-BA9C-0025905A6118.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/46E525E5-9827-E411-AC6E-0026189438EF.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/481A8490-9927-E411-8144-0025905B85EE.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/4A273DB5-9827-E411-AFB3-0026189438F7.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/4C15FFE9-9827-E411-9A4A-0025905A612C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/4C2FF283-9727-E411-8126-00261894394B.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/4C4629E9-9827-E411-902A-003048FFD71E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/4C9D62FE-9827-E411-BD35-00259059642E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/4CDF7285-9727-E411-8A7D-002618943831.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/529656E3-9827-E411-B5C2-00261894387C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/544707E9-9827-E411-AA75-002618FDA208.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/588F6FAC-9927-E411-B0D6-0025905A610C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/58B1E1AB-9727-E411-BE11-0025905A6132.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/5A92B89C-9727-E411-9904-00261894397A.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/5E592731-9727-E411-95A5-0025905A6110.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/5EFF8BAD-9727-E411-922F-0025905A6060.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/6000867C-9927-E411-948D-0025905A607A.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/64514E6E-9927-E411-BCDF-003048FFD728.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/64934640-9727-E411-9B8E-0025905A610C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/6624EA9A-9727-E411-B3DD-0025905A60B0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/6A2D8FBB-9727-E411-A862-0025905A60DE.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/70AEF280-9727-E411-A878-00261894382D.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/76910193-9727-E411-9086-0025905B8576.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/769E9D06-9927-E411-A351-003048D15DF0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/78F5967C-9927-E411-9652-003048FFCB74.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/7AF76042-9727-E411-B24E-0026189438F5.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/7AFD2AD4-9927-E411-8A13-003048FFD728.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/7EC644A3-9827-E411-A56D-003048FFD71E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/7EE94CAE-9927-E411-AC8B-0025905A60E0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/80CB1383-9727-E411-BA22-0026189438C0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/828FBA21-9627-E411-822B-0026189438F5.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/84811BA1-9927-E411-A61F-0026189437FD.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/84B5E9EA-9827-E411-AA3E-0025905A612C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/884D10A1-9827-E411-BB89-002618943832.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/8A181D82-9727-E411-8672-0026189437F5.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/8ABA79FF-9827-E411-B9C7-0025905A6056.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/8C36EB84-9727-E411-9B2C-0025905A609E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/8CF27AE2-9827-E411-89E0-0026189438F5.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/8E01CA97-9727-E411-A060-003048FFCBA4.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/8EB5E7D3-9827-E411-A7DC-0025905B85AA.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/907A958D-9727-E411-A89E-0025905B8582.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/90C03D81-9727-E411-8F47-002618943950.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/90DD9785-9927-E411-9514-0025905B859E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/94310C70-9727-E411-BB16-00261894398D.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/9644AACA-9827-E411-855C-002618943901.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/9672CD97-9827-E411-A536-002618943845.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/96A07A81-9727-E411-8ECC-002618943901.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/96BFA6A8-9827-E411-BDD3-002618943858.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/981DEFE1-9827-E411-B990-0025905B8582.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/987740B3-9927-E411-A821-0026189438C0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/9AA85924-9627-E411-A982-0025905A610C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/9AF1D5E8-9827-E411-8B83-0025905A607E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A095C9AB-9727-E411-92CF-0025905A6132.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A0F45672-9927-E411-A9D1-003048FFD71E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A2420BC8-9927-E411-B6D9-0025905A6136.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A27D6850-9727-E411-ABE6-0025905A6136.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A2F1F2F0-9827-E411-A94D-003048FFD75C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A412B18C-9927-E411-B10E-0025905B85AE.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A4372DA5-9927-E411-8807-00248C55CC7F.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A48FA804-9927-E411-9D3F-0025905A6066.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A4DA58A1-9727-E411-AA30-0025905B858C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A6333F0E-9927-E411-8E12-0025905AA9CC.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A845E73F-9727-E411-95F2-00259059642E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/A87A5996-9927-E411-8553-0025905A60B0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/AA5DB884-9927-E411-B426-00261894397A.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/AA6191C5-9927-E411-9D45-002618943858.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/AC1434BA-9827-E411-8709-0025905B85AA.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/AC738EBB-9727-E411-8040-0025905A612C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/B285078A-9727-E411-AC41-0025905A48F0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/B459B219-9627-E411-899F-002618FDA28E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/B49DBBE2-9827-E411-BAE0-00261894397A.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/B4F498B8-9827-E411-98C2-0025905A48F2.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/B835145E-9727-E411-A95F-0025905B8596.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/B8C0F3D3-9827-E411-B609-002618FDA207.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/BADC179C-9827-E411-BE72-0025905B85D6.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/BC57EB83-9727-E411-92E0-0026189438CE.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/BCEE0EE1-9827-E411-B209-0025905B85AA.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/BEE034A9-9827-E411-8914-00261894394B.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/C0F0B788-9727-E411-98A1-003048FFCB74.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/C2CA61ED-9827-E411-BF65-003048FFD740.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/C80D80AA-9727-E411-96D5-0025905B859E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/CAEB3B87-9727-E411-A882-0025905B858A.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/D03D56EB-9827-E411-B90F-003048FFD71E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/D63C5DEE-9827-E411-A801-0025905A608C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/D8407432-9727-E411-B495-0025905A611E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/DC07028D-9827-E411-9EBE-0026189438C0.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/E00831A0-9727-E411-A2BD-0025905B85F6.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/E2333DCA-9827-E411-929A-0025905A611E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/E2349CC4-9827-E411-8977-0025905B85AA.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/E4EFA58B-9727-E411-B12A-003048FFD730.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/E60E9B00-9927-E411-8983-0025905A6118.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/E63470EC-9827-E411-ABEA-0026189438D8.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/E8EB189F-9827-E411-AD07-0026189438CE.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/EC2770F8-9827-E411-99DD-002618943842.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/EECF2519-9627-E411-9052-0025905B85D6.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/F054BD80-9727-E411-B943-002618943845.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/F226C78E-9727-E411-A300-0025905A60DA.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/F2452EC5-9927-E411-A3C8-0025905B85F6.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/F6313FB5-9927-E411-890A-0025905A612C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/F8C950E2-9827-E411-B0E0-0026189438AE.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/FC822AC8-9927-E411-9A0B-003048FFD71E.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/FE0D6BFB-9827-E411-A6FD-0025905964A6.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/FE741ECD-9827-E411-95BF-0025905B860C.root',
       '/store/results/b2g/StoreResults/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/USER/Run2012D_22Jan2013_v2_TLBSM_53x_v3_45cbb6c27540456f7aaf244304c73a89-v1/00000/FEEB6973-9927-E411-8272-0025905A6132.root' ] );


secFiles.extend( [
               ] )
