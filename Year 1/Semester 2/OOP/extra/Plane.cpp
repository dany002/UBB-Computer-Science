//
// Created by moldo on 4/30/2022.
//

#include "Plane.h"

#include <utility>

Plane::Plane(const int &unique_identifier, const std::string &model, const std::string &activity, const int &maximum,
             bool isPrivate, std::string main_wings)
             :Aircraft{unique_identifier, model, activity, maximum}, isPrivate(isPrivate), main_wings(std::move(main_wings)){


}

std::string Plane::toString() {
    return "Plane Unique identifier: " + std::to_string(unique_identifier) + " model: " + model + " activity: " + activity + " maximum: " + std::to_string(maximum) + " isPrivate: " + std::to_string(isPrivate) + " main wings: " + main_wings + '\n';
}

Plane::~Plane() {

}

Plane::Plane() {

}
