#!/usr/bin/env python
from math import *
import re
import ROOT
from copy import *
ROOT.gROOT.SetBatch(True)

MM=0;ME=1;EM=2;EE=3;
class CutsFile:
    def __init__(self,txtfileOrCuts,options=None):
        if type(txtfileOrCuts) == list:
            self._cuts = deepcopy(txtfileOrCuts[:])
        elif isinstance(txtfileOrCuts,CutsFile):
            self._cuts = deepcopy(txtfileOrCuts.cuts())
        else:
            self._cuts = []
            file = open(txtfileOrCuts, "r")
            if not file: raise RuntimeError, "Cannot open "+txtfileOrCuts+"\n"
            for cr,cn,cv in options.cutsToAdd:
                if re.match(cr,"entry point"): self._cuts.append((cn,cv))
            for line in file:
                (name,cut) = [x.strip() for x in line.split(":")]
                if name == "entry point" and cut == "1": continue
                if options.startCut and not re.search(options.startCut,name): continue
                if options.startCut and re.search(options.startCut,name): options.startCut = None
                self._cuts.append((name,cut))
                for cr,cn,cv in options.cutsToAdd:
                    if re.match(cr,name): self._cuts.append((cn,cv))
                if options.upToCut and re.search(options.upToCut,name):
                    break
            for ci in options.cutsToInvert:  self.invert(ci)
            for ci in options.cutsToExclude: self.remove(ci)
            for cr,cn,cv in options.cutsToReplace: self.replace(cr,cn,cv)
    def remove(self,cut):
        self._cuts = [(cn,cv) for (cn,cv) in self._cuts if not re.search(cut,cn)]
        return self
    def invert(self,cut):
        for i,(cn,cv) in enumerate(self._cuts[:]):
            if re.search(cut,cn):
                if cn.startswith("not ") and re.match(r"!\(.*\)", cv):
                    self._cuts[i] = (cn[4:], cv[2:-1])
                else:
                    self._cuts[i] = ("not "+cn, "!("+cv+")")
        return self
    def replace(self,cut,newname,newcut):       
        for i,(cn,cv) in enumerate(self._cuts[:]):
            if re.search(cut,cn):
                self._cuts[i] = (newname, newcut)
        return self
    def cuts(self):
        return self._cuts[:]
    def nMinusOne(self):
        return CutsFile(self.nMinusOneCuts())
    def nMinusOneCuts(self):
        ret = []
        for cn,cv in self._cuts:
            nm1 = " && ".join("(%s)" % cv1 for cn1,cv1 in self._cuts if cn1 != cn)
            ret.append(("all but "+cn, nm1))
        return ret
    def allCuts(self):
        return " && ".join("(%s)" % x[1] for x in self._cuts)

class PlotsFile:
    def __init__(self,txtfileOrPlots,options=None):
        if type(txtfileOrPlots) == list:
            self._plots = txtfileOrPlots[:]
        else:
            self._plots = []
            file = open(txtfileOrPlots, "r")
            if not file: raise RuntimeError, "Cannot open "+txtfileOrPlots+"\n"
            for line in file:
                (name,expr,bins) = [x.strip() for x in line.split(":")]
                self._plots.append((name,expr,bins))
    def plots(self):
        return self._plots[:]

