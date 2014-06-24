from ROOT import TFile, TTree



fileName = "/uscms/home/awhitbe1/eos/RA2nTupleExtension/29May2014_SignalTree_SMS_MG_T5tttt/scanTree_T5tttt_287_1_7NQ_withFatJets.root"
treeName = "RA2PreSelection"

f = TFile(fileName,"READ")
t = f.Get(treeName)

t->Draw("HT")