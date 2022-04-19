
#pragma once
#include "WatchList.h"
#include "Movie.h"
#include "DynamicVector.h"

WatchList::WatchList(){
    /*
     * Default constructor.
     */
    this->movies = DynamicVector<Movie>();
}

void WatchList::add_movie(const Movie& m) {
    /*
     * It adds a movie in watch list.
     */
    movies.add(m);
}

int WatchList::get_size_of_watch_list() {
    /*
     * It gets the size of watch list.
     */
    return movies.get_size();
}

Movie WatchList::get_movie_by_index_from_watch_list(int i) {
    /*
     * It returns the n-th movie from watch list.
     */
    return movies.get_element(i);
}

void WatchList::delete_movie_from_watch_list(const std::string &title) {
    /*
     * It deletes a specific movie from watch list.
     */
    for(int i = 0; i < movies.get_size(); i++)
        if(movies.get_element(i).get_title() == title){
            movies.remove_element_from_a_specific_index(i);
            break;
        }
}

bool WatchList::check_movie(const std::string &title) {
    /*
     * It checks if a movie is in the watch list.
     */
    for(int i = 0; i < movies.get_size(); i++)
        if(movies.get_element(i).get_title() == title)
            return true;
    return false;
}

WatchList::~WatchList(){
    /*
     * Default destructor.
     */
}

WatchList &WatchList::operator=(const WatchList &watch) {
    this->movies = watch.movies;
    return *this;
}





