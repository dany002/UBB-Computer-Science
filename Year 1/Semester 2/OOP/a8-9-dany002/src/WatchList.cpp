
#pragma once
#include "WatchList.h"
#include "Movie.h"
#include "DynamicVector.h"

WatchList::WatchList(){
    /*
     * Default constructor.
     */

}

void WatchList::add_movie(const Movie& m) {
    /*
     * It adds a movie in watch list.
     */
    movies.push_back(m);
}

unsigned long long int WatchList::get_size_of_watch_list() {
    /*
     * It gets the size of watch list.
     */
    return movies.size();
}

Movie WatchList::get_movie_by_index_from_watch_list(int i) {
    /*
     * It returns the n-th movie from watch list.
     */
    return movies[i];
}

void WatchList::delete_movie_from_watch_list(const std::string &title) {
    /*
     * It deletes a specific movie from watch list.
     */
    for(int i = 0; i < movies.size(); i++)
        if(movies[i].get_title() == title){
            movies.erase(movies.begin()+i);
            break;
        }
}

bool WatchList::check_movie(const std::string &title) {
    /*
     * It checks if a movie is in the watch list.
     */
    for(auto & movie : movies)
        if(movie.get_title() == title)
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

Movie *WatchList::get_all_movies_wl() {
    return this->movies.data();
}

void WatchList::save_file() {

}





