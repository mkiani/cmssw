// -*- C++ -*-
//-----------------------------------------------------------------------
//
// Package:    
//      HtoWWTreeDumper
// Description:
//      Class CmsTriggerTreeFiller
//      Simple class for dumping RECO (or AOD) contents to an ntuple
//      
// Original Author:  Alessio Ghezzi, Pietro Govoni
//         Created:  Fri Apr  6 18:05:34 CEST 2007
//
//-----------------------------------------------------------------------

#ifndef CmsTriggerTreeFiller_h
#define CmsTriggerTreeFiller_h

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/TriggerResults.h"

#include <TTree.h>
#include <string>

#include "HiggsAnalysis/HiggsToWW2e/interface/CmsTree.h"

class CmsTriggerTreeFiller {

 public:

  /// Constructors
  CmsTriggerTreeFiller(CmsTree *);

  /// Destructor
  virtual ~CmsTriggerTreeFiller();

  /// Write the trigger bits to the tree
  void writeTriggerToTree (edm::InputTag triggerResultsTag,
			   const edm::Event& iEvent,
                           const std::string & columnPrefix, const std::string & columnSuffix) ;

 protected:
  
  std::vector<std::string> m_TrigNames ;

  CmsTree *cmstree;

};

#endif // CmsTriggerTreeFiller_h
