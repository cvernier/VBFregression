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

do = True
path = './'
jobpath ='optimizationForGroup/flatTree_VBFPowheg125-NewGenjets'



for iter in range(1,31):
    ROOT.gROOT.SetBatch(True)	
    iteration = 'optimizationForGroup/weightDirectory_%.0f/factoryJetRegNewGenJets3_BDT.weights.xml'%(iter)
    if iter == 28 :  regWeight='MVA_BDT_REG_Mar13.weights.xml'
    else : regWeight = iteration 
    input = TFile.Open(path+'/'+jobpath+'.root','read')
    output = TFile.Open(path+'/'+jobpath+'_weights_All_%.0f.root'%(iter),'recreate')

    input.cd()
    obj = ROOT.TObject
    for key in ROOT.gDirectory.GetListOfKeys():
        input.cd()
        obj = key.ReadObj()
        if obj.GetName() == 'Hbb/events':
            continue
        output.cd()
        obj.Write(key.GetName())
        
    input.cd()
    tree = input.Get('Hbb/events')
    nEntries = tree.GetEntries()
        
    tree.SetBranchStatus('H',0)
    output.cd()
    newtree = tree.CloneTree(0)


    regDict_1 = {"jetBtag":"jetBtag[0]","jetPtRaw": "jetPtRaw[0]","jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetMt_":"jetMt_[0]","jetUnc": "jetUnc[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","jetChf":"jetChf[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetPtD":"jetPtD[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]","met":"met","rho":"rho","jetPart":"jetPart[0]", "jetEt":"jetEt[0]"}
    regVars_1 = ["jetBtag","jetPtRaw","jetPt","jetEta","jetMt_","jetUnc","jetMetPhi","jetLeadTrkPt","jetChf","jetPhf","jetNhf","jetElf","jetMuf","jetPtD","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR","met","rho","jetPart","jetEt"]
    regDict_2 = {"jetBtag":"jetBtag[0]","jetPtRaw": "jetPtRaw[0]","jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetMt_":"jetMt_[0]","jetUnc": "jetUnc[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","jetChf":"jetChf[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetPtD":"jetPtD[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]","met":"met","rho":"rho","jetPart":"jetPart[0]", "jetEt":"jetEt[0]"}
    regVars_2 = ["jetBtag","jetPtRaw","jetPt","jetEta","jetMt_","jetUnc","jetMetPhi","jetLeadTrkPt","jetChf","jetPhf","jetNhf","jetElf","jetMuf","jetPtD","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR","met","rho","jetPart","jetEt"]
    regDict_3 = {"jetBtag":"jetBtag[0]","jetPtRaw": "jetPtRaw[0]","jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetMt_":"jetMt_[0]","jetUnc": "jetUnc[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","jetChf":"jetChf[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetPtD":"jetPtD[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]","met":"met","rho":"rho","jetPart":"jetPart[0]", "jetEt":"jetEt[0]"}
    regVars_3 = ["jetBtag","jetPtRaw","jetPt","jetEta","jetMt_","jetUnc","jetMetPhi","jetLeadTrkPt","jetChf","jetPhf","jetNhf","jetElf","jetMuf","jetPtD","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR","met","rho","jetPart","jetEt"]
    regDict_7 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","met":"met","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPtD":"jetPtD[0]","jetChf":"jetChf[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_7 = ["jetPt","jetEta","jetM","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPtD","jetChf","jetPhf","jetNhf","jetElf","jetMuf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_8 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","met":"met","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPtD":"jetPtD[0]","jetChf":"jetChf[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_8 = ["jetPt","jetEta","jetM","jetUnc","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPtD","jetChf","jetPhf","jetNhf","jetElf","jetMuf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_9 = {"jetPtRaw": "jetPtRaw[0]", "jetPt": "jetPt[0]", "jetEt":"jetEt[0]","jetMt_":"jetMt_[0]","jetUnc":"jetUnc[0]","met":"met","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPtD":"jetPtD[0]","jetChf":"jetChf[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_9 = ["jetPtRaw","jetPt","jetEt","jetMt_","jetUnc","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPtD","jetChf","jetPhf","jetNhf","jetElf","jetMuf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_10 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","met":"met","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPtD":"jetPtD[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_10 = ["jetPt","jetEta","jetM","jetUnc","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPtD","jetPhf","jetNhf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_11 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","met":"met","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPtD":"jetPtD[0]","jetChf":"jetChf[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_11 = ["jetPt","jetEta","jetM","jetUnc","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPtD","jetChf","jetElf","jetMuf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_12 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPtD":"jetPtD[0]","jetChf":"jetChf[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_12 = ["jetPt","jetEta","jetM","jetUnc","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPtD","jetChf","jetPhf","jetNhf","jetElf","jetMuf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_13 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","met":"met[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPtD":"jetPtD[0]","jetChf":"jetChf[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_13 = ["jetPt","jetEta","jetM","jetUnc","met","jetLeadTrkPt","rho","jetPart","jetPtD","jetChf","jetPhf","jetNhf","jetElf","jetMuf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_14 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPtD":"jetPtD[0]","jetChf":"jetChf[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_14 = ["jetPt","jetEta","jetM","jetUnc","jetLeadTrkPt","rho","jetPart","jetPtD","jetChf","jetPhf","jetNhf","jetElf","jetMuf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_15 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_15 = ["jetPt","jetEta","jetM","jetUnc","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_16 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_16 = ["jetPt","jetEta","jetM","jetUnc","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3dL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_17 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_17 = ["jetPt","jetEta","jetM","jetUnc","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_18 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_18 = ["jetPt","jetEta","jetM","jetUnc","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepDR"] 
    regDict_19 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]"}
    regVars_19 = ["jetPt","jetEta","jetM","jetUnc","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel"]  
    regDict_20 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","jetUnc":"jetUnc[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_20 = ["jetPt","jetEta","jetM","jetUnc","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPtRel","jetSoftLepDR"]
    regDict_21 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_21 = ["jetPt","jetEta","jetM","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepDR"]
    regDict_22 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_22 = ["jetPt","jetEta","jetM","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepDR"]
    regDict_23 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]"}
    regVars_23 = ["jetPt","jetEta","jetM","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel"]
    regDict_24 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_24 = ["jetPt","jetEta","jetM","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepDR"]
    regDict_25 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_25 = ["jetPt","jetEta","jetM","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepDR"]
    regDict_26 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]"}
    regVars_26 = ["jetPt","jetEta","jetM","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel"]
    regDict_27 = {"jetPtRaw": "jetPtRaw[0]","jetPt": "jetPt[0]", "jetEt":"jetEt[0]","jetMt_":"jetMt_[0]","jetUnc": "jetUnc[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]","met":"met","jetPart":"jetPart[0]"}
    regVars_27 = ["jetPtRaw","jetPt","jetEt","jetMt_","jetUnc","jetMetPhi","jetLeadTrkPt","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel","jetSoftLepDR","met","jetPart"]
    regDict_28 = {"jetPt": "jetPt[0]","jetPtRaw": "jetPtRaw[0]","jetUnc": "jetUnc[0]", "jetEt":"jetEt[0]","jetMt_":"jetMt_[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]","jetSoftLepDR":"jetSoftLepDR[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetElf":"jetElf[0]","jetPart":"jetPart[0]","jetVtxPt":"jetVtxPt[0]","jetVtxMass":"jetVtxMass[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","met":"met","jetMetPhi":"jetMetPhi[0]"}
    regVars_28 = ["jetPt","jetPtRaw","jetUnc","jetEt","jetMt_","jetLeadTrkPt","jetSoftLepPtRel","jetSoftLepDR","jetSoftLepPt","jetElf","jetPart","jetVtxPt","jetVtxMass","jetVtx3dL","jetVtx3deL","met","jetMetPhi"]
    regDict_29 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetElf":"jetElf[0]","jetMuf":"jetMuf[0]","jetVtx3dL":"jetVtx3dL[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepDR":"jetSoftLepDR[0]"}
    regVars_29 = ["jetPt","jetEta","jetM","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetElf","jetMuf","jetVtx3dL","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepDR"]
    regDict_30 = {"jetPt": "jetPt[0]", "jetEta":"jetEta[0]","jetM":"jetM[0]","met":"met[0]","jetMetPhi":"jetMetPhi[0]","jetLeadTrkPt": "jetLeadTrkPt[0]","rho":"rho","jetPart":"jetPart[0]","jetPhf":"jetPhf[0]","jetNhf":"jetNhf[0]","jetVtx3deL":"jetVtx3deL[0]","jetVtxMass":"jetVtxMass[0]","jetSoftLepPt":"jetSoftLepPt[0]","jetSoftLepPtRel":"jetSoftLepPtRel[0]"}
    regVars_30 = ["jetPt","jetEta","jetM","met","jetMetPhi","jetLeadTrkPt","rho","jetPart","jetPhf","jetNhf","jetVtx3deL","jetVtxMass","jetSoftLepPt","jetSoftLepPtRel"]
   
 
    regDict = eval(('regDict_%.0f')%(iter))
    regVars = eval(('regVars_%.0f')%(iter))

    applyRegression = True
    hJ0 = ROOT.TLorentzVector()
    hJet_regWeight = array('f',[0]*4)
    hJet_MyPt = array('f',[0]*4)
    hJet_MyE = array('f',[0]*4)
    newtree.Branch('hJet_regWeight',hJet_regWeight,'hJet_regWeight[4]/F')
    newtree.Branch('hJet_MyPt',hJet_MyPt,'hJet_MyPt[4]/F')
    newtree.Branch('hJet_MyE',hJet_MyE,'hJet_MyE[4]/F')
    


    def addVarsToReader(reader,theVars,theForms,i):
        for key in regVars:
            var = regDict[key]
            theVars[key] = array( 'f', [ 0 ] )
            reader.AddVariable(key,theVars[key])
            formula = regDict[key].replace("[0]","[%.0f]" %i)
            print 'Adding var: %s with %s to readerJet%.0f' %(key,formula,i)
            theForms['form_reg_%s_%.0f'%(key,i)] = formula #ROOT.TTreeFormula("form_reg_%s_%.0f"%(key,i),'%s' %(formula),tree)
        return



    readerJet0 = ROOT.TMVA.Reader("!Color:!Silent" )
    readerJet1 = ROOT.TMVA.Reader("!Color:!Silent" )
    readerJet2 = ROOT.TMVA.Reader("!Color:!Silent" )
    readerJet3 = ROOT.TMVA.Reader("!Color:!Silent" )
    theForms = {}
    theVars0 = {}
    theVars1 = {}  
    theVars2 = {}
    theVars3 = {}
    addVarsToReader(readerJet0,theVars0,theForms,0)
    addVarsToReader(readerJet1,theVars1,theForms,1)
    addVarsToReader(readerJet2,theVars2,theForms,2)
    addVarsToReader(readerJet3,theVars3,theForms,3)
    #print theVars1
    readerJet0.BookMVA( "BDT0", regWeight )
    readerJet1.BookMVA( "BDT1", regWeight )
    readerJet2.BookMVA( "BDT2", regWeight )
    readerJet3.BookMVA( "BDT3", regWeight )


    for entry in range(0,nEntries):
            tree.GetEntry(entry)
            met_0=tree.met
            rho_0=tree.rho
            met_1=tree.met
            rho_1=tree.rho
            met_2=tree.met
            rho_2=tree.rho
            met_3=tree.met
            rho_3=tree.rho
	    #print met	
            jetPt_0= tree.jetPt[0]
            jetPt_1= tree.jetPt[1]
            jetPt_2= tree.jetPt[2]
            jetPt_3= tree.jetPt[3]
            jetNhf_0= tree.jetNhf[0]
            jetNhf_1= tree.jetNhf[1]
            jetNhf_2= tree.jetNhf[2]
            jetNhf_3= tree.jetNhf[3] 
            jetBtag_0= tree.jetBtag[0]
            jetBtag_1= tree.jetBtag[1]
            jetBtag_2= tree.jetBtag[2]
            jetBtag_3= tree.jetBtag[3]
            jetEta_0= tree.jetEta[0]
            jetEta_1= tree.jetEta[1]
            jetEta_2= tree.jetEta[2]
            jetEta_3= tree.jetEta[3]
            jetMetPhi_0= tree.jetMetPhi[0]
            jetMetPhi_1= tree.jetMetPhi[1]
            jetMetPhi_2= tree.jetMetPhi[2]
            jetMetPhi_3= tree.jetMetPhi[3]
            jetChf_0= tree.jetChf[0]
            jetChf_1= tree.jetChf[1]
            jetChf_2= tree.jetChf[2]
            jetChf_3= tree.jetChf[3]
            jetPhf_0= tree.jetPhf[0]
            jetPhf_1= tree.jetPhf[1]
            jetPhf_2= tree.jetPhf[2]
            jetPhf_3= tree.jetPhf[3]
            jetElf_0= tree.jetElf[0]
            jetElf_1= tree.jetElf[1]
            jetElf_2= tree.jetElf[2]
            jetElf_3= tree.jetElf[3]
            jetMuf_0= tree.jetMuf[0]
            jetMuf_1= tree.jetMuf[1]
            jetMuf_2= tree.jetMuf[2]
            jetMuf_3= tree.jetMuf[3]  
            jetPtD_0= tree.jetPtD[0]
            jetPtD_1= tree.jetPtD[1]
            jetPtD_2= tree.jetPtD[2]
            jetPtD_3= tree.jetPtD[3]
            jetVtxPt_0= tree.jetVtxPt[0]
            jetVtxPt_1= tree.jetVtxPt[1]
            jetVtxPt_2= tree.jetVtxPt[2]
            jetVtxPt_3= tree.jetVtxPt[3]
            jetVtx3dL_0= tree.jetVtx3dL[0]
            jetVtx3dL_1= tree.jetVtx3dL[1]
            jetVtx3dL_2= tree.jetVtx3dL[2]
            jetVtx3dL_3= tree.jetVtx3dL[3]
            jetVtx3deL_0= tree.jetVtx3deL[0]
            jetVtx3deL_1= tree.jetVtx3deL[1]
            jetVtx3deL_2= tree.jetVtx3deL[2]
            jetVtx3deL_3= tree.jetVtx3deL[3]
            jetVtxMass_0= tree.jetVtxMass[0]
            jetVtxMass_1= tree.jetVtxMass[1]
            jetVtxMass_2= tree.jetVtxMass[2]
            jetVtxMass_3= tree.jetVtxMass[3]
            jetLeadTrkPt_0= tree.jetLeadTrkPt[0]
            jetLeadTrkPt_1= tree.jetLeadTrkPt[1]
            jetLeadTrkPt_2= tree.jetLeadTrkPt[2]
            jetLeadTrkPt_3= tree.jetLeadTrkPt[3]
            jetPtRaw_0= tree.jetPt[0]/tree.jetJec[0]
            jetPtRaw_1= tree.jetPt[1]/tree.jetJec[1]
            jetPtRaw_2= tree.jetPt[2]/tree.jetJec[2]
            jetPtRaw_3= tree.jetPt[3]/tree.jetJec[3]
            jetSoftLepPt_0= tree.jetSoftLepPt[0]
            jetSoftLepPt_1= tree.jetSoftLepPt[1]
            jetSoftLepPt_2= tree.jetSoftLepPt[2]
            jetSoftLepPt_3= tree.jetSoftLepPt[3]
            jetSoftLepPtRel_0= tree.jetSoftLepPtRel[0]
            jetSoftLepPtRel_1= tree.jetSoftLepPtRel[1]
            jetSoftLepPtRel_2= tree.jetSoftLepPtRel[2]
            jetSoftLepPtRel_3= tree.jetSoftLepPtRel[3]
            jetSoftLepDR_0= tree.jetSoftLepDR[0]
            jetSoftLepDR_1= tree.jetSoftLepDR[1]
            jetSoftLepDR_2= tree.jetSoftLepDR[2]
            jetSoftLepDR_3= tree.jetSoftLepDR[3]
            jetPart_0= tree.jetPart[0]
            jetPart_1= tree.jetPart[1]
            jetPart_2= tree.jetPart[2]
            jetPart_3= tree.jetPart[3]
            jetUnc_0= tree.jetUnc[0]
            jetUnc_1= tree.jetUnc[1]
            jetUnc_2= tree.jetUnc[2]
            jetUnc_3= tree.jetUnc[3]
            jetPhi_0= tree.jetPhi[0]
            jetPhi_1= tree.jetPhi[1]
            jetPhi_2= tree.jetPhi[2]
            jetPhi_3= tree.jetPhi[3]
            v0=ROOT.TLorentzVector()
            v0.SetPtEtaPhiM(jetPt_0,jetEta_0,jetPhi_0,tree.jetMass[0]);
            jetMt__0= v0.Mt()
            jetM_0=v0.M()
            jetEt_0= v0.Et()
            v1=ROOT.TLorentzVector()
            v1.SetPtEtaPhiM(jetPt_1,jetEta_1,jetPhi_1,tree.jetMass[1]);
            jetMt__1= v1.Mt()
            jetEt_1= v1.Et()
            jetM_1=v1.M()
            v2=ROOT.TLorentzVector()
            v2.SetPtEtaPhiM(jetPt_2,jetEta_2,jetPhi_2,tree.jetMass[2]);
            jetMt__2= v2.Mt()
            jetEt_2= v2.Et()
            jetM_2=v2.M()
            v3=ROOT.TLorentzVector()
            v3.SetPtEtaPhiM(jetPt_3,jetEta_3,jetPhi_3,tree.jetMass[3]);
            jetMt__3= v3.Mt()
            jetM_3=v3.M()
            jetEt_3= v3.Et()

	




 
            rPt={}	
            for key in regVars:
                    theVars0[key][0] = eval("%s_0" %(key)) #theForms["form_reg_%s_0" %(key)].EvalInstance()
                    theVars1[key][0] =  eval("%s_1" %(key)) #theForms["form_reg_%s_1" %(key)].EvalInstance()
                    theVars2[key][0] =  eval("%s_2" %(key)) #theForms["form_reg_%s_2" %(key)].EvalInstance()
                    theVars3[key][0] = eval("%s_3" %(key))# theForms["form_reg_%s_3" %(key)].EvalInstance()
	    rPt[0] = max(0.0001,readerJet0.EvaluateRegression( "BDT0" )[0])
            rPt[1] = max(0.0001,readerJet1.EvaluateRegression( "BDT1" )[0])
            rPt[2] = max(0.0001,readerJet2.EvaluateRegression( "BDT2" )[0])
            rPt[3] = max(0.0001,readerJet3.EvaluateRegression( "BDT3" )[0])
	    for i in range(0,4):
               hJet_regWeight[i] = rPt[i]/tree.jetPt[i]
               if hJet_regWeight[i] > 5. :
                    print 'warning##########################################'
                    print 'MET %.2f' %(met_0)
                    print 'rho %.2f' %(rho_0)
                    print 'corr  %.2f' %(hJet_regWeight[i])
                    print 'rPt %.2f' %(rPt[i])
                

            
            newtree.Fill()
    del readerJet0
    del readerJet1
    del readerJet2
    del readerJet3     
    del rPt           
    newtree.AutoSave()
    output.Close()
        
