//
// Created by moldo on 4/30/2022.
//

#ifndef PREGATIRE_AIRCRAFT_H
#define PREGATIRE_AIRCRAFT_H
#include <string>

class Aircraft {
protected:
    int unique_identifier, maximum;
    std::string model, activity;

public:
    Aircraft();
    Aircraft(const int& unique_identifier, const std::string& model, const std::string& activity, const int& maximum);
    ~Aircraft();

    std::string get_activity();
    int get_maximum();
    virtual std::string toString() = 0;
};


#endif //PREGATIRE_AIRCRAFT_H
