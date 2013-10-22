import FWCore.ParameterSet.Config as cms
from CMGTools.External.pujetidsequence_cff import puJetMva

treeDumper = cms.EDAnalyzer("HWWTreeDumper",
                            HLTObjectsInfo = cms.untracked.PSet(triggerResults = cms.InputTag("TriggerResults","","AUTO"),
                                                                processName = cms.string("AUTO"),
                                                                triggerSummaryAOD = cms.InputTag("hltTriggerSummaryAOD","","HLT")
                                                                ),
                            electronCollection = cms.InputTag("gsfElectrons"),
                            calibElectronCollection = cms.InputTag("calibratedElectrons","calibratedGsfElectrons"),
                            #pflowElectronCollection = cms.InputTag("particleFlow","electrons"),
                            pflowElectronCollection = cms.InputTag("particleFlow"),
                            photonCollection = cms.InputTag("goodPhotons"),
                            muonCollection = cms.InputTag("muons"),
                            pfTauCollection = cms.InputTag("shrinkingConePFTauProducer"),
                            hpspfTauCollection = cms.InputTag("hpsPFTauProducer"),
                            hpsTancTausCollection = cms.InputTag("hpsTancTaus"),
                            PFCandidateCollection = cms.InputTag("particleFlow"),
                            PFNoPUCandidateCollection = cms.InputTag("pfNoPileUp"),
                            PFPUCandidateCollection = cms.InputTag("pfPileUp"),
                            ecalSCCollection = cms.InputTag("electronAndPhotonSuperClusters"),
                            ecalBarrelSCCollection = cms.InputTag("correctedHybridSuperClusters"),
                            ecalEndcapSCCollection = cms.InputTag("multi5x5SuperClusters","multi5x5EndcapSuperClusters"),
                            ecalElePFClusterCollection = cms.InputTag("pfElectronTranslator","pf"),
                            ecalPhoPFClusterCollection = cms.InputTag("pfPhotonTranslator","pfphot"),
                            ecalBCCollection = cms.InputTag("seedBasicClusters"),
                            ecalBarrelRecHits = cms.InputTag("reducedEcalRecHitsEB"),
                            ecalEndcapRecHits = cms.InputTag("reducedEcalRecHitsEE"),
                            esRecHits = cms.InputTag("reducedEcalRecHitsES"),
                            calotowersForIsolationProducer = cms.InputTag("towerMaker"),
                            generalTrackCollection = cms.InputTag("generalTracks"),
                            trackCollection = cms.InputTag("leptonLinkedTracks"),
                            gsfTrackCollection = cms.InputTag("electronGsfTracks"),
                            globalMuonTrackCollection = cms.InputTag("globalMuons"),
                            standAloneMuonTrackCollection = cms.InputTag("standAloneMuons"),
                            #  refittedForDeDxTrackCollection = cms.InputTag("RefitterForDeDx"),
                            refittedForDeDxTrackCollection = cms.InputTag("generalTracks"),
                            vertexCollection = cms.InputTag("offlinePrimaryVertices"),
                            K0sCollection = cms.InputTag("generalV0Candidates","Kshort"),
                            genJetCollection = cms.InputTag("goodGenJets"),
                            jetCollection1 = cms.InputTag("ak5CaloJets"),
                            jetCollection2 = cms.InputTag("ak5CaloJets","","RECO"), # the process name is needed because that collection only has the jet ID attached
                            JPTjetCollection1 = cms.InputTag("ak5JPTJetsL2L3Residual"),
                            JPTjetCollection2 = cms.InputTag("JetPlusTrackZSPCorJetAntiKt5"),
                            PFjetCollection1 = cms.InputTag("goodPFCHSJets"),
                            PFJetCorrectionService = cms.string("ak5PFL1FastL2L3Residual"),
                            JetCorrectionService = cms.string("ak5CaloL1FastL2L3Residual"),
                            PFpuCorrJetCollection1 = cms.InputTag("goodPFJets"),
                            # jet id MVA
                            puJetIDAlgos = puJetMva.algos,
                            metCollection = cms.InputTag("met"), # preselection
                            # corrmetCollection = cms.InputTag("metMuonJESCorAK5"), # type I and II corr applied
                            TCmetCollection = cms.InputTag("tcMet"),
                            genMetCollection = cms.InputTag("genMetCalo"),
                            PFmetCollection = cms.InputTag("pfmets"),
                            chargedMetCollection = cms.InputTag("chargedMetProducer"), # std, one per each vertex
                            PFChMetCollection = cms.InputTag("ourChPFMet"),
                            leptonLinkedPFCandidates = cms.InputTag("reducedPFCandsToSave"),
                            PFpreIdCollection = cms.InputTag("trackerDrivenElectronSeeds:preid"),
                            calotowerCollection = cms.InputTag("lowThrCaloTowers"),
                            conversionCollection = cms.InputTag("allConversions"),
                            hbheInput = cms.InputTag("hbhereco"),
                            hoInput = cms.InputTag("horeco"),
                            hfInput = cms.InputTag("hfreco"),
                            ecalInputs = cms.VInputTag(cms.InputTag("reducedEcalRecHitsEB"),
                                                       cms.InputTag("reducedEcalRecHitsEE")),
                            hcalNoiseSummary = cms.InputTag("hcalnoise"),
                            hepMcCollection = cms.InputTag("source"),
                            genInfoCollection = cms.InputTag("source"),
                            genWeightCollection = cms.untracked.string('CSA07WeightProducer'),
                            nameFile = cms.untracked.string('analysisTree.root'),
                            nameTree = cms.untracked.string('ntp1'),
                            # switch ON/OFF the candidate collections to dump
                            dumpRunInfo = cms.untracked.bool(True),
                            dumpElectrons = cms.untracked.bool(True),
                            dumpCalibratedElectrons = cms.untracked.bool(True),
                            dumpPFlowElectrons = cms.untracked.bool(False),
                            dumpPFpreId = cms.untracked.bool(False),
                            dumpPhotons = cms.untracked.bool(True),
                            dumpConversions = cms.untracked.bool(True),
                            dumpMuons = cms.untracked.bool(True),
                            dumpPFTaus = cms.untracked.bool(False),
                            dumphpsPFTaus = cms.untracked.bool(False),
                            dumphpsTancTaus = cms.untracked.bool(False),
                            dumpPFCandidates = cms.untracked.bool(True),
                            dumpTracks = cms.untracked.bool(False),
                            dumpLinkedTracks = cms.untracked.bool(True),
                            dumpGsfTracks = cms.untracked.bool(True),
                            dumpMuonTracks = cms.untracked.bool(True),
                            dumpVertices = cms.untracked.bool(False),
                            dumpK0s = cms.untracked.bool(False),
                            dumpCaloTowers = cms.untracked.bool(False),
                            dumpSCs = cms.untracked.bool(False),
                            usePhotonFix = cms.untracked.bool(False),
                            useEnergyRegression = cms.untracked.bool(False),
                            energyRegressionElectronFile = cms.untracked.string("http://cern.ch/meridian/regweights/gbrele.root"),
                            energyRegressionPhotonFile = cms.untracked.string("http://cern.ch/meridian/regweights/gbrph.root"),
                            posCalcParameters = cms.PSet( T0_barl      = cms.double(7.4),
                                                 T0_endc      = cms.double(6.3),
                                                 T0_endcPresh = cms.double(3.6),
                                                 LogWeighted  = cms.bool(True),
                                                 W0           = cms.double(4.2),
                                                 X0           = cms.double(0.89)
                                                 ),
                             PhotonFix_4_2e = cms.untracked.PSet(
    meanScale = cms.vdouble(1.03294629,-0.000210626517,0.000268568795,0.338053561,0.86164193,-0.0001184458,0.000232979403,0.310305987,0.961072344,8.81367775e-05,-0.000270690177,0.745461418,0.288888347,6.52038486e-06,0.000173654897,0.422671325),
    meanAT = cms.vdouble(0.0200811135,0,0,0,0.0103409006,0,0,0,0.532495533,0,0,0,0.0614964598,0,0,0),
    meanAC = cms.vdouble(-0.00326696352,0.010765809,513.763513,546.438243,-0.00325081301,0.0208748426,165.245698,292.03632,-0.000539999855,0.0100918811,953.905309,808.944612,-0.00123181641,0.0133568947,165.847556,332.705784),
    meanAS = cms.vdouble(0,0,0,0,0.0330004,-148569.764,87999432.1,7787218.96,-0.000597157153,0.0571921693,700.692431,924.653733,-0.00088161986,0.0304986746,382.755876,616.470187),
    meanAM = cms.vdouble(-0.00135522301,0.166490439,278.324187,245.998361,-0.000867413605,0.10580464,396.92529,263.112883,0.000230736156,1.77368196,4461.03178,3300.73792,0.000980695422,0.63575757,0.0336097848,0.043315868),
    meanBT = cms.vdouble(0,0,0,0,0,0.216283067,312.543466,463.601293,0.483274186,0,0,0,0.11623414,0,0,0),
    meanBC = cms.vdouble(-0.00332906015,0.00792585358,514.766605,488.870257,-0.00505883024,0.00182528255,507.478054,-6837.26736,-0.000651403853,0.0111101805,1276.07724,1489.51887,-0.00716072255,-0.440696266,1887.74154,118612),
    meanBS = cms.vdouble(-0.00199241828,0.0037942702,29.9438726,1077.1644,-166707004,0.0928055999,-5.30004162e-11,11442.2,-0.000251246189,0.0530409004,767.699586,835.195311,-0.000492035977,0.0292167014,433.232787,484.310448),
    meanBM = cms.vdouble(-0.00159080193,0.107998922,229.934523,231.786153,-5.93998135e-05,0.0096852184,59.8040186,-440000000,-0.187856578,-0.00821848896,0.891813494,-580000000,0.00299476541,0.0149328977,-48728700,37.0041547),
    meanR9 = cms.vdouble(0.857844414,-16.8494499,125.493331,0,0.0716647946,-0.204241803,0.154962477,0,0.96358076,28.7116938,697.709731,0,0.19617696,-0.350976375,0.181094838,0),
    sigmaScale = cms.vdouble(0.392737806,0.0353140568,-0.00613223131,0,0.469123815,-0.090283052,0.000469934719,0,0.46256953,-2.50963561e-08,0.0139636379,0,1.26164895,-6.61150347e-07,0.0280532297,0),
    sigmaAT = cms.vdouble(1.02977565,0,0,0,1.77629522,0,0,0,6.47165025,0,0,0,-0.232612761,0,0,0),
    sigmaAC = cms.vdouble(-0.00350109526,-0.951103069,-54434.4267,-3e+17,-0.00636220086,-0.781271127,4.90734224,65.6835127,48.1275,150005000,21231.6,2.6e+11,0.00137406444,-0.377659364,27171.5802,-560000000),
    sigmaAS = cms.vdouble(0,0,0,0,0,0,0,0,0.000209127817,2.19868731,1695.98579,967.250228,0.00022943714,0.335082568,590.511812,387.352521),
    sigmaAM = cms.vdouble(0.00127749544,5.03867192,563.047721,272.293234,0.000179292631,7.62815501,743.55507,354.656661,0.0217972665,1.26317651,34.0924905,55.1895282,-0.000780390674,1.05127796,33.7378914,61.3730807),
    sigmaBT = cms.vdouble(0.00480679465,7.56230742,-33600000,-257.677353,-0.0507778073,3.00903133,-0.526032834,-0.630748789,5.21983754,0,0,0,0.529507693,0,0,0),
    sigmaBC = cms.vdouble(-0.00169935002,2790083.26,-97275416.4,23710676.7,0.00490009575,-1.53772346,553415.545,2.36808e+19,-0.004,-120000,7.49509e+12,36643600,-0.00203996,93000,61225800,-4.43323e+17),
    sigmaBS = cms.vdouble(0,0,0,0,0,0,0,0,0.000250338051,1.98819262,1967.55308,1098.23855,0.00125939613,0.31048111,295.258764,263.974257),
    sigmaBM = cms.vdouble(-0.00194553738,7.77713222,264.960159,363.487107,-0.00113947453,3.74348887,91.9478901,101.304882,0.00101799874,88.0546723,8.47552e+10,-132255.757,-0.046100748,1.22348596,1.9e+09,1254.99),
    sigmaR9 = cms.vdouble(0.952571,0,0,0,-0.261512815,-1.69974425,0,0,144.031062,-6.11507616e-07,1.18181734e-08,0,9.09347838,-10.0390435,0,0)
    ),
                            PhotonFix_4_2p = cms.untracked.PSet(
    meanScale = cms.vdouble(0.995941423,-1.41986304e-05,3.66129541e-05,-0.0774047233,0.982680412,3.13860176e-05,-2.89107109e-05,-0.458678502,0.990082016,-3.75802712e-06,2.56693516e-05,-0.0492813428,0.331585644,-4.97323079e-05,0.000208912195,-1.36032052),
    meanAT = cms.vdouble(0.000720281545,0,0,0,-0.00204222443,0,0,0,0.072352478,0,0,0,-0.0640673292,0,0,0),
    meanAC = cms.vdouble(-0.00344862444,0.0101395802,466.112225,507.628173,-0.00329797061,0.0212879256,135.879912,238.247576,-0.0002936899,0.0160546814,1183.48593,761.29774,-0.00129027954,0.00733510902,182.714706,621.652554),
    meanAS = cms.vdouble(0,0,0,0,0,0,0,0,-0.000462243216,0.0795658256,887.080242,1067.72442,-0.000490574173,0.0308208884,385.372647,492.313289),
    meanAM = cms.vdouble(-0.000871553792,0.141419889,281.104504,195.875679,-0.000512006976,0.124281288,480.326634,286.165783,0.000354495505,0.516700576,4376.14811,2093.33478,-0.0064828927,0.649443452,0.0573092773,0.0743069),
    meanBT = cms.vdouble(0,0.026344491,-104.20518,-176099,0,0.204384889,303.764745,408.14741,0.077752944,0,0,0,-0.147343956,0,0,0),
    meanBC = cms.vdouble(-0.00272095949,0.012411788,587.318903,381.415059,-0.0035698745,0.00402323151,980.296598,869.711616,-0.000411367107,0.0161135906,1414.07982,951.556042,-0.00503351921,-57691.5085,46202.9758,118612),
    meanBS = cms.vdouble(-0.00201265145,0.00372948657,41.2773112,748.890936,0,0,0,0,8.51070829e-05,0.0699037982,1565.72963,841.509573,-0.000793147706,0.0238305184,402.215233,455.848092),
    meanBM = cms.vdouble(-0.00168471013,0.0685484442,217.983503,207.660928,-0.00321305828,0.0454848819,147.827487,227.625382,-0.00252281385,0.00600665031,268.761304,46.5945865,0.000434549102,0.0443539812,-39970930.5,-635.815445),
    meanR9 = cms.vdouble(0.946581139,20.6034189,187.28856,0,0.0253777359,-0.0420810898,0.0181966013,0,0.964231565,30.1631606,414.510458,0,-0.411370898,1.30133082,-0.890618718,0),
    sigmaScale = cms.vdouble(0.206349443,0.0206592338,0.00653752299,0,1.53707929,0.0946423194,-0.00765920151,0,0.218991853,6.93889e-18,0.00939222285,0,1.49352299,1.38778e-17,0.0248352105,0),
    sigmaAT = cms.vdouble(0.178629422,0,0,0,0.808880052,0,0,0,1.61339852,0,0,0,-1.18239629,0,0,0),
    sigmaAC = cms.vdouble(-0.00335501889,0.0997921532,93.6397821,1519.43272,-0.00195542375,-2.09949949,4.30292193,5.09475964,0.00019476922,0.697650974,-0.000125668382,12.8659982,0.00155030534,-0.673931391,134075.829,-7e+09),
    sigmaAS = cms.vdouble(0,0,0,0,0,0,0,0,-1.68218147e-05,6.57794255,1555.93015,1401.542,6.95848091e-05,0.522471203,463.305497,1159.49992),
    sigmaAM = cms.vdouble(0.000927325527,10.2678389,619.975988,285.190815,-0.00105652021,5.83420851,506.986527,468.330744,0.0570038229,0.633551691,9.59639e+11,16.4637695,-0.00509006951,0.945276887,46.4072512,7.11474e+12),
    sigmaBT = cms.vdouble(0,0.895041707,94.6834192,62.3012502,0,2.83411417,-0.211242292,-0.198231087,-0.0591443023,0,0,0,-1.59480683,0,0,0),
    sigmaBC = cms.vdouble(-0.00169896783,0.323973706,1234.03309,907.352988,0.00580038243,0.165505659,4133.45418,375000000,-0.00320070019,25.5502578,7.49509e+12,3798165.72,-0.00202302997,15.4301057,-33315545.5,-6e+09),
    sigmaBS = cms.vdouble(0,0,0,0,0,0,0,0,9.63685051e-05,6.91673581,2447.68053,1721.11327,0.00271126099,0.325669289,2322.66097,298.692034),
    sigmaBM = cms.vdouble(-0.00249508825,57.8982306,665.068952,1075.1094,-0.00269993666,3.42390459,171.300481,284.718025,0.00148006,28,5400000,-9000000,-0.0454765849,6.81541098,1.9e+09,-26353.4449),
    sigmaR9 = cms.vdouble(0.952890416,1958.37946,21612.0219,0,-3.75255938,4.3849733,-1.81745726,0,187.987786,-1.91777372e-07,8.29820105e-09,0,41.1074567,-86.9595346,45.7818889,0)
    ),
                            dumpBCs = cms.untracked.bool(False),
                            dumpJets = cms.untracked.bool(True),
                            dumpPUcorrPFJet = cms.untracked.bool(True),
                            dumpMet = cms.untracked.bool(True),
                            dumpLogErrorFlags = cms.untracked.bool(True),
                            dumpHcalNoiseFlags = cms.untracked.bool(False),
                            AODHcalNoiseFlags = cms.untracked.bool(True),
                            # switch ON/OFF the particle flow objects to dump
                            dumpParticleFlowObjects = cms.untracked.bool(False),
                            # switch ON/OFF the additional informations to dump
                            saveEcal = cms.untracked.bool(True),
                            saveFatEcal = cms.untracked.bool(True),
                            saveTrk = cms.untracked.bool(True),
                            saveFatTrk = cms.untracked.bool(True),
                            saveTrackDeDx = cms.untracked.bool(False),
                            saveTrackImpactParameters = cms.untracked.bool(True),
                            saveEleID = cms.untracked.bool(True),
                            savePFEleGsfTrk = cms.untracked.bool(True),
                            savePFEleBasic = cms.untracked.bool(True),
                            saveJetBTag = cms.untracked.bool(True),
                            savePFTauBasic = cms.untracked.bool(True),
                            saveLeadPFCand = cms.untracked.bool(True),
                            savePFTauDiscriminators = cms.untracked.bool(True),
                            # MC truth
                            mcTruthCollection = cms.InputTag("genParticles"),
                            dumpGenMet = cms.untracked.bool(True),
                            dumpGenJets = cms.untracked.bool(True),
                            dumpMCTruth = cms.untracked.bool(True),
                            dumpMCTruthExtra = cms.untracked.bool(False), 
                            dumpGenInfo = cms.untracked.bool(True),
                            dumpLHE = cms.untracked.bool(False),
                            dumpPreselInfo = cms.untracked.bool(False),
                            dumpSignalKfactor = cms.untracked.bool(True),
                            # trigger results
                            dumpTriggerResults = cms.untracked.bool(False),
                            dumpHLTObjects = cms.untracked.bool(False),
                            # PDFs
                            dumpPdfWeight = cms.untracked.bool(False),
                            #tau discriminators
                            tauDiscrByLeadingTrackFindingTag = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackFinding"),
                            tauDiscrByLeadingTrackPtCutTag = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingTrackPtCut"),
                            tauDiscrByLeadingPionPtCutTag = cms.InputTag("shrinkingConePFTauDiscriminationByLeadingPionPtCut"),
                            tauDiscrByIsolationTag = cms.InputTag("shrinkingConePFTauDiscriminationByIsolation"),
                            tauDiscrByIsolationUsingLeadingPionTag = cms.InputTag("shrinkingConePFTauDiscriminationByIsolationUsingLeadingPion"),
                            tauDiscrByTrackIsolationTag = cms.InputTag("shrinkingConePFTauDiscriminationByTrackIsolation"),
                            tauDiscrByTrackIsolationUsingLeadingPionTag = cms.InputTag("shrinkingConePFTauDiscriminationByTrackIsolationUsingLeadingPion"),
                            tauDiscrByECALIsolationTag = cms.InputTag("shrinkingConePFTauDiscriminationByECALIsolation"),
                            tauDiscrByECALIsolationUsingLeadingPionTag = cms.InputTag("shrinkingConePFTauDiscriminationByECALIsolationUsingLeadingPion"),
                            tauDiscrAgainstMuonTag = cms.InputTag("shrinkingConePFTauDiscriminationAgainstMuon"),
                            tauDiscrAgainstElectronTag = cms.InputTag("shrinkingConePFTauDiscriminationAgainstElectron"),
                            tauDiscrByTaNCTag = cms.InputTag("shrinkingConePFTauDiscriminationByTaNC"),
                            tauDiscrByTaNCfrHalfPercentTag = cms.InputTag("shrinkingConePFTauDiscriminationByTaNCfrHalfPercent"),
                            tauDiscrByTaNCfrOnePercentTag = cms.InputTag("shrinkingConePFTauDiscriminationByTaNCfrOnePercent"),
                            tauDiscrByTaNCfrQuarterPercentTag = cms.InputTag("shrinkingConePFTauDiscriminationByTaNCfrQuarterPercent"),
                            tauDiscrByTaNCfrTenthPercentTag = cms.InputTag("shrinkingConePFTauDiscriminationByTaNCfrTenthPercent"),
                            #hps tau discriminators
                            hpsTauDiscrByLooseElectronRejectionTag = cms.InputTag("hpsPFTauDiscriminationByLooseElectronRejection"),
                            hpsTauDiscrByMediumElectronRejectionTag = cms.InputTag("hpsPFTauDiscriminationByMediumElectronRejection"),
                            hpsTauDiscrByTightElectronRejectionTag = cms.InputTag("hpsPFTauDiscriminationByTightElectronRejection"),
                            hpsTauDiscrByLooseMuonRejectionTag = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection"),
                            hpsTauDiscrByTightMuonRejectionTag = cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection"),
                            hpsTauDiscrByDecayModeFindingTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"),
                            hpsTauDiscrByVLooseIsolationTag = cms.InputTag("hpsPFTauDiscriminationByVLooseIsolation"),
                            hpsTauDiscrByLooseIsolationTag = cms.InputTag("hpsPFTauDiscriminationByLooseIsolation"),
                            hpsTauDiscrByMediumIsolationTag = cms.InputTag("hpsPFTauDiscriminationByMediumIsolation"),
                            hpsTauDiscrByTightIsolationTag = cms.InputTag("hpsPFTauDiscriminationByTightIsolation"),
                            hpsTauDiscrByVLooseCombinedIsolationDBSumPtCorrTag = cms.InputTag("hpsPFTauDiscriminationByVLooseCombinedIsolationDBSumPtCorr"),
                            hpsTauDiscrByLooseCombinedIsolationDBSumPtCorrTag = cms.InputTag("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr"),
                            hpsTauDiscrByMediumCombinedIsolationDBSumPtCorrTag = cms.InputTag("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr"),
                            hpsTauDiscrByTightCombinedIsolationDBSumPtCorrTag = cms.InputTag("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr"),    
                            hpsTauDiscrAgainstMuonLoose2Tag = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection2"),
                            hpsTauDiscrAgainstMuonMedium2Tag = cms.InputTag("hpsPFTauDiscriminationByMediumMuonRejection2"),
                            hpsTauDiscrAgainstMuonTight2Tag = cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection2"),
                            hpsTauDiscrByLooseCombinedIsolationDeltaBetaCorr3HitsTag = cms.InputTag("hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits"),
                            hpsTauDiscrByMediumCombinedIsolationDeltaBetaCorr3HitsTag = cms.InputTag("hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits"),
                            hpsTauDiscrByTightCombinedIsolationDeltaBetaCorr3HitsTag = cms.InputTag("hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits"),
                            hpsTauDiscrAgainstElectronLooseMVA3Tag = cms.InputTag("hpsPFTauDiscriminationByMVA3LooseElectronRejection"),
                            hpsTauDiscrAgainstElectronMediumMVA3Tag = cms.InputTag("hpsPFTauDiscriminationByMVA3MediumElectronRejection"),
                            hpsTauDiscrAgainstElectronTightMVA3Tag = cms.InputTag("hpsPFTauDiscriminationByMVA3TightElectronRejection"),
                            hpsTauDiscrAgainstElectronVTightMVA3Tag = cms.InputTag("hpsPFTauDiscriminationByMVA3VTightElectronRejection"),
                            #hpsTanc tau discriminators
                            hpsTancTausDiscrByLeadingTrackFindingTag = cms.InputTag("hpsTancTausDiscriminationByLeadingTrackFinding"),
                            hpsTancTausDiscrByLeadingTrackPtCutTag = cms.InputTag("hpsTancTausDiscriminationByLeadingTrackPtCut"),
                            hpsTancTausDiscrByLeadingPionPtCutTag = cms.InputTag("hpsTancTausDiscriminationByLeadingPionPtCut"),
                            hpsTancTausDiscrByTancTag = cms.InputTag("hpsTancTausDiscriminationByTanc"),
                            hpsTancTausDiscrByTancRawTag = cms.InputTag("hpsTancTausDiscriminationByTancRaw"),
                            hpsTancTausDiscrByTancVLooseTag = cms.InputTag("hpsTancTausDiscriminationByTancVLoose"),
                            hpsTancTausDiscrByTancLooseTag = cms.InputTag("hpsTancTausDiscriminationByTancLoose"),
                            hpsTancTausDiscrByTancMediumTag = cms.InputTag("hpsTancTausDiscriminationByTancMedium"),
                            hpsTancTausDiscrByTancTightTag = cms.InputTag("hpsTancTausDiscriminationByTancTight"),
                            hpsTancTausDiscrByLooseElectronRejectionTag = cms.InputTag("hpsTancTausDiscriminationByLooseElectronRejection"),
                            hpsTancTausDiscrByMediumElectronRejectionTag = cms.InputTag("hpsTancTausDiscriminationByMediumElectronRejection"),
                            hpsTancTausDiscrByTightElectronRejectionTag = cms.InputTag("hpsTancTausDiscriminationByTightElectronRejection"),
                            hpsTancTausDiscrByLooseMuonRejectionTag = cms.InputTag("hpsTancTausDiscriminationByLooseMuonRejection"),
                            hpsTancTausDiscrByTightMuonRejectionTag = cms.InputTag("hpsTancTausDiscriminationByTightMuonRejection"),
                            hpsTancTausDiscrByDecayModeSelectionTag = cms.InputTag("hpsTancTausDiscriminationByDecayModeSelection"),
                            hpsTancTausDiscrByVLooseIsolationTag = cms.InputTag("hpsTancTausDiscriminationByVLooseIsolation"),
                            hpsTancTausDiscrByLooseIsolationTag = cms.InputTag("hpsTancTausDiscriminationByLooseIsolation"),
                            hpsTancTausDiscrByMediumIsolationTag = cms.InputTag("hpsTancTausDiscriminationByMediumIsolation"),
                            hpsTancTausDiscrByTightIsolationTag = cms.InputTag("hpsTancTausDiscriminationByTightIsolation"),
                            # pdf
                            pdfSet1 = cms.InputTag("pdfWeights:cteq66"),
                            pdfSet2 = cms.InputTag("pdfWeights:MRST2006nnlo"),
                            pdfSet3 = cms.InputTag("pdfWeights:NNPDF10"), # no _ are allowed in the names: NN10_100 => NN10
                            namepdf1 = cms.untracked.string("CTEQ66"),
                            namepdf2 = cms.untracked.string("MRST2006NNLO"),
                            namepdf3 = cms.untracked.string("NNPDF10100"),

                            dumpTree = cms.untracked.bool(False),
                            PFJetsBTags = cms.untracked.PSet( combinedSecondaryVertexBJetTags = cms.InputTag("newCombinedSecondaryVertexBPFNoPUJetTags"),
                                                              combinedSecondaryVertexMVABJetTags = cms.InputTag("newCombinedSecondaryVertexMVABPFNoPUJetTags"),
                                                              jetBProbabilityBJetTags = cms.InputTag("newJetBProbabilityBPFNoPUJetTags"),
                                                              jetProbabilityBJetTags = cms.InputTag("newJetProbabilityBPFNoPUJetTags"),
                                                              simpleSecondaryVertexHighEffBJetTags = cms.InputTag("newSimpleSecondaryVertexHighEffBPFNoPUJetTags"),
                                                              simpleSecondaryVertexHighPurBJetTags = cms.InputTag("newSimpleSecondaryVertexHighPurBPFNoPUJetTags"),
                                                              trackCountingHighPurBJetTags = cms.InputTag("newTrackCountingHighPurBPFNoPUJetTags"),
                                                              trackCountingHighEffBJetTags = cms.InputTag("newTrackCountingHighEffBPFNoPUJetTags"),
                                                              trackCountingVeryHighEffBJetTags = cms.InputTag("newTrackCountingVeryHighEffBPFNoPUJetTags")),
                            PFPUcorrJetsBTags = cms.untracked.PSet( combinedSecondaryVertexBJetTags = cms.InputTag("newCombinedSecondaryVertexBPFPUcorrJetTags"),
                                                                    combinedSecondaryVertexMVABJetTags = cms.InputTag("newCombinedSecondaryVertexMVABPFPUcorrJetTags"),
                                                                    jetBProbabilityBJetTags = cms.InputTag("newJetBProbabilityBPFPUcorrJetTags"),
                                                                    jetProbabilityBJetTags = cms.InputTag("newJetProbabilityBPFPUcorrJetTags"),
                                                                    simpleSecondaryVertexHighEffBJetTags = cms.InputTag("newSimpleSecondaryVertexHighEffBPFPUcorrJetTags"),
                                                                    simpleSecondaryVertexHighPurBJetTags = cms.InputTag("newSimpleSecondaryVertexHighPurBPFPUcorrJetTags"),
                                                                    trackCountingHighPurBJetTags = cms.InputTag("newTrackCountingHighPurBPFPUcorrJetTags"),
                                                                    trackCountingHighEffBJetTags = cms.InputTag("newTrackCountingHighEffBPFPUcorrJetTags"),
                                                                    trackCountingVeryHighEffBJetTags = cms.InputTag("newTrackCountingVeryHighEffBPFPUcorrJetTags"))
                            )
