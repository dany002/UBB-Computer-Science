//
// Created by moldo on 5/27/2022.
//

#ifndef A14_DANY002_UNDO_H
#define A14_DANY002_UNDO_H
#include <vector>
#include "Movie.h"

class Undo {
private:
    std::vector<Movie> movies;
public:
    Undo();
    ~Undo();
    void add_movie(Movie movie);
    void delete_movie(Movie movie);
    void update_movie(Movie movie);
    std::vector<Movie> get_all();
    void pop_last();
};


#endif //A14_DANY002_UNDO_H
