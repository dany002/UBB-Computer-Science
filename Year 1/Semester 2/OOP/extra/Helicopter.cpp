//
// Created by moldo on 4/30/2022.
//

#include "Helicopter.h"
#include <exception>


Helicopter::Helicopter(const int &unique_identifier, const std::string &model, const std::string &activity,
                       const int &maximum, bool isPrivate)
                       :Aircraft{unique_identifier, model, activity, maximum}, isPrivate(isPrivate){

}

Helicopter::Helicopter() {

}

Helicopter::~Helicopter() {

}

std::string Helicopter::toString() {
    return "Helicopter Unique identifier: " + std::to_string(unique_identifier) + " model: " + model + " activity: " + activity + " maximum: " + std::to_string(maximum) + " isPrivate: " + std::to_string(isPrivate) + '\n';
}
