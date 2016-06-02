setenv SCRAM_ARCH slc6_amd64_gcc493


cmsrel CMSSW_7_6_5

cd CMSSW_7_6_5/src/

cmsenv

git cms-init

git cms-merge-topic dmajumder:CMSSW_7_6_X_AnalysisDataFormats_BoostedObjects

git clone git@github.com:dmajumder/EventCounter.git Analysis/EventCounter 

git clone -b CMSSW_7_6_X git@github.com:tmitchel/VLQAna.git Analysis/VLQAna  

 
#To just build this stuff
scram b -j20

# To run on OS2L analysis
cd Analysis/VLQAna/test

cmsRun os2lana_cfg.py

# To run crab jobs for B2GEDM Ntuples

Analysis/VLQAna/test/CRAB_B2G/ 

# make sure rab_dummy_os2lana.py is correct, and appropriate paths to allJobList.py, changle line 89 in run.py (comment 113 to get config file without submitting)
# to run using crab
python run.py --options

This will create an output condor directory, through which you can check the status of the jobs.

crab status -d MY_CONDOR_DIR

# To run condor jobs for B2GEDM Ntuples

Analysis/VLQAna/test/Condor/<appropriate masspoint if relevant>
More to come....

Please see more details https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial.
