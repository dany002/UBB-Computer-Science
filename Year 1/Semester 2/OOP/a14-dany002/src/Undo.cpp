//
// Created by moldo on 5/27/2022.
//

#include "Undo.h"

Undo::Undo() {

}

Undo::~Undo() {

}

void Undo::add_movie(Movie movie) {
    movie.set_id(1);
    movies.push_back(movie);
}

void Undo::delete_movie(Movie movie) {
    movie.set_id(2);
    movies.push_back(movie);
}

void Undo::update_movie(Movie movie) {
    movie.set_id(3);
    movies.push_back(movie);
}

std::vector<Movie> Undo::get_all() {
    return movies;
}

void Undo::pop_last() {
    movies.pop_back();
}
