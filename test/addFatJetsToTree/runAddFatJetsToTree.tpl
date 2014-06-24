#!/bin/sh

date

source /uscmst1/prod/sw/cms/bashrc prod
workerNodeDir=`pwd`
echo $workerNodeDir
cd /uscms_data/d2/awhitbe1/workArea/RA2studies/gitTop/CMSSW_5_3_8_patch1/src/AWhitbeck/SuSySubstructure/test/addFatJetsToTree/
eval `scram runtime -sh`
cd -

./addFatJetsToTree.exe /eos/uscms/store/user/awhitbe1/RA2nTuple/29May2014_SignalTree_SMS_MG_T5tttt/  /eos/uscms/store/user/awhitbe1/RA2nTupleExtension/29May2014_SignalTree_SMS_MG_T5tttt/ <FILE> RA2TreeMaker/RA2PreSelection
