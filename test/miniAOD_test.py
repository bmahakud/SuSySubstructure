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

process.ak1p2Jets = ak5PFJets.clone(src = cms.InputTag("packedPFCandidates"),
                                    rParam = cms.double(1.2),
                                    useTrimming = cms.bool(True),
                                    rFilt = cms.double(0.2),
                                    trimPtFracMin = cms.double(0.05),
                                    useExplicitGhosts = cms.bool(False)
                                    )

# Produce subjet collection

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

# build fat jets from AK5 jets

process.fattenedJets = cms.EDProducer("JetFatteningProducer",
                                     jetCollection = cms.untracked.string("slimmedJets"),
                                     clusterRadius = cms.untracked.double(1.2),
                                     debug         = cms.untracked.bool(False)
                                     )

# jet selections

process.HTJets = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                              cut = cms.string  ('pt > 50.0 && eta < 2.5 && eta > -2.5'),
                              src = cms.InputTag("slimmedJets"),
                              )

process.MHTJets = cms.EDFilter("CandPtrSelector", #"CandViewSelector",
                               cut = cms.string  ('pt > 30.0 && eta < 5.0 && eta > -2.5'),
                               src = cms.InputTag("slimmedJets"),
                               )

# di-lepton control region
process.hardMuons = cms.EDFilter("CandPtrSelector", #"CandViewSelector",
                               cut = cms.string  ('pt > 20.0'),
                               src = cms.InputTag("slimmedMuons"),
                               )
process.muonFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("hardMuons"),
    minNumber = cms.uint32(2),
  )
# photon control region
process.hardPhotons = cms.EDFilter("CandPtrSelector", #"CandViewSelector",
                               cut = cms.string  ('pt > 100.0'),
                               src = cms.InputTag("slimmedPhotons"),
                               )
process.photonFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("hardPhotons"),
    minNumber = cms.uint32(1),
  )
# FILLS TREES WITH THE RELEVANT VARIABLES FOR SUM JET MASS

process.TreeFiller = cms.EDAnalyzer("AnalysisTreeFiller",
                                    jetCollection = cms.untracked.string("HTJets:MHTJets"), #:ak1p2Jets"),
                                    pseudoParticleCollection = cms.untracked.string(""), #"fatJetSubjets:fattenedJets"),
                                    METcollection = cms.untracked.InputTag("slimmedMETs"),
                                    muonCollection = cms.untracked.InputTag("slimmedMuons"),
                                    electronCollection = cms.untracked.InputTag("slimmedElectrons"),
                                    photonCollection = cms.untracked.InputTag("slimmedPhotons"),
                                    ConversionsSource = cms.InputTag("reducedEgamma"),
                                    VertexSource = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                    BeamSpotSource = cms.InputTag("offlineBeamSpot"),
                                    RhoIsoSource = cms.InputTag("kt6PFJets","rho"),
                                    EleIsoValInputTags = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03PFIdPFIso'),
                                                                       cms.InputTag('elPFIsoValueGamma03PFIdPFIso'),
                                                                       cms.InputTag('elPFIsoValueNeutral03PFIdPFIso')),
                                    PhotonIsoValInputTags = cms.VInputTag(cms.InputTag('phPFIsoValueCharged03PFIdPFIso'),
                                                                          cms.InputTag('phPFIsoValueGamma03PFIdPFIso'),
                                                                          cms.InputTag('phPFIsoValueNeutral03PFIdPFIso')),
                                    debug         = cms.untracked.bool(False)
                                    )

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

##  EVENTS TO PROCESS
process.skipEvents = cms.untracked.PSet( input = cms.untracked.uint32(options.skipEvents) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.numEvents) )

##  DEFINE SCHEDULE

process.bulkSequence = cms.Sequence(#process.ak1p2Jets
                                    #*process.fatJetSubjets
                                    process.fattenedJets 
                                    #process.hardPhotons
                                    #*process.photonFilter
                                    #*process.hardMuons
                                    #*process.muonFilter
                                    *process.HTJets
                                    *process.MHTJets
                                    *process.TreeFiller
                                    )

process.path = cms.Path( process.bulkSequence )

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
