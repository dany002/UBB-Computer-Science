//
// Created by moldo on 3/18/2022.
//
#pragma once
#ifndef A5_6_DANY002_WATCHLIST_H
#define A5_6_DANY002_WATCHLIST_H
#include "DynamicVector.h"
#include "Movie.h"
#include <vector>

class WatchList {
protected:
    std::vector<Movie> movies;

public:
    WatchList();
    ~WatchList();
    virtual void add_movie(const Movie& m);
    unsigned long long int get_size_of_watch_list();
    Movie get_movie_by_index_from_watch_list(int index);
    virtual void delete_movie_from_watch_list(const std::string& title);
    bool check_movie(const std::string& title);
    WatchList& operator= (const WatchList& watch);
    Movie* get_all_movies_wl();
    virtual void save_file();
};


#endif //A5_6_DANY002_WATCHLIST_H
