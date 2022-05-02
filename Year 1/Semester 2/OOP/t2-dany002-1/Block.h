//
// Created by dani on 02.05.2022.
//

#ifndef T2_DANY002_1_BLOCK_H
#define T2_DANY002_1_BLOCK_H
#include <string>
#include "Building.h"

class Block : public Building{
private:
    int total, occupied;

public:
    Block();
    Block(const std::string& address, const int& year, const int& total, const int& occupied);
    ~Block();
    bool must_be_restored() override;
    bool can_be_demolished() override;
    std::string to_string() override;
};


#endif //T2_DANY002_1_BLOCK_H
