#include <iostream>
#include <thread>
#include <vector>
#include "Inventory.h"
#include "SalesManager.h"

int main() {
    // Create an inventory
    Inventory inventory;

    // Create a sales manager
    SalesManager salesManager(inventory);

    // Add initial products to the inventory
    Product product1(1, 100, 10); // Product ID: 1, Initial Quantity: 100, Unit Price: $10
    Product product2(2, 50, 20);  // Product ID: 2, Initial Quantity: 50, Unit Price: $20
    Product product3(3, 75, 15);  // Product ID: 3, Initial Quantity: 75, Unit Price: $15

    inventory.addProduct(product1, product1.getQuantity());
    inventory.addProduct(product2, product2.getQuantity());
    inventory.addProduct(product3, product3.getQuantity());

    // Create threads for sales operations
    std::vector<std::thread> salesThreads;

    // Simulate concurrent sales operations
    for (int i = 0; i < 5; ++i) {
        salesThreads.emplace_back([&, product1, product2, product3]() { // Capture by value
            std::vector<std::pair<Product, int>> items;

            // Simulate a sale (e.g., random products and quantities)
            items.emplace_back(product1, rand() % 10 + 1); // Random quantity between 1 and 10
            items.emplace_back(product2, rand() % 10 + 1);
            items.emplace_back(product3, rand() % 10 + 1);

            // Perform a sale
            salesManager.performSale(items);
        });
    }


    // Start the sales threads
    for (auto& thread : salesThreads) {
        thread.join();
    }

    // Perform an inventory check
    bool isInventoryValid = inventory.performInventoryCheck();

    if (isInventoryValid) {
        std::cout << "Inventory check passed." << std::endl;
    } else {
        std::cout << "Inventory check failed. There are inconsistencies." << std::endl;
    }

    return 0;
}
