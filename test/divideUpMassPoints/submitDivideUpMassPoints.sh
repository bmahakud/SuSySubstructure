
#for i in $(ls ~/eos/RA2nTuple/) 
#  do
#
#  n=0
#  while [ n -lt ]
#  echo $i
#  sed -e 's|<DIR>|'$i'|' -e 's|<START>||'< runDivideUpMassPoints.tpl > runDivideUpMassPoints_$i.sh
#  chmod u+x runDivideUpMassPoints_$i.sh
#  sed -e 's|<DIR>|'$i'|' < runDivideUpMassPoints_condorSub.tpl > runDivideUpMassPoints_condorSub_$i

#  condor_submit runDivideUpMassPoints_condorSub_$i

#done


###############

import os

dirList = 