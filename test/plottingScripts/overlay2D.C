#include "stackedBackground_2D.C"
#include "TDirectory.h"


void overlay2D(char* draw = "sumJetMass:HT" , 
	       char* cut = "HT>500&&MHT>100&&NJets>5&&NJets<8"){

  TH2F* bkg = stackedBackground_2D(draw,cut,40,500,3500,40,0,2500);

  bkg->Scale(1./bkg->Integral());

  TChain* t = new TChain("TreeFiller/AnalysisTree");
  t->Add("~/eos/SuSySubstructureAnalysisNtuples_V8/T1qqqq_HiddenValley_SumJetMass_AnalysisTree.root");

  t->SetAlias("JetsPt","pt_patJetsAK5PFPt50Eta25") ; 
  t->SetAlias("JetsEta","eta_patJetsAK5PFPt50Eta25") ; 
  t->SetAlias("JetsPhi","phi_patJetsAK5PFPt50Eta25") ; 
  t->SetAlias("dPhiRaw","JetsPhi[0]-JetsPhi[1]");
  t->SetAlias("dPhi","(dPhiRaw<-3.1415)*(dPhiRaw+2*3.1415)+(dPhiRaw>3.1415)*(dPhiRaw-2*3.1415)+(dPhiRaw<=3.1415&&dPhiRaw>=-3.1415)*(dPhiRaw)");		
  t->SetAlias("dPhiRaw","JetsPhi[0] - JetsPhi[1]") ; 
  t->SetAlias("HT","HT_patJetsAK5PFPt50Eta25") ; 
  t->SetAlias("MHT","MHT_patJetsAK5PFPt30") ; 
  t->SetAlias("NJets","NJets_patJetsAK5PFPt50Eta25") ; 
  t->SetAlias("sumJetMass","sumJetMass_fattenedJets") ; 
  t->SetAlias("DeltaPhi1","abs(JetsPhi[0]-MHTphi_patJetsAK5PFPt30)");
  t->SetAlias("DeltaPhi2","abs(JetsPhi[1]-MHTphi_patJetsAK5PFPt30)");
  t->SetAlias("DeltaPhi3","abs(JetsPhi[2]-MHTphi_patJetsAK5PFPt30)");
  
  char signalDrawString[256];
  sprintf(signalDrawString,"%s>>sig(40,500,3500,40,0,2500)",draw);

  t->Draw(signalDrawString,cut);

  bkg->Draw("box");
  bkg->GetXaxis()->SetTitle("H_{T} [GeV]");
  bkg->GetYaxis()->SetTitle("#Sigma m_{j} [GeV]");
  TH2F* sig = (TH2F*) gDirectory->Get("sig");
  sig->Scale(1./sig->Integral());
  sig->Draw("samebox");

}
