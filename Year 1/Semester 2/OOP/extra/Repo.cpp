//
// Created by moldo on 4/30/2022.
//

#include "Repo.h"
#include <iostream>

std::vector<Aircraft*> Repo::find_all_the_aircrafts_for_a_certain_activity(const std::string &activity) {
    std::vector<Aircraft*> new_vector;
    for(auto &i : this->aircraft){
        if( i->get_activity() == activity)
            new_vector.push_back(i);
    }
    return new_vector;

}

void Repo::add_an_aircraft(Aircraft* a) {
    this->aircraft.push_back(a);
}

std::vector<Aircraft*> Repo::get_all(){
    return this->aircraft;
}

std::vector<Aircraft*> Repo::get_all_the_aircrafts_for_a_minimum_altitude(const int &altitude) {

    std::vector<Aircraft*> new_vector;
    for(auto &i : this->aircraft){
        if(i->get_maximum() >= altitude)
            new_vector.push_back(i);
    }
    return new_vector;
}

Repo::Repo(const Repo &repo) {
    this->aircraft = repo.aircraft;
}

Repo::Repo() {

}

Repo::~Repo() {
    for(auto &i: this->aircraft)
        delete i;
}






