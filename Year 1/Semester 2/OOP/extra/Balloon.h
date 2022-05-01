//
// Created by moldo on 4/30/2022.
//

#ifndef PREGATIRE_BALLOON_H
#define PREGATIRE_BALLOON_H
#include "Aircraft.h"

class Balloon : public Aircraft{
private:
    int weight_limit;
public:
    Balloon();
    Balloon(const int& unique_identifier, const std::string& model, const std::string& activity, const int& maximum, const int& weight_limit);
    ~Balloon();
    std::string toString() override;
};


#endif //PREGATIRE_BALLOON_H
