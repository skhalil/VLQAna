#!/bin/bash                                                                                                                                                                                                                                                                                                                                                                                                                                                             

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/
eval `scram runtime -sh`

cd ${_CONDOR_SCRATCH_DIR}
echo ${_CONDOR_SCRATCH_DIR}
let "sample=${1}+1"
cp /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Condor/vlqMass1200/tprime1200/tprime1200_${sample}.py .
cp /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/*.txt .
cp /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/*.root .
cp /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/inputFiles_cfi.py .
cmsRun tprime1200_${sample}.py
rm btag-eff-subjet.root
rm PU*
rm scale*
rm Run*
rm dataset*
rm os2lana*
xrdcp *.root root://cmseos.fnal.gov//store/user/tmitchel/condor/vlqMass1200/tprime1200
rm tprime1200_${sample}.py
rm *.root
ls
echo "DONE!"
