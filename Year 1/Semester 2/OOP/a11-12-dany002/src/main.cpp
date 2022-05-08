//
// Created by SenZatIonALL on 3/18/2022.
//
#pragma once

#include "mainwindow.h"
#include "Repository.h"
#include "Controller.h"
#include "UI.h"
#include "WatchList.h"
#include "TextFiles.h"
#include <iostream>
#include "HtmlFile.h"
#include "CsvFiles.h"
#include <fstream>
#include <QApplication>
#include <QPushButton>
#include <iostream>
#include <QGridLayout>
#include <QLabel>
#include <QListWidget>
#include <QLineEdit>
#include <QTextEdit>


int initGUICmpsAdmin( int argc, char **argv) {
    QApplication a(argc, argv);
    QWidget* window=new QWidget{};
    QVBoxLayout* vL=new QVBoxLayout{};
    window->setLayout(vL);
    QListWidget* list=new QListWidget{};


    /// read from the file and create a new item for each movie.
    std::ifstream file("wow");
    std::string line;
    int i = 0;
    if(file.is_open())
        while(std::getline(file, line)){
            QListWidgetItem* item = new QListWidgetItem(line.c_str());
            QFont font("Courier", 20, 10, true);
            item->setFont(font);
            list->insertItem(i, item);
        }

    vL->addWidget(list);
    /// MENU
    QWidget* options_window=new QWidget{};
    QGridLayout* options_grid=new QGridLayout{};
    options_window->setLayout(options_grid);
    /// add movie
    QLabel* title_label=new QLabel{"&Title:"};
    QLineEdit* lineEdit=new QLineEdit{};
    title_label->setBuddy(lineEdit);
    QLabel* genre_label=new QLabel{"&Genre:"};
    QLineEdit* lineEdit2=new QLineEdit{};
    genre_label->setBuddy(lineEdit2);
    QLabel* year_of_release_label=new QLabel{"&Year of release:"};
    QLineEdit* lineEdit3=new QLineEdit{};
    year_of_release_label->setBuddy(lineEdit3);
    QLabel* number_of_likes_label=new QLabel{"&Number of likes:"};
    QLineEdit* lineEdit4=new QLineEdit{};
    number_of_likes_label->setBuddy(lineEdit4);
    QLabel* trailer_label=new QLabel{"&Trailer:"};
    QLineEdit* lineEdit5=new QLineEdit{};
    trailer_label->setBuddy(lineEdit5);
    QPushButton* add_movie_btn=new QPushButton{"Add movie"};
    options_grid->addWidget(title_label, 0, 0, 1, 1);
    options_grid->addWidget(lineEdit,1,0,1,1);
    options_grid->addWidget(year_of_release_label, 2, 0, 1, 1);
    options_grid->addWidget(lineEdit3,3,0,1,1);
    options_grid->addWidget(genre_label, 4, 0, 1, 1);
    options_grid->addWidget(lineEdit2,5,0,1,1);
    options_grid->addWidget(number_of_likes_label, 6, 0, 1, 1);
    options_grid->addWidget(lineEdit4,7,0,1,1);
    options_grid->addWidget(trailer_label, 8, 0, 1, 1);
    options_grid->addWidget(lineEdit5,9,0,1,1);
    options_grid->addWidget(add_movie_btn,10,0,1,1);
    /// remove movie
    QLabel* title_remove=new QLabel{"&Title to remove:"};
    QLineEdit* lineEdit6=new QLineEdit{};
    title_remove->setBuddy(lineEdit6);
    QPushButton* remove_movie_btn=new QPushButton{"Remove movie"};
    options_grid->addWidget(title_remove, 0, 1, 1, 1);
    options_grid->addWidget(lineEdit6,1,1,1,1);
    options_grid->addWidget(remove_movie_btn, 2, 1, 1, 1);
    /// update movie
    QLabel* title_label_update=new QLabel{"Title:"};
    QLineEdit* lineEditUpdate=new QLineEdit{};
    title_label->setBuddy(lineEdit);
    QLabel* genre_label_update=new QLabel{"Genre:"};
    QLineEdit* lineEdit2Update=new QLineEdit{};
    genre_label->setBuddy(lineEdit2);
    QLabel* year_of_release_label_update=new QLabel{"Year of release:"};
    QLineEdit* lineEdit3Update=new QLineEdit{};
    year_of_release_label->setBuddy(lineEdit3);
    QLabel* number_of_likes_label_update=new QLabel{"Number of likes:"};
    QLineEdit* lineEdit4Update=new QLineEdit{};
    number_of_likes_label->setBuddy(lineEdit4);
    QLabel* trailer_label_update=new QLabel{"Trailer:"};
    QLineEdit* lineEdit5Update=new QLineEdit{};
    trailer_label->setBuddy(lineEdit5);
    QPushButton* add_movie_btnUpdate=new QPushButton{"Update movie"};
    options_grid->addWidget(title_label_update, 0, 3, 1, 1);
    options_grid->addWidget(lineEditUpdate,1,3,1,1);
    options_grid->addWidget(year_of_release_label_update, 2, 3, 1, 1);
    options_grid->addWidget(lineEdit3Update,3,3,1,1);
    options_grid->addWidget(genre_label_update, 4, 3, 1, 1);
    options_grid->addWidget(lineEdit2Update,5,3,1,1);
    options_grid->addWidget(number_of_likes_label_update, 6, 3, 1, 1);
    options_grid->addWidget(lineEdit4Update,7,3,1,1);
    options_grid->addWidget(trailer_label_update, 8, 3, 1, 1);
    options_grid->addWidget(lineEdit5Update,9,3,1,1);
    options_grid->addWidget(add_movie_btnUpdate, 10, 3, 1, 1);
    vL->addWidget(options_window);
    window->resize(1200,1200);
    window->show();
    return a.exec();
}


