//
// Created by senzationall on 10/6/23.
//

#include "Product.h"

Product::Product(int id, int quantity, int price) : quantity(quantity), id(id), price(price){

}

Product::Product() = default;

Product::~Product() = default;

int Product::getQuantity() const {
    return this->quantity;
}

void Product::setQuantity(int quantity) {
    this->quantity = quantity;
}

int Product::getPrice() const {
    return this->price;
}

bool Product::operator==(const Product &rhs) const {
    return quantity == rhs.quantity && id == rhs.id;
}

bool Product::operator!=(const Product &rhs) const {
    return !(*this == rhs);
}


Product& Product::operator=(const Product& other) {
    if (this != &other) {
        this->quantity = other.quantity;
        this->price = other.price;
        this->id = other.id;
    }
    return *this;
}

Product::Product(const Product &product) : id(product.id), quantity(product.quantity), price(product.price) {

}

int Product::getId() const {
    return id;
}
