#! /usr/bin/env python
from __future__ import print_function
import os
import glob
import math
import copy
import subprocess
from ROOT import gROOT,std,ROOT,TFile,TH1F,TH2F,TStopwatch,TLorentzVector,TMath
gROOT.Macro("~/rootlogon.C")
import sys, logging
# Import what we need from FWLite
from DataFormats.FWLite import Events, Handle
#ROOT.gSystem.Load('libCondFormatsJetMETObjects')
from ROOT import JetCorrectionUncertainty, FactorizedJetCorrector, JetCorrectorParameters
#ROOT.gSystem.Load('libDataFormatsPatCandidates')
from ROOT import std #,pat

from optparse import OptionParser
parser = OptionParser()

parser.add_option('--files', metavar='F', type='string', action='store',
                  default = 'root://cmsxrootd.fnal.gov//store/user/lpcbprime/noreplica/skhalil/Zmumu/TprimeTprime_M-1400_TuneCUETP8M1_13TeV-madgraph-pythia8/crab_TprimeTprime_M-1400_v2/161230_003259/0000/skim_1.root',
                  dest='files',
                  help='Input files')

parser.add_option('--dataJEC', metavar='F', type='string', action='store',
                  default = 'BCD',
                  dest='dataJEC',
                  help='JEC payloads. BCD for run:1,276811, EF for run:276831,278801, G for run: 278802,280385, H for run:280919,Infinity')

parser.add_option('--JES', metavar='F', type='string', action='store',
                  default='nominal',
                  dest='JES',
                  help='JEC Systematic variation. Options are "nominal, up, down"')

parser.add_option("--data", action='store_true',
                  default=False,
                  dest="data",
                  help="data / no pileup")

# Parse and get arguments
(options, args) = parser.parse_args()
isData = options.data
JECData = options.dataJEC
if   JECData == 'BCD' and isData: d = 'Spring16_23Sep2016BCDV2_DATA/Spring16_23Sep2016BCDV2_DATA_'
elif JECData == 'EF'  and isData: d = 'Spring16_23Sep2016EFV2_DATA/Spring16_23Sep2016EFV2_DATA_'
elif JECData == 'G'   and isData: d = 'Spring16_23Sep2016GV2_DATA/Spring16_23Sep2016GV2_DATA_'
elif JECData == 'H'   and isData: d = 'Spring16_23Sep2016HV2_DATA/Spring16_23Sep2016HV2_DATA_'
else:                             d = 'Spring16_25nsV10_MC/Spring16_25nsV10_MC_'

# JEC
jecScale = 0.0
if options.JES   == 'up'   : jecScale =  1.0
elif options.JES == 'down' : jecScale = -1.0
flatJecUnc = 0.0

print('options', options)
print ('Getting files : ' + options.files)

# Load new JEC if/when needed
# ===========================
# https://twiki.cern.ch/twiki/bin/view/CMS/JECDataMC#Jet_Energy_Corrections_in_Run2
jecPar = [d+'L1FastJet_AK4PFchs.txt', d+'L2L3Residual_AK4PFchs.txt', d+'L3Absolute_AK4PFchs.txt', d+'L2L3Residual_AK4PFchs.txt']
vPar = std.vector(JetCorrectorParameters)()
for ipayload in jecPar:
    print ('ipayload for ak4 jets =' , ipayload)
    pars = JetCorrectorParameters(ipayload)
    vPar.push_back(pars)
jec = FactorizedJetCorrector( vPar )

# jec uncertainty
jecParStr = std.string(d+'Uncertainty_AK4PFchs.txt')
jecUnc = JetCorrectionUncertainty( jecParStr )

# Get the FWLite "Events"
events = Events (options.files)

# Get the handles
zll_H     = Handle ("std::vector<vlq::Candidate>"); zll_L = ("ana", "zllcands")

rho_H     = Handle ("double");             rho_L = ("fixedGridRhoFastjetAll", "")
npv_H     = Handle ("int");                npv_L = ("vertexInfo", "npv")
jetJEC_H  = Handle ("std::vector<float>"); jetJEC_L = ("jetsAK4CHS", "jetAK4CHSjecFactor0")
jetArea_H = Handle ("std::vector<float>"); jetArea_L = ("jetsAK4CHS", "jetAK4CHSjetArea")
jetCVS_H  = Handle ("std::vector<float>"); jetCVS_L = ("jetsAK4CHS", "jetAK4CHSCSVv2")

# option 1: call the B2G jets
jetPt_H   = Handle ("std::vector<float>"); jetPt_L  = ("jetsAK4CHS", "jetAK4CHSPt")
jetPhi_H  = Handle ("std::vector<float>"); jetPhi_L = ("jetsAK4CHS", "jetAK4CHSPhi")
jetEta_H  = Handle ("std::vector<float>"); jetEta_L = ("jetsAK4CHS", "jetAK4CHSEta")
jetE_H    = Handle ("std::vector<float>"); jetE_L   = ("jetsAK4CHS", "jetAK4CHSE")

