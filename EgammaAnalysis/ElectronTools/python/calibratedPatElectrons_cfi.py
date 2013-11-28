
import FWCore.ParameterSet.Config as cms


#==============================================================================
# corrected pat electrons
#==============================================================================

calibratedPatElectrons = cms.EDProducer("CalibratedPatElectronProducer",

    # input collections
    inputPatElectronsTag = cms.InputTag("eleRegressionEnergy"),
    #inputPatElectronsTag = cms.InputTag("cleanPatElectrons"),

    # data or MC corrections
    # if isMC is false, data corrections are applied
    isMC = cms.bool(False),

    # set to True to get more printout   
    verbose = cms.bool(False),

    # set to True to get special "fake" smearing for synchronization. Use JUST in case of synchronization
    synchronization = cms.bool(False),
 
    updateEnergyError = cms.bool(True),

    # define the type of the scale corrections
    correctionsType = cms.int32(2),
    # Apply or not the linearity correction on data
    # Can only be applied with combinationType = 3
    applyLinearityCorrection = cms.bool(True),
    # define the type of the E-p combination
    combinationType = cms.int32(3),
    
    lumiRatio = cms.double(0.0),
    
    # input datasets
    # Prompt means May10+Promptv4+Aug05+Promptv6 for 2011
    # ReReco means Jul05+Aug05+Oct03 for 2011
    # Jan16ReReco means Jan16 for 2011
    # Summer11 means summer11 MC..
    #inputDataset = cms.string("ReReco"),
    inputDataset = cms.string("Jan16ReReco"),
    combinationRegressionInputPath = cms.string("EgammaAnalysis/ElectronTools/data/eleEnergyReg2011Weights_WithSubClusters_VMay28.root"),
    scaleCorrectionsInputPath = cms.string("EgammaAnalysis/ElectronTools/data/scales2011NewReg-May2013.csv"),
    linearityCorrectionsInputPath = cms.string("EgammaAnalysis/ElectronTools/data/linearityNewReg2011-May2013.csv")
    
)


