//
// Created by SenZatIonALL on 3/18/2022.
//
#pragma once

#include "Controller.h"
#include "WatchList.h"
#include "TextFiles.h"
#include <iostream>
#include "HtmlFile.h"
#include "CsvFiles.h"
#include "GUI.h"
#include <fstream>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QFormLayout>


int initial_settings(int argc, char** argv){
    QApplication a(argc, argv);
//    QWidget* layout_widget = new QWidget;
//    auto* layout = new QVBoxLayout{layout_widget};
//    layout_widget->resize(300, 100);
//    QLineEdit* text = new QLineEdit{};
//    layout->addWidget(layout_widget);
//    layout->addWidget(text);


    WatchList *watch_list;
    HtmlFile h("test.HTML");
    watch_list = &h;
    TextFiles repo("wow");
    Controller control(repo, watch_list);
    GUI gui{control};
    gui.show();
//    layout_widget->show();

    return a.exec();
}


int main(int argc, char** argv){

    initial_settings(argc, argv);
    return 0;

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



}