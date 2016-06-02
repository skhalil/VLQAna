#!/bin/python

import subprocess

suffix = '_pre'

options = [
           # ['cutflow'],
           ['npv_noweight'+suffix],
           ['npv'+suffix],
           ['nak4'+suffix],
           ['ht'+suffix],
           ['st'+suffix],
           ['met'+suffix],
           ['metPhi'+suffix],
           ['ptak4jet1'+suffix],
           ['ptak4jet2'+suffix],
           ['ptak4jet3'+suffix],
           ['ptak4jet4'+suffix],
           ['etaak4jet1'+suffix],
           ['etaak4jet2'+suffix],
           ['etaak4jet3'+suffix],
           ['etaak4jet4'+suffix],
           ['cvsak4jet1'+suffix],
           ['cvsak4jet2'+suffix],
           ['cvsak4jet3'+suffix],
           ['cvsak4jet4'+suffix],
           ['phi_jet1MET'+suffix],
           ['mass_zmumu'+suffix],
           ['dr_mumu'+suffix],
            ['pt_zmumu'+suffix],
           ['nbjets'],
           ['nwjet'],
           ['nhjet'],
           ['ntjet'],
           ['ptak8leading'],
           ['ptbjetleading'],
           ['etabjetleading'],
           ['etaak8leading'],
           ['mak8leading'],
           ['prunedmak8leading'],
           ['trimmedmak8leading'],
           ['softdropmak8leading'],
           ['ptak82nd'],
           ['etaak82nd'],
           ['mak82nd'],
           ['prunedmak82nd'],
           ['trimmedmak82nd'],
           ['softdropmak82nd'],
           ['ptTprime'],
           ['yTprime'],
           ['mTprime'],
           ['ptBprime'],
           ['yBprime'],
           ['mBprime'],
            # ['pt_eta_b_all'],
            # ['pt_eta_c_all'],
            # ['pt_eta_l_all'],
            # ['pt_eta_b_btagged'],
            # ['pt_eta_c_btagged'],
            # ['pt_eta_l_btagged'],
           ['lepBJetMass'],
           ['ZJetMasslep'],
           ['chi2_chi'],
           ['sqrtChi2'],
           ['chi_mass'],
          #['pt_mu1_pre'],
          #['pt_mu2_pre'],
    ]

command = "python plot.py --var={0:s} --plotDir='withEWKcorr_pre'"

for option in options :
    s = command.format(
        option[0]
        )

    subprocess.call( ["echo --------------------------------------------------------------------------",""], shell=True)
    subprocess.call( ["echo --------------------------------------------------------------------------",""], shell=True)
    subprocess.call( ["echo %s"%s,""]                                                                      , shell=True)
    subprocess.call( ["echo --------------------------------------------------------------------------",""], shell=True)
    subprocess.call( ["echo --------------------------------------------------------------------------",""], shell=True)
    subprocess.call( [s, ""]                                                                               , shell=True)