int initGUICmpsUser( int argc, char **argv) {
    QApplication a(argc, argv);
    QWidget* window=new QWidget{};
    QGridLayout* gL=new QGridLayout{};
    window->setLayout(gL);
    QTextEdit* dog_info=new QTextEdit{};
    dog_info->setText("The movies will appear in a magical way right here after you use the filter button cuz that's why I created it.");

    QPushButton* next_button=new QPushButton{"next movie"};
    QPushButton* add_watch_list=new QPushButton{"add in watch list"};
    QPushButton* reset_movie_iteration=new QPushButton{"reset movie iteration"};
    QPushButton* reset_watch_list=new QPushButton{"reset watch list"};
    QPushButton* display_watch_list=new QPushButton{"display watch list"};
    QPushButton* save_watch_list=new QPushButton{"save watch list"};
    QLabel* genre_filter=new QLabel{"&->Genre filter value"};
    QLineEdit* genre_filter_edit=new QLineEdit{};
    genre_filter->setBuddy(genre_filter_edit);
    QPushButton* set_filters=new QPushButton{"Set the entered filters"};

    gL->addWidget(dog_info,0,0,1,1);
    gL->addWidget(next_button,0,1,1,1);
    gL->addWidget(add_watch_list, 0, 2, 1, 1);
    gL->addWidget(reset_movie_iteration, 0, 3, 1, 1);
    gL->addWidget(reset_watch_list, 1, 1, 1, 1);
    gL->addWidget(display_watch_list, 1, 2, 1, 1);
    gL->addWidget(save_watch_list, 1, 3, 1, 1);
    gL->addWidget(genre_filter, 2, 3, 1, 1);
    gL->addWidget(genre_filter_edit, 2, 0, 1, 3);
    gL->addWidget(set_filters,4,0,1,3);
    window->resize(1200,1200);
    window->show();
    return a.exec();
}


int main(int argc, char** argv){
    /*
    std::cout << "Are you an admin or a user? ";
    std::string admin_user;
    std::cin >> admin_user;
    if(admin_user == "admin"){
        std::string file_name;
        std::cout << "What is the file name of the database? \n";
        std::cin >> file_name;

        std::string type;
        std::cout << "Choose between HTML and CSV \n";
        std::cin >> type;
        std::string name;
        std::cout << "What is the file name? (Type it without the extension.)\n";
        std::cin >> name;
        name += '.';
        name += type;
        WatchList *watch_list;
        if(type == "HTML") {
            HtmlFile h(name);
            watch_list = &h;
            TextFiles repo(file_name);
            Controller control(repo, watch_list);
            UI ui(control);
            ui.run_command_for_admin();
        }
        else
        {
            CsvFiles c(name);
            watch_list = &c;
            TextFiles repo(file_name);
            Controller control(repo, watch_list);
            UI ui(control);
            ui.run_command_for_admin();
        }
    }
    else{
        std::cout << "Do you want to open a saved watch list for you?";
        std::string yep_or_no;
        if(yep_or_no == "yes"){
            std::cout << "What is the extension of the file? HTML or CSV?";
            std::string html_or_csv;
            if(html_or_csv == "HTML"){
                std::string file;
                std::cout << "What is the file? Type it without the extension";
                std::cin >> file;
                file += ".HTML";
                std::ifstream new_file(file);
                if(new_file.is_open());
                else
                    std::cout << "The given file doesn't exist.";
            }
            else{
                std::string file;
                std::cout << "What is the file? Type it without the extension";
                std::cin >> file;
                file += ".CSV";
                std::ifstream new_file(file);
                if(new_file.is_open());
                else
                    std::cout << "The given file doesn't exist.";
            }
            std::string yep_or_nooo;
            std::cout << "Do you want to continue with the program? Or that's more than enough for you? Yes or No";
            if(yep_or_nooo == "No")
                return 0;
        }

        std::string file_name;
        std::cout << "What is the file name of the database? \n";
        std::cin >> file_name;

        std::string type;
        std::cout << "Choose between HTML and CSV \n";
        std::cin >> type;
        std::string name;
        std::cout << "What is the file name? (Type it without the extension.)\n";
        std::cin >> name;
        name += '.';
        name += type;
        WatchList *watch_list;
        if(type == "HTML") {
            HtmlFile h(name);
            watch_list = &h;
            TextFiles repo(file_name);
            Controller control(repo, watch_list);
            UI ui(control);
            ui.run_command_for_user();
        }
        else
        {
            CsvFiles c(name);
            watch_list = &c;
            TextFiles repo(file_name);
            Controller control(repo, watch_list);
            UI ui(control);
            ui.run_command_for_user();
        }
    }
    */

    WatchList *watch_list;
    HtmlFile h("test.HTML");
    watch_list = &h;
    TextFiles repo("wow");
    Controller control(repo, watch_list);
    //GUI gui(control);
    std::cout << "Hi are you an admin or a user? \n";
    std::string admin_user;
    std::cin >> admin_user;
    if(admin_user == "admin")
        initGUICmpsAdmin(argc, argv);
    else
        initGUICmpsUser(argc, argv);


    return 0;


}