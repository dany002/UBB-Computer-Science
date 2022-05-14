//
// Created by moldo on 4/7/2022.
//

#include "CsvFiles.h"
#include <iostream>
#include <fstream>


CsvFiles::CsvFiles(const std::string &text_file) {
    this->text_file = text_file;
    this->save_file();
}

CsvFiles::~CsvFiles() {

}

CsvFiles::CsvFiles() {

}

CsvFiles::CsvFiles(const CsvFiles &txt) {
    this->text_file = txt.text_file;
}

void CsvFiles::add_movie(const Movie &m) {
    WatchList::add_movie(m);
    this->save_file();
}

void CsvFiles::delete_movie_from_watch_list(const std::string &title) {
    WatchList::delete_movie_from_watch_list(title);
    this->save_file();
}

void CsvFiles::save_file(){
    std::ofstream file;
    file.open(this->text_file);
    for(auto & movie : movies)
        file << movie.get_title() << "," << movie.get_genre() << "," << movie.get_trailer() << "," << movie.get_number_of_likes() << "," << movie.get_year_of_release() << std::endl;
    file.close();
}

void CsvFiles::load_file() {
    std::string line;
    std::ifstream file(this->text_file);
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

            WatchList::add_movie(Movie(title, genre, std::stoi(year), std::stoi(likes), trailer));
            trailer = "";
            genre = "";
            title = "";
            likes = "";
            year = "";

        }

    file.close();
}

std::string CsvFiles::get_file_name() {
    return this->text_file;
}

void CsvFiles::save_f(const std::vector<Movie>& movi) {
    std::ofstream file;
    file.open(this->text_file);
    for(auto & movie : movi)
        file << movie.get_title() << "," << movie.get_genre() << "," << movie.get_trailer() << "," << movie.get_number_of_likes() << "," << movie.get_year_of_release() << std::endl;
    file.close();
}
