//
// Created by senzationall on 10/6/23.
//

#ifndef LAB1_PRODUCT_H
#define LAB1_PRODUCT_H

#include <iostream>
#include <unordered_map>



class Product {
private:
    int id{};
    int quantity{};
    int price{};
public:

    struct Hasher {
        std::size_t operator()(const Product& product) const {
            return std::hash<int>()(product.id);
        }
    };

    Product(int id, int quantity, int price);

    Product(const Product& product);

    int getQuantity() const;

    void setQuantity(int quantity);

    int getPrice() const;

    bool operator==(const Product &rhs) const;

    bool operator!=(const Product &rhs) const;

    Product& operator=(const Product& other);

    int getId() const;


    Product();
    ~Product();
};


#endif //LAB1_PRODUCT_H
