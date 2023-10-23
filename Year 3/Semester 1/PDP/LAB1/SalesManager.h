//
// Created by senzationall on 10/6/23.
//

#ifndef LAB1_SALESMANAGER_H
#define LAB1_SALESMANAGER_H


#include "Inventory.h"

class SalesManager {
private:
    Inventory& inventory;

public:
    explicit SalesManager(Inventory& inventory);
    void performSale(const std::vector<std::pair<int, int>>& items);

};


#endif //LAB1_SALESMANAGER_H
