//
// Created by moldo on 4/6/2022.
//

#include "HtmlFile.h"
#include <iostream>
#include <fstream>

HtmlFile::HtmlFile(const std::string &file_name) {
    this->text_file = file_name;
    this->save_file();
}

HtmlFile::~HtmlFile() {

}

HtmlFile::HtmlFile() {

}

HtmlFile::HtmlFile(const HtmlFile &txt) {
    this->text_file = txt.text_file;
}

void HtmlFile::add_movie(const Movie &m) {
    WatchList::add_movie(m);
    this->save_file();
}

void HtmlFile::delete_movie_from_watch_list(const std::string &title) {
    WatchList::delete_movie_from_watch_list(title);
    this->save_file();
}

void HtmlFile::save_file() {
    std::ofstream file;
    file.open(this->text_file);
    file << "<!DOCTYPE html>\n";
    file << "<html>\n";
    file << "<head>\n";
    file << "\t<title>Watch list</title>\n";
    file << "</head>\n";
    file << "<body>\n";
    file << "<table border=\"1\">\n";
    file << "\t<tr>\n";
    file << "\t\t<td>Title</td>\n";
    file << "\t\t<td>Genre</td>\n";
    file << "\t\t<td>Year of release</td>\n";
    file << "\t\t<td>Number of likes</td>\n";
    file << "\t\t<td>Trailer</td>\n";
    file << "\t</tr>\n";
    for(auto & movie: movies){
        file << "\t<tr>\n";
        file << "\t\t<td>" << movie.get_title() << "</td>\n";
        file << "\t\t<td>" << movie.get_genre() << "</td>\n";
        file << "\t\t<td>" << movie.get_year_of_release() << "</td>\n";
        file << "\t\t<td>" << movie.get_number_of_likes() << "</td>\n";
        file << "\t\t<td><a href=\"" << movie.get_trailer() << "\">Link</a></td>\n";
        file << "\t</tr>\n";
    }
    file << "</table>\n";
    file << "</body>\n";
    file << "</html>";
    file.close();
}

void HtmlFile::load_file() {
    std::string line;
    std::ifstream file(this->text_file);
    std::string title, genre, trailer, likes, year;
    title = "";
    genre = "";
    trailer = "";
    likes = "";
    year = "";
    int count = 1;
    if(file.is_open()){
        while(std::getline(file, line) && count < 14)
            count++;
        count = -1;
        while(std::getline(file, line)){

            if(line == "</table>")
                break;
            if(line == "\t<tr>" || line == "\t</tr>"){
                count = 0;
                title = "";
                genre = "";
                trailer = "";
                likes = "";
                year = "";
            }
            else if(line[line.length()-2] == 'd') // It's the d from </td>
                count++;

            int start, final;
            if(count == 1 || count == 2 || count == 3 || count == 4) { // It means that we are on a field that it's not the link.
                for (int i = 0; i < line.length(); i++) {
                    if (line[i] == '/') { // It means that you are on </td>
                        final = i - 1;
                        break;
                    }
                    if (line[i] == '>')
                        start = i + 1; // It means that you are on <td>.
                }
            }
            if(count == 1) { // It's the title.
                for (int i = start; i < final; i++)
                    title += line[i];
            }

            else if(count == 2) { // It s the genre.
                for (int i = start; i < final; i++)
                    genre += line[i];
            }
            else if(count == 3) {// It s the year.
                for (int i = start; i < final; i++)
                    year += line[i];
            }
            else if(count == 4) { // It s the number of likes.
                for (int i = start; i < final; i++)
                    likes += line[i];
            }
            else if(count == 5){
                start = -1;
                for (int i = 0; i < line.length(); i++) {
                    if(line[i] == '=' && start == -1) // it means we are on = from href= ( we care abt 1st = )
                        start = i + 2;
                    if(line[i] == 'L' && line[i+1] == 'i' && line[i+2] == 'n' && line[i+3] == 'k' && line[i+4] == '<') { // It means we are on Link</a>..
                        final = i - 2;
                        break;
                    }
                }

                for (int i = start; i < final; i++)
                    trailer += line[i];
                WatchList::add_movie(Movie(title, genre, std::stoi(year), std::stoi(likes), trailer));
            }
        }
    }

}

std::string HtmlFile::get_file_name() {
    return this->text_file;
}

void HtmlFile::save_f(const std::vector<Movie>& movi) {
    std::ofstream file;
    file.open(this->text_file);
    file << "<!DOCTYPE html>\n";
    file << "<html>\n";
    file << "<head>\n";
    file << "\t<title>Watch list</title>\n";
    file << "</head>\n";
    file << "<body>\n";
    file << "<table border=\"1\">\n";
    file << "\t<tr>\n";
    file << "\t\t<td>Title</td>\n";
    file << "\t\t<td>Genre</td>\n";
    file << "\t\t<td>Year of release</td>\n";
    file << "\t\t<td>Number of likes</td>\n";
    file << "\t\t<td>Trailer</td>\n";
    file << "\t</tr>\n";
    for(auto & movie: movi){
        file << "\t<tr>\n";
        file << "\t\t<td>" << movie.get_title() << "</td>\n";
        file << "\t\t<td>" << movie.get_genre() << "</td>\n";
        file << "\t\t<td>" << movie.get_year_of_release() << "</td>\n";
        file << "\t\t<td>" << movie.get_number_of_likes() << "</td>\n";
        file << "\t\t<td><a href=\"" << movie.get_trailer() << "\">Link</a></td>\n";
        file << "\t</tr>\n";
    }
    file << "</table>\n";
    file << "</body>\n";
    file << "</html>";
    file.close();
}


