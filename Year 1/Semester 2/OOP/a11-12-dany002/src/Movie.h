//
// Created by SenZatIonALL on 3/18/2022.
//

#pragma once

#ifndef A5_6_DANY002_MOVIE_H
#define A5_6_DANY002_MOVIE_H
#include <string>

class Movie {
private:
    std::string title;
    std::string genre;
    int year_of_release{};
    int number_of_likes{};
    std::string trailer;

public:
    Movie();
    Movie(std::string title, std::string genre, int year_of_release, int number_of_likes, std::string trailer);
    Movie(const Movie &m);
    ~Movie();
    std::string get_title() const;
    std::string get_genre() const;
    int get_year_of_release() const;
    int get_number_of_likes() const;
    std::string get_trailer() const;
    void set_title(std::string s);
    void set_genre(std::string s);
    void set_year_of_release(int year);
    void set_number_of_likes(int likes);
    void set_trailer(std::string t);
    Movie& operator= (const Movie& m);
    std::string toString() const;
};


#endif //A5_6_DANY002_MOVIE_H
