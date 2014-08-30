#!/bin/bash

date

source /uscmst1/prod/sw/cms/bashrc prod
workerNodeDir=`pwd`
echo $workerNodeDir
cd <CMSSW_BASE>
eval `scram runtime -sh`
cd -

cmsRun SuSySubstructureAnalysis_withRA2baseline.py outputFile=<SAMPLE>_<INDEX> applySUSYfilter=False files=<FILELIST>

