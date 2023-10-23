//
// Created by senzationall on 10/6/23.
//

#ifndef LAB1_PRODUCT_H
#define LAB1_PRODUCT_H


class Product {
private:
    int id;
    int price;
    int quantity;

public:
    Product(int id, int price, int quantity);
    int getId() const;
    int getPrice() const;
    int getQuantity() const;
    void setQuantity(int quantity);
    Product();
};


#endif //LAB1_PRODUCT_H
