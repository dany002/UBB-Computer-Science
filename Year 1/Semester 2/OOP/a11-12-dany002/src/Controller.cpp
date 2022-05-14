//
// Created by moldo on 3/18/2022.
//
#pragma once

#include "Controller.h"

#include <utility>
#include <bits/stdc++.h>
#include "Exceptions.h"
#include <iostream>


Controller::Controller(){}

Controller::Controller(const TextFiles &repo, WatchList* watch_list) {
    /*
     * It creates a controller using as parameters the repository,the watch list (html or csv).
     */
    this->repo = repo;
    this->watch_list = watch_list;
}

Controller::Controller(const Controller &control) {
    /*
     * Copy constructor.
     */
    this->repo = control.repo;
    this->watch_list = control.watch_list;

}

void Controller::add_movie_admin(std::string title, std::string genre, std::string trailer, int year_of_release, int number_of_likes){
    /*
     * It adds a new movie in database.
     */

    if(year_of_release < 0 || number_of_likes < 0)
        throw IntegerError();
    try{
        this->repo.add_movie(Movie(title, genre, year_of_release, number_of_likes, trailer));
    }
    catch(RepositoryException const&){
        throw MovieAlreadyExists();
    }
}

unsigned long long int Controller::get_size() {
    /*
     * It gets the size of the repository.
     */
    return this->repo.get_size();
}

std::vector<Movie> Controller::get_movies() {
    /*
     * It gets the movies of the repository.
     */
    return this->repo.get_movies();
}

Movie Controller::get_movie_by_index(int index) {
    /*
     * It gets a movie by index from repository.
     */
    try{
        return this->repo.get_movie_by_index(index);
    }
    catch(RepositoryException const&){
        throw IndexGreaterThanSize();
    }

}

void Controller::remove_movie_admin(std::string title) {
    /*
     * It removes a movie from repository with the given title.
     */
    try{
        this->repo.delete_movie(title);
    }
    catch(RepositoryException const&){
        throw MovieDoesntExist();
    }
}

void Controller::update_movie_admin(std::string title, std::string new_trailer) {
    /*
     * It updates the trailer for a movie with the given title from the repository.
     */

    try{
        this->repo.update_movie_trailer(title, new_trailer);
    }
    catch(RepositoryException const&){
        throw MovieDoesntExist();
    }
}

Movie Controller::get_movie_index_genre(const std::string& genre, int index){
    /*
     * It gets the n-th element from the list with the given genre.
     */
    return this->repo.get_movie_index_genre_repo(genre, index);
}

int Controller::get_size_for_a_genre(const std::string &genre) {
    /*
     * It gets the size of the list for a given genre.
     */
    return this->repo.get_size_for_a_genre(genre);
}

void Controller::add_movie_watch_list(const Movie& movie) {
    /*
     * It adds a movie to the watch list.
     */
    this->watch_list->add_movie(movie);
}

unsigned long long int Controller::get_size_watch_list() {
    /*
     * It gets the size of watch list.
     */
    return this->watch_list->get_size_of_watch_list();
}

Movie Controller::get_movie_watch_list_by_index(int index) {
    /*
     * It gets the n-th movie from the watch list.
     */
    return this->watch_list->get_movie_by_index_from_watch_list(index);
}

void Controller::increment_likes_for_a_movie(const std::string &title) {
    /*
     * It increments the number of likes for a movie.
     */
    this->repo.increment_likes(title);
}

void Controller::delete_movie_from_watch_list(const std::string& title) {
    /*
     * It deletes the movie with the given title from the watch list.
     */
    this->watch_list->delete_movie_from_watch_list(title);
}

bool Controller::check_movie_in_watch_list(const std::string &title) {
    /*
     * It checks if the movie is in the watch list.
     */
    return this->watch_list->check_movie(title);
}


Controller::~Controller(){
/*
 * Default destructor.
 */
}

Controller &Controller::operator=(const Controller &control) {
    this->repo = control.repo;
    this->watch_list = control.watch_list;
    return *this;
}

std::vector<Movie> Controller::get_all_movies_from_wl() {
    return this->watch_list->get_all_movies_wl();
}

std::vector<Movie> Controller::get_movies(std::string filter) {
    std::vector<Movie> all_movies = this->repo.get_movies();
    int count = (int) std::count_if(all_movies.begin(), all_movies.end(), [=](Movie m) { return m.toString().find(filter) != std::string::npos;});
    std::vector<Movie> movies(count);
    std::copy_if(all_movies.begin(), all_movies.end(), movies.begin(), [=](Movie m){ return m.toString().find(filter) != std::string::npos;});
    std::sort(movies.begin(), movies.end(), [](Movie m1, Movie m2){ return m1.get_number_of_likes() < m2.get_number_of_likes();});
    return movies;
}








