//
// Created by moldo on 3/18/2022.
//
#pragma once
#ifndef A5_6_DANY002_REPOSITORY_H
#define A5_6_DANY002_REPOSITORY_H

#include "Movie.h"
#include <string>
#include <vector>
class Repository {
protected:
    std::vector<Movie> movies;


public:
    Repository();
    ~Repository();
    Repository(const Repository& repo);
    Movie* get_movies();
    unsigned long long int get_size();
    Movie get_movie_by_index(int index);

    virtual void add_movie(const Movie& m);
    virtual void delete_movie(const std::string& title);
    virtual void update_movie_trailer(const std::string& title, const std::string& new_trailer);
    Movie get_movie_index_genre_repo(const std::string& genre, int index);
    int get_size_for_a_genre(const std::string& genre);
    void increment_likes(const std::string& title);
    Repository& operator= (const Repository& repo);
};


#endif //A5_6_DANY002_REPOSITORY_H
