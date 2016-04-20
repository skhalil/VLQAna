#ifndef ANALYSIS_VLQANA_METMAKER_HH
#define ANALYSIS_VLQANA_METMAKER_HH

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "AnalysisDataFormats/BoostedObjects/interface/Met.h"

using namespace std;
using namespace edm;

class METMaker {
public:
	METMaker (edm::ParameterSet const& pars) ;
	~METMaker () ;
	void operator () (edm::Event& evt, vlq::MetCollection& MET) ;

private:
	edm::InputTag l_metFullPhi			;
	edm::InputTag l_metFullPt 			;
	edm::InputTag l_metFullPx 			;
	edm::InputTag l_metFullPy 			;
	edm::InputTag l_metFulluncorPhi 	;
	edm::InputTag l_metFulluncorPt 		;
	edm::InputTag l_metFulluncorSumEt 	;
	edm::InputTag l_metNoHFPhi 			;
	edm::InputTag l_metNoHFPt 			;
	edm::InputTag l_metNoHFPx 			;
	edm::InputTag l_metNoHFPy 			;
	edm::InputTag l_metNoHFuncorPhi 	;
	edm::InputTag l_metNoHFuncorPt 		;
	edm::InputTag l_metNoHFuncorSumEt 	;
 
	double METPtMin_ ;
	double METPtMax_ ;
};
#endif
