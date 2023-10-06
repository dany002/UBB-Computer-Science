//
// Created by senzationall on 10/6/23.
//

#ifndef LAB1_BILL_H
#define LAB1_BILL_H
#include <vector>
#include "Product.h"

class Bill {
private:
    std::vector<std::pair<Product, int>> list_of_products;

public:
    Bill(const std::vector<std::pair<Product, int>> &listOfProducts);
    int computeTotalPrice() const;
    Bill();
    ~Bill();

};


#endif //LAB1_BILL_H
