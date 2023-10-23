//
// Created by senzationall on 10/6/23.
//

#ifndef LAB1_INVENTORY_H
#define LAB1_INVENTORY_H

#include <vector>
#include <mutex>
#include <unordered_map>
#include "Product.h"

class Inventory {
private:
    std::unordered_map<int, Product> productMap;
    int moneyAmount;
    std::vector<std::vector<std::pair<int, int>>> salesRecord; // Bill
    std::mutex inventoryMutex;
    std::mutex moneyMutex;

public:
    Inventory();
    void addProduct(const Product& product);
    void sellProducts(const std::vector<std::pair<int, int>>& items);
    bool performInventoryCheck();
    int getMoneyAmount() const;
};

#endif // LAB1_INVENTORY_H
