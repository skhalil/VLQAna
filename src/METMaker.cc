#include <iostream>
#include "Analysis/VLQAna/interface/METMaker.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

using namespace std ;
using namespace edm ;

METMaker::METMaker(edm::ParameterSet const& pars) :
l_metFullPhi 				(pars.getParameter<edm::InputTag>("metFullPhiLabel")),
l_metFullPt 				(pars.getParameter<edm::InputTag>("metFullPtLabel")),
l_metFullPx 				(pars.getParameter<edm::InputTag>("metFullPxLabel")),
l_metFullPy 				(pars.getParameter<edm::InputTag>("metFulluncorPhiLabel")),
l_metFulluncorPhi 			(pars.getParameter<edm::InputTag>("metFulluncorPhiLabel")),
l_metFulluncorPt 			(pars.getParameter<edm::InputTag>("metFulluncorPtLabel")),
l_metFulluncorSumEt 		(pars.getParameter<edm::InputTag>("metFulluncorSumEtLabel")),
l_metNoHFPhi 				(pars.getParameter<edm::InputTag>("metNoHFPhiLabel")),
l_metNoHFPt 				(pars.getParameter<edm::InputTag>("metNoHFPtLabel")),
l_metNoHFPx 				(pars.getParameter<edm::InputTag>("metNoHFPxLabel")),
l_metNoHFPy 				(pars.getParameter<edm::InputTag>("metNoHFPyLabel")),
l_metNoHFuncorPhi 			(pars.getParameter<edm::InputTag>("metNoHFuncorPhiLabel")),
l_metNoHFuncorPt 			(pars.getParameter<edm::InputTag>("metNoHFuncorPtLabel")),
l_metNoHFuncorSumEt 		(pars.getParameter<edm::InputTag>("metNoHFuncorSumEtLabel")),
METPtMin_ (pars.getParameter<double>("METPtMin")),
METPtMax_ (pars.getParameter<double>("METPtMax"))
{}

METMaker::~METMaker () {}

void METMaker::operator () (edm::Event& evt, vlq::MetCollection& MET){
	Handle<vector<float>> h_metFullPhi			; evt.getByLabel(l_metFullPhi 			, h_metFullPhi)			;
	Handle<vector<float>> h_metFullPt 			; evt.getByLabel(l_metFullPt 			, h_metFullPt)			;
	Handle<vector<float>> h_metFullPx 			; evt.getByLabel(l_metFullPx 			, h_metFullPx)			;
	Handle<vector<float>> h_metFullPy 			; evt.getByLabel(l_metFullPy 			, h_metFullPy)			;
	Handle<vector<float>> h_metFulluncorPhi 	; evt.getByLabel(l_metFulluncorPhi		, h_metFulluncorPhi)	;
	Handle<vector<float>> h_metFulluncorPt 		; evt.getByLabel(l_metFulluncorPt 		, h_metFulluncorPt)		;
	Handle<vector<float>> h_metFulluncorSumEt 	; evt.getByLabel(l_metFulluncorSumEt 	, h_metFulluncorSumEt)	;
	Handle<vector<float>> h_metNoHFPhi 			; evt.getByLabel(l_metNoHFPhi 			, h_metNoHFPhi)			;
	Handle<vector<float>> h_metNoHFPt 			; evt.getByLabel(l_metNoHFPt 			, h_metNoHFPt)			;
	Handle<vector<float>> h_metNoHFPx 			; evt.getByLabel(l_metNoHFPx			, h_metNoHFPx)			;
	Handle<vector<float>> h_metNoHFPy 			; evt.getByLabel(l_metNoHFPy			, h_metNoHFPy)			;
	Handle<vector<float>> h_metNoHFuncorPhi 	; evt.getByLabel(l_metNoHFuncorPhi		, h_metNoHFuncorPhi)	;
	Handle<vector<float>> h_metNoHFuncorPt 		; evt.getByLabel(l_metNoHFuncorPt		, h_metNoHFuncorPt)		;
	Handle<vector<float>> h_metNoHFuncorSumEt 	; evt.getByLabel(l_metNoHFuncorSumEt	, h_metNoHFuncorSumEt)	;

    double metFullPt = (h_metFullPt.product())->at(0);
    TLorentzVector  metP4;
    metP4.SetPtEtaPhiM(h_metFullPt.product()->at(0), 0, h_metFullPhi.product()->at(0), 0); 
    if (metFullPt > METPtMin_ && metFullPt < METPtMax_){
       vlq::Met met;
       met.setFullPhi 			(h_metFullPhi 			.product()->at(0));
       met.setFullPt 			(h_metFullPt 			.product()->at(0));
       met.setFullPx 			(h_metFullPx 			.product()->at(0));
       met.setFullPy 			(h_metFullPy 			.product()->at(0));
       met.setFulluncorPhi 	    (h_metFulluncorPhi 		.product()->at(0));
       met.setFulluncorPt 		(h_metFulluncorPt 		.product()->at(0));
       met.setFulluncorSumEt 	(h_metFulluncorSumEt 	.product()->at(0));
       met.setNoHFPhi 			(h_metNoHFPhi 			.product()->at(0));
       met.setNoHFPt 			(h_metNoHFPt 			.product()->at(0));
       met.setNoHFPx 			(h_metNoHFPx 			.product()->at(0));
       met.setNoHFPy 			(h_metNoHFPy 			.product()->at(0));
       met.setNoHFuncorPhi 	    (h_metNoHFuncorPhi 		.product()->at(0));
       met.setNoHFuncorPt 		(h_metNoHFuncorPt 		.product()->at(0));
       met.setNoHFuncorSumEt 	(h_metNoHFuncorSumEt 	.product()->at(0));
       met.setP4                (metP4);
       
       MET.push_back(met);       
    }
}
