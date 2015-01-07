import FWCore.ParameterSet.Config as cms
from commandLineParameters import *

process = cms.Process("analysis")

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
    )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery

process.options   = cms.untracked.PSet(
    SkipEvent   = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(True)
    )

## configure geometry & conditions
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

##################################
# DEFINE MODULES FOR ANALYSIS
##################################

###############
# photon stuff
###############

process.photonProd = cms.EDProducer("PhotonIDisoProducer",
                                    photonCollection = cms.untracked.InputTag("slimmedPhotons"),
                                    rhoCollection = cms.untracked.InputTag("fixedGridRhoFastjetAll"), 
                                    debug = cms.untracked.bool(False)
                                    )

###############
# tree maker
###############

from AllHadronicSUSY.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeTreeFromMiniADO
makeTreeTreeFromMiniADO(process,
                outFileName="ReducedSelection",
                NJetsMin=options.minNjets,
                HTMin=options.minHT,
                MHTMin=options.minMHT,
                reportEveryEvt=options.reportEvery,
                testFileName="",
		Global_Tag="PHYS14_25_V2::All",
		MC=True,
		QCD=True,
		LostLepton=True,
		debug = False,
                numProcessedEvt=options.numEvents
                        )

#vector<TLorentzVector>      "photonProd"   ""                      "analysis"   
#vector<double>              "photonProd"   "genMatched"            "analysis"   
#vector<double>              "photonProd"   "hadTowOverEM"          "analysis"   
#vector<double>              "photonProd"   "hasPixelSeed"          "analysis"   
#vector<double>              "photonProd"   "isEB"                  "analysis"   
#vector<double>              "photonProd"   "pfChargedIso"          "analysis"   
#vector<double>              "photonProd"   "pfChargedIsoRhoCorr"   "analysis"   
#vector<double>              "photonProd"   "pfGammaIso"            "analysis"   
#vector<double>              "photonProd"   "pfGammaIsoRhoCorr"     "analysis"   
#vector<double>              "photonProd"   "pfNeutralIso"          "analysis"   
#vector<double>              "photonProd"   "pfNeutralIsoRhoCorr"   "analysis"   
#vector<double>              "photonProd"   "sigmaIetaIeta"         "analysis" 

process.TreeMaker2.VarsTLorentzVector.append(cms.InputTag("photonProd",""))
process.TreeMaker2.VarsTLorentzVectorNamesInTree.append("photon4vec")

## CONFIGURE TFILESERVICE

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(options.outputFile+"_SumJetMass_AnalysisTree.root"),
                                   closeFileFast = cms.untracked.bool(True)
                                   )

##  LOAD DATAFILES
if options.inputFilesConfig!="" :
    process.load("AWhitbeck.SuSySubstructure."+options.inputFilesConfig+"_cff")

if options.files!=[] :   
    readFiles = cms.untracked.vstring()
    readFiles.extend( options.files )
    process.source = cms.Source("PoolSource",
                                fileNames = readFiles )

##  DEFINE SCHEDULE

process.path = cms.Path( process.Baseline * process.photonProd * process.WriteTree )

#OUPUT CONFIGURATION
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('test.root'),
                               #save only events passing the full path
                               #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               outputCommands = cms.untracked.vstring('drop *','keep *_*photon*_*_*'
                                                                      )
                               )

process.outpath = cms.EndPath(process.out)
