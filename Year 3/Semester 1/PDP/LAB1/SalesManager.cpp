// SalesManager.cpp
#include "SalesManager.h"

SalesManager::SalesManager(Inventory& inventory) : inventory(inventory) {}

void SalesManager::performSale(const std::vector<std::pair<int, int>>& items) {
    inventory.sellProducts(items);
}
