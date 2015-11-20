import sys
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.register('outFileName', 'os2lana.root',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Output file name"
    )
options.register('doPUReweightingOfficial', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Do pileup reweighting using official recipe"
    )
options.register('doPUReweightingNPV', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Do pileup reweighting based on NPV"
    )
options.register('isData', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Is data?"
    )
options.register('zdecaymode', '',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Z->mumu or Z->elel? Choose: 'zmumu' or 'zelel'"
    )
options.register('filterSignal', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Select only tZtt or bZbZ modes"
    )
options.setDefault('maxEvents', 10)
options.parseArguments()

print options

hltpaths = []
if options.isData:
  options.filterSignal = False 
  if options.zdecaymode == "zmumu":
    hltpaths = [
        #"HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v",
        "HLT_DoubleIsoMu17_eta2p1_v"
        ]
  elif options.zdecaymode == "zelel":
    hltpaths = [
        #"HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v",
        "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v"
        ]
  else:
    sys.exit("Wrong Z decay mode option chosen. Choose either 'zmumu' or 'zelel'") 

process = cms.Process("OS2LAna")

#from inputFiles_cfi import * 

process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
    'root://cms-xrd-global.cern.ch//store/group/phys_b2g/vorobiev/TprimeTprime_M-1000_TuneCUETP8M1_13TeV-madgraph-pythia8/B2GAnaFW_Run2Spring15_25ns_v74x_V61/151004_184150/0000/B2GEDMNtuple_1.root'
    #'root://eoscms.cern.ch//eos/cms/store/group/phys_b2g/B2GAnaFW/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/B2GAnaFW_v74x_v6p1_25ns/150930_172851/0000/B2GEDMNtuple_8.root'
    #fileNamess_TT_M800_Spring15_25ns
    #files_DY_M50
    #files_doubleMuon_Run2015D
    #fileNames_BB_M1000_Spring15_25ns
    #FileNames
    ) 
    )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

process.load("Analysis.VLQAna.EventCleaner_cff") 
process.evtcleaner.isData = options.isData 
process.evtcleaner.hltPaths = cms.vstring (hltpaths)  
process.evtcleaner.DoPUReweightingNPV = cms.bool(options.doPUReweightingNPV)  

from Analysis.VLQAna.OS2LAna_cfi import * 

### Low pt Z candidate with low pt jets 
process.ana = ana.clone(
    filterSignal = cms.bool(options.filterSignal),
    DoPUReweightingNPV = cms.bool(options.doPUReweightingNPV),
    )
process.ana.elselParams.useVID = cms.bool(options.isData)
process.ana.BoostedZCandParams.ptMin = cms.double(0.)
process.ana.jetAK8selParams.jetPtMin = cms.double(100)
process.ana.jetAK4BTaggedselParams.jetPtMin = cms.double(40)


### Boosted Z candidate
process.anaBoosted = ana.clone(
    filterSignal = cms.bool(options.filterSignal),
    DoPUReweightingNPV = cms.bool(options.doPUReweightingNPV),
    )
process.anaBoosted.elselParams.useVID = cms.bool(options.isData)


process.TFileService = cms.Service("TFileService",
       fileName = cms.string(
         options.outFileName
         )
       )

## Event counters
from Analysis.EventCounter.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone(isData=options.isData)
process.cleanedEvents = eventCounter.clone(isData=options.isData)
process.finalEvents = eventCounter.clone(isData=options.isData)

process.p = cms.Path(
    process.allEvents
    *process.evtcleaner
    *process.cleanedEvents
    *cms.ignore(process.ana)
    *cms.ignore(process.anaBoosted)
    * process.finalEvents
    )

#open('dump.py','w').write(process.dumpPython())
