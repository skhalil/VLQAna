#!/bin/bash                                                                                                                                                                                                                                                                                                                                                                                                                       

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /uscms_data/d3/tmitchel/Analysis2016/CMSSW_7_4_16_patch2/src
eval `scram runtime -sh`

cd ${_CONDOR_SCRATCH_DIR}
echo ${_CONDOR_SCRATCH_DIR}
let "sample=${1}+1"
cp /uscms_data/d3/tmitchel/Analysis2016/CMSSW_7_4_16_patch2/src/Analysis/VLQAna/test/Condor/vlqMass800/dy_HT400-600/dy_HT400-600_${sample}.py .
cp /uscms_data/d3/tmitchel/Analysis2016/CMSSW_7_4_16_patch2/src/Analysis/VLQAna/test/*.txt .
cp /uscms_data/d3/tmitchel/Analysis2016/CMSSW_7_4_16_patch2/src/Analysis/VLQAna/test/*.root .
cp /uscms_data/d3/tmitchel/Analysis2016/CMSSW_7_4_16_patch2/src/Analysis/VLQAna/test/inputFiles_cfi.py .
cmsRun dy_HT400-600_${sample}.py
rm PU*
rm Run*
rm dataset*
rm hnpv*
rm os2lana*
xrdcp *.root root://cmseos.fnal.gov//store/user/tmitchel/condor/dy_HT400-600
rm dy_HT400-600_${sample}.py
rm *.root
ls
echo "DONE!"