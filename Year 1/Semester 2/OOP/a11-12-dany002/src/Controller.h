//
// Created by moldo on 3/18/2022.
//

#ifndef A5_6_DANY002_CONTROLLER_H
#define A5_6_DANY002_CONTROLLER_H
#pragma once

#include "Repository.h"
#include "WatchList.h"
#include "TextFiles.h"
#include "HtmlFile.h"
#include "CsvFiles.h"

class Controller {
private:

    TextFiles repo;
    WatchList* watch_list;

public:
    Controller();
    Controller(const TextFiles& repo, WatchList* watch_list);
    Controller(const Controller&);
    ~Controller();
    unsigned long long int get_size();
    Movie* get_movies();
    Movie get_movie_by_index(int index);
    void add_movie_admin(std::string title, std::string genre, std::string trailer, int year_of_release, int number_of_likes);
    void remove_movie_admin(std::string title);
    void update_movie_admin(std::string title, std::string new_trailer);
    Movie get_movie_index_genre(const std::string& genre, int index);
    int get_size_for_a_genre(const std::string& genre);
    void add_movie_watch_list(const Movie& movie);
    unsigned long long int get_size_watch_list();
    Movie get_movie_watch_list_by_index(int index);
    void increment_likes_for_a_movie(const std::string& title);
    void delete_movie_from_watch_list(const std::string& title);
    bool check_movie_in_watch_list(const std::string& title);
    Controller& operator= (const Controller& control);
    Movie* get_all_movies_from_wl();
};


#endif //A5_6_DANY002_CONTROLLER_H
