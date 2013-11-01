# Starting with a skeleton process which gets imported with the following line
from PhysicsTools.PatAlgos.patTemplate_cfg import *

from PhysicsTools.PatAlgos.tools.coreTools import *

process.source.fileNames = [
    # gluino -> everything...
    '/store/mc/Summer12/SMS-MadGraph_Pythia6Zstar_8TeV_T1tttt_2J_mGo-1100to1400_mLSP-25to500_50GeVX50GeV_Binning/AODSIM/START52_V9_FSIM-v2/30000/00326D6D-FE83-E211-9C42-001A648F1A4A.root'
        ]

process.GlobalTag.globaltag = cms.string( 'START53_V7G::All' )

from PhysicsTools.PatAlgos.patTemplate_cfg import *

#######################################
# PRIMARY VERTICES
#######################################

from PhysicsTools.SelectorUtils.pvSelector_cfi import pvSelector

process.goodOfflinePrimaryVertices = cms.EDFilter(
    "PrimaryVertexObjectFilter",
    filterParams = pvSelector.clone( maxZ = cms.double(24.0),
                                     minNdof = cms.double(4.0) # this is >= 4
                                     ),
    src=cms.InputTag('offlinePrimaryVertices')
    )

## IVF and BCandidate producer for Vbb cross check analysis
process.load('RecoVertex/AdaptiveVertexFinder/inclusiveVertexing_cff')

process.load("RecoJets.Configuration.GenJetParticles_cff")

#######################################
# SMS MODEL FILTER -- from Seema Sharma
#######################################

process.load('TopQuarkAnalysis.TopPairBSM.smsModelFilter_cfi')
process.smsModelFilter.SusyScanTopology   = cms.string('T1tttt')
process.smsModelFilter.SusyScanMotherMass = cms.double(1150)
process.smsModelFilter.SusyScanLSPMass    = cms.double(75)
process.smsModelFilter.SusyScanFracLSP    = cms.double(0.0)
process.smsModelFilter.Debug              = cms.bool(False)

# let it run
process.p0 = cms.Path(
    #process.smsModelFilter
    #*process.goodOfflinePrimaryVertices
    #*process.inclusiveVertexing
    #*
    process.genParticlesForJetsNoNu
    )

# reduce verbosity
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)

# process all the events
process.maxEvents.input = 100000
process.options.wantSummary = True

##  OUPUT CONFIGURATION
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('genParticlesForJets.root'),
                               #save only events passing the full path
                               SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p0') ),
                               outputCommands = cms.untracked.vstring('keep *_*genParticle*_*_*')
                               )

process.outpath = cms.EndPath(process.out)
