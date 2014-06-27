from os import system
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--submit", dest="submit",default=False,action="store_true",
		                    help="submit jobs to add fat jets to trees and divide up mass points", metavar="SUBMIT")

parser.add_option("-a", "--hadd", dest="hadd",default=False,action="store_true",
		                    help="hadd the various sets of files", metavar="HADD")

parser.add_option("-n", "--name", dest="name",default="",
                  help="name of directory that files are taken from", metavar="NAME")

parser.add_option("-c", "--check", dest="check",default=False,action="store_true",
                  help="check if all jobs finished", metavar="CHECK")

(options, args) = parser.parse_args()

prePath="/eos/uscms/store/user/awhitbe1/RA2nTupleExtension/"

def selectSample(name):

    if name == "T1tttt":

        samples=["19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_25to550_8TeV",
                 "19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_400to750_mLSP_1_8TeV",
                 "19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_525to1000_8TeV_V2",
                 "19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_25to500_8TeV",
                 "19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_1100to1400_mLSP_1025to1200_8TeV",
                 "19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_25to500_8TeV",
                 "19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_775to1075_mLSP_525to875_8TeV",
                 "19June2013_SignalTree_SMS_MG_T1tttt_2J_mGo_800to1400_mLSP_1_8TeV"]

    elif name == "T5VV" :

        samples=["19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_800to1100_mLSP_25to525_8TeV",
                 "19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_800to1100_mLSP_575to875_8TeV",
                 "19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_1150to1400_mLSP_25to525_8TeV",
                 "19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_1150to1400_mLSP_550to700_8TeV",
                 "19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_1150to1400_mLSP_725to850_8TeV",
                 "19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_1150to1400_mLSP_875to1175_8TeV",
                 "19June2013_SignalTree_SMS_MG_T5VV_2J_mGo_400to750_mLSP_25to525_8TeV"]
        
    elif name == "T1qqqq" :
                
        samples=["19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_1050to1100_mLSP_675to1075_8TeV_V2",
                 "19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_1150to1400_mLSP_1025to1375_8TeV",
                 "19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_1150to1400_mLSP_25to675_8TeV_V2",
                 "19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_1150to1400_mLSP_700to850_8TeV_V2",
                 "19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_1150to1400_mLSP_875to1000_8TeV_V2",
                 "19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_400to750_mLSP_25to725_8TeV_V2",
                 "19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_800to1100_mLSP_25to625_8TeV_V2",
                 "19June2013_SignalTree_SMS_MG_T1qqqq_2J_mGo_800to1100_mLSP_675to1075_8TeV_V2"]
    else : 
        raise NameError(name)
        samples = []

    return samples
                
def checkFiles(samList = []) :

    for s in samList :
        system("ls "+prePath+"/"+s+"/divided/*.root | wc -l")
        system("ls "+prePath+"/"+s+"/*.root | wc -l")

def haddFiles(samList = []) :

    for s in samList :
        system("hadd -f "+prePath+"/"+s+"/divided/"+s+".root "+prePath+"/"+s+"/scan*.root")

def submitFatJetJobs(samList = []) :

    for s in samList :

        system("rm "+prePath+"/"+s+"/*root")
        system("rm "+prePath+"/"+s+"/divided/scan*.root")

        system("submitAddFatJetsToTree.py -s "+s)

samples = selectSample(options.name)

if options.submit :
    submitFatJetJobs(samples)

if options.hadd :
    haddFiles(samples)

if options.check :
    checkFiles(samples)


