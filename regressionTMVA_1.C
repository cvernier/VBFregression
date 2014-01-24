#include "TFile.h"
#include "TTree.h"
#include "TCut.h"
#include "TMVA/Factory.h"
using namespace TMVA;
void regressionTMVA_1()
{
  TFile *inf = TFile::Open("SignalRegressionTrain.root");
  TTree *tr  = (TTree*)inf->Get("jets");
  
  TFile *outf = new TFile("regressionTMVANewGenJets3_1.root","RECREATE");
  TMVA::Factory* factory = new TMVA::Factory("factoryJetRegNewGenJets3",outf,"!V:!Silent:Color:DrawProgressBar:AnalysisType=Regression");
(TMVA::gConfig().GetIONames()).fWeightFileDir = "weightDirectory_1";
  factory->AddRegressionTree(tr);
  
  factory->AddVariable("jetBtag"   ,'F');
  factory->AddVariable("jetPtRaw"     ,'F');
  factory->AddVariable("jetPt"    ,'F');
  factory->AddVariable("jetEta"    ,'F');
  factory->AddVariable("jetMt_"    ,'F');
  factory->AddVariable("jetUnc"    ,'F');
  factory->AddVariable("jetMetPhi" ,'F');
  factory->AddVariable("jetLeadTrkPt" ,'F');
  factory->AddVariable("jetChf"    ,'F');
  factory->AddVariable("jetPhf"    ,'F');
  factory->AddVariable("jetNhf"    ,'F');
  factory->AddVariable("jetElf"    ,'F');
  factory->AddVariable("jetMuf"    ,'F');
  factory->AddVariable("jetPtD"    ,'F');
//  factory->AddVariable("jetVtxPt"  ,'F');
  factory->AddVariable("jetVtx3dL" ,'F');
  factory->AddVariable("jetVtx3deL",'F');
  factory->AddVariable("jetVtxMass"  ,'F');
  factory->AddVariable("jetSoftLepPt" ,'F');
  factory->AddVariable("jetSoftLepPtRel",'F');
  factory->AddVariable("jetSoftLepDR",'F');
  factory->AddVariable("met"       ,'F');
  factory->AddVariable("rho"       ,'F');
  factory->AddVariable("jetPart"       ,'I');
  factory->AddVariable("jetEt"      ,'F');
  
  factory->AddTarget("jetGenPt");
    
  TCut preselectionCut("jetGenDR<0.25 && jetPrtDR<0.25 && abs(jetPrtId)==5 && jetPt>30 && jetSoftLepPt <200. && abs(jetSoftLepSigDB3D)<20");  
//TCut preselectionCut("jetPrtDR<0.25 && abs(jetPrtId)==5");

  factory->PrepareTrainingAndTestTree(preselectionCut,"nTrain_Regression=0:nTest_Regression=0");
//  factory->BookMethod(TMVA::Types::kMLP,"MLP","NCycles=700:HiddenLayers=N,N-1:TestRate=5:TrainingMethod=BFGS:VarTRansform=Norm");
  //factory->BookMethod(TMVA::Types::kMLP,"MLP","NCycles=700:HiddenLayers=N,N+1:TestRate=5:TrainingMethod=BFGS:VarTRansform=Norm");
  //factory->BookMethod(TMVA::Types::kBDT,"BDT","NTrees=200:nCuts=25");  
    factory->BookMethod(TMVA::Types::kBDT,"BDT","NTrees=100:nEventsMin=5:BoostType=AdaBoostR2:SeparationType=RegressionVariance:nCuts=20:PruneMethod=CostComplexity:PruneStrength=30");//NTrees=200:nCuts=25");  

  factory->TrainAllMethods();
  factory->TestAllMethods();
  factory->EvaluateAllMethods(); 
}
