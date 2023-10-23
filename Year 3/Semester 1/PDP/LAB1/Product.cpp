// Product.cpp
#include "Product.h"

Product::Product(int id, int price, int quantity) : id(id), price(price), quantity(quantity) {}

int Product::getId() const {
    return id;
}

int Product::getPrice() const {
    return price;
}

int Product::getQuantity() const {
    return quantity;
}

void Product::setQuantity(int quantity) {
    this->quantity = quantity;
}

Product::Product() : id(0), price(0), quantity(0) {}

