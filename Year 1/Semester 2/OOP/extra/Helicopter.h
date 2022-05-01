//
// Created by moldo on 4/30/2022.
//

#ifndef PREGATIRE_HELICOPTER_H
#define PREGATIRE_HELICOPTER_H
#include "Aircraft.h"

class Helicopter : public Aircraft{
private:
    bool isPrivate;
public:
    Helicopter();
    Helicopter(const int& unique_identifier, const std::string& model, const std::string& activity, const int& maximum, bool isPrivate);
    ~Helicopter();
    std::string toString() override;
};


#endif //PREGATIRE_HELICOPTER_H
