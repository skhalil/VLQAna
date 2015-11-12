#ifndef GenVLQSel_h
#define GenVLQSel_h

// system include files
#include <memory>
#include <vector>
#include <string>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Particle.h"

//
// class declaration
//

class GenVLQSel : public edm::EDProducer {
public:
   explicit GenVLQSel(const edm::ParameterSet&);
   ~GenVLQSel();
private:
   virtual void beginJob();
   virtual void produce(edm::Event&, const edm::EventSetup&);
   virtual void endJob();
   // ----------member data ---------------------------
   void setPointers(std::vector<const reco::Candidate *> decayList);

   std::vector<int> ids_ ;
   std::vector<int> statuses_ ;
   bool checkstatus_ ;
   std::vector<int> momids_ ;
   std::vector<int> dauids_;
   bool checkmomid_ ;
   bool checkdauid_ ;
   bool verbose_;

   edm::InputTag l_genPartCharge ; 
   edm::InputTag l_genPartE      ; 
   edm::InputTag l_genPartEta    ; 
   edm::InputTag l_genPartID     ; 
   edm::InputTag l_genPartMass   ; 
   edm::InputTag l_genPartPhi    ; 
   edm::InputTag l_genPartPt     ; 
   edm::InputTag l_genPartStatus ; 
   edm::InputTag l_genPartMom0ID ; 
   edm::InputTag l_genPartMom1ID ;
   edm::InputTag l_genPartMom0Status ;
   edm::InputTag l_genPartMom1Status ;
   edm::InputTag l_genPartDau0ID ;
   edm::InputTag l_genPartDau1ID ;
   edm::InputTag l_genPartDau0Status ;
   edm::InputTag l_genPartDau1Status ; 
};
#endif
//
// constants, enums and typedefs
//
typedef reco::Candidate::PolarLorentzVector LorentzV;
typedef std::vector< LorentzV > p4_vector;
typedef std::vector< int > pdgID_vector;
typedef edm::Handle <std::vector<float>> hfloat ;
//
// static data member definitions
//
void GenVLQSel::setPointers(std::vector<const reco::Candidate *> decayList){
   for(std::vector<const reco::Candidate *>::iterator iter = decayList.begin(); decayList.end() != iter; ++iter){
      *iter = 0;
   }
}

//
// constructors and destructor
//
GenVLQSel::GenVLQSel(const edm::ParameterSet& iConfig)
{
   ids_            = iConfig.getParameter<std::vector<int>>("ids");
   statuses_       = iConfig.getParameter<std::vector<int>>("statuses");
   checkstatus_    = iConfig.getParameter<bool>("checkstatus");
   momids_         = iConfig.getParameter<std::vector<int>>("momids");
   dauids_         = iConfig.getParameter<std::vector<int>>("dauids");
   checkmomid_     = iConfig.getParameter<bool>("checkmomid");
   checkdauid_     = iConfig.getParameter<bool>("checkdauid"); 
   verbose_        = iConfig.getParameter<bool>("verbose");
   l_genPartCharge = iConfig.getParameter<edm::InputTag>("genPartCharge");
   l_genPartE      = iConfig.getParameter<edm::InputTag>("genPartE");
   l_genPartEta    = iConfig.getParameter<edm::InputTag>("genPartEta"); 
   l_genPartID     = iConfig.getParameter<edm::InputTag>("genPartID");
   l_genPartMass   = iConfig.getParameter<edm::InputTag>("genPartMass"); 
   l_genPartPhi    = iConfig.getParameter<edm::InputTag>("genPartPhi");
   l_genPartPt     = iConfig.getParameter<edm::InputTag>("genPartPt"); 
   l_genPartStatus = iConfig.getParameter<edm::InputTag>("genPartStatus");
   l_genPartMom0ID = iConfig.getParameter<edm::InputTag>("genPartMom0ID");
   l_genPartMom1ID = iConfig.getParameter<edm::InputTag>("genPartMom1ID");
   l_genPartMom0Status = iConfig.getParameter<edm::InputTag>("genPartMom0Status");
   l_genPartMom1Status = iConfig.getParameter<edm::InputTag>("genPartMom1Status");
   l_genPartDau0ID     = iConfig.getParameter<edm::InputTag>("genPartDau0ID");
   l_genPartDau1ID     = iConfig.getParameter<edm::InputTag>("genPartDau1ID");
   l_genPartDau0Status = iConfig.getParameter<edm::InputTag>("genPartDau0Status");
   l_genPartDau1Status = iConfig.getParameter<edm::InputTag>("genPartDau1Status");

   //register your products
   produces<unsigned> ("TTtoWbZt");
   produces<unsigned> ("TTtoWbHt"); 
   produces<unsigned> ("TTtoHtZt");  
   produces<unsigned> ("TTtoWbWb");
   produces<unsigned> ("TTtoHtHt");
   produces<unsigned> ("TTtoZtZt");

   produces<unsigned> ("BBtoWtZb");
   produces<unsigned> ("BBtoWtHb"); 
   produces<unsigned> ("BBtoHbZb");  
   produces<unsigned> ("BBtoWtWt");
   produces<unsigned> ("BBtoHbHb");
   produces<unsigned> ("BBtoZbZb");
}


GenVLQSel::~GenVLQSel()
{
}

// ------------ method called once each job just before starting event loop  ------------
void 
GenVLQSel::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenVLQSel::endJob() {
   std::cout << "----------------------------------------------------------------------------------------" << std::endl;
   std::cout << "So long, and thanks for all the fish..." << std::endl;
   std::cout << "----------------------------------------------------------------------------------------" << std::endl;
}