class TreeToYield:
    def __init__(self,root,options,report=None):
        self._fname = root
        self._tfile = ROOT.TFile.Open(root)
        if not self._tfile: raise RuntimeError, "Cannot open %s\n" % root
        self._options = options
        self._trees = []
        for h in ("mumu","muel","elmu","elel",):
            t = self._tfile.Get((options.tree % h)+"/probe_tree")
            if not t: raise RuntimeError, "Cannot find tree %s/probe_tree in file %s\n" % (options.tree % h, root)
            self._trees.append((h,t))
        self._weight  = (options.weight and self._trees[0][1].GetBranch("weight") != None)
    def attachMVA(self,name):
        self._fnameMVA = self._fname.replace(".root","."+name+".root")
        self._tfileMVA = ROOT.TFile.Open(self._fnameMVA)
        if not self._tfileMVA: raise RuntimeError, "Cannot open %s\n" % self._fnameMVA
        self._treesMVA = []
        for h,t0 in self._trees:
            t = self._tfile.Get((options.tree % h)+"/"+name)
            if not t: raise RuntimeError, "Cannot find tree %s/%s in file %s\n" % (options.tree % h, name, self._fnameMVA)
            self._treesMVA.append((h,t))
            t0.AddFriend(t)
    def getYields(self,cuts):
        report = []; cut = ""
        cutseq = [ ['entry point','1'] ]
        sequential = False
        if self._options.nMinusOne: 
            cutseq = cuts.nMinusOneCuts()
            cutseq += [ ['all',cuts.allCuts()] ]
            sequential = False
        elif self._options.final:
            cutseq += [ ['all', cuts.allCuts()] ]
        else:
            cutseq += cuts.cuts();
            sequential = True
        for cn,cv in cutseq:
            if sequential:
                if cut: cut += " && "
                cut += "(%s)" % cv
            else:
                cut = cv
            report.append((cn,self._getYields(cut)))
        return report
    def prettyPrint(self,report):
        clen = max([len(cut) for cut,yields in report])
        nch  = len(report[0][1]);
        flen=26 if self._options.errors else 18;
        cfmt = "%%-%ds   " % clen;
        print cfmt % "   cut",
        for (hypo,nev,err) in report[0][1]:
            print "           %4s   " % hypo,
            if self._options.errors: print " "*7,
        print ""
        print "-"*(flen*(nch+1)+clen+3)
        for i,(cut,yields) in enumerate(report):
            print cfmt % cut,
            for j,(hypo,nev,err) in enumerate(yields):
                den = report[i-1][1][j][1] if i>0 else 0
                fraction = nev/float(den) if den > 0 else 1
                if self._options.nMinusOne: 
                    fraction = report[-1][1][j][1]/nev if nev > 0 else 1
                if self._options.errors:
                    if self._weight and nev < 1000:
                        print (u"%7.2f \u00b1%6.2f  %6.2f%%   " % (nev, err, fraction * 100)).encode('utf-8'),
                        #print "%7.2f +%6.2f  %6.2f%%   " % (nev, err, fraction * 100),
                    else:
                        print (u"%7d \u00b1%6.1f  %6.2f%%   " % (nev, err, fraction * 100)).encode('utf-8'),
                        #print "%7d +%6.1f  %6.2f%%   " % (nev, err, fraction * 100),
                else:
                    if self._weight and nev < 1000:
                        print "%7.2f  %6.2f%%   " % (nev, fraction * 100),
                    else:
                        print "%7d  %6.2f%%   " % (nev, fraction * 100),
            print ""
    def getPlots(self,plots,cut):
        ret = [ [name, self.getPlots(expr,name,bins,cut)] for (expr,name,bins) in plots.plots()]
        return ret
    def getPlots(self,expr,name,bins,cut):
        plots = [ [k,self._getPlot(t,expr,name+"_"+k,bins,cut)] for (k,t) in self._trees ]
        hall  = plots[0][1].Clone(name+"_all"); hall.Reset()
        for k,h in plots: hall.Add(h)
        all   = [ ['all', hall] ]
        if self._options.inclusive:
            plots = all
        else:
            plots += all
        return plots
    def dumpEvents(self,cut,vars=['run','lumi','event']):
        for (k,t) in self._trees:
            print "Dump for channel ",k
            t.Scan(":".join(vars), cut)
            print
    def getAverageWeight(self,cut):
        if not self._weight: return 1.0
        nev = 0; sumw = 0;
        for (k,t) in self._trees: 
            (n,sw) = self._getNumAndWeight(t,cut)
            nev += n; sumw += sw
        return sumw/nev;
    def _getYields(self,cut):
        yields = [ [k] + self._getYield(t,cut) for (k,t) in self._trees ]
        all    = [ ['all', sum(x for h,x,e in yields), sqrt(sum(e*e for h,x,e in yields))] ]
        if self._options.inclusive:
            yields = all
        else:
            yields += all
        return yields
    def _getYield(self,tree,cut):
        if self._weight:
            histo = self._getPlot(tree,"0.5","dummy","1,0.,1.",cut)
            return [ histo.GetBinContent(1), histo.GetBinError(1) ]
        else: 
            npass = tree.Draw("1",cut,"goff");
            return [ npass, sqrt(npass) ]
    def _getNumAndWeight(self,tree,cut):
            histo = TH1F("dummy","dummy",1,0.,1.)
            nev = tree.Draw("0.5>>dummy", "weight*("+cut+")","goff")
            if nev == 0: return (0,0)
            sumw = histo.GetBinContent(1)*self._options.lumi
            histo.Delete()
            return (nev,sumw)
    def _getPlot(self,tree,expr,name,bins,cut):
            if self._weight: cut = "weight*"+str(self._options.lumi)+"*("+cut+")"
            (nb,xmin,xmax) = bins.split(",")
            histo = ROOT.TH1F(name,name,int(nb),float(xmin),float(xmax))
            histo.Sumw2()
            nev = tree.Draw("%s>>%s" % (expr,name), cut ,"goff")
            return histo

