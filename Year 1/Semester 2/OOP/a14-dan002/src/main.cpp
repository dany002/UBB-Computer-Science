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
#include <fstream>
#include "WatchListGUI.h"
#include "admin_or_user.h"
/*
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QFormLayout>
*/

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
    Undo undo;
    Undo redo;
    Controller control(repo, watch_list, undo, redo);
    admin_or_user gui(control);
    //gui.show();
    //WatchListGUI gui(control);
    //gui.show();


    return a.exec();
}


int main(int argc, char** argv){

    initial_settings(argc, argv);
    return 0;


}