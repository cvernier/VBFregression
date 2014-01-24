#include <iostream>
#include "TString.h"
#include "TH1F.h"
#include "TTree.h"
#include "TFile.h"
#include "TMath.h"
#include "TLorentzVector.h"
#include <vector>
using std::cin;
using std::cout;
using std::endl;

void CreateRegressionTMVATree()
{
  TFile *inf   = TFile::Open("flatTree_forRegression.root");//flatTree_VBFPowheg125-NewGenjets.root");//flatTree_VBFPowheg125.root");
  TFile *outf  = new TFile("SignalRegressionTrainNewGenJets.root","RECREATE");
  TTree *trIN  = (TTree*)inf->Get("Hbb/events");
  TTree *trOUT = new TTree("jets","jets");
  vector<int> *btagIdx(0),*jetPart(0), *blikNOMIdx(0);
  int  b1[4], b2[4];
  int nvtx;
  vector<float> *jetPtD(0),*jetPt(0),*jetJec(0),*jetEta(0),*jetPhi(0),*jetMass(0),*jetBtag(0),*jetChf(0),*jetNhf(0),*jetPhf(0),*jetElf(0),*jetMuf(0),*jetVtxPt(0),*jetVtx3dL(0),*jetVtx3deL(0), *jetVtxMass(0), *jetSoftLepPt(0), *jetSoftLepPtRel(0), *jetSoftLepDR(0), *jetLeadTrkPt(0), *jetUnc(0), *jetSoftLepSigDB3D(0), *jetEnergy(0);
  float dEtaqq[4], mqq[4], dPhibb[4];
  vector<bool> *triggerResult(0);
  float met,metPhi,rho;
  vector<float> *genjetPt(0),*genjetEta(0),*genjetPhi(0),*genjetE(0),*partonPt(0),*partonEta(0),*partonPhi(0),*partonE(0);
  vector<int>   *partonId(0);
  int nvtx_,jetPart_;
  float jetPtD_,jetPt_,jetPtRaw_,jetE_,jetEta_,jetPhi_,jetMetPhi_,jetMass_,jetChf_,jetNhf_,jetPhf_,jetElf_,jetMuf_,jetUnc_,jetEt_, jetMt_, jetM_,
        jetBtag_,jetVtxPt_,jetVtx3dL_,jetVtx3deL_,
        jetGenDR_,jetGenR_,jetGenPt_,jetGenE_,jetPrtDR_,jetPrtR_,jetPrtPt_,jetPrtE_, jetLeadTrkPt_, jetJec_, jetVtxMass_, jetSoftLepPt_, jetSoftLepPtRel_, jetSoftLepDR_, jetSoftLepSigDB3D_;
  int   jetPrtId_;
  float met_,metPhi_,rho_;
 
  //------- input tree --------------
  
  trIN->SetBranchAddress("jetPt"     ,&jetPt);
  trIN->SetBranchAddress("jetPtD"    ,&jetPtD);
  trIN->SetBranchAddress("jetEta"    ,&jetEta);
  trIN->SetBranchAddress("jetEnergy"    ,&jetEnergy); 
  trIN->SetBranchAddress("jetPhi"    ,&jetPhi);
  trIN->SetBranchAddress("jetMass"   ,&jetMass);
  trIN->SetBranchAddress("jetBtag"   ,&jetBtag);
  trIN->SetBranchAddress("jetJec"    ,&jetJec);
  trIN->SetBranchAddress("jetUnc"    ,&jetUnc);
  trIN->SetBranchAddress("jetChf"    ,&jetChf);
  trIN->SetBranchAddress("jetNhf"    ,&jetNhf);
  trIN->SetBranchAddress("jetPhf"    ,&jetPhf);
  trIN->SetBranchAddress("jetElf"    ,&jetElf);
  trIN->SetBranchAddress("jetMuf"    ,&jetMuf);
  trIN->SetBranchAddress("jetPart"   ,&jetPart);
  trIN->SetBranchAddress("jetVtxPt"  ,&jetVtxPt);
  trIN->SetBranchAddress("jetVtx3dL" ,&jetVtx3dL);
  trIN->SetBranchAddress("jetVtx3deL",&jetVtx3deL);
  trIN->SetBranchAddress("btagIdx"   ,&btagIdx);
  trIN->SetBranchAddress("b1"   ,&b1);
  trIN->SetBranchAddress("b2"   ,&b2);
  trIN->SetBranchAddress("met"       ,&met);
  trIN->SetBranchAddress("metPhi"    ,&metPhi);
  trIN->SetBranchAddress("nvtx"      ,&nvtx);
  trIN->SetBranchAddress("rho"       ,&rho);
  trIN->SetBranchAddress("genjetPt"  ,&genjetPt);
  trIN->SetBranchAddress("genjetEta" ,&genjetEta);
  trIN->SetBranchAddress("genjetPhi" ,&genjetPhi);
  trIN->SetBranchAddress("genjetE"   ,&genjetE);
  trIN->SetBranchAddress("partonPt"  ,&partonPt);
  trIN->SetBranchAddress("partonEta" ,&partonEta);
  trIN->SetBranchAddress("partonPhi" ,&partonPhi);
  trIN->SetBranchAddress("partonE"   ,&partonE);
  trIN->SetBranchAddress("partonId"  ,&partonId);
  trIN->SetBranchAddress("jetLeadTrkPt", &jetLeadTrkPt);
  trIN->SetBranchAddress("jetVtxMass"  ,&jetVtxMass);
  trIN->SetBranchAddress("jetSoftLepPt"  ,&jetSoftLepPt);
  trIN->SetBranchAddress("jetSoftLepPtRel"  ,&jetSoftLepPtRel);
  trIN->SetBranchAddress("jetSoftLepDR"  ,&jetSoftLepDR);
  trIN->SetBranchAddress("jetSoftLepSigDB3D"  ,&jetSoftLepSigDB3D);
  trIN->SetBranchAddress("triggerResult",&triggerResult);
  trIN->SetBranchAddress("dEtaqq",&dEtaqq);
  trIN->SetBranchAddress("dPhibb",&dPhibb);
  trIN->SetBranchAddress("mqq",&mqq);
 //------- output tree --------------
  trOUT->Branch("jetE"      ,&jetE_       ,"jetE_/F");
  trOUT->Branch("jetEt"      ,&jetEt_       ,"jetEt_/F");
  trOUT->Branch("jetMt_"      ,&jetMt_       ,"jetMt_/F");
  trOUT->Branch("jetM"      ,&jetM_       ,"jetM_/F");
  trOUT->Branch("jetPt"     ,&jetPt_      ,"jetPt_/F");
  trOUT->Branch("jetPtRaw"  ,&jetPtRaw_   ,"jetPtRaw_/F");
  trOUT->Branch("jetPtD"    ,&jetPtD_     ,"jetPtD_/F");
  trOUT->Branch("jetEta"    ,&jetEta_     ,"jetEta_/F");
  trOUT->Branch("jetPhi"    ,&jetPhi_     ,"jetPhi_/F");
  trOUT->Branch("jetMetPhi" ,&jetMetPhi_  ,"jetMetPhi_/F");
  trOUT->Branch("jetMass"   ,&jetMass_    ,"jetMass_/F");
  trOUT->Branch("jetBtag"   ,&jetBtag_    ,"jetBtag_/F");
  trOUT->Branch("jetChf"    ,&jetChf_     ,"jetChf_/F");
  trOUT->Branch("jetNhf"    ,&jetNhf_     ,"jetNhf_/F");
  trOUT->Branch("jetPhf"    ,&jetPhf_     ,"jetPhf_/F");
  trOUT->Branch("jetElf"    ,&jetElf_     ,"jetElf_/F");
  trOUT->Branch("jetMuf"    ,&jetMuf_     ,"jetMuf_/F");
  trOUT->Branch("jetPart"   ,&jetPart_    ,"jetPart_/I");
  trOUT->Branch("jetGenDR"  ,&jetGenDR_   ,"jetGenDR_/F");
  trOUT->Branch("jetGenPt"  ,&jetGenPt_   ,"jetGenPt_/F");
  trOUT->Branch("jetGenE"   ,&jetGenE_    ,"jetGenE_/F");
  trOUT->Branch("jetGenR"   ,&jetGenR_    ,"jetGenR_/F");
  trOUT->Branch("jetPrtId"  ,&jetPrtId_   ,"jetPrtId_/I");
  trOUT->Branch("jetPrtDR"  ,&jetPrtDR_   ,"jetPrtDR_/F");
  trOUT->Branch("jetPrtPt"  ,&jetPrtPt_   ,"jetPrtPt_/F");
  trOUT->Branch("jetPrtE"   ,&jetPrtE_    ,"jetPrtE_/F");
  trOUT->Branch("jetPrtR"   ,&jetPrtR_    ,"jetPrtR_/F");
  trOUT->Branch("jetVtxPt"  ,&jetVtxPt_   ,"jetVtxPt_/F");
  trOUT->Branch("jetVtx3dL" ,&jetVtx3dL_  ,"jetVtx3dL_/F");
  trOUT->Branch("jetVtx3deL",&jetVtx3deL_ ,"jetVtx3deL_/F");
  trOUT->Branch("nvtx"      ,&nvtx_       ,"nvtx_/I");
  trOUT->Branch("rho"       ,&rho_        ,"rho_/F");
  trOUT->Branch("met"       ,&met_        ,"met_/F");
  trOUT->Branch("metPhi"    ,&metPhi_     ,"metPhi_/F");
  trOUT->Branch("jetLeadTrkPt", &jetLeadTrkPt_, "jetLeadTrkPt_/F");
  trOUT->Branch("jetJec", &jetJec_, "jetJec_/F");
  trOUT->Branch("jetVtxMass"  ,&jetVtxMass_, "jetVtxMass_/F");
  trOUT->Branch("jetUnc"  ,&jetUnc_,"jetUnc_/F");
  trOUT->Branch("jetSoftLepPt"  ,&jetSoftLepPt_,"jetSoftLepPt_/F");
  trOUT->Branch("jetSoftLepPtRel"  ,&jetSoftLepPtRel_, "jetSoftLepPtRel_/F");
  trOUT->Branch("jetSoftLepDR"  ,&jetSoftLepDR_, "jetSoftLepDR_/F");
  trOUT->Branch("jetSoftLepSigDB3D"  ,&jetSoftLepSigDB3D_, "jetSoftLepSigDB3D_/F");

  int decade(0);
  int NN = trIN->GetEntries();
  cout<<"Reading "<<NN<<" entries"<<endl;
  TLorentzVector v(0,0,0,0);
  for(int iev=0;iev<NN;iev++) {
    double progress = 10.0*iev/(1.0*NN);
    int k = TMath::FloorNint(progress); 
    if (k > decade) 
      cout<<10*k<<" %"<<endl;
    decade = k; 
    trIN->GetEntry(iev);   
    //nominal if(((*triggerResult)[9] && mqq[2]>1000 && dPhibb[2]<2.0 && dEtaqq[2]>2.5 )){
    {
    //vbf if(((*triggerResult)[0]||(*triggerResult)[1])&&dEtaqq[1]>2.5&&mqq[1]>250.&&dPhibb[1]<2.0){
    rho_     = rho;
    nvtx_    = nvtx;
    met_     = met;
    metPhi_  = metPhi;
    for(unsigned j=0;j<2;j++) {
      int ib =(*btagIdx)[j];
      jetPt_      = (*jetPt)[ib];
      jetUnc_   = (*jetUnc)[ib];
      jetPtRaw_   = (*jetPt)[ib]/(*jetJec)[ib];
      jetPtD_     = (*jetPtD)[ib];
      jetPart_    = (*jetPart)[ib];
      jetEta_     = (*jetEta)[ib];
      jetPhi_     = (*jetPhi)[ib];
      float tmpPhi = fabs((*jetPhi)[ib]-metPhi);
      if (tmpPhi > 3.14159) {
        tmpPhi = 2*3.14159-tmpPhi;
      }
      jetMetPhi_  = tmpPhi;
      jetMass_    = (*jetMass)[ib];
      v.SetPtEtaPhiM(jetPt_,jetEta_,jetPhi_,jetMass_);
      jetE_       =v.E();// (*jetEnergy)[ib];
      jetEt_      =v.Et();
      jetMt_      =v.Mt();
      jetM_      =jetMass_;
      jetBtag_    = (*jetBtag)[ib];
      jetChf_     = (*jetChf)[ib];
      jetNhf_     = (*jetNhf)[ib];
      jetPhf_     = (*jetPhf)[ib];
      jetElf_     = (*jetElf)[ib];
      jetMuf_     = (*jetMuf)[ib];
      jetVtxPt_   = (*jetVtxPt)[ib]; 
      jetVtx3dL_  = (*jetVtx3dL)[ib];
      jetVtx3deL_ = (*jetVtx3deL)[ib];
      jetVtxMass_ = (*jetVtxMass)[ib];
      jetLeadTrkPt_ = (*jetLeadTrkPt)[ib];
      jetSoftLepPt_ = (*jetSoftLepPt)[ib];
      jetSoftLepPtRel_ = (*jetSoftLepPtRel)[ib];
      jetSoftLepDR_ = (*jetSoftLepDR)[ib];      
      jetSoftLepSigDB3D_ = (*jetSoftLepSigDB3D)[ib];
      // ---- loop over the genjets ----------------
      float dR_MIN = 100;
      for(unsigned int i=0;i<genjetPt->size();i++) {
        float pt  = (*genjetPt)[i];
        float eta = (*genjetEta)[i];
        float phi = (*genjetPhi)[i];
        float e   = (*genjetE)[i];
        float dR = sqrt(pow((*jetEta)[ib]-eta,2)+pow((*jetPhi)[ib]-phi,2));
        if (dR < dR_MIN) {
          jetGenDR_  = dR;
          jetGenPt_  = pt;
          jetGenE_   = e;
          jetGenR_   = jetPt_/pt;
          dR_MIN     = dR;
        }
      }// gen loop
      // ---- loop over the partons ----------------
      dR_MIN = 100;
      for(unsigned int i=0;i<partonPt->size();i++) {
        float pt  = (*partonPt)[i];
        float eta = (*partonEta)[i];
        float phi = (*partonPhi)[i];
        float e   = (*partonE)[i];
        int id    = (*partonId)[i];
        float dR  = sqrt(pow((*jetEta)[ib]-eta,2)+pow((*jetPhi)[ib]-phi,2));
        if (dR < dR_MIN) {
          jetPrtId_  = id;
          jetPrtDR_  = dR;
          jetPrtPt_  = pt;
          jetPrtE_   = e;
          jetPrtR_   = jetPt_/pt;
          dR_MIN     = dR;
        }
      }// parton loop
      trOUT->Fill();
    }// jet loop
  }
}
  outf->cd();
  trOUT->Write();
  outf->Close();
  inf->Close();
}























