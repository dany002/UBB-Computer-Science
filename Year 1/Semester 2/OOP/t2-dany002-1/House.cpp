//
// Created by dani on 02.05.2022.
//

#include "House.h"

House::House() {

}

House::House(const std::string &address, const int &year, bool historical)
:Building(address, year), historical(historical)
{

}

House::~House() {

}

bool House::must_be_restored() {
    if(this->year < 1920)
        return true;
    return false;
}

bool House::can_be_demolished() {
    if(this->historical)
        return false;
    return true;
}

std::string House::to_string() {
    return "House address " + this->address + " year " + std::to_string(this->year) + " Historical " + std::to_string(this->historical) + '\n';
}
