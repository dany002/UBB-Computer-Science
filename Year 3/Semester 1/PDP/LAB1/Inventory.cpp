// Inventory.cpp
#include "Inventory.h"

Inventory::Inventory() : moneyAmount(0) {}


void Inventory::addProduct(const Product& product) {
    std::lock_guard<std::mutex> lock(inventoryMutex);
    productMap[product.getId()] = product;
}


void Inventory::sellProducts(const std::vector<std::pair<int, int>>& items) {
    double totalSale = 0.0;
    std::vector<std::pair<int, int>> soldItems;

    for (const auto& item : items) {
        int productId = item.first;
        int quantity = item.second;

        std::lock_guard<std::mutex> lock(inventoryMutex);
        auto productIt = productMap.find(productId);

        if (productIt != productMap.end() && productIt->second.getQuantity() >= quantity) {
            productIt->second.setQuantity(productIt->second.getQuantity() - quantity);
            totalSale += quantity * productIt->second.getPrice();
            soldItems.push_back(item);
        }
    }

    if (!soldItems.empty()) {
        std::lock_guard<std::mutex> lock(moneyMutex);
        salesRecord.push_back(soldItems);
        moneyAmount += totalSale;
    }
}

bool Inventory::performInventoryCheck() {
    std::lock_guard<std::mutex> lock(inventoryMutex);

    for (const auto& record : salesRecord) {
        for (const auto& item : record) {
            int productId = item.first;
            int quantity = item.second;

            auto productIt = productMap.find(productId);

            if (productIt == productMap.end() || productIt->second.getQuantity() < quantity) {
                return false; // Sold more than available
            }
        }
    }

    return moneyAmount >= 0;
}

int Inventory::getMoneyAmount() const {
    return moneyAmount;
}
