//
// Created by moldo on 4/30/2022.
//

#include "Aircraft.h"


Aircraft::Aircraft(const int &unique_identifier, const std::string &model, const std::string &activity,
                   const int &maximum) {
    this->unique_identifier = unique_identifier;
    this->model = model;
    this->activity = activity;
    this->maximum = maximum;
}

std::string Aircraft::get_activity() {
    return this->activity;
}

int Aircraft::get_maximum() {
    return this->maximum;
}

Aircraft::Aircraft() {

}

Aircraft::~Aircraft() {

}
