//
// Created by moldo on 4/30/2022.
//

#ifndef PREGATIRE_PLANE_H
#define PREGATIRE_PLANE_H
#include "Aircraft.h"

class Plane : public Aircraft{
private:
    bool isPrivate;
    std::string main_wings;
public:
    Plane();
    Plane(const int& unique_identifier, const std::string& model, const std::string& activity, const int& maximum, bool isPrivate, std::string  main_wings);
    ~Plane();
    std::string toString() override;
};


#endif //PREGATIRE_PLANE_H
