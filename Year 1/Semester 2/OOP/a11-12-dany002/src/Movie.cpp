//
// Created by SenZatIonALL on 3/18/2022.
//
#pragma once

#include "Movie.h"
#include <iostream>

Movie::Movie(std::string title, std::string genre, int year_of_release, int number_of_likes, std::string trailer) {
    /*
     * It creates a constuctor for movie.
     */
    this->title = title;
    this->genre = genre;
    this->year_of_release = year_of_release;
    this->number_of_likes = number_of_likes;
    this->trailer = trailer;

}

Movie::Movie(const Movie &m) {
    /*
     * It's the copy constructor for a new movie.
     */
    this->title = m.title;
    this->genre = m.genre;
    this->year_of_release = m.year_of_release;
    this->number_of_likes = m.number_of_likes;
    this->trailer = m.trailer;


}

std::string Movie::get_title() const{
    /*
     * It gets the title.
     */
    return this->title;
}

std::string Movie::get_genre() const{
    /*
     * It gets the genre.
     */
    return this->genre;
}

int Movie::get_year_of_release() const {
    /*
     * It gets the year of release.
     */
    return this->year_of_release;
}

int Movie::get_number_of_likes() const {
    /*
     * It gets the number of likes.
     */
    return this->number_of_likes;
}

std::string Movie::get_trailer() const{
    /*
     * It gets the trailer.
     */
    return this->trailer;
}

void Movie::set_title(std::string s) {
    /*
     * It sets the title.
     */
    this->title = s;
}

void Movie::set_genre(std::string s) {
    /*
     * It sets the genre.
     */
    this->genre = s;
}

void Movie::set_year_of_release(int year) {
    /*
     * It sets the year of release.
     */
    this->year_of_release = year;
}

void Movie::set_number_of_likes(int likes) {
    /*
     * It sets the number of likes.
     */
    this->number_of_likes = likes;
}

void Movie::set_trailer(std::string t) {
    /*
     * It sets the trailer.
     */
    this->trailer = t;
}

Movie::Movie(){
    /*
     * It creates a new object ( default constructor )
     */
    this->trailer = "";
    this->title = "";
    this->number_of_likes = 0;
    this->genre = "";
    this->year_of_release = 0;

}

Movie::~Movie(){
    /*
     * Default destructor.
     */

}

Movie& Movie::operator=(const Movie &m) {
    this->title = m.title;
    this->genre = m.genre;
    this->year_of_release = m.year_of_release;
    this->number_of_likes = m.number_of_likes;
    this->trailer = m.trailer;
    return *this;
}

std::string Movie::toString() const{
    return get_title() + " - " + get_genre() + " - " + get_trailer() + " - " + std::to_string(get_number_of_likes()) + " - " + std::to_string(get_year_of_release()) + '\n';
}
