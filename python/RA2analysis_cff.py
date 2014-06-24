import FWCore.ParameterSet.Config as cms

from SandBox.Skims.RA2Leptons_cff import *
from SandBox.Skims.RA2Jets_cff import *

from SandBox.Skims.mhtProducer_cfi import *
mht.JetCollection = "patJetsAK5PFPt30"
from SandBox.Skims.mhtFilter_cfi import *

from SandBox.Skims.htProducer_cfi import *
ht.JetCollection = "patJetsAK5PFPt50Eta25"
from SandBox.Skims.htFilter_cfi import *
from SandBox.Skims.jetMHTDPhiFilter_cfi import *
jetMHTDPhiFilter.JetSource = "patJetsAK5PFPt30"

##  DEFINE PATH
baselineSelectionSequence = cms.Sequence(ra2ElectronVeto*
                                         ra2PFMuonVeto*
                                         countJetsAK5PFPt50Eta25*
                                         ht*
                                         mht*
                                         htFilter*
                                         mhtFilter*
                                         jetMHTDPhiFilter
                                         )


