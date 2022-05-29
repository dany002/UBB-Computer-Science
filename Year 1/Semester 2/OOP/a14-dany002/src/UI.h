//
// Created by moldo on 3/18/2022.
//
#pragma once
#ifndef A5_6_DANY002_UI_H
#define A5_6_DANY002_UI_H
#include "Controller.h"

class UI {
private:
    Controller control;

public:
    UI(const Controller& control);
    ~UI();
    void run_command();
    static void print_menu_for_admin();
    static void print_menu_for_user();
    void run_command_for_admin();
    void run_command_for_user();
    void add_movie_admin();
    void delete_movie_admin();
    void update_movie_admin();
    void print_movies_admin();
    void initial_list();
    void play_movies();
    int play_trailer(const Movie& m);
    void see_movies_from_watch_list();
    void watch_movie();
};


#endif //A5_6_DANY002_UI_H
