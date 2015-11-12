import FWCore.ParameterSet.Config as cms

genParams = cms.PSet(
    genPartCharge  = cms.InputTag("genPart", "genPartCharge"),
    genPartE       = cms.InputTag("genPart", "genPartE"),
    genPartEta     = cms.InputTag("genPart", "genPartEta"),
    genPartID      = cms.InputTag("genPart", "genPartID"),
    genPartMass    = cms.InputTag("genPart", "genPartMass"),
    genPartPhi     = cms.InputTag("genPart", "genPartPhi"),
    genPartPt      = cms.InputTag("genPart", "genPartPt"),
    genPartStatus  = cms.InputTag("genPart", "genPartStatus"),
    genPartMom0ID       = cms.InputTag("genPart", "genPartMom0ID"),
    genPartMom1ID       = cms.InputTag("genPart", "genPartMom1ID"),
    genPartDau0ID       = cms.InputTag("genPart", "genPartDau0ID"),
    genPartDau1ID       = cms.InputTag("genPart", "genPartDau1ID"),
    genPartMom0Status   = cms.InputTag("genPart", "genPartMom0Status"),
    genPartMom1Status   = cms.InputTag("genPart", "genPartMom1Status"),
    genPartDau0Status   = cms.InputTag("genPart", "genPartDau0Status"),
    genPartDau1Status   = cms.InputTag("genPart", "genPartDau1Status"),   

    ids            = cms.vint32(8000001, -8000001),#TPrime
    momids         = cms.vint32(8000001, -8000001),#TPrime
    dauids        = cms.vint32(25,24,23,6,5,-25,-24,-23,-6,-5), #H, W, Z, t, b
   
    checkmomid     = cms.bool(False),
    statuses       = cms.vint32(22),#if its a T' or B', it shouldn't be the final state particle.
    checkstatus    = cms.bool(True),
    checkdauid     = cms.bool(True),
    verbose        = cms.bool(False),
)
