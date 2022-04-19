//
// Created by SenZatIonALL on 3/5/2022.
//

#include "Validator.h"
#include <string.h>

int validator_quantity(int quantity){
    if(quantity < 0)
        return 0;
    return 1;
}

int validator_price(float price){
    if(price < 0)
        return 0;
    return 1;

}
int validator_concentration(float concentration){
    if(concentration <= 0 || concentration >= 100)
        return 0;
    return 1;
}

int validator_name(char* name){
    int ok = 0;
    for(int i = 0; i < strlen(name); i++)
        if(!((name[i] >= 'a' && name[i] <= 'z') || (name[i] >= 'A' && name[i] <= 'Z')))
            return 0;
    return 1;
}