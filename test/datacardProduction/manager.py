import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--submit", dest="submit",default=False,action="store_true",
		                    help="submit jobs to condor, if false, run interactively", metavar="SUBMIT")

parser.add_option("-n", "--name", dest="sample",default="T1tttt",
                  help="name of directory that files are taken from", metavar="NAME")

parser.add_option("--mGluino", dest="mGluino", default = 1025,
		  help="mass of gluionos", metavar="MGLUINO")

parser.add_option("--mLSP", dest="mLSP", default = 25,
		  help="mass of LSP", metavar="MLSP")

parser.add_option("--binning", dest="binning", default="Classic",
		  help="Select binning to be used: Classic, SMJ, extSMJ", metavar="binning")

parser.add_option("-a","--all", dest="all", default=False, action = "store_true",
		  help="submit all masses for given sample", metavar="ALL")

(options, args) = parser.parse_args()

def submitToCondor(sample, mGluino, mLSP, binning) :

    currentDir = os.getcwd()

    shellScript = """#!/bin/sh 
date 
source /uscmst1/prod/sw/cms/bashrc prod 
workerNodeDir=`pwd`
echo $workerNodeDir 
cd {0}
eval `scram runtime -sh` 
cd - 
python datacardProduction.py -s {1} --mGo {2} --mLSP {3} --binning {4}
""".format(currentDir,sample,mGluino,mLSP,binning)

    condorSubmit = """universe = vanilla
x509userproxy = <PROXY> 
Executable            = runDatacardProduction_{0}_mGo{1}_mLSP{2}_{3}.sh 
Requirements          = Memory >= 199 &&OpSys == "LINUX"&& (Arch != "DUMMY" )&& Disk > 1000000  
Should_Transfer_Files = YES 
transfer_input_files=runDatacardProduction_{0}_mGo{1}_mLSP{2}_{3}.sh,datacardProduction.py,binning.py, datacard.py, sumJetMassBinning.py, extendedSumJetMassBinning.py, gluinoXsec.py
WhenToTransferOutput  = ON_EXIT_OR_EVICT 
Output = out_{0}_mGo{1}_mLSP{2}_{3}_$(Cluster).stdout 
Error  = out_{0}_mGo{1}_mLSP{2}_{3}_$(Cluster).stderr 
Log    = out_{0}_mGo{1}_mLSP{2}_{3}_$(Cluster).log 
Notification    = Error 
notify_user     = awhitbe1@FNAL.GOV  
Queue 1 \n
""".format(sample,mGluino,mLSP,binning)

    print shellScript
    print condorSubmit
    print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

    shellFile = open("runDatacardProduction_{0}_mGo{1}_mLSP{2}_{3}.sh".format(sample,mGluino,mLSP,binning) , 'w' )
    shellFile.write(shellScript)
    shellFile.close()
    condorFile = open("condorSub_{0}_mGo{1}_mLSP{2}_{3}".format(sample,mGluino,mLSP,binning) , 'w' )
    condorFile.write(condorSubmit)
    condorFile.close()

    #get grid proxy
    #os.system("voms-proxy-init")
    os.system("sed -i 's|<PROXY>|'`voms-proxy-info -path`'|g' condorSub_{0}_mGo{1}_mLSP{2}_{3}".format(sample,mGluino,mLSP,binning))

    #submit
    os.system("condor_submit condorSub_{0}_mGo{1}_mLSP{2}_{3}".format(sample,mGluino,mLSP,binning) )


def submitAll(name = "T1tttt") :

    if name == "T1tttt" :
        massList = []
        for mGluino in range(400,775,50) :
            for mLSP in range(25,mGluino-175,50) :
                print "gluino:",mGluino,"LSP:",mLSP
                submitToCondor(name,mGluino,mLSP,options.binning)
        for mGluino in range(775,1100,50) :
            for mLSP in range(25,mGluino-175,50) :
                print "gluino:",mGluino,"LSP:",mLSP
                submitToCondor(name,mGluino,mLSP,options.binning)
        for mGluino in range(1100,1425,50) :
            for mLSP in range(25,mGluino-175,50) :
                print "gluino:",mGluino,"LSP:",mLSP
                submitToCondor(name,mGluino,mLSP,options.binning)
                
    else :
        raise NameError(name)
        return

    
    
def main() :

    os.system("cmsenv")

    if options.all :
        submitAll(options.sample)
    elif options.submit :
        submitToCondor(options.sample,options.mGluino,options.mLSP,options.binning)
    else :
        os.system("python datacardProduction.py -s {0} --mGo {1} --mLSP {2} --binning {3}".format(options.sample,options.mGluino,options.mLSP,options.binning) )
        
if __name__ == "__main__":
        main()
        
