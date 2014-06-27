#!/bin/sh

date

source /uscmst1/prod/sw/cms/bashrc prod
workerNodeDir=`pwd`
echo $workerNodeDir
cd /uscms_data/d2/awhitbe1/workArea/RA2studies/gitTop/CMSSW_5_3_8_patch1/src/AWhitbeck/SuSySubstructure/test/addFatJetsToTree/
eval `scram runtime -sh`
cd -

./addFatJetsToTree.exe /eos/uscms/store/user/lpcsusyhad/SusyRA2Analysis2012/<SAMPLE>/  /eos/uscms/store/user/awhitbe1/RA2nTupleExtension/<SAMPLE>/ <FILE>.root RA2TreeMaker/RA2PreSelection

python divideUpMassPoints.py -d /eos/uscms/store/user/awhitbe1/RA2nTupleExtension/<SAMPLE>/ -o /eos/uscms/store/user/awhitbe1/RA2nTupleExtension/<SAMPLE>/divided/ -f <FILE>_withFatJets.root 