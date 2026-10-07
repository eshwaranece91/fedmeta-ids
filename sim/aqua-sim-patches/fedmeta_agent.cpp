#include "fedmeta_agent.h"
#include "packet.h"

static class FedMetaAgentClass : public TclClass {
public:
    FedMetaAgentClass() : TclClass("Agent/FedMeta") {}
    TclObject* create(int, const char* const*) {
        return new FedMetaAgent();
    }
} class_fedmeta_agent;

FedMetaAgent::FedMetaAgent()
    : Agent(PT_FEDMETA), node_class_(0), energy_mj_(100.0),
      model_params_(2100), quantize_bits_(8) {
    bind("node_class_", &node_class_);
    bind("energy_mj_", &energy_mj_);
    bind("model_params_", &model_params_);
    bind("quantize_bits_", &quantize_bits_);
}

FedMetaAgent::~FedMetaAgent() {}

void FedMetaAgent::recv(Packet* p, Handler* h) {
    detect_intrusion(p);
    Agent::recv(p, h);
}

void FedMetaAgent::adapt_local_model() {
    // Placeholder for on-node meta-adaptation.
}

void FedMetaAgent::upload_update() {
    int update_bytes = model_params_ * quantize_bits_ / 8;
    // Forward to edge gateway via acoustic channel.
}

void FedMetaAgent::detect_intrusion(Packet* p) {
    // Lightweight IDS inference on incoming packet.
}