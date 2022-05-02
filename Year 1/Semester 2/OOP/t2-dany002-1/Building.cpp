//
// Created by dani on 02.05.2022.
//

#include "Building.h"

Building::Building() {

}

Building::Building(const std::string &address, const int &year) {
    this->address = address;
    this->year = year;
}

Building::~Building() {

}

int Building::get_year() {
    return this->year;
}
