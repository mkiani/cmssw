import FWCore.ParameterSet.Config as cms

nverticesModule = cms.EDProducer("VertexMultiplicityCounter",
    probes = cms.InputTag("REPLACE_ME"),
    objects = cms.InputTag("goodPrimaryVertices"),
    objectSelection = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
)

# "( (abs(pdgId(0))==11) * ( 0.998 * (pt(0) < 20 && abs(eta(0)) < 1.479) + "   + 
# "                          0.948 * (pt(0) > 20 && abs(eta(0)) < 1.479) + "   + 
# "                          0.948 * (pt(0) < 20 && abs(eta(0)) > 1.479) + "   + 
# "                          0.948 * (pt(0) > 20 && abs(eta(0)) > 1.479) ) + " + 
# "  (abs(pdgId(0))==13) * ( 0.998 * (pt(1) < 20 && abs(eta(1)) < 1.479) + "   + 
# "                          0.948 * (pt(1) > 20 && abs(eta(1)) < 1.479) + "   + 
# "                          0.948 * (pt(1) < 20 && abs(eta(1)) > 1.479) + "   + 
# "                          0.948 * (pt(1) > 20 && abs(eta(1)) > 1.479) ) ) * " + 
# "( (abs(pdgId(1))==11) * ( 0.998 * (pt(0) < 20 && abs(eta(0)) < 1.479) + "   + 
# "                          0.948 * (pt(0) > 20 && abs(eta(0)) < 1.479) + "   + 
# "                          0.948 * (pt(0) < 20 && abs(eta(0)) > 1.479) + "   + 
# "                          0.948 * (pt(0) > 20 && abs(eta(0)) > 1.479) ) + " + 
# "  (abs(pdgId(1))==13) * ( 0.998 * (pt(1) < 20 && abs(eta(1)) < 1.479) + "   + 
# "                          0.948 * (pt(1) > 20 && abs(eta(1)) < 1.479) + "   + 
# "                          0.948 * (pt(1) < 20 && abs(eta(1)) > 1.479) + "   + 
# "                          0.948 * (pt(1) > 20 && abs(eta(1)) > 1.479) ) )" + 

