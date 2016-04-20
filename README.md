setenv SCRAM_ARCH slc6_amd64_gcc491

cmsrel CMSSW_7_4_16_patch2

cd CMSSW_7_4_16_patch2/src/

cmsenv

git cms-init

git cms-merge-topic dmajumder:CMSSW_7_4_X_AnalysisDataFormats_BoostedObjects

git clone git@github.com:dmajumder/EventCounter.git Analysis/EventCounter 

git clone -b Data2015D  git@github.com:skhalil/VLQAna.git  Analysis/VLQAna

#Copy one new MET file from local directory

cp /uscms_data/d2/skhalil/MyVLQAna/CMSSW_7_4_16_patch2/src/AnalysisDataFormats/BoostedObjects/interface/Met.h /AnalysisDataFormats/BoostedObjects/interface
 
#To just build this stuff
scram b -j4

# To run on OS2L analysis
cd Analysis/VLQAna/test

cmsRun os2lana_cfg.py

# To run crab jobs on B2GEDMNtuples

Analysis/VLQAna/test/CRAB_On_B2GEDM

Modify the input parameters in allJobList.py, by changing the relvant parameters, like config.General.requestName, config.Data.inputDataset, config.Data.outLFNDirBase, config.Site.storageSite etc. Enable new options of optimizeReco when needed for MC. Finally, generate and submit a crab jobs.

Python run.py

Please see more details https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial for CRAB3 related issues.

