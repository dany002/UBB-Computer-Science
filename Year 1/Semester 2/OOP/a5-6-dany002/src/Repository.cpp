//
// Created by moldo on 3/18/2022.
//
#pragma once
#include "Repository.h"
#include "Movie.h"
#include "Exceptions.h"
#include <iostream>

Repository::Repository(){
    /*
     * Default constructor.
     */
    this->movies = DynamicVector<Movie>();
}

Movie *Repository::get_movies() {
    /*
     * It returns all the movies.
     */
    return movies.get_all_elems();
}

void Repository::add_movie(const Movie& m) {
    /*
     * It adds a movie in repository.
     */
    for(int i = 0; i < movies.get_size(); i++)
        if(movies.get_element(i).get_title() == m.get_title() && movies.get_element(i).get_trailer() == m.get_trailer())
            throw RepositoryException();
    movies.add(m);
}

int Repository::get_size() {
    /*
     * It returns how many movies are in repository.
     */
    return movies.get_size();
}

Movie Repository::get_movie_by_index(int index) {
    /*
     * It returns the n-th movie, where n is given.
     */
    try{
        return movies.get_element(index);
    }
    catch(IndexGreaterThanSize const&){
        throw RepositoryException();
    }
}

void Repository::delete_movie(const std::string& title) {
    /*
     * It delets a movie with the given title.
     */
    bool ok = false;
    for(int i = 0; i < movies.get_size(); i++)
        if(movies.get_element(i).get_title() == title){
            movies.remove_element_from_a_specific_index(i);
            ok = true;
            break;
        }
    if(!ok)
        throw RepositoryException();
}

void Repository::update_movie_trailer(const std::string& title, const std::string& new_trailer) {
    /*
     * It updates the trailer of the movie with the given title.
     */
    bool ok = false;
    for(int i = 0; i < movies.get_size(); i++)
        if(movies.get_element(i).get_title() == title){
            Movie m = movies.get_element(i);
            m.set_trailer(new_trailer);
            movies.set_element(m, i);
            ok = true;
            break;
        }
    if(!ok)
        throw RepositoryException();
}

Movie Repository::get_movie_index_genre_repo(const std::string& genre, int index){
    /*
     * It gets the nth movie with the given genre from repository.
     */
    int indexx = -1;
    for(int i = 0; i < movies.get_size(); i++){
        if(movies.get_element(i).get_genre() == genre){
            indexx++;
            if(index == indexx){
                return movies.get_element(i);
            }
        }
    }
    return get_movie_index_genre_repo(genre, 0);
}

int Repository::get_size_for_a_genre(const std::string &genre) {
    /*
     * It returns how many movies are for a given genre.
     */
    int count = 0;
    for(int i = 0; i < movies.get_size(); i++){
        if(movies.get_element(i).get_genre() == genre)
            count++;
    }
    return count;
}

void Repository::increment_likes(const std::string &title) {
    /*
     * It increments the number of likes for a given title.
     */
    int likes;
    for(int i = 0; i < movies.get_size(); i++)
        if(movies.get_element(i).get_title() == title){
            Movie movie = movies.get_element(i);
            likes = movie.get_number_of_likes();
            likes++;
            movie.set_number_of_likes(likes);
            movies.set_element(movie, i);
            break;
        }
}

Repository::~Repository(){
    /*
     * Default destructor
     */
}

Repository::Repository(const Repository &repo) {
    /*
     * Copy constructor.
     */
    this->movies = repo.movies;
}

Repository& Repository::operator=(const Repository &repo) {
    this->movies = repo.movies;
    return *this;
}






