//
// Created by moldo on 4/30/2022.
//

#ifndef PREGATIRE_UI_H
#define PREGATIRE_UI_H
#include "Service.h"

class UI {
private:
    Service service;
public:
    UI();
    UI(const Service& service);
    ~UI();
    void main_menu();
    void run();
    void add();
    void display_certain_activity();
    void minimum_altitude();
    void print_all();
    void initial_list();
};


#endif //PREGATIRE_UI_H
