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

}

std::vector<Movie> Repository::get_movies() {
    /*
     * It returns all the movies.
     */
    return movies;

}

void Repository::add_movie(const Movie& m) {
    /*
     * It adds a movie in repository.
     */
    for(auto & movie : movies)
        if(movie.get_title() == m.get_title())
            throw RepositoryException();
    movies.push_back(m);
}

unsigned long long int Repository::get_size() {
    /*
     * It returns how many movies are in repository.
     */
    return movies.size();
}

Movie Repository::get_movie_by_index(int index) {
    /*
     * It returns the n-th movie, where n is given.
     */
    if(index >= movies.size() || index < 0)
        throw RepositoryException();

    return movies[index];

}

void Repository::delete_movie(const std::string& title) {
    /*
     * It delets a movie with the given title.
     */
    bool ok = false;
    for(int i = 0; i < movies.size(); i++)
        if(movies[i].get_title() == title){
            movies.erase(movies.begin() + i);
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
    for(auto & movie : movies)
        if(movie.get_title() == title){
            Movie m = movie;
            m.set_trailer(new_trailer);
            movie = m;
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
    for(auto & movie : movies){
        if(movie.get_genre() == genre){
            indexx++;
            if(index == indexx){
                return movie;
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
    for(auto & movie : movies){
        if(movie.get_genre() == genre)
            count++;
    }
    return count;
}

void Repository::increment_likes(const std::string &title) {
    /*
     * It increments the number of likes for a given title.
     */
    int likes;
    for(auto & i : movies)
        if(i.get_title() == title){
            Movie movie = i;
            likes = movie.get_number_of_likes();
            likes++;
            movie.set_number_of_likes(likes);
            i = movie;
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

Movie Repository::get_specific_movie(const std::string &title) {
    for(const auto& mov : movies)
        if(mov.get_title() == title)
            return mov;
    return {"NULL", "NULL", -1, -1, "NULL"};
}