def addTreeToYieldOptions(parser):
    parser.add_option("-l", "--lumi",           dest="lumi",   type="float", default="1.0", help="Luminosity (in 1/fb)");
    parser.add_option("-w", "--weight",         dest="weight", action="store_true", help="Use weight (in MC events)");
    parser.add_option("-i", "--inclusive",  dest="inclusive", action="store_true", help="Only show totals, not each final state separately");
    parser.add_option("-f", "--final",  dest="final", action="store_true", help="Just compute final yield after all cuts");
    parser.add_option("-e", "--errors",  dest="errors", action="store_true", help="Include uncertainties in the reports");
    parser.add_option("-S", "--start-at-cut",   dest="startCut",   type="string", help="Run selection starting at the cut matched by this regexp, included.") 
    parser.add_option("-U", "--up-to-cut",      dest="upToCut",   type="string", help="Run selection only up to the cut matched by this regexp, included.") 
    parser.add_option("-X", "--exclude-cut", dest="cutsToExclude", action="append", default=[], help="Cuts to exclude (regexp matching cut name), can specify multiple times.") 
    parser.add_option("-I", "--invert-cut",  dest="cutsToInvert",  action="append", default=[], help="Cuts to invert (regexp matching cut name), can specify multiple times.") 
    parser.add_option("-R", "--replace-cut", dest="cutsToReplace", action="append", default=[], nargs=3, help="Cuts to invert (regexp of old cut name, new name, new cut); can specify multiple times.") 
    parser.add_option("-A", "--add-cut",     dest="cutsToAdd",     action="append", default=[], nargs=3, help="Cuts to insert (regexp of cut name after which this cut should go, new name, new cut); can specify multiple times.") 
    parser.add_option("-N", "--n-minus-one", dest="nMinusOne", action="store_true", help="Compute n-minus-one yields and plots")
    parser.add_option("-t", "--tree",           dest="tree", default='%sTree', help="Pattern for tree name");

def mergeReports(reports):
    one = reports[0]
    for i,(c,x) in enumerate(one):
        for j,xj in enumerate(x):
            one[i][1][j][2] = pow(one[i][1][j][2], 2)
    for two in reports[1:]:
        for i,(c,x) in enumerate(two):
            for j,xj in enumerate(x):
                one[i][1][j][1] += xj[1]
                one[i][1][j][2] += pow(xj[2],2)
    for i,(c,x) in enumerate(one):
        for j,xj in enumerate(x):
            one[i][1][j][2] = sqrt(one[i][1][j][2])
    return one

def mergePlots(plots):
    one = plots[0]
    for two in plots[1:]:
        for i,(k,h) in enumerate(two): 
            one[i][1].Add(h)
    return one

