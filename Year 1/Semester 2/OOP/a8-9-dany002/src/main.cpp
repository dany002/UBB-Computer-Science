//
// Created by SenZatIonALL on 3/18/2022.
//
#pragma once


#include "Repository.h"
#include "Controller.h"
#include "UI.h"
#include "WatchList.h"
#include "TextFiles.h"
#include <iostream>
#include "HtmlFile.h"
#include "CsvFiles.h"
#include <fstream>
#include <cstdlib>

int main(){

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
        std::cout << "Do you want to open a saved watch list for you? \n";
        std::string yep_or_no;
        std::cin >> yep_or_no;
        if(yep_or_no == "yes"){
            std::cout << "What is the extension of the file? HTML or CSV?";
            std::string html_or_csv;
            std::cin >> html_or_csv;
            if(html_or_csv == "HTML"){
                std::string file;
                std::cout << "What is the file? Type it without the extension";
                std::cin >> file;
                file += ".HTML";
                std::ifstream new_file(file);
                if(new_file.is_open()) {
                    std::string command = "xdg-open ";
                    command += file;

                    system(command.c_str());
                }
                else
                    std::cout << "The given file doesn't exist.";
            }
            else{
                std::string file;
                std::cout << "What is the file? Type it without the extension \n";
                std::cin >> file;
                file += ".CSV";
                std::ifstream new_file(file);
                if(new_file.is_open()){
                    std::string command = "kate "; // or "xdg-open "
                    command += file;
                    system(command.c_str());
                }
                else
                    std::cout << "The given file doesn't exist. \n";
            }
            std::string yep_or_nooo;
            std::cout << "Do you want to continue with the program? Or that's more than enough for you? Yes or No \n";
            std::cin >> yep_or_nooo;
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


    return 0;
}