step3Tree = cms.EDFilter("ProbeTreeProducer",
    cut = cms.string("q(0)*q(1) < 0 && !isSTA(0) && !isSTA(1) && "+
                     "leptEtaCut(2.4,2.5) && ptMax > 20 && ptMin > 10"
#                      " && triggerMatchingCut('DATASET')"
#                      "nExtraLep(10) == 0 "
#                     +" && passesIP"
#                    +(" && triggerMatchingCut('DATASET')")
    ),
    variables = cms.PSet(
        hypo = cms.string("hypo()"),
        channel = cms.string("channel()"),
        mll  = cms.string("mll()"),
        ptll = cms.string("pTll()"),
        yll  = cms.string("yll()"),  #fixed! returns (p4a+p4b).Rapidity()
        pt1  = cms.string("ptMax"),
        pt2  = cms.string("ptMin"),
        peaking  = cms.string("peaking"),
        trigger  = cms.string("guillelmoTrigger('DATASET')"),
        nextra  = cms.string("nExtraLep(10)"),
        tcmet  = cms.string("tcMet"),
        tcmetphi  = cms.string("tcMetPhi"),
        ptcmet = cms.string("projTcMet"),
        pfmet  = cms.string("pfMet"),
        pfmetphi  = cms.string("pfMetPhi"),
        ppfmet = cms.string("projPfMet"),
        chmet = cms.string("chargedMetSmurf"), 
        chmetphi = cms.string("chargedMetSmurfPhi"), 
        pchmet = cms.string("projChargedMetSmurf"), 
        redmet = cms.string("-9999"), 
        predmet = cms.string("-9999"), 
        mpmet = cms.string("min(projPfMet,projChargedMetSmurf)"), ##note: min of proj and proj of min are not the same
        dphill = cms.string("dPhill()"),
        drll   = cms.string("dRll()"),
        dphilljet  = cms.string("dPhillLeadingJet(5.0)"),
        dphillmet  = cms.string("dPhillMet('PFMET')"),
        dphilmet = cms.string("dPhilMet('PFMET')"),
        dphilmet1 = cms.string("dPhilMet(0,'PFMET')"),
        dphilmet2 = cms.string("dPhilMet(1,'PFMET')"),
        mtw1 = cms.string("mTByPt(0,'PFMET')"),
        mtw2 = cms.string("mTByPt(1,'PFMET')"),
        mth  = cms.string("mTHiggs('PFMET')"),
        gammaMRStar = cms.string("gammaMRStar"),
        njet  = cms.string("nCentralJets(30,5.0)"),
        njetid  = cms.string("nCentralJets(30,5.0,1,0)"),
        nbjet = cms.string("bTaggedJetsOver(30,2.1)"),
        jetpt1 = cms.string("leadingJetPt(0,0,5.0)"),
        jetpt2 = cms.string("leadingJetPt(1,0,5.0)"),
        jeteta1 = cms.string("leadingJetEta(0,0,5.0)"),
        jeteta2 = cms.string("leadingJetEta(1,0,5.0)"),
        jetphi1 = cms.string("leadingJetPhi(0,0,5.0)"),
        jetphi2 = cms.string("leadingJetPhi(1,0,5.0)"),
        jettche1 = cms.string("leadingJetBtag(0,'trackCountingHighEffBJetTags',0,5.0)"),
        jettche2 = cms.string("leadingJetBtag(1,'trackCountingHighEffBJetTags',0,5.0)"),
        jettchp1 = cms.string("leadingJetBtag(0,'trackCountingHighPurBJetTags',0,5.0)"),
        jettchp2 = cms.string("leadingJetBtag(1,'trackCountingHighPurBJetTags',0,5.0)"),
        iso1 = cms.string("allIsoByPt(0)/ptByPt(0)"),
        iso2 = cms.string("allIsoByPt(1)/ptByPt(1)"),
        eta1 = cms.string("etaByPt(0)"),
        eta2 = cms.string("etaByPt(1)"),
        phi1 = cms.string("phiByPt(0)"),
        phi2 = cms.string("phiByPt(1)"),
        ch1 = cms.string("qByPt(0)"),
        ch2 = cms.string("qByPt(1)"),
        softbdisc = cms.string("highestSoftBDisc(30.0)"),
        hardbdisc = cms.string("highestHardBDisc(30.0)"),
        tightmu = cms.string("passesSmurfMuonID"),
        worstJetLepPt = cms.string("max(matchedJetPt(0, 0.5)/pt(0), matchedJetPt(1, 0.5)/pt(1))"),
        dataset = cms.string("REPLACE_ME"),
        puW   = cms.InputTag("puWeight"),
        kfW   = cms.InputTag("ptWeight"),
        baseW = cms.string("REPLACE_ME"),
        fourW = cms.string("REPLACE_ME"),
        effW = cms.string("1"),
        triggW = cms.string("1"),
        #vbf stuff:
        njetvbf = cms.string("nJetVBF(30,5.)"),
        mjj = cms.string("mjj(30,5.)"),
        detajj = cms.string("dEtajj(30,5.)"),
        #zep
    ),
    flags = cms.PSet(
        sameflav   = cms.string("hypo == 3 || hypo == 6"),
        zveto      = cms.string("abs(mll-91.1876)>15 || hypo == 4 || hypo == 5"),
        bveto      = cms.string("bTaggedJetsUnder(30,2.1) == 0 && nSoftMu(3) == 0"),
        bveto_ip   = cms.string("bTaggedJetsUnder(30,2.1) == 0"),
        bveto_mu   = cms.string("nSoftMu(3) == 0"),
        bveto_nj   = cms.string("bTaggedJetsUnder(30,2.1) == 0 && nSoftMu(3,1) == 0"),
        bveto_munj = cms.string("nSoftMu(3,1) == 0"),
        dphiveto   = cms.string("passesDPhillJet"),
        passTight1 = cms.string('passTightByPt(0)'),
        passTight2 = cms.string('passTightByPt(1)'),
        #passLoose1 = cms.string('passLooseByPt(0)'),
        #passLoose2 = cms.string('passLooseByPt(1)'),        
    ),
    addRunLumiInfo = cms.bool(True)
)

