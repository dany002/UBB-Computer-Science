#include "Product.h"
#include "Inventory.h"
#include "SalesManager.h"
#include <iostream>
#include <thread>

int main() {
    // Create products
    Product productA(1, 10, 100);
    Product productB(2, 15, 50);
    Product productC(3, 5, 200);
    Product productD(4, 8, 75);

    // Create inventory
    Inventory inventory;
    inventory.addProduct(productA);
    inventory.addProduct(productB);
    inventory.addProduct(productC);
    inventory.addProduct(productD);

    // Create sales manager
    SalesManager salesManager(inventory);

    // Simulate concurrent sales
    std::thread saleThread1([&](){
        std::vector<std::pair<int, int>> items1 = {{1, 5}, {2, 10}, {3, 20}};
        salesManager.performSale(items1);
    });

    std::thread saleThread2([&](){
        std::vector<std::pair<int, int>> items2 = {{1, 3}, {2, 20}, {3, 15}};
        salesManager.performSale(items2);
    });

    saleThread1.join();
    saleThread2.join();

    // Perform inventory check
    bool isValid = inventory.performInventoryCheck();

    if (isValid) {
        std::cout << "Inventory check passed. Money: $" << inventory.getMoneyAmount() << std::endl;
    } else {
        std::cout << "Inventory check failed." << std::endl;
    }

    return 0;
}
