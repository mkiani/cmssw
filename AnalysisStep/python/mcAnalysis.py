#!/usr/bin/env python
from WWAnalysis.AnalysisStep.tree2yield import *

class MCAnalysis:
    def __init__(self,samples,options):
        self._foutName = options.out if options.out else samples.replace(".txt","")+".root"
        self._fout     = None
        self._options = options
        self._allData     = {}
        self._data        = []
        self._signals     = []
        self._backgrounds = [] 
        self._isSignal    = {}
        for line in open(samples,'r'):
            field = line.split(':')
            rootfile = "tree_%s.root" % field[1].strip()
            signal = ("%d" in rootfile)
            if field[0][-1] == "+": 
                signal = True
                field[0] = field[0][:-1]
            if field[0][-1] == "-": 
                signal = False
                field[0] = field[0][:-1]
            if ("%d" in rootfile): rootfile = rootfile % options.mass
            tty = TreeToYield(rootfile, options)
            if len(field) == 3: tty.setScaleFactor(float(field[2]))
            if signal: 
                self._signals.append(tty)
                self._isSignal[field[0]] = True
            elif field[0] == "data":
                self._data.append(tty)
            else:
                self._isSignal[field[0]] = False
                self._backgrounds.append(tty)
            if field[0] in self._allData: self._allData[field[0]].append(tty)
            else                        : self._allData[field[0]] =     [tty]
        #if len(self._signals) == 0: raise RuntimeError, "No signals!"
        #if len(self._backgrounds) == 0: raise RuntimeError, "No backgrounds!"
    def listProcesses(self):
        return self._allData.keys()[:]
    def scaleProcess(self,process,scaleFactor):
        for tty in self._allData[process]: tty.setScaleFactor(scaleFactor)
    def getYields(self,cuts,process=None,nodata=False,makeSummary=False):
        ret = { }
        allSig = []; allBg = []
        for key in self._allData:
            if key == 'data' and nodata: continue
            if process != None and key != process: continue
            ret[key] = self._getYields(self._allData[key],cuts)
            if key != 'data':
                if self._isSignal[key]: allSig.append(ret[key])
                else: allBg.append(ret[key])
        if makeSummary:
            if self._signals and not ret.has_key('signal'):
                ret['signal'] = mergeReports(allSig)
            if self._backgrounds and not ret.has_key('background'):
                ret['background'] = mergeReports(allBg)
        return ret
    def prettyPrint(self,reports,makeSummary=True):
        allSig = []; allBg = []
        for key in self._allData:
            if key == 'data': continue
            print "\n ==== {0} ====".format(key)
            self._allData[key][0].prettyPrint(reports[key])
            if key != 'data':
                if self._isSignal[key]: allSig.append(reports[key])
                else: allBg.append(reports[key])
        if makeSummary:
            if self._signals:
                print "\n ==== ALL SIGNALS ==== "
                self._signals[0].prettyPrint(mergeReports(allSig))
            if self._backgrounds:
                print "\n ==== ALL BACKGROUNDS ==== "
                self._backgrounds[0].prettyPrint(mergeReports(allBg))
        if self._allData.has_key('data'):
            print "\n ==== DATA ==== "
            self._allData['data'][0].prettyPrint(reports['data'])
    def getPlots(self,plots,cut,makeSummary=False):
        for (name,expr,bins) in plots.plots():
            self.getPlotsForCut(name,expr,bins,cut,makeSummary=makeSummary)
    def getPlotsForCut(self,name,expr,bins,cut,write=True,nodata=False,makeSummary=False):
        report = {}
        allSig = []; allBg = []
        for key in self._allData:
            if key == 'data' and nodata: continue
            report[key] = self._getPlots(name,expr,bins,cut,self._allData[key])
            for (k,h) in report[key]:
                if write: self._fOut(key).WriteTObject(h)
            if key != 'data':
                if self._isSignal[key]: allSig.append(report[key])
                else: allBg.append(report[key])
        if makeSummary:
            if self._signals and not report.has_key('signal'):
                report['signal'] = mergePlots(allSig)
            if self._backgrounds and not report.has_key('background'):
                report['background'] = mergePlots(allBg)
        return report;
    def dumpEvents(self,cut,vars=['run','lumi','event']):
        for tty in self._data: tty.dumpEvents(cut,vars)
    def _getYields(self,ttylist,cuts):
        return mergeReports([tty.getYields(cuts) for tty in ttylist])
    def _getPlots(self,name,expr,bins,cut,ttylist):
        return mergePlots([tty.getPlots(name,expr,bins,cut) for tty in ttylist])
    def _fOutName(self):
            return self._foutName;
    def _fOut(self,dir=None):
        if dir == None:
            if not self._fout: self._fout = ROOT.TFile.Open(self._foutName, "RECREATE")
            return self._fout
        else:
            self._fOut()
            tdir = self._fout.GetDirectory(dir)
            if tdir: return tdir
            else:    return self._fout.mkdir(dir)
        
if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser(usage="%prog [options] tree.root cuts.txt")
    addTreeToYieldOptions(parser)
    parser.add_option("-o", "--out",    dest="out",  help="Output file name. by default equal to input -'.txt' +'.root'");
    parser.add_option("-D", "--dump",   dest="dump", action="store_true", help="Dump events passing selection");
    parser.add_option("-p", "--plots",  dest="plots", type="string", metavar="FILE", help="Make the plots defined in plot file");
    parser.add_option("-m", "--mass",   dest="mass", type="int", default="160", help="Higgs boson mass");
    (options, args) = parser.parse_args()
    tty = TreeToYield(args[0],options) if ".root" in args[0] else MCAnalysis(args[0],options)
    cf  = CutsFile(args[1],options)
    if options.plots:
        pf = PlotsFile(options.plots, options)
        tty.getPlots(pf, cf.allCuts())
    else:
        report = tty.getYields(cf)
        tty.prettyPrint(report)
    #tty.getPlots("gammaMRStar","gammaMRStar","200,0.,200.",cf.allCuts())
    #if options.dump: tty.dumpEvents(cf.allCuts())