# from WWAnalysis.AnalysisStep.pileupReweighting_cfi import reWeightVector
from WWAnalysis.AnalysisStep.pileupReweighting_cfi import puS4,dataWeights
puWeight     = cms.EDProducer("CombinedWeightProducer",
    baseWeight = cms.double(1.0),
#     puWeight   = cms.vdouble(*reWeightVector[:]),
#     puLabel    = cms.InputTag("addPileupInfo"),
    s4Dist = cms.vdouble(puS4[:]),
    dataDist = cms.vdouble(dataWeights[:]),
    src        = cms.InputTag("REPLACE_ME"),
)
higgsPt = cms.EDProducer("HWWKFactorProducer",
    genParticlesTag = cms.InputTag("prunedGen"),
    inputFilename = cms.untracked.string("REPLACE_ME"),
    ProcessID = cms.untracked.int32(10010),
    Debug =cms.untracked.bool(False)
)
ptWeight     = cms.EDProducer("CombinedWeightProducer",
    baseWeight = cms.double(1.0),
    ptWeight   = cms.InputTag("higgsPt"),
    src        = cms.InputTag("REPLACE_ME"),
)



def addBTaggingVariables(pt):
    if hasattr(pt,"variables"):
        pt.variables.softtche = cms.string("highestSoftBDisc(30.0,'trackCountingHighEffBJetTags')")
        pt.variables.hardtche = cms.string("highestHardBDisc(30.0,'trackCountingHighEffBJetTags')")
        pt.variables.softtchp = cms.string("highestSoftBDisc(30.0,'trackCountingHighPurBJetTags')")
        pt.variables.hardtchp = cms.string("highestHardBDisc(30.0,'trackCountingHighPurBJetTags')")
        pt.variables.softcsv  = cms.string("highestSoftBDisc(30.0,'combinedSecondaryVertexBJetTags')")
        pt.variables.hardcsv  = cms.string("highestHardBDisc(30.0,'combinedSecondaryVertexBJetTags')")
        pt.variables.softcsvm = cms.string("highestSoftBDisc(30.0,'combinedSecondaryVertexMVABJetTags')")
        pt.variables.hardcsvm = cms.string("highestHardBDisc(30.0,'combinedSecondaryVertexMVABJetTags')")
        pt.variables.softjbpb = cms.string("highestSoftBDisc(30.0,'jetBProbabilityBJetTags')")
        pt.variables.hardjbpb = cms.string("highestHardBDisc(30.0,'jetBProbabilityBJetTags')")
        pt.variables.softjpb  = cms.string("highestSoftBDisc(30.0,'jetProbabilityBJetTags')")
        pt.variables.hardjpb  = cms.string("highestHardBDisc(30.0,'jetProbabilityBJetTags')")

        pt.variables.jetcsv1 = cms.string("leadingJetBtag(0,'combinedSecondaryVertexBJetTags',0,5.0)")
        pt.variables.jetcsv2 = cms.string("leadingJetBtag(1,'combinedSecondaryVertexBJetTags',0,5.0)")
        pt.variables.jetcsvm1 = cms.string("leadingJetBtag(0,'combinedSecondaryVertexMVABJetTags',0,5.0)")
        pt.variables.jetcsvm2 = cms.string("leadingJetBtag(1,'combinedSecondaryVertexMVABJetTags',0,5.0)")
        pt.variables.jetjbpb1 = cms.string("leadingJetBtag(0,'jetBProbabilityBJetTags',0,5.0)")
        pt.variables.jetjbpb2 = cms.string("leadingJetBtag(1,'jetBProbabilityBJetTags',0,5.0)")
        pt.variables.jetjpb1 = cms.string("leadingJetBtag(0,'jetProbabilityBJetTags',0,5.0)")
        pt.variables.jetjpb2 = cms.string("leadingJetBtag(1,'jetProbabilityBJetTags',0,5.0)")
    else:
        raise RuntimeError, "In addBTaggingVariables, %s doesn't look like a ProbeTreeProducer object, it has no 'variables' attribute." % pt

