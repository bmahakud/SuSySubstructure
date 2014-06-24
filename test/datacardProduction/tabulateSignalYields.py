from os import listdir
from os.path import isfile, join
from ROOT import TChain, TH2F, TFile, TTree

t = TChain("RA2PreSelection")

T1ttttFileNames = []

sigDir = "/eos/uscms/store/user/awhitbe1/RA2nTupleExtension/"

T1ttttFileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV/")
T1ttttFileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_25to550_8TeV/")
T1ttttFileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_25to500_8TeV/")
T1ttttFileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_525to875_8TeV/")
T1ttttFileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV/")
T1ttttFileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_525to1000_8TeV_V2/")
T1ttttFileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV/")
T1ttttFileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_800to1400_mLSP_1_8TeV/")

T5VVfileNames = []

T5VVfileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_800to1100_mLSP_25to525_8TeV/")
T5VVfileNames.append(sigDir+"19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_800to1100_mLSP_575to875_8TeV/")

T5ttttFileNames = []

T5ttttFileNames.append(sigDir+"29May2014_SignalTree_SMS_MG_T5tttt/")

sigYields = {}

for dir in T1ttttFileNames :

    onlyfiles = [ f for f in listdir(dir) if isfile(join(dir,f)) ]

    for f in onlyfiles : 

        print f
        rootFile = TFile(dir+"/"+f,"READ")
        rootTree = rootFile.Get("RA2PreSelection")

        if rootTree == None :
            continue
        
        for iEvt in range(rootTree.GetEntries()) :

            print iEvt

            rootTree.GetEntry(iEvt)

            histoKey = "massMom{0}_massDau{1}".format(rootTree.massMom,rootTree.massDau)
            print histoKey
            if histoKey in sigYields :
                sigYields[histoKey].Fill(rootTree.MHT,rootTree.HT)
            else :
                sigYields[histoKey] = TH2F("sigYields_mGo{0}_mLSP{1}".format(rootTree.massMom,rootTree.massDau),"sigYields_mGo{0}_mLSP{1}".format(rootTree.massMom,rootTree.massDau),8,200,600,20,500,1500)
                sigYields[histoKey].Fill(rootTree.MHT,rootTree.HT)
                     
outputFile = TFile("tesrootTree.root","RECREATE")

for key in sigYields :
    sigYields[key].Write()


outputFile.Close()

