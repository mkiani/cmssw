#ifndef PF_DisplayCommon_h
#define PF_DisplayCommon_h

enum View_t { XY = 0, RZ = 1, EPE = 2, EPH = 3, EHO =4, NViews = 5 };

enum ObjType { 
  RECHITECALID=0, 
  RECHITHCALID,
  RECHITHOID,
  RECHITHFEMID,
  RECHITHFHADID,
  RECHITPSID,
  CLUSTERECALID,
  CLUSTERHCALID,
  CLUSTERHOID,
  CLUSTERHFEMID,
  CLUSTERHFHADID,
  CLUSTERPSID,
  CLUSTERIBID,
  RECTRACKID,
  BREMID,
  GSFRECTRACKID,
  SIMPARTICLEID,
  GENPARTICLEID
};   

const unsigned int SHIFTID=26;
const int HITTYPES=5;
             
#endif