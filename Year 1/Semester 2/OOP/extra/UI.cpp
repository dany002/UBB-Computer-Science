//
// Created by moldo on 4/30/2022.
//

#include "UI.h"
#include <iostream>
#include <exception>


using std::cout, std::endl, std::cin, std::getline;


UI::UI(const Service& service) {
    this->service = service;
}

void UI::run() {
    this->initial_list();
    while(true){
        this->main_menu();
        int command;
        std::cin >> command;
        if(command == 1)
            this->add();
        if(command == 2)
            this->display_certain_activity();
        if(command == 3)
            this->minimum_altitude();
        if(command == 4)
            this->print_all();
        if(command == 5)
            break;
    }
}

void UI::main_menu() {
    cout << "1. to add an aircraft" << endl;
    cout << "2. display for a certain activity." << endl;
    cout << "3. display all aircraft that can reach at least a given altitude." << endl;
    cout << "4. display all aircraft" << endl;
    cout << "5. exit" << endl;
}

void UI::add() {
    std::string aircraft;
    cout << "What do you want to add? helicopter/plane/balloon?";
    cin >> aircraft;
    if(aircraft == "helicopter"){
        std::string model, activity, isPrivate;
        bool new_private;
        int maximum, unique_identifier;
        cout << "Unique identifier = ";
        cin >> unique_identifier;
        cin.get();
        cout << "Model = ";
        getline(cin, model);
        cout << "Activity = ";
        getline(cin, activity);
        cout << "isPrivate = ";
        getline(cin, isPrivate);
        if(isPrivate == "true")
            new_private = true;
        else
            new_private = false;
        cout << "maximum = ";
        cin >> maximum;
        try {
            this->service.add_helicopter(unique_identifier, model, activity, maximum, new_private);
        }
        catch(std::exception const &e){
            cout << e.what();
        }
    }
    else if(aircraft == "plane"){
        std::string model, activity, isPrivate, main_wings;
        bool new_private;
        int maximum, unique_identifier;
        cout << "Unique identifier = ";
        cin >> unique_identifier;
        cin.get();
        cout << "Model = ";
        getline(cin, model);
        cout << "Activity = ";
        getline(cin, activity);
        cout << "isPrivate = ";
        getline(cin, isPrivate);
        cout << "maximum = ";
        cin >> maximum;
        cout << "main wings = ";
        getline(cin, main_wings);
        if(isPrivate == "true")
            new_private = true;
        else
            new_private = false;
        try{
            this->service.add_plane(unique_identifier, model, activity, maximum, new_private, main_wings);
        }
        catch(std::exception const &e){
            cout << e.what();
        }
    }
    else if(aircraft == "balloon"){
        std::string model, activity;
        int maximum, unique_identifier, weight_limit;
        cout << "Unique identifier = ";
        cin >> unique_identifier;
        cin.get();
        cout << "Model = ";
        getline(cin, model);
        cout << "Activity = ";
        getline(cin, activity);
        cout << "maximum = ";
        cin >> maximum;
        cout << "weight limit = ";
        cin >> weight_limit;
        try{
            this->service.add_balloon(unique_identifier, model, activity, maximum, weight_limit);
        }
        catch(std::exception const &e){
            cout << e.what();
        }
    }
}

void UI::display_certain_activity() {
    cout << "What is the activity? \n";
    std::string activity;
    cin.get();
    getline(cin, activity);
    auto a = this->service.find_all_the_aircrafts_for_a_certain_activity(activity);
    for(auto &i : a)
        std::cout << i->toString();
}

void UI::minimum_altitude() {
    cout << "What is the altitude? \n";
    int altitude;
    cin >> altitude;
    auto a = this->service.get_all_the_aircrafts_for_a_minimum_altitude(altitude);
    for(auto &i : a)
        std::cout << i->toString();
}

UI::~UI() {

}

void UI::print_all() {
    auto a = this->service.get_all();
    for(auto &i : a)
        std::cout << i->toString();
}

void UI::initial_list() {
    this->service.add_helicopter(142, "adg", "WAgd", 1, true);
    this->service.add_helicopter(1, "adasdg", "yth", 3, false);
    this->service.add_helicopter(1432, "adgfg", "Wzxcgd", 5, true);
    this->service.add_plane(1732, "adg", "yth", 7, false, "biplane");
    this->service.add_plane(132, "adcfg", "wags", 9, false, "monoplane");
    this->service.add_plane(1632, "adxfg", "fjs", 11, true, "biplane");
    this->service.add_balloon(132, "wyer", "yth", 7, 9);
    this->service.add_balloon(2, "wyesfgr", "yatsdh", 1, 15);
    this->service.add_balloon(12, "wyejkfghr", "ythsdgh", 3, 912);
}
