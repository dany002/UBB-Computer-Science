//
// Created by dani on 02.05.2022.
//

#ifndef T2_DANY002_1_UI_H
#define T2_DANY002_1_UI_H
#include "Service.h"

class UI {
private:
    Service service;
public:
    UI(Service service);
    UI();
    ~UI();
    void print_menu();
    void run_command();
    void add_a_new_building();
    void show_all_buildings();
    void must_be_restored();
    void initial_list();
    void save_file();
};


#endif //T2_DANY002_1_UI_H
