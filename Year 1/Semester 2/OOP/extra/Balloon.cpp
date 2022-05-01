//
// Created by moldo on 4/30/2022.
//

#include "Balloon.h"

Balloon::Balloon(const int &unique_identifier, const std::string &model, const std::string &activity,
                 const int &maximum, const int &weight_limit)
                 : Aircraft{unique_identifier, model, activity, maximum}, weight_limit(weight_limit){

}

Balloon::~Balloon() {

}

Balloon::Balloon() {

}

std::string Balloon::toString() {
    return "Balloon Unique identifier: " + std::to_string(unique_identifier) + " model: " + model + " activity: " + activity + " maximum: " + std::to_string(maximum) + " weight limit: " + std::to_string(weight_limit) + '\n';

}
