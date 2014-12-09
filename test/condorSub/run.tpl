#!/bin/bash

date

source /uscmst1/prod/sw/cms/bashrc prod
workerNodeDir=`pwd`
echo $workerNodeDir
cd <CMSSW_BASE>
eval `scram runtime -sh`
cd -

#cmsRun miniAOD_test.py outputFile=/eos/uscms/store/user/awhitbe1/13TeVGJetsStudies/<SAMPLE>_<INDEX> files=<FILELIST>
cmsRun fatJetStudies.py outputFile=/eos/uscms/store/user/awhitbe1/SuSySubstructureAnalysisNtuples_V11/<SAMPLE>_<INDEX> files=<FILELIST>

