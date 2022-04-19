//
// Created by moldo on 3/18/2022.
//
#pragma once
#ifndef A5_6_DANY002_WATCHLIST_H
#define A5_6_DANY002_WATCHLIST_H
#include "DynamicVector.h"
#include "Movie.h"

class WatchList {
private:
    DynamicVector<Movie> movies;

public:
    WatchList();
    ~WatchList();
    void add_movie(const Movie& m);
    int get_size_of_watch_list();
    Movie get_movie_by_index_from_watch_list(int index);
    void delete_movie_from_watch_list(const std::string& title);
    bool check_movie(const std::string& title);
    WatchList& operator= (const WatchList& watch);
};


#endif //A5_6_DANY002_WATCHLIST_H