# option 2: call the jet collections from skim, however they are stored after full event selections. So, we need is to store collections after pre-selections for any systematic uncert. related to jets
jet_H    = Handle ("std::vector<vlq::Jet>"); jet_L = ("ana", "jets")
bjet_H   = Handle ("std::vector<vlq::Jet>"); bjet_L = ("ana", "bjets")

# Keep some timing information
nEventsAnalyzed = 0
timer = TStopwatch()
timer.Start()

# loop over events
i = 0
for event in events:
    i = i + 1
    if i % 1000 == 0 :
        print("EVENT ", i)
    nEventsAnalyzed = nEventsAnalyzed + 1

    # at least one Z boson candidate passing full event selection (NOTE THIS CHOICE WON'T WORK IF JETS ARE ALREADY SELECTED TIGHTLY FOR SYS VARIATION)
    #event.getByLabel (zll_L, zll_H);
    #if zll_H.isValid(): zll = zll_H.product()
    #else: continue
    
    # get JEC:
    event.getByLabel (jetJEC_L, jetJEC_H); 
    event.getByLabel (jetArea_L, jetArea_H); 
    event.getByLabel (rho_L, rho_H);
    event.getByLabel (npv_L, npv_H);
    JEC = jetJEC_H.product()
    jetArea = jetArea_H.product()
    rho     = (rho_H.product())[0]
    npv     = (npv_H.product())[0]    

    # option 1: get the AK4 jets
    event.getByLabel (jetPt_L, jetPt_H );   
    event.getByLabel (jetPhi_L, jetPhi_H );
    event.getByLabel (jetEta_L, jetEta_H ); 
    event.getByLabel (jetE_L, jetE_H );     
    jetPt  = jetPt_H.product()
    jetPhi = jetPhi_H.product()
    jetEta = jetEta_H.product()
    jetE   = jetE_H.product()

    ak4jetP4       = TLorentzVector(0.0,0.0,0.0,0.0)
    uncorrJetP4 = TLorentzVector(0.0,0.0,0.0,0.0)
    scaledJetP4 = TLorentzVector(0.0,0.0,0.0,0.0)
    
    for ijet in range(0, jetPt.size()):      
        ak4jetP4.SetPtEtaPhiE(jetPt.at(ijet), jetEta.at(ijet), jetPhi.at(ijet), jetE.at(ijet))
        # get raw jets
        uncorrJetP4 = ak4jetP4 * JEC.at(ijet) 
        # apply L1, L2, L3 JEC on fly 
        jec.setJetEta ( uncorrJetP4.Eta() )
        jec.setJetPt  ( uncorrJetP4.Pt() )
        jec.setJetE   ( uncorrJetP4.Energy() )
        jec.setJetA   ( jetArea.at(ijet) )
        jec.setRho    ( rho )
        jec.setNPV    ( npv )
        corr = jec.getCorrection()
        scaledJetP4 = uncorrJetP4 * corr
        # if bottom line is uncommented, then you are applying JEC on fly, otherwise you proceed with jets as stored in ntuples.
        ak4jetP4.SetPtEtaPhiE( scaledJetP4.Pt(), scaledJetP4.Eta(), scaledJetP4.Phi(), scaledJetP4.E())
        # JES variation
        jetScale = 1.0
        if not isData and abs(jecScale) > 0.0001 : 
            jecUnc.setJetEta( ak4jetP4.Eta() )
            jecUnc.setJetPt( ak4jetP4.Pt() )
            upOrDown = bool(jecScale > 0.0)
            unc = abs(jecUnc.getUncertainty(upOrDown))
            jetScale = 1 + unc * jecScale
        # now rescale the ak4jetP4 with this scale
     
    # option 2: get the AK4 jets
    #njets_pre = 0
    #jet_vec2 =  []
    #event.getByLabel (jet_L, jet_H);
    #if jet_H.isValid(): 
    #    jets = jet_H.product()
        #assuming jet pt cut in skims will be 20 GeV, apply tight cuts of > 30 GeV.
    #    for j in jets:            
    #        if j.getP4().Pt() <= 30: continue
    #        jet_vec2.append(j)
    #        njets_pre = njets_pre + 1
    #print ('njets', njets_pre)

    # apply jet pt cuts in signal region
    
    # at least one b-jet: however it will be very difficult to propagate the b-tag SF uncertainty,
    #event.getByLabel (bjet_L, bjet_H);
    #if bjet_H.isValid(): 
    #    bjets = bjet_H.product()
    #else: continue
 
    #print('bjets size', bjets.size())

    #for ibj in bjets:
    #    print ('bjet pt = ', ibj.getP4().Pt())


timer.Stop()

# Print out our timing information
rtime = timer.RealTime(); # Real time (or "wall time")
ctime = timer.CpuTime(); # CPU time
print("Analyzed events: {0:6d}".format(nEventsAnalyzed))
print("RealTime={0:6.2f} seconds, CpuTime={1:6.2f} seconds".format(rtime,ctime))
print("{0:4.2f} events / RealTime second .".format( nEventsAnalyzed/rtime))
print("{0:4.2f} events / CpuTime second .".format( nEventsAnalyzed/ctime))
subprocess.call( ["ps aux | grep skhalil | cat > memory.txt", ""], shell=True )
