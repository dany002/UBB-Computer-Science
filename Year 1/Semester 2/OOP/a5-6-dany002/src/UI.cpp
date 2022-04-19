//
// Created by moldo on 3/18/2022.
//
#pragma once
#include "UI.h"
#include <iostream>
#include <string>
#include "Exceptions.h"

UI::UI(const Controller& control) {
    this->control = control;
}

void UI::initial_list() {
    this->control.add_movie_admin("Matrix", "SF", "https://www.youtube.com/watch?v=m8e-FF8MsqU", 1999, 500);
    this->control.add_movie_admin("Batman v Superman", "SF", "https://www.youtube.com/watch?v=0WWzgGyAH6Y", 2016, 300);
    this->control.add_movie_admin("Bruce Almighty", "Comedy", "https://www.youtube.com/watch?v=fe-luzrqWSk", 2003, 398);
    this->control.add_movie_admin("Ted", "Comedy", "https://www.youtube.com/watch?v=9fbo_pQvU7M", 2012, 1000);
    this->control.add_movie_admin("Ted 2", "Comedy", "https://www.youtube.com/watch?v=S3AVcCggRnU", 2015, 2183);
    this->control.add_movie_admin("Pirates of the Caribbean", "Action", "https://www.youtube.com/watch?v=naQr0uTrH_s", 2003, 580);
    this->control.add_movie_admin("Fast and Furious 9", "Action", "https://www.youtube.com/watch?v=aSiDu3Ywi8E", 2021, 200);
    this->control.add_movie_admin("Inception", "SF", "https://www.youtube.com/watch?v=YoHD9XEInc0", 2010, 743);
    this->control.add_movie_admin("The Wolf of Wall Street", "Action", "https://www.youtube.com/watch?v=iszwuX1AK6A", 2013, 1534);
    this->control.add_movie_admin("Countdown", "Horror", "https://www.youtube.com/watch?v=TZsgNH17_X4", 2019, 59);
}

void UI::print_menu_for_admin() {
    std::cout << "What do you want to do? \nType 'add' to add a new movie. \nType 'delete' to delete a movie.\nType 'update' to update a movie.\n"
                 "Type 'print' to see all the movies.\nType 'switch' to go in user mode.\nType 'exit' to exit the program.\n";
}

void UI::add_movie_admin() {
    std::string title, genre, trailer;
    int year_of_release, number_of_likes;

    std::cout << "What is the title? \n";
    std::cin >> title;
    std::cout << "What is the genre? \n";
    std::cin >> genre;
    std::cout << "What is the trailer? \n";
    std::cin >> trailer;
    std::cout << "What is the year of release? \n";
    std::cin >> year_of_release;
    std::cout << "What is the number of likes? \n";
    std::cin >> number_of_likes;
    try{
        this->control.add_movie_admin(title, genre, trailer, year_of_release, number_of_likes);
    }

    catch(IntegerError const& i){
        std::cout << i.what() << std::endl;
    }
    catch(MovieAlreadyExists const& m){
        std::cout << m.what() << std::endl;
    }
}

void UI::delete_movie_admin() {
    std::string title;
    std::cout << "What is the title? \n";
    std::cin >> title;
    try{
        this->control.remove_movie_admin(title);
    }
    catch(MovieDoesntExist const& m){
        std::cout << m.what() << std::endl;
    }
}

void UI::update_movie_admin() {
    std::string title, trailer;
    std::cout << "What is the title for the movie that you want to update? \n";
    std::cin >> title;
    std::cout << "What is the new trailer?";
    std::cin >> trailer;
    try{
        this->control.update_movie_admin(title, trailer);
    }

    catch(MovieDoesntExist const& m){
        std::cout << m.what() << std::endl;
    }
}

void UI::print_movies_admin() {
    for(int i = 0; i < this->control.get_size(); i++){
        std::cout << "Title: " << this->control.get_movie_by_index(i).get_title() << "    ";
        std::cout << "Genre: " << this->control.get_movie_by_index(i).get_genre() << "    ";
        std::cout << "Year of release: " << this->control.get_movie_by_index(i).get_year_of_release() << "\n";
        std::cout << "Number of likes: " << this->control.get_movie_by_index(i).get_number_of_likes() << "    ";
        std::cout << "Trailer: " << this->control.get_movie_by_index(i).get_trailer() << '\n';
        std::cout << "\n";
    }
}


