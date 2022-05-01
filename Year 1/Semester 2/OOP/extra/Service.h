//
// Created by moldo on 4/30/2022.
//

#ifndef PREGATIRE_SERVICE_H
#define PREGATIRE_SERVICE_H


#include "Repo.h"

class Service {
private:
    Repo repo;
public:
    Service();
    Service(const Repo& repo);
    ~Service();
    void add_helicopter(const int& unique_identifier, const std::string& model, const std::string& activity, const int& maximum, bool isPrivate);
    void add_balloon(const int& unique_identifier, const std::string& model, const std::string& activity, const int& maximum, const int& weight_limit);
    void add_plane(const int& unique_identifier, const std::string& model, const std::string& activity, const int& maximum, bool isPrivate, const std::string& main_wings);
    std::vector<Aircraft*> get_all();
    std::vector<Aircraft*> get_all_the_aircrafts_for_a_minimum_altitude(const int& altitude);
    std::vector<Aircraft*> find_all_the_aircrafts_for_a_certain_activity(const std::string &activity);
};


#endif //PREGATIRE_SERVICE_H
