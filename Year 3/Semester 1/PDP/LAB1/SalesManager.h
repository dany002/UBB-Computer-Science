//
// Created by senzationall on 10/6/23.
//

#ifndef LAB1_SALESMANAGER_H
#define LAB1_SALESMANAGER_H


#include "Inventory.h"
#include "Bill.h"

class SalesManager {
private:
    Inventory& inventory;
    std::vector<Bill> salesHistory;
    mutable std::mutex salesMutex;

public:
    explicit SalesManager(Inventory& inventory);
    void performSale(const std::vector<std::pair<Product, int>>& items);
    std::vector<Bill> getSalesHistory() const;
};


#endif //LAB1_SALESMANAGER_H
