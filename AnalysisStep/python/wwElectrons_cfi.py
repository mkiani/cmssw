import FWCore.ParameterSet.Config as cms

        
from PhysicsTools.PatAlgos.patSequences_cff import *

wwEleMatch = selectedPatElectrons.clone()
wwEleMatch.src = "boostedElectrons"
wwEleMatch.filter = cms.bool(False)
wwEleMatch.cut = ( "pt > 10 && abs(eta)<2.5 ")
#wwEleMatch.cut = ( "pt > 10 && genParticleRef.isNonnull() && abs(genParticleRef.get().pdgId())==11 && abs(genParticleRef.get().mother().mother().pdgId()) ==24")


from WWAnalysis.AnalysisStep.electronIDs_cff import *


# LHL
wwEleIDLHL = selectedPatElectrons.clone()
wwEleIDLHL.src = "wwEleMatch"
wwEleIDLHL.filter = cms.bool(False)
wwEleIDLHL.cut = ( ELE_ID_LH_95_2011 )

wwEleISOLHL = selectedPatElectrons.clone()
wwEleISOLHL.src = "wwEleIDLHL"
wwEleISOLHL.filter = cms.bool(False)
wwEleISOLHL.cut = ( ELE_ISO_LH_95_2011 )

wwEleCONVLHL = selectedPatElectrons.clone()
wwEleCONVLHL.src = "wwEleISOLHL"
wwEleCONVLHL.filter = cms.bool(False)
wwEleCONVLHL.cut = ( ELE_NOCONV )

wwEleIPLHL = selectedPatElectrons.clone()
wwEleIPLHL.src = "wwEleCONVLHL"
wwEleIPLHL.filter = cms.bool(False)
wwEleIPLHL.cut = ( ELE_IP )

# LHT
wwEleIDLHT = selectedPatElectrons.clone()
wwEleIDLHT.src = "wwEleMatch"
wwEleIDLHT.filter = cms.bool(False)
wwEleIDLHT.cut = ( ELE_ID_LH_90_2011 )

wwEleISOLHT = selectedPatElectrons.clone()
wwEleISOLHT.src = "wwEleIDLHT"
wwEleISOLHT.filter = cms.bool(False)
wwEleISOLHT.cut = ( ELE_ISO_LH_90_2011 )

wwEleCONVLHT = selectedPatElectrons.clone()
wwEleCONVLHT.src = "wwEleISOLHT"
wwEleCONVLHT.filter = cms.bool(False)
wwEleCONVLHT.cut = ( ELE_NOCONV )

wwEleIPLHT = selectedPatElectrons.clone()
wwEleIPLHT.src = "wwEleCONVLHT"
wwEleIPLHT.filter = cms.bool(False)
wwEleIPLHT.cut = ( ELE_IP )

wwEleISOPFLHT = selectedPatElectrons.clone()
wwEleISOPFLHT.src = "wwEleIDLHT"
wwEleISOPFLHT.filter = cms.bool(False)
wwEleISOPFLHT.cut = ( ELE_ISOPF_LH_90_2011 )

wwEleCONVPFLHT = selectedPatElectrons.clone()
wwEleCONVPFLHT.src = "wwEleISOPFLHT"
wwEleCONVPFLHT.filter = cms.bool(False)
wwEleCONVPFLHT.cut = ( ELE_NOCONV )

wwEleIPPFLHT = selectedPatElectrons.clone()
wwEleIPPFLHT.src = "wwEleCONVPFLHT"
wwEleIPPFLHT.filter = cms.bool(False)
wwEleIPPFLHT.cut = ( ELE_IP )

# CBL
wwEleIDCBL = selectedPatElectrons.clone()
wwEleIDCBL.src = "wwEleMatch"
wwEleIDCBL.filter = cms.bool(False)
wwEleIDCBL.cut = ( ELE_ID_CB_95_2011 )

wwEleISOCBL = selectedPatElectrons.clone()
wwEleISOCBL.src = "wwEleIDCBL"
wwEleISOCBL.filter = cms.bool(False)
wwEleISOCBL.cut = ( ELE_ISO_CB_95_2011 )

wwEleCONVCBL = selectedPatElectrons.clone()
wwEleCONVCBL.src = "wwEleISOCBL"
wwEleCONVCBL.filter = cms.bool(False)
wwEleCONVCBL.cut = ( ELE_NOCONV )

wwEleIPCBL = selectedPatElectrons.clone()
wwEleIPCBL.src = "wwEleCONVCBL"
wwEleIPCBL.filter = cms.bool(False)
wwEleIPCBL.cut = ( ELE_IP )

# CBT
wwEleIDCBT = selectedPatElectrons.clone()
wwEleIDCBT.src = "wwEleMatch"
wwEleIDCBT.filter = cms.bool(False)
wwEleIDCBT.cut = ( ELE_ID_CB_90_2011 )

wwEleISOCBT = selectedPatElectrons.clone()
wwEleISOCBT.src = "wwEleIDCBT"
wwEleISOCBT.filter = cms.bool(False)
wwEleISOCBT.cut = ( ELE_ISO_CB_90_2011 )

wwEleCONVCBT = selectedPatElectrons.clone()
wwEleCONVCBT.src = "wwEleISOCBT"
wwEleCONVCBT.filter = cms.bool(False)
wwEleCONVCBT.cut = ( ELE_NOCONV )

wwEleIPCBT = selectedPatElectrons.clone()
wwEleIPCBT.src = "wwEleCONVCBT"
wwEleIPCBT.filter = cms.bool(False)
wwEleIPCBT.cut = ( ELE_IP )

# Merge
wwEleIDMerge = selectedPatElectrons.clone()
wwEleIDMerge.src = "wwEleMatch"
wwEleIDMerge.filter = cms.bool(False)
wwEleIDMerge.cut = ( ELE_MERGE_ID )

wwEleISOMerge = selectedPatElectrons.clone()
wwEleISOMerge.src = "wwEleIDMerge"
wwEleISOMerge.filter = cms.bool(False)
wwEleISOMerge.cut = ( ELE_MERGE_ISO )

wwEleCONVMerge = selectedPatElectrons.clone()
wwEleCONVMerge.src = "wwEleISOMerge"
wwEleCONVMerge.filter = cms.bool(False)
wwEleCONVMerge.cut = ( ELE_MERGE_CONV )

wwEleIPMerge = selectedPatElectrons.clone()
wwEleIPMerge.src = "wwEleCONVMerge"
wwEleIPMerge.filter = cms.bool(False)
wwEleIPMerge.cut = ( ELE_MERGE_ISO )

wwElectronSequence = cms.Sequence(  
    wwEleMatch *
#     wwEleIDLHL *
#     wwEleISOLHL *
#     wwEleCONVLHL *
#     wwEleIPLHL *
    wwEleIDLHT *
    wwEleISOLHT *
    wwEleCONVLHT *
    wwEleIPLHT *
    wwEleIDMerge *
    wwEleISOMerge *
    wwEleCONVMerge *
    wwEleIPMerge 
#     wwEleISOPFLHT *
#     wwEleCONVPFLHT *
#     wwEleIPPFLHT 
#     wwEleIDCBL *
#     wwEleISOCBL *
#     wwEleCONVCBL *
#     wwEleIPCBL *
#     wwEleIDCBT *
#     wwEleISOCBT *
#     wwEleCONVCBT *
#     wwEleIPCBT 
)


