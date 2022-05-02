//
// Created by dani on 02.05.2022.
//

#ifndef T2_DANY002_1_HOUSE_H
#define T2_DANY002_1_HOUSE_H
#include <string>
#include "Building.h"

class House : public Building{
private:
    bool historical;
public:
    House();
    House(const std::string& address, const int& year, bool historical);
    ~House();
    bool must_be_restored() override;
    bool can_be_demolished() override;
    std::string to_string() override;
};


#endif //T2_DANY002_1_HOUSE_H
