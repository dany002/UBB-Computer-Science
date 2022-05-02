//
// Created by dani on 02.05.2022.
//

#include "UI.h"
#include <iostream>
#include "House.h"
#include "Block.h"

using namespace std;
UI::UI(Service service) {
    this->service = service;
}

UI::UI() {

}

UI::~UI() {

}

void UI::run_command() {
    this->initial_list();
    int command;
    while(true){
        this->print_menu();
        cin >> command;
        if(command == 1)
            this->add_a_new_building();
        if(command == 2)
            this->show_all_buildings();
        if(command == 3)
            this->must_be_restored();
        if(command == 4)
            this->save_file();
        if(command == 5)
            break;
    }
}

void UI::print_menu() {
    cout << "1. Add a new building" << endl;
    cout << "2. Show all buildings" << endl;
    cout << "3. Show all buildings that must be restored older than a given year." << endl;
    cout << "4. Save" << endl;
    cout << "5. exit" << endl;
}

void UI::add_a_new_building() {
    string type;
    cout << "What type? Block or House? ";
    cin >> type;
    if(type == "house"){
        int year;
        string address, historical;
        cout << "Year=";
        cin >> year;
        cout << "Address";
        cin >> address;
        cout << "Historical yes or no";
        cin >> historical;
        bool etc;
        if(historical == "yes")
            etc = true;
        else
            etc = false;
        Building* a;
        auto b = new House(address, year, etc);
        a = b;
        this->service.add_a_building(a);
    }
    else if(type == "block"){
        int year, total, occupied;
        string address;
        cout << "Year=";
        cin >> year;
        cout << "Address=";
        cin >> address;
        cout << "Total=";
        cin >> total;
        cout << "Occupied";
        cin >> occupied;
        Building* a;
        auto b = new Block(address, year, total, occupied);
        a = b;
        this->service.add_a_building(a);
    }
}

void UI::show_all_buildings() {
    auto a = this->service.get_all_buildings();
    for(auto &i : a){
        cout << i->to_string();
    }
}

void UI::must_be_restored() {
    auto a = this->service.get_all_to_be_restored();
    vector<Building*> help;
    int given_year;
    cout << "given year=";
    cin >> given_year;
    for(auto &i: a){
        if(i->get_year() < given_year)
            help.push_back(i);
    }
    for(auto &i : help)
        cout << i->to_string();
}

void UI::initial_list() {
    Building* a;
    auto b = new Block("awfas", 1943, 300, 30);
    a = b;
    this->service.add_a_building(a);
    auto c = new Block("awfasasf", 143, 3140, 3012);
    a = c;
    this->service.add_a_building(a);
    auto d = new House("wge earh", 1502, true);
    a = d;
    this->service.add_a_building(a);

    auto e = new House("wge waf earh", 1572, false);
    a = e;
    this->service.add_a_building(a);
}

void UI::save_file() {
    string file_for_restored, file_for_demolished;
    cout << "File for restored";
    cin >> file_for_restored;
    cout << "File for demolished";
    cin >> file_for_demolished;
    auto a = this->service.get_all_to_be_restored();
    this->service.write_to_file(file_for_restored, a);

    auto c = this->service.get_all_to_be_demolished();
    this->service.write_to_file(file_for_demolished, c);
}

