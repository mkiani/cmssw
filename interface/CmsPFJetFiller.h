// -*- C++ -*-
//-----------------------------------------------------------------------
//
// Package:    
//      HiggsAnalysis/HiggsToWW2e
// Description:
//      Class CmsPFJetFiller
//      Simple class for dumping RECO (or AOD) contents to a ROOT tree
//      
// Original Author:  Emanuele Di Marco
//         Created:  Mon Sep  29 18:05:34 CEST 2008
//
//-----------------------------------------------------------------------

#ifndef CmsPFJetFiller_h
#define CmsPFJetFiller_h

#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "HiggsAnalysis/HiggsToWW2e/interface/CmsTree.h"
#include "HiggsAnalysis/HiggsToWW2e/interface/CmsCandidateFiller.h"

#include <vector>
#include <TTree.h>

struct CmsPFJetFillerData : public CmsCandidateFillerData {

  std::vector<float> *chargedHadronEnergy, *neutralHadronEnergy, *chargedEmEnergy, *neutralEmEnergy;
  std::vector<float> *neutralMultiplicity, *chargedMultiplicity, *muonMultiplicity;
  std::vector<float> *uncorrEnergy;

public:
  void initialise();
  void clearTrkVectors();

};

class CmsPFJetFiller : public CmsCandidateFiller {

 public:

  // Constructors

  // Dump everything
  CmsPFJetFiller(CmsTree *, 
	       int maxTracks=500, int maxMCTracks=2000, 
	       bool noOutputIfLimitsReached=false );

  // Destructor
  virtual ~CmsPFJetFiller();

  // Operators

  // run number and all of that --- to implement

  void writeCollectionToTree(edm::InputTag collectionTag,
			     const edm::Event&, const edm::EventSetup&,
			     const std::string &columnPrefix, const std::string &columnSuffix,
			     bool dumpData=false,
                             edm::InputTag uncorrectedCollectionTag=edm::InputTag("",""));

 private:
  
  void writeJetInfo(const reco::Candidate *cand, const edm::Event&, const edm::EventSetup&);
  void treeJetInfo(const std::string &colPrefix, const std::string &colSuffix);

  // Friends

  bool hitLimitsMeansNoOutput_;
  int maxTracks_;
  int maxMCTracks_;

  bool dumpUncorrEnergy_;

  std::string *trkIndexName_;

  CmsPFJetFillerData *privateData_;

  CmsTree *cmstree;

};

#endif // CmsPFJetFiller_h