def addIsoStudyVariables(process,pt):
    if hasattr(pt,"variables"):
      for i,l in enumerate(["lep1", "lep2"]):
        setattr(pt.variables, l+"isoMergePf"     , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).userFloat('muSmurfPF') : candByPt({0}).userFloat('eleSmurfPF')".format(i)))
        setattr(pt.variables, l+"isoRecoTracks"  , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().sumPt : candByPt({0}).dr03TkSumPt".format(i)))
        setattr(pt.variables, l+"isoRecoEcal"    , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().emEt  : ".format(i) +
                                                              "  ( max(0,candByPt({0}).dr03EcalRecHitSumEt - 1)*candByPt({0}).isEB + (1-candByPt({0}).isEB)*candByPt({0}).dr03EcalRecHitSumEt )".format(i)))
        setattr(pt.variables, l+"isoRecoHCal"    , cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().hadEt  : candByPt({0}).dr03HcalTowerSumEt ".format(i)))
        setattr(pt.variables, l+"isoRecoHCalFull", cms.string("? abs(candByPt({0}).pdgId) == 13 ? candByPt({0}).isolationR03().hadEt  : candByPt({0}).userFloat('hcalFull')".format(i)))
        setattr(pt.variables, l+"isoPfCharged"   , cms.string("candByPt({0}).userFloat('pfCharged')".format(i)))
        setattr(pt.variables, l+"isoPfNeutral"   , cms.string("candByPt({0}).userFloat('pfNeutral')".format(i)))
        setattr(pt.variables, l+"isoPfPhoton"    , cms.string("candByPt({0}).userFloat('pfPhoton')".format(i)))
        setattr(pt.variables, l+"isoSmurfCharged", cms.string("candByPt({0}).userFloat('smurfCharged')".format(i)))
        setattr(pt.variables, l+"isoSmurfNeutral", cms.string("candByPt({0}).userFloat('smurfNeutral')".format(i)))
        setattr(pt.variables, l+"isoSmurfPhoton" , cms.string("candByPt({0}).userFloat('smurfPhoton')".format(i)))
        setattr(pt.variables, l+"isoSmurfNoOverCharged", cms.string("candByPt({0}).userFloat('smurfNoOverCharged')".format(i)))
        setattr(pt.variables, l+"isoSmurfNoOverNeutral", cms.string("candByPt({0}).userFloat('smurfNoOverNeural')".format(i)))
        setattr(pt.variables, l+"isoSmurfNoOverPhoton" , cms.string("candByPt({0}).userFloat('smurfNoOverPhoton')".format(i)))
        for algo in ("JetCone", "FixCone03", "FixCone04", "MaxCone03", "MaxCone04", "SumCone02", "SumCone04"):
            for name in ("Charged", "ChargedNoOvRem"): #, "NeutralHadAll", "NeutralHadPt05", "NeutralHadPt1", "Photons", "PhotonsMuStrip"):
                setattr(pt.variables, "%sjetiso%s%s"%(l,algo,name), cms.string("candByPt(%d).userFloat('jetIso%s%s')"%(i,algo,name)))
    else:
        raise RuntimeError, "In addIsoStudyVariables, %s doesn't look like a ProbeTreeProducer object, it has no 'variables' attribute." % pt
    if not hasattr(process,"isoStudySequence"):
        process.load("WWAnalysis.AnalysisStep.isoStudySequence_cff")

