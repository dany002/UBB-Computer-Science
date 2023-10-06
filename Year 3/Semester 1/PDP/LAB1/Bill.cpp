//
// Created by senzationall on 10/6/23.
//

#include "Bill.h"

Bill::Bill(const std::vector<std::pair<Product, int>> &listOfProducts){
}


Bill::Bill() : list_of_products() {
}


Bill::~Bill() = default;

int Bill::computeTotalPrice() const {
    int total = 0;
    for(const auto& item : this->list_of_products){
        total += item.first.getPrice() * item.second;
    }
    return total;
}


