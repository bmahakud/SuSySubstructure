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

##################
# lepton stuff
##################

## --- Selection sequences ---------------------------------------------
# leptons
process.load("PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi")
process.load("PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi")
process.selectedIDIsoMuons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedMuons"), cut = cms.string('''abs(eta)<2.5 && pt>10. &&
    (pfIsolationR04().sumChargedHadronPt+
    max(0.,pfIsolationR04().sumNeutralHadronEt+
    pfIsolationR04().sumPhotonEt-
    0.50*pfIsolationR04().sumPUPt))/pt < 0.20 && 
    (isPFMuon && (isGlobalMuon || isTrackerMuon) )'''))
process.selectedIDMuons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedMuons"), cut = cms.string('''abs(eta)<2.5 && pt>10. && 
    (isPFMuon && (isGlobalMuon || isTrackerMuon) )'''))
process.selectedIDIsoElectrons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedElectrons"), cut = cms.string('''abs(eta)<2.5 && pt>10. &&
    gsfTrack.isAvailable() &&
    gsfTrack.trackerExpectedHitsInner.numberOfLostHits<2 &&
    (pfIsolationVariables().sumChargedHadronPt+
    max(0.,pfIsolationVariables().sumNeutralHadronEt+
    pfIsolationVariables().sumPhotonEt-
    0.5*pfIsolationVariables().sumPUPt))/pt < 0.20'''))
process.selectedIDElectrons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedElectrons"), cut = cms.string('''abs(eta)<2.5 && pt>10. &&
    gsfTrack.isAvailable() &&
    gsfTrack.trackerExpectedHitsInner.numberOfLostHits<2'''))

process.muonVeto = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("selectedIDIsoMuons"),
    minNumber = cms.uint32(1),
  )

process.ElectronVeto = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("selectedIDIsoElectrons"),
    minNumber = cms.uint32(1),
  )
    
##################
# jet stuff 
##################
from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.ak5GenJets_cfi import *
from RecoJets.JetProducers.ak5PFJets_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *

######################

process.nonZeroGenParticles = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                                          cut = cms.string  (' pt > 0.0 '),
                                          src = cms.InputTag("prunedGenParticles")
                                          )

process.ak1p2GenJets = ak5GenJets.clone(src = cms.InputTag("nonZeroGenParticles"),
                                        rParam = cms.double(1.2),
                                        useTrimming = cms.bool(True),
                                        rFilt = cms.double(0.2),
                                        trimPtFracMin = cms.double(0.05),
                                        useExplicitGhosts = cms.bool(False)
                                        )

process.ak1p2Jets = ak5PFJets.clone(src = cms.InputTag("packedPFCandidates"),
                                  rParam = cms.double(1.2),
                                  useTrimming = cms.bool(True),
                                  rFilt = cms.double(0.2),
                                  trimPtFracMin = cms.double(0.05),
                                  useExplicitGhosts = cms.bool(False)
                                  )

# jet selections
process.slimmedGenJetsPt10 = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                                          cut = cms.string  ('pt > 10.0 && eta < 5.0 && eta > -5.0'),
                                          src = cms.InputTag("slimmedGenJets")
                                          )

process.slimmedGenJetsPt20 = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                                          cut = cms.string  ('pt > 20.0 && eta < 5.0 && eta > -5.0'),
                                          src = cms.InputTag("slimmedGenJets")
                                          )

process.slimmedGenJetsPt30 = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                                          cut = cms.string  ('pt > 30.0 && eta < 5.0 && eta > -5.0'),
                                          src = cms.InputTag("slimmedGenJets")
                                          )

process.slimmedGenJetsPt50 = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                                          cut = cms.string  ('pt > 50.0 && eta < 5.0 && eta > -5.0'),
                                          src = cms.InputTag("slimmedGenJets")
                                          )

process.HTGenJets = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                                 cut = cms.string  ('pt > 50.0 && eta < 2.5 && eta > -2.5'),
                                 src = cms.InputTag("slimmedGenJets"),
                                 )

process.MHTGenJets = cms.EDFilter("CandPtrSelector", #"CandViewSelector",
                                  cut = cms.string  ('pt > 30.0 && eta < 5.0 && eta > -5.0'),
                                  src = cms.InputTag("slimmedGenJets"),
                                  )


process.slimmedJetsPt10 = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                                          cut = cms.string  ('pt > 10.0 && eta < 5.0 && eta > -5.0'),
                                          src = cms.InputTag("slimmedJets")
                                          )

process.slimmedJetsPt20 = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                                          cut = cms.string  ('pt > 20.0 && eta < 5.0 && eta > -5.0'),
                                          src = cms.InputTag("slimmedJets")
                                          )

process.slimmedJetsPt30 = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                                          cut = cms.string  ('pt > 30.0 && eta < 5.0 && eta > -5.0'),
                                          src = cms.InputTag("slimmedJets")
                                          )

process.slimmedJetsPt50 = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                                          cut = cms.string  ('pt > 50.0 && eta < 5.0 && eta > -5.0'),
                                          src = cms.InputTag("slimmedJets")
                                          )

process.HTJets = cms.EDFilter("CandPtrSelector",  #"CandViewSelector",
                              cut = cms.string  ('pt > 50.0 && eta < 2.5 && eta > -2.5'),
                              src = cms.InputTag("slimmedJets")
                                 )

process.MHTJets = cms.EDFilter("CandPtrSelector", #"CandViewSelector",
                                  cut = cms.string  ('pt > 30.0 && eta < 5.0 && eta > -5.0'),
                                  src = cms.InputTag("slimmedJets")
                                  )



# build fat jets from AK5 jets
process.fattenedGenJetsPt10 = cms.EDProducer("JetFatteningProducer",
                                             jetCollection = cms.untracked.string("slimmedGenJetsPt10"),
                                             clusterRadius = cms.untracked.double(1.2),
                                             trim          = cms.untracked.bool(False),
                                             debug         = cms.untracked.bool(False)
                                             )

process.fattenedGenJetsPt20 = cms.EDProducer("JetFatteningProducer",
                                             jetCollection = cms.untracked.string("slimmedGenJetsPt20"),
                                             clusterRadius = cms.untracked.double(1.2),
                                             trim          = cms.untracked.bool(False),
                                             debug         = cms.untracked.bool(False)
                                             )

process.fattenedGenJetsPt30 = cms.EDProducer("JetFatteningProducer",
                                             jetCollection = cms.untracked.string("slimmedGenJetsPt30"),
                                             clusterRadius = cms.untracked.double(1.2),
                                             trim          = cms.untracked.bool(False),
                                             debug         = cms.untracked.bool(False)
                                             )

process.fattenedGenJetsPt50 = cms.EDProducer("JetFatteningProducer",
                                             jetCollection = cms.untracked.string("slimmedGenJetsPt50"),
                                             clusterRadius = cms.untracked.double(1.2),
                                             trim          = cms.untracked.bool(False),
                                             debug         = cms.untracked.bool(False)
                                             )

process.fattenedJetsPt10 = cms.EDProducer("JetFatteningProducer",
                                          jetCollection = cms.untracked.string("slimmedJetsPt10"),
                                          clusterRadius = cms.untracked.double(1.2),
                                          trim          = cms.untracked.bool(False),
                                          debug         = cms.untracked.bool(False)
                                          )

process.fattenedJetsPt20 = cms.EDProducer("JetFatteningProducer",
                                          jetCollection = cms.untracked.string("slimmedJetsPt20"),
                                          clusterRadius = cms.untracked.double(1.2),
                                          trim          = cms.untracked.bool(False),
                                          debug         = cms.untracked.bool(False)
                                          )

process.fattenedJetsPt30 = cms.EDProducer("JetFatteningProducer",
                                          jetCollection = cms.untracked.string("slimmedJetsPt30"),
                                          clusterRadius = cms.untracked.double(1.2),
                                          trim          = cms.untracked.bool(False),
                                          debug         = cms.untracked.bool(False)
                                          )

process.fattenedJetsPt50 = cms.EDProducer("JetFatteningProducer",
                                          jetCollection = cms.untracked.string("slimmedJetsPt50"),
                                          clusterRadius = cms.untracked.double(1.2),
                                          trim          = cms.untracked.bool(False),
                                          debug         = cms.untracked.bool(False)
                                          )

# now with trimming...
process.fattenedJetsPt10Trim = cms.EDProducer("JetFatteningProducer",
                                              jetCollection = cms.untracked.string("slimmedJetsPt10"),
                                              clusterRadius = cms.untracked.double(1.2),
                                              trim          = cms.untracked.bool(True),
                                              debug         = cms.untracked.bool(False)
                                              )

process.fattenedJetsPt20Trim = cms.EDProducer("JetFatteningProducer",
                                              jetCollection = cms.untracked.string("slimmedJetsPt20"),
                                              clusterRadius = cms.untracked.double(1.2),
                                              trim          = cms.untracked.bool(True),
                                              debug         = cms.untracked.bool(False)
                                              )


process.fattenedJetsPt30Trim = cms.EDProducer("JetFatteningProducer",
                                              jetCollection = cms.untracked.string("slimmedJetsPt30"),
                                              clusterRadius = cms.untracked.double(1.2),
                                              trim          = cms.untracked.bool(True),
                                              debug         = cms.untracked.bool(False)
                                              )


process.fattenedJetsPt50Trim = cms.EDProducer("JetFatteningProducer",
                                              jetCollection = cms.untracked.string("slimmedJetsPt50"),
                                              clusterRadius = cms.untracked.double(1.2),
                                              trim          = cms.untracked.bool(True),
                                              debug         = cms.untracked.bool(False)
                                              )

process.fattenedGenJetsPt10Trim = cms.EDProducer("JetFatteningProducer",
                                                 jetCollection = cms.untracked.string("slimmedGenJetsPt10"),
                                                 clusterRadius = cms.untracked.double(1.2),
                                                 trim          = cms.untracked.bool(True),
                                                 debug         = cms.untracked.bool(False)
                                                 )

process.fattenedGenJetsPt20Trim = cms.EDProducer("JetFatteningProducer",
                                                 jetCollection = cms.untracked.string("slimmedGenJetsPt20"),
                                                 clusterRadius = cms.untracked.double(1.2),
                                                 trim          = cms.untracked.bool(True),
                                                 debug         = cms.untracked.bool(False)
                                                 )

process.fattenedGenJetsPt30Trim = cms.EDProducer("JetFatteningProducer",
                                                 jetCollection = cms.untracked.string("slimmedGenJetsPt30"),
                                                 clusterRadius = cms.untracked.double(1.2),
                                                 trim          = cms.untracked.bool(True),
                                                 debug         = cms.untracked.bool(False)
                                                 )

process.fattenedGenJetsPt50Trim = cms.EDProducer("JetFatteningProducer",
                                                 jetCollection = cms.untracked.string("slimmedGenJetsPt50"),
                                                 clusterRadius = cms.untracked.double(1.2),
                                                 trim          = cms.untracked.bool(True),
                                                 debug         = cms.untracked.bool(False)
                                                 )

# FILLS TREES WITH THE RELEVANT VARIABLES FOR SUM JET MASS

process.TreeFiller = cms.EDAnalyzer("AnalysisTreeFiller",
                                    jetCollection = cms.untracked.string("HTJets:MHTJets:ak1p2Jets:ak1p2GenJets"),
                                    pseudoParticleCollection = cms.untracked.string("fattenedJetsPt50:fattenedJetsPt30:fattenedJetsPt20:fattenedJetsPt10:fattenedGenJetsPt50:fattenedGenJetsPt30:fattenedGenJetsPt20:fattenedGenJetsPt10:fattenedJetsPt50Trim:fattenedJetsPt30Trim:fattenedJetsPt20Trim:fattenedJetsPt10Trim:fattenedGenJetsPt50Trim:fattenedGenJetsPt30Trim:fattenedGenJetsPt20Trim:fattenedGenJetsPt10Trim"), #"fatJetSubjets:fattenedJets"),
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

process.bulkSequence = cms.Sequence(#process.selectedIDMuons
                                    process.selectedIDIsoMuons
                                    *~process.muonVeto
                                    #*process.selectedIDElectrons
                                    *process.selectedIDIsoElectrons
                                    *~process.ElectronVeto
                                    *process.nonZeroGenParticles
                                    *process.ak1p2Jets
                                    *process.ak1p2GenJets
                                    *process.slimmedJetsPt10
                                    *process.slimmedJetsPt20
                                    *process.slimmedJetsPt30
                                    *process.slimmedJetsPt50
                                    *process.fattenedJetsPt10 
                                    *process.fattenedJetsPt20 
                                    *process.fattenedJetsPt30 
                                    *process.fattenedJetsPt50 
                                    *process.fattenedJetsPt10Trim 
                                    *process.fattenedJetsPt20Trim
                                    *process.fattenedJetsPt30Trim
                                    *process.fattenedJetsPt50Trim
                                    *process.HTJets
                                    *process.MHTJets
                                    *process.slimmedGenJetsPt10
                                    *process.slimmedGenJetsPt20
                                    *process.slimmedGenJetsPt30
                                    *process.slimmedGenJetsPt50
                                    *process.fattenedGenJetsPt10 
                                    *process.fattenedGenJetsPt20 
                                    *process.fattenedGenJetsPt30 
                                    *process.fattenedGenJetsPt50 
                                    *process.fattenedGenJetsPt10Trim 
                                    *process.fattenedGenJetsPt20Trim 
                                    *process.fattenedGenJetsPt30Trim 
                                    *process.fattenedGenJetsPt50Trim 
                                    *process.HTGenJets
                                    *process.MHTGenJets
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
