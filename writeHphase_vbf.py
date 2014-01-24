#!/usr/bin/env python
#from samplesclass import sample
#from printcolor import printc
import pickle
import sys
import os
import ROOT 
import math
import shutil
from ROOT import TFile
import ROOT
ROOT.gROOT.SetBatch(True)
from array import array
import warnings
from optparse import OptionParser
from BetterConfigParser import BetterConfigParser
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )
argv = sys.argv

def deltaPhi(phi1, phi2): 
    result = phi1 - phi2
    while (result > math.pi): result -= 2*math.pi
    while (result <= -math.pi): result += 2*math.pi
    return result

path = './optimizationForGroup/'
pathIN = path
pathOUT = path+'out_optimization/VBF_'

jobdir = 'Hbb'
jobtree = 'events'
print 'INput samples:\t%s'%pathIN
print 'OUTput samples:\t%s'%pathOUT


def deltaPhi(phi1, phi2):
    result = phi1 - phi2
    while (result > math.pi): result -= 2*math.pi
    while (result <= -math.pi): result += 2*math.pi
    return result


def deltaR(eta1,phi1,eta2,phi2):
      deta = eta1 - eta2;
      dphi = deltaPhi(phi1, phi2);
      return math.sqrt(deta*deta + dphi*dphi)

#def Xmass():

ROOT.gROOT.ProcessLine(
        "struct H {\
        float         mass;\
        float         pt1corr;\
        float         pt2corr;\
        float         pt1;\
        float         pt2;\
        } ;"
    )

for iter in range(26,31):
    ROOT.gROOT.SetBatch(True)
    job = 'flatTree_VBFPowheg125-NewGenjets_weights_All_%.0f.root'%(iter)

    input = ROOT.TFile.Open(pathIN+job,'read')
    output = ROOT.TFile.Open(pathOUT+job,'recreate')

    input.cd()
    input.ls()
    tree = input.Get(jobtree)
    nEntries = tree.GetEntries()
    print nEntries
    H = ROOT.H()
    tree.SetBranchStatus('H',0)
    output.cd()
    newtree = tree.CloneTree(0)
    hJet_e = array('f',[0]*20)
    hJet_pt = array('f',[0]*20)
    hJet_eta = array('f',[0]*20)
    hJet_phi = array('f',[0]*20)
    hJet_PU = array('f',[0]*20)
    hJet_PUM = array('f',[0]*20)
    hJet_btag = array('f',[0]*20)
    hJet_regE = array('f',[0]*20)
    hJet_regPt = array('f',[0]*4)
    h_njets = ROOT.TH1F('njet','njets', 10, 0, 10)
    h_eta = ROOT.TH1F('eta','eta',40, -5, 5)
    h_btag = ROOT.TH1F('btag','btag', 20, -1,1)
    h_pt = ROOT.TH1F('pt','pt', 20, 0., 100.)
    h_mH_reg = ROOT.TH1F('h_mH_reg','h_mH_reg', 90, 80., 170.)
    h_mH = ROOT.TH1F('h_mH','h_mH', 90, 80., 170.)
    cont = 0
    newtree.Branch( 'H', H , 'mass/F:pt1corr/F:pt2corr/F:pt1/F:pt2/F' )
    for entry in range(1,nEntries):
        tree.GetEntry(entry)
#        if ((tree.nJets>3) and (tree.triggerResult[0] or tree.triggerResult[1]) and tree.mqq[1]>250 and tree.dPhibb[1]<2.0 and tree.jetPt[0]>80 and tree.jetPt[1]>65 and tree.jetPt[2]>50 and tree.jetPt[3]>35 and tree.dEtaqq[1]>2.5):# and tree.mvaNOM>0.9):
        if ((tree.nJets>3) and (tree.triggerResult[9] ) and tree.mqq[2]>600 and tree.dPhibb[2]<2.0 and tree.jetPt[0]>80 and tree.jetPt[1]>65 and tree.jetPt[2]>50 and tree.jetPt[3]>35 and tree.dEtaqq[2]>2.5 and tree.jetBtagM[tree.b1[0]] and tree. jetBtagL[tree.b2[0]]):
           Bid = []
           hJ0 = ROOT.TLorentzVector()
           hJ1 = ROOT.TLorentzVector()
           if tree.b1[0] <4 and tree.b2[0]< 4 :
              Bid.append(tree.b1[0])
              Bid.append(tree.b2[0])
              for i in range(0,tree.nJets):
               hJet_e[i] = tree.jetMass[i]
               hJet_pt[i] = tree.jetPt[i]
               hJet_eta[i] = tree.jetEta[i]
               hJet_phi[i] = tree.jetPhi[i]
               hJet_PU[i] = tree.jetPuIdL[i]
               hJet_PUM[i] = tree.jetPuIdM[i]
               hJet_btag[i] = tree.jetBtag[i]
               if i<4 :
                  hJet_regPt[i] = tree.hJet_regWeight[i]
                  hJet_regE[i] = tree.hJet_regWeight[i]

              hJ0.SetPtEtaPhiM(hJet_pt[Bid[0]],hJet_eta[Bid[0]],hJet_phi[Bid[0]],hJet_e[Bid[0]])
              hJ1.SetPtEtaPhiM(hJet_pt[Bid[1]],hJet_eta[Bid[1]],hJet_phi[Bid[1]],hJet_e[Bid[1]])
              if tree.hJet_regWeight[Bid[0]] < 5. :
                hJ0Pt= hJ0.Pt()*tree.hJet_regWeight[Bid[0]]
                hJ0E= hJ0.E()*tree.hJet_regWeight[Bid[0]]
                hJ0.SetPtEtaPhiE(hJ0Pt,hJet_eta[Bid[0]],hJet_phi[Bid[0]],hJ0E)
              if tree.hJet_regWeight[Bid[1]] < 5. :
                hJ1Pt= hJ1.Pt()*tree.hJet_regWeight[Bid[1]]
                hJ1E= hJ1.E()*tree.hJet_regWeight[Bid[1]]
                hJ1.SetPtEtaPhiE(hJ1Pt,hJet_eta[Bid[1]],hJet_phi[Bid[1]],hJ1E)

              H.mass = (hJ0+hJ1).M()
              diff = tree.mbb[0]-tree.mbbReg[0]
              #if diff>0.1 :
                        #print 'my mass %s, tree mass %s '%(H.mass,tree.mbbReg)
              hJ00=hJ0.Pt()
              hJ01=hJ1.Pt()
              H.pt1 = hJ00
              H.pt2 = hJ01
              h_mH.Fill(H.mass)
              h_mH_reg.Fill(tree.mbb[0])
              H.pt1corr = hJ00-hJ0.Pt()
              H.pt2corr = hJ01-hJ1.Pt()
              del Bid
              newtree.Fill()
           else: print 'WARNING'
    h_eta.Write()
    h_pt.Write()
    h_njets.Write()
    h_btag.Write()
    h_mH.Write()
    h_mH_reg.Write()
    print cont
    print 'Exit loop'
    newtree.AutoSave()
    print 'Save'
    output.Close()
    print 'Close'

