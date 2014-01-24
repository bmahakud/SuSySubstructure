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

##################################
# DEFINE MODULES FOR ANALYSIS
##################################

# selects events in which all tops decay hadronically ---- USE ONLY FOR GEN-LEVEL STUDIES
process.AllHadronicFilter = cms.EDFilter("AllHadronicGenFilter")

# Find events with at least one selected PAT muon/electron for vetoing

process.minPtMuons = cms.EDFilter("PtMinCandViewSelector",
                                  src = cms.InputTag("selectedPatMuonsPF"),
                                  ptMin = cms.double(10)
                                  )


process.MuonFinder = cms.EDFilter("CandViewCountFilter",
                                  src = cms.InputTag("minPtMuons"),
                                  minNumber = cms.uint32(1)
                                  )

process.minPtElectrons = cms.EDFilter("PtMinCandViewSelector",
                                      src = cms.InputTag("selectedPatElectronsPF"),
                                      ptMin = cms.double(10)
                                      )


process.ElectronFinder = cms.EDFilter("CandViewCountFilter",
                                      src = cms.InputTag("minPtElectrons"),
                                      minNumber = cms.uint32(1)
                                      )

# CLUSTER PARTICLES

from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.ak5GenJets_cfi import *
from RecoJets.JetProducers.ak5PFJets_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *


#####################
# CLEAN GEN PARTICLES
#####################

process.minPtGenParticles = cms.EDFilter("PtMinCandViewSelector",
                                  src = cms.InputTag("genParticles"),
                                  ptMin = cms.double(0.001)
                                  )

process.load("RecoJets.Configuration.GenJetParticles_cff")
#genParticlesForJetsNoNu gets loaded above ---
process.genParticlesForJetsNoNu.src = cms.InputTag("genParticles")

######################

process.ak1p2GenJets = ak5GenJets.clone(src = cms.InputTag("genParticles"),
                                        rParam = cms.double(1.2),
                                        useTrimming = cms.bool(True),
                                        rFilt = cms.double(0.2),
                                        trimPtFracMin = cms.double(0.05),
                                        useExplicitGhosts = cms.bool(False)
                                        )

process.ak1p2Jets = ak5PFJets.clone(src = cms.InputTag("pfNoPileUpIsoPF"),
                                    rParam = cms.double(1.2),
                                    useTrimming = cms.bool(True),
                                    rFilt = cms.double(0.2),
                                    trimPtFracMin = cms.double(0.05),
                                    useExplicitGhosts = cms.bool(False)
                                    )
    
# Calculate Substructure Variables and put into event
process.SubstructureGenJets = cms.EDProducer("SubstructureGenJets",
                                             jetCollection = cms.untracked.string("ak1p2GenJets"),
                                             clusterRadius = cms.untracked.double(1.2),
                                             trimJets      = cms.untracked.bool(True),
                                             trimPtFracMin = cms.untracked.double(0.05),
                                             debug         = cms.untracked.bool(False)
                                             )

process.Substructure = cms.EDProducer("Substructure",
                                      jetCollection = cms.untracked.string("ak1p2Jets"),
                                      clusterRadius = cms.untracked.double(1.2),
                                      trimJets      = cms.untracked.bool(True),
                                      trimPtFracMin = cms.untracked.double(0.05),
                                      debug         = cms.untracked.bool(False)
                                      )

# FILLS TREES WITH THE RELEVANT VARIABLES FOR SUM JET MASS

process.GenTreeFiller = cms.EDAnalyzer("GenJetTreeFiller",
                                       stdJetCollection = cms.untracked.string("ak5GenJetsNoNu"),
                                       fatJetCollection = cms.untracked.string("ak1p2GenJets"),
                                       debug            = cms.untracked.bool(False)
                                       )

process.TreeFiller = cms.EDAnalyzer("AnalysisTreeFiller",
                                    stdJetCollection = cms.untracked.string("patJetsAK5PF"),
                                    fatJetCollection = cms.untracked.string("ak1p2Jets"),
                                    debug            = cms.untracked.bool(False)
                                    )

#######################################                                                                                                      
# SMS MODEL FILTER -- from Seema Sharma                                                                                                      
#######################################                                                                                                      

process.load('AWhitbeck.SuSySubstructure.smsModelFilter_cfi')
process.smsModelFilter.SusyScanTopology = cms.string(options.SUSYtopo)
process.smsModelFilter.SusyScanMotherMass = cms.double(options.mGo)
process.smsModelFilter.SusyScanLSPMass = cms.double(options.mLSP)
process.smsModelFilter.SusyScanFracLSP = cms.double(0.0)
process.smsModelFilter.Debug = cms.bool(False)

## CONFIGURE TFILESERVICE

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string(options.outputFile+"_SumJetMass_AnalysisTree.root"),
                                   closeFileFast = cms.untracked.bool(True)
                                   )

##  LOAD DATAFILES
process.load("AWhitbeck.SuSySubstructure."+options.inputFilesConfig+"_cff")

##  EVENTS TO PROCESS
process.skipEvents = cms.untracked.PSet( input = cms.untracked.uint32(options.skipEvents) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.numEvents) )

##  DEFINE SCHEDULE

process.bulkPath = cms.Path(process.ak1p2Jets
                            *process.Substructure
                            *process.TreeFiller
                            #*process.minPtGenParticles
                            *process.genParticlesForJetsNoNu
                            *process.ak1p2GenJets
                            *process.SubstructureGenJets
                            *process.GenTreeFiller
                            )

if( options.useGenJets ):

    process.leptonFilterPath = cms.Path( process.AllHadronicFilter )

else:

    process.leptonFilterPath = cms.Path(#process.minPtElectrons*~process.ElectronFinder
                                        *process.minPtMuons*~process.MuonFinder
                                        )

process.susyFilterPath = cms.Path( process.smsModelFilter )

if( options.applySUSYfilter ):

    process.schedule = cms.Schedule( process.susyFilterPath,
                                     process.leptonFilterPath,
                                     process.bulkPath
                                     )
    
else:

    process.schedule = cms.Schedule( process.leptonFilterPath,
                                     process.bulkPath
                                     )

#OUPUT CONFIGURATION
#process.out = cms.OutputModule("PoolOutputModule",
#                               fileName = cms.untracked.string('test.root'),
#                               #save only events passing the full path
#                               #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
#                               outputCommands = cms.untracked.vstring('keep *_*Jet*_*_*',
#                                                                      'keep *_*Substructure*_*_*')
#                               )
#
#process.outpath = cms.EndPath(process.out)
