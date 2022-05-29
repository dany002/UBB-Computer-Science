//
// Created by moldo on 4/6/2022.
//

#include "TextFiles.h"
#include "Exceptions.h"
#include <iostream>
#include <fstream>
#include "Movie.h"

void TextFiles::add_movie(const Movie &m) {
    try{
        Repository::add_movie(m);
    }
    catch(RepositoryException const&) {
        throw RepositoryException();
    }
    this->save_file();
}

void TextFiles::delete_movie(const std::string &title) {
    try {
        Repository::delete_movie(title);
    }
    catch(RepositoryException const&){
        throw RepositoryException();
    }
    this->save_file();
}

void TextFiles::update_movie_trailer(const std::string &title, const std::string &new_trailer) {
    try{
    Repository::update_movie_trailer(title, new_trailer);
    }
    catch(RepositoryException const&){
        throw RepositoryException();
    }
    this->save_file();
}

void TextFiles::save_file() {
    std::ofstream file;
    file.open(this->file_name);

    for(auto & movie : movies)
        file << movie.get_title() << "," << movie.get_genre() << "," << movie.get_trailer() << "," << movie.get_number_of_likes() << "," << movie.get_year_of_release() << std::endl;
    file.close();
}


TextFiles::TextFiles(const std::string &file_name) {
    this->file_name = file_name;
    std::ifstream file;
    file.open(this->file_name);
    if(file){
        this->load_file();
    }
    else
        this->save_file();
}

TextFiles::~TextFiles() {
}

void TextFiles::load_file() {
    std::string line;
    std::ifstream file(this->file_name);
    std::string title, genre, trailer, likes, year;
    title = "";
    genre = "";
    trailer = "";
    likes = "";
    year = "";
    if(file.is_open())
        while(std::getline(file, line)) {
            int count = 0;
            int pos = 0;
            for (int i = 0; i < line.length(); i++) {
                if (line[i] == ',') {
                    if (count == 0)
                        for (int j = pos; j < i; j++)
                            title += line[j];
                    else if (count == 1)
                        for (int j = pos; j < i; j++)
                            genre += line[j];
                    else if (count == 2)
                        for (int j = pos; j < i; j++)
                            trailer += line[j];
                    else if (count == 3)
                        for (int j = pos; j < i; j++)
                            likes += line[j];
                    count++;
                    pos = i + 1;
                }
            }
            for (int j = pos; j < line.length(); j++)
                year += line[j];

            Repository::add_movie(Movie(title, genre, std::stoi(year), std::stoi(likes), trailer));
            trailer = "";
            genre = "";
            title = "";
            likes = "";
            year = "";

        }

    file.close();
}

TextFiles::TextFiles(const TextFiles &txt) {
    this->file_name = txt.file_name;
}

TextFiles::TextFiles() {

}

void TextFiles::increment_likes(const std::string &title) {
    Repository::increment_likes(title);
    this->save_file();
}

Movie TextFiles::get_specific_movie(const std::string &title) {
    return Repository::get_specific_movie(title);
}
