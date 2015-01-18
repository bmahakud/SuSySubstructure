import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/08EEEB63-8B7F-E411-A70B-0025905A606A.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/10EEB691-717F-E411-AC97-0025905A612E.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/24C359FA-DF80-E411-9EDD-002618943908.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/281D8D34-C07F-E411-9AA3-0025905B85AE.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/2ABAB4A8-717F-E411-A65C-0025905B8610.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/2C03AF50-1A80-E411-B236-0026189438EF.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/44E9F434-C07F-E411-A321-0025905A48C0.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/46DE234B-897F-E411-BAAB-0026189438F4.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/486E7F35-C07F-E411-86C3-0025905A60BC.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/48EF5791-627D-E411-9F04-00261894382D.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/703124EE-957F-E411-BA48-0025905A6064.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/72DB8D35-C07F-E411-9A7A-0025905A60BC.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/7AB5CC9C-837F-E411-8383-002618943869.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/7AEDA9A2-907F-E411-935D-003048FFD796.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/7E7E4F1C-6281-E411-8CDA-0025905A60D6.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/82440872-4A7F-E411-8627-002618943856.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/9096BD63-1A80-E411-A2EB-0026189438EF.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/989124FF-627D-E411-BEEA-003048FFD7A2.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/A0B12328-937F-E411-B60C-003048FFD796.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/A2F4A69C-627D-E411-BAA2-003048FFD756.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/A8E6C133-C07F-E411-8C80-0025905B855E.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/B2B7EBA0-5681-E411-B1CD-002590593920.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/BCBC9B3E-2A7E-E411-AE18-0025905B8576.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/C0DE2981-877F-E411-BF8E-00259059642E.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/D214B34E-637D-E411-8FA2-0026189438B0.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/D4B91C5C-2B7E-E411-AB2B-0025905B85A2.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/D66236A7-2A7E-E411-8487-0025905B85F6.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/E05C1852-637D-E411-B508-002618943902.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/E0D0E033-1A80-E411-A6CF-0025905A60D6.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/E2EB6897-5681-E411-A015-0025905B8596.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/F6C285EF-897F-E411-B06C-0026189438F2.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/00000/FA76E64F-637D-E411-940B-002618943983.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/0635F76A-EA78-E411-A848-0025905A6066.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/068D235B-677D-E411-A9AC-0025905A497A.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/14C3CD6B-EA78-E411-B6B6-00261894398B.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/2AB8736A-EA78-E411-ACFB-0025905A48C0.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/40C7176A-EA78-E411-BAD0-0025905A60A0.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/44C90E68-EA78-E411-9C55-0026189438B8.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/7C4874A7-4481-E411-B616-003048FFCBB0.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/7C55106B-EA78-E411-8A76-0025905A60D0.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/8A343C4F-5C7D-E411-B723-002354EF3BD0.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/8AAA426C-EA78-E411-AA5B-0025905A48F0.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/B641686A-EA78-E411-BB53-0025905A60CA.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/B875486D-EA78-E411-B226-0025905A6110.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/C2759868-EA78-E411-AC3E-00261894383B.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/CA6F58C6-6B7D-E411-B78F-0025905A6122.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/D24F1C69-EA78-E411-A2E8-002618943809.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/D608546A-EA78-E411-B1E5-0025905A6126.root',
       '/store/mc/Phys14DR/QCD_Pt-470to600_Tune4C_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_castor_PHYS14_25_V1-v2/10000/F609926A-EA78-E411-89BC-0025905A60BC.root' ] );


secFiles.extend( [
               ] )

