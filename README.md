setenv SCRAM_ARCH slc6_amd64_gcc491

cmsrel CMSSW_7_4_12
cd CMSSW_7_4_12/src/
cmsenv

git cms-init
git cms-merge-topic dmajumder:CMSSW_7_4_X_AnalysisDataFormats_BoostedObjects
git clone git://github.com/dmajumder/EventCounter.git Analysis/EventCounter 
git clone https://github.com/skhalil/VLQAna.git Analysis/VLQAna  

#To just build this stuff
cd Analysis/VLQAna
scram b -j20

#To run OS2L analysis 
cmsRun os2lana_cfg.py

#To run crab jobs for skims, e.g for CR in dielrcton channel
Analysis/VLQAna/test/Skim/CRAB/Skims_CR_Zelel 

Modify the crab_DY50_HT_100to200.py file to the MC you want to skim, and change the relvant parameters, like config.General.requestName, config.Data.inputDataset, config.Data.outLFNDirBase, config.Site.storageSite etc.

cmsRun crab_XX.py
