import FWCore.ParameterSet.Config as cms

from RecoEgamma.ElectronIdentification.electronIdLikelihoodExt_cfi import *
import RecoEgamma.ElectronIdentification.electronIdLikelihoodExt_cfi
egammaIDLikelihood = RecoEgamma.ElectronIdentification.electronIdLikelihoodExt_cfi.eidLikelihoodExt.clone()

eIdSequence = cms.Sequence( egammaIDLikelihood )

# to compute FastJet rho to correct isolation (note: EtaMax restricted to 2.5)
from RecoJets.JetProducers.kt4PFJets_cfi import *
kt6PFJetsForIsolation = kt4PFJets.clone( rParam = 0.6,
                                         doRhoFastjet = True,
                                         doAreaFastjet = cms.bool(True) )

kt6PFJetsForIsolation.Rho_EtaMax = cms.double(2.5)
kt6PFJetsForIsolation.Ghost_EtaMax = cms.double(2.5)

FastjetForIsolation = cms.Sequence( kt6PFJetsForIsolation )
