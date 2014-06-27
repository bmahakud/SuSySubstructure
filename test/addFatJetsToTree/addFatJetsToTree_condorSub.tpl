universe = vanilla
Executable            = runAddFatJetsToTree_<SAMPLE>_<INDEX>.sh
Requirements          = Memory >= 199 &&OpSys == "LINUX"&& (Arch != "DUMMY" )&& Disk > 1000000
Should_Transfer_Files = YES
transfer_input_files=addFatJetsToTree.exe, runAddFatJetsToTree_<SAMPLE>_<INDEX>.sh, divideUpMassPoints.py
WhenToTransferOutput  = ON_EXIT_OR_EVICT
Output = out_<SAMPLE>_<INDEX>_$(Cluster).stdout
Error  = out_<SAMPLE>_<INDEX>_$(Cluster).stderr
Log    = out_<SAMPLE>_<INDEX>_$(Cluster).log
Notification    = Error
notify_user     = awhitbe1@FNAL.GOV
Queue 1
