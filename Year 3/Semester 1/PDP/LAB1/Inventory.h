//
// Created by senzationall on 10/6/23.
//

#ifndef LAB1_INVENTORY_H
#define LAB1_INVENTORY_H
#include <mutex>
#include <unordered_map>
#include <vector>
#include "Product.h"

class Inventory {
private:
    std::unordered_map<Product, int, Product::Hasher> productQuantityMap;
    int moneyAmount;
    std::mutex inventoryMutex;

public:
    Inventory();
    void addProduct(const Product& product, int quantity);
    void sellProducts(const std::vector<std::pair<Product, int>>& items);
    bool performInventoryCheck();
};


#endif //LAB1_INVENTORY_H
