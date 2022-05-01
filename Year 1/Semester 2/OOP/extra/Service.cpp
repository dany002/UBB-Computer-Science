//
// Created by moldo on 4/30/2022.
//

#include "Service.h"
#include <exception>
#include "Plane.h"
#include "Helicopter.h"
#include "Aircraft.h"
#include "Balloon.h"


Service::Service(const Repo& repo) {
    this->repo = repo;
}

void Service::add_helicopter(const int &unique_identifier, const std::string &model, const std::string &activity,
                             const int &maximum, bool isPrivate) {

    if(maximum > 12)
        throw std::exception();
    if(activity == "leisure time" && !isPrivate)
        throw std::exception();

    Aircraft* a;
    auto b = new Helicopter(unique_identifier, model, activity, maximum, isPrivate);

    a = b;
    this->repo.add_an_aircraft(a);

}

Service::~Service() {

}

Service::Service() {

}


void Service::add_balloon(const int &unique_identifier, const std::string &model, const std::string &activity,
                          const int &maximum, const int &weight_limit) {
    if(maximum > 21)
        throw std::exception();
    Aircraft* a;
    auto b = new Balloon(unique_identifier, model, activity, maximum, weight_limit);
    a = b;
    this->repo.add_an_aircraft(a);

}

void Service::add_plane(const int &unique_identifier, const std::string &model, const std::string &activity,
                        const int &maximum, bool isPrivate, const std::string &main_wings) {
    if(activity == "leisure time" && main_wings != "biplane")
        throw std::exception();
    Aircraft* a;
    auto b = new Plane(unique_identifier, model, activity, maximum, isPrivate, main_wings);
    a = b;
    this->repo.add_an_aircraft(a);


}

std::vector<Aircraft*> Service::get_all() {
    return this->repo.get_all();
}

std::vector<Aircraft *> Service::get_all_the_aircrafts_for_a_minimum_altitude(const int &altitude) {
    return this->repo.get_all_the_aircrafts_for_a_minimum_altitude(altitude);
}

std::vector<Aircraft *> Service::find_all_the_aircrafts_for_a_certain_activity(const std::string &activity) {
    return this->repo.find_all_the_aircrafts_for_a_certain_activity(activity);
}
