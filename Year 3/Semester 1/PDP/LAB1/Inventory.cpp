//
// Created by senzationall on 10/6/23.
//

#include "Inventory.h"

Inventory::Inventory() {
    this->moneyAmount = 0;
}

void Inventory::addProduct(const Product &product, int quantity) {
    std::lock_guard<std::mutex> lock(this->inventoryMutex);
    productQuantityMap[product] += quantity;
}


// Sell products and update the inventory and money amount
void Inventory::sellProducts(const std::vector<std::pair<Product, int>>& items) {
    std::lock_guard<std::mutex> lock(inventoryMutex);
    for (const auto& item : items) {
        const Product& product = item.first;
        int quantity = item.second;

        auto it = productQuantityMap.find(product);
        if (it != productQuantityMap.end() && it->second >= quantity) {
            it->second -= quantity;
            moneyAmount += quantity * product.getPrice();
        }
        // Handle cases where the product is not found or the quantity is insufficient
    }
}

bool Inventory::performInventoryCheck() {
    std::lock_guard<std::mutex> lock(inventoryMutex);

    // Check if all product quantities are non-negative
    for (const auto& pair : productQuantityMap) {
        if (pair.second < 0) {
            return false;
        }
    }

    // Check if the money amount is non-negative
    if (moneyAmount < 0) {
        return false;
    }

    return true;
}
