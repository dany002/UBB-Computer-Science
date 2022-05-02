//
// Created by dani on 02.05.2022.
//

#include "Block.h"

Block::Block() {

}

Block::Block(const std::string &address, const int &year, const int &total, const int &occupied)
:Building(address, year), total(total), occupied(occupied)
{

}

Block::~Block() {

}

bool Block::must_be_restored() {
    if(2022-this->year > 40 && this->occupied >= 0.8*this->total)
        return true;
    return false;
}

bool Block::can_be_demolished() {
    if(this->occupied < 0.05*this->total)
        return true;
    return false;
}

std::string Block::to_string() {
    return "Block address " + this->address + " year " + std::to_string(this->year) + " total " + std::to_string(total) + " occupied " + std::to_string(occupied) + '\n';
}
