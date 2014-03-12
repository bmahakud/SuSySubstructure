import FWCore.ParameterSet.Config as cms

process = cms.Process("analysis")

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
    )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.options   = cms.untracked.PSet(
    SkipEvent   = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool(True)
    )

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = "START53_V11::All"

##################################
# DEFINE MODULES FOR ANALYSIS
##################################

# CLUSTER PARTICLES

from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.ak5GenJets_cfi import *
from RecoJets.JetProducers.ak5PFJets_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *

######################

# cluster PF candidates into anti-kt (R=1.2) jets

process.ak1p2Jets = ak5PFJets.clone(src = cms.InputTag("pfNoPileUpIsoPF"),
                                    rParam = cms.double(1.2),
                                    useTrimming = cms.bool(True),
                                    rFilt = cms.double(0.2),
                                    trimPtFracMin = cms.double(0.05),
                                    useExplicitGhosts = cms.bool(False)
                                    )
    

# Produce subjet collection from the anti-kt (R=1.2) jets
# subjets save to the event as a simple collection of XYZTLorentzVectors

process.fatJetSubjets = cms.EDProducer("SubjetProducer",
                                       jetCollection     = cms.untracked.string("ak1p2Jets"),
                                       clusterRadius     = cms.untracked.double(1.2),
                                       trimJets          = cms.untracked.bool(True),
                                       trimPtFracMin     = cms.untracked.double(0.05),
                                       subjetPtCut       = cms.untracked.double(30.),
                                       subjetMassCut     = cms.untracked.double(30.),
                                       subjetRcut        = cms.untracked.double(0.15),
                                       subjetPtImbalance = cms.untracked.double(0.15),
                                       debug             = cms.untracked.bool(False)
                                       )


# anti-kt (R=0.5) jets are reclustered into anti-kt (R=1.2) "jets"
# subjets save to the event as a simple collection of XYZTLorentzVectors


process.fattenedJets = cms.EDProducer("JetFatteningProducer",
                                     jetCollection = cms.untracked.string("patJetsAK5PFPt30"),
                                     clusterRadius = cms.untracked.double(1.2),
                                     debug         = cms.untracked.bool(False)
                                     )

# TTree filled with basic kinematic informatino for each jet collection (separated by ":") 
# or pseudo-particle (collection of XYZTLorentzVectors) collection.  Variables filled are
# jet - pt, eta, phi, mass (pt>30 |eta|<5.0)  
# event - Ht, missing Ht, delta-phi (pt>30 |eta|<5.0)
# event sumJetMass (pt>50 |eta|<2.5)

process.TreeFiller = cms.EDAnalyzer("AnalysisTreeFiller",
                                    jetCollection = cms.untracked.string("patJetsAK5PFPt30:ak1p2Jets"),
                                    pseudoParticleCollection = cms.untracked.string("fatJetSubjets:fattenedJets"),
                                    debug         = cms.untracked.bool(False)
                                    )

## CONFIGURE TFILESERVICE

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("example_SumJetMass_AnalysisTree.root"),
                                   closeFileFast = cms.untracked.bool(True)
                                   )

##  LOAD DATAFILES
process.load("AWhitbeck.SuSySubstructure.SMS-T1tttt_mGo-1025_mLSP_225_8TeV_LPCSUSYPAT_cff")

##  DEFINE SCHEDULE

process.bulkSequence = cms.Sequence(process.ak1p2Jets
                                    *process.fatJetSubjets
                                    *process.fattenedJets
                                    *process.TreeFiller
                                    )

process.path = cms.Path(process.bulkSequence)

