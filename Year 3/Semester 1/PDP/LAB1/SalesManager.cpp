//
// Created by senzationall on 10/6/23.
//

#include "SalesManager.h"

SalesManager::SalesManager(Inventory &inventory): inventory(inventory) {
    ;
}

void SalesManager::performSale(const std::vector<std::pair<Product, int>>& items) {
    Bill bill(items);
    std::lock_guard<std::mutex> lock(salesMutex);

    this->inventory.sellProducts(items);

    this->salesHistory.push_back(bill);

}

std::vector<Bill> SalesManager::getSalesHistory() const {
    std::lock_guard<std::mutex> lock(salesMutex);
    return this->salesHistory;
}
