//
// Created by moldo on 4/30/2022.
//

#ifndef PREGATIRE_REPO_H
#define PREGATIRE_REPO_H
#include "Aircraft.h"
#include "Helicopter.h"
#include "Plane.h"
#include "Balloon.h"
#include <vector>
#include <memory>

class Repo {
private:

    std::vector<Aircraft*> aircraft;
public:
    Repo();
    ~Repo();
    Repo(const Repo& repo);
    void add_an_aircraft(Aircraft* a);
    std::vector<Aircraft*> find_all_the_aircrafts_for_a_certain_activity(const std::string& activity);
    std::vector<Aircraft*> get_all_the_aircrafts_for_a_minimum_altitude(const int& altitude);
    std::vector<Aircraft*> get_all();

};


#endif //PREGATIRE_REPO_H