void UI::run_command_for_admin() {
    while(true){
        std::string command;
        print_menu_for_admin();
        std::cin >> command;
        if(command == "add")
            add_movie_admin();

        if(command == "delete")
            delete_movie_admin();

        if(command == "update")
            update_movie_admin();

        if(command == "switch")
            run_command_for_user();
        if(command == "print")
            print_movies_admin();

        if(command == "exit")
            exit(0);
    }
}

void UI::watch_movie() {
    std::string title;
    see_movies_from_watch_list();
    std::cout << "What movie do you want to see from the watch list? Give me the title.\n";
    std::cin >> title;
    if(title == "exit")
        run_command_for_user();
    if(!this->control.check_movie_in_watch_list(title)){
         std::cout << "The movie doesnt exist. or type 'exit' \n";
         watch_movie();
    }
    std::string yes_or_no;
    std::cout << "Movie is playing.. \n";
    std::cout << "Do you want to delete the movie from the watch list?\n";
    std::cin >> yes_or_no;
    if(yes_or_no == "yes"){
        this->control.delete_movie_from_watch_list(title);
        std::string new_yes_or_no;
        std::cout << "Do you want to rate with a like the movie?\n";
        std::cin >> new_yes_or_no;
        if(new_yes_or_no == "yes")
            this->control.increment_likes_for_a_movie(title);
    }
}

void UI::see_movies_from_watch_list() {
    for(int i = 0; i < this->control.get_size_watch_list(); i++){
        std::cout << "Title: " << this->control.get_movie_watch_list_by_index(i).get_title() << "    ";
        std::cout << "Genre: " << this->control.get_movie_watch_list_by_index(i).get_genre() << "    ";
        std::cout << "Year of release: " << this->control.get_movie_watch_list_by_index(i).get_year_of_release() << "\n";
        std::cout << "Number of likes: " << this->control.get_movie_watch_list_by_index(i).get_number_of_likes() << "    ";
        std::cout << "Trailer: " << this->control.get_movie_watch_list_by_index(i).get_trailer() << '\n';
        std::cout << "\n";
    }
}

int UI::play_trailer(const Movie& m) {
    std::cout << "Do you want to play the trailer? yes or no? \n";
    std::string yes_or_no;
    std::cin >> yes_or_no;
    if(yes_or_no == "yes"){
        std::cout << "Trailer is playing. \n";
        std::string like_or_no;
        std::cout << "Did you like the trailer?. \n";
        std::cin >> like_or_no;
        std::cout << "Do you want to add the movie in the watch list? \n";
        std::string add_or_not;
        std::cin >> add_or_not;
        if(add_or_not == "yes")
            this->control.add_movie_watch_list(m);
        if(add_or_not == "no")
            return 1;
        std::cout << "Do you want to continue? \n";
        std::cin >> add_or_not;
        if(add_or_not == "yes")
            return 1;
        else
            return 0;
        }
    else{
        return 1;
    }
}

void UI::play_movies(){
    std::cout << "What is the genre? \n";
    std::string genre;
    std::cin >> genre;
    int x;
    int i = 0;
    while(i < control.get_size_for_a_genre(genre)){
        Movie m = this->control.get_movie_index_genre(genre, i);
        std::cout << "Title: " << m.get_title() << "    ";
        std::cout << "Genre: " << m.get_genre() << "    ";
        std::cout << "Year of release: " << m.get_year_of_release() << "\n";
        std::cout << "Number of likes: " << m.get_number_of_likes() << "    ";
        std::cout << "Trailer: " << m.get_trailer() << '\n';
        x = play_trailer(m);
        if(x == 0)
            break;

        std::cout << "\n";
        i++;
        std::cout << control.get_size_for_a_genre(genre) << std::endl;
        if(i == control.get_size_for_a_genre(genre))
            i = 0;
    }
}

void UI::print_menu_for_user() {
    std::cout << "What do you want to do? \nType 'genre' to see the movies for a given genre.\nType 'see' to see the watch list."
                 "\nType 'switch' to go in admin mode.\nType 'watch' to watch a movie.\nType 'exit' to exit.\n";
}

void UI::run_command_for_user() {
    while(true){
        std::string command;
        print_menu_for_user();
        std::cin >> command;
        if(command == "genre")
            play_movies();
        if(command == "switch")
            run_command_for_admin();
        if(command == "see")
            see_movies_from_watch_list();
        if(command == "watch")
            watch_movie();
        if(command == "exit")
            exit(0);
    }
}


void UI::run_command() {
    initial_list();
    std::cout << "Hi there! Are you an admin or a user?";
    std::string mode;
    std::cin >> mode;
    if(mode == "admin" or mode == "administrator")
        run_command_for_admin();
    else if(mode == "user")
        run_command_for_user();

}




UI::~UI() = default;
