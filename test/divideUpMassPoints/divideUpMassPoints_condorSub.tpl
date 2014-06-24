universe = vanilla
Executable            = runDivideUpMassPoints_<SAMPLE>_<INDEX>.sh
Requirements          = Memory >= 199 &&OpSys == "LINUX"&& (Arch != "DUMMY" )&& Disk > 1000000
Should_Transfer_Files = YES
transfer_input_files=/uscms_data/d2/awhitbe1/workArea/RA2studies/CMSSW_5_3_8_patch1/src/AWhitbeck/SuSySubstructure/test/divideUpMassPoints/divideUpMassPoints.py, /uscms_data/d2/awhitbe1/workArea/RA2studies/CMSSW_5_3_8_patch1/src/AWhitbeck/SuSySubstructure/test/divideUpMassPoints/runDivideUpMassPoints_<SAMPLE>_<INDEX>.sh
WhenToTransferOutput  = ON_EXIT_OR_EVICT
Output = out_<SAMPLE>_<INDEX>_$(Cluster).stdout
Error  = out_<SAMPLE>_<INDEX>_$(Cluster).stderr
Log    = out_<SAMPLE>_<INDEX>_$(Cluster).log
Notification    = Error
notify_user     = awhitbe1@FNAL.GOV
Queue 1
