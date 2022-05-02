//
// Created by dani on 02.05.2022.
//

#include "Service.h"
#include <iostream>
#include <fstream>


Service::Service() {

}

Service::~Service() {
    for(auto &i : this->build)
        delete i;
}

void Service::add_a_building(Building *a) {
    this->build.push_back(a);
}

std::vector<Building *> Service::get_all_buildings() {
    return this->build;
}

std::vector<Building *> Service::get_all_to_be_restored() {
    std::vector<Building*> help;
    for(auto &i : this->build)
        if(i->must_be_restored())
            help.push_back(i);
    return help;
}

std::vector<Building *> Service::get_all_to_be_demolished() {
    std::vector<Building*> help;
    for(auto &i : this->build)
        if(i->can_be_demolished())
            help.push_back(i);
    return help;
}

void Service::write_to_file(std::string file, std::vector<Building *> buildings) {
    std::ofstream fout(file);
    for(auto &i : buildings)
        fout << i->to_string();
}
