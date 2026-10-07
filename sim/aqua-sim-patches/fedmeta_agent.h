#ifndef FEDMETA_AGENT_H
#define FEDMETA_AGENT_H

#include "agent.h"

class FedMetaAgent : public Agent {
public:
    FedMetaAgent();
    virtual ~FedMetaAgent();

    void recv(Packet* p, Handler* h);
    void adapt_local_model();
    void upload_update();
    void detect_intrusion(Packet* p);

protected:
    int node_class_;       // 0=static, 1=glider, 2=AUV, 3=edge
    double energy_mj_;
    int model_params_;
    int quantize_bits_;
};

#endif  // FEDMETA_AGENT_H