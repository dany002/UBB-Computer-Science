//
// Created by moldo on 5/26/2022.
//

// You may need to build the project (run Qt uic code generator) to get "ui_UserGUI.h" resolved

#include "usergui.h"
#include "ui_UserGUI.h"
#include <QItemDelegate>
#include <QMessageBox>
#include <windows.h>
#include <shellapi.h>


UserGUI::UserGUI(Controller contr, QWidget *parent) :
        QMainWindow(parent), control{contr}{
    ui.setupUi(this);
    this->populate_list();
    this->connectSignalsAndSlots();
}

void UserGUI::populate_list() {
    for(int i = 0; i < this->ui.movie_listWidget->rowCount(); i++){
        QTableWidgetItem* item;
        for(int j = 0; j < this->ui.movie_listWidget->columnCount(); j++){
            item = new QTableWidgetItem;
            item->setText("");
            this->ui.movie_listWidget->setItem(i, j, item);
        }
    }
    std::vector<Movie> all_movies = this->control.get_movies();

    this->ui.movie_listWidget->setRowCount(all_movies.size());

    for(int i = 0; i < all_movies.size(); i++){

        QTableWidgetItem* item = new QTableWidgetItem;
        item->setText(QString::fromStdString(all_movies[i].get_title()));
        this->ui.movie_listWidget->setItem(i, 0, item);
        QTableWidgetItem* item2 = new QTableWidgetItem;
        item2->setText(QString::fromStdString(all_movies[i].get_genre()));
        this->ui.movie_listWidget->setItem(i, 1, item2);
        QTableWidgetItem* item3 = new QTableWidgetItem;
        item3->setText(QString::fromStdString(all_movies[i].get_trailer()));
        this->ui.movie_listWidget->setItem(i, 2, item3);
        QTableWidgetItem* item4 = new QTableWidgetItem;
        item4->setText(QString::number(all_movies[i].get_year_of_release()));
        this->ui.movie_listWidget->setItem(i, 3, item4);
        QTableWidgetItem* item5 = new QTableWidgetItem;
        item5->setText(QString::number(all_movies[i].get_number_of_likes()));
        this->ui.movie_listWidget->setItem(i, 4, item5);

    }
    this->ui.movie_listWidget->setAlternatingRowColors(true);
}

void UserGUI::populate_watch_list() {
    for(int i = 0; i < this->ui.watch_list_tableWidget->rowCount(); i++){
        QTableWidgetItem* item;
        for(int j = 0; j < this->ui.watch_list_tableWidget->columnCount(); j++){
            item = new QTableWidgetItem;
            item->setText("");
            this->ui.watch_list_tableWidget->setItem(i, j, item);
        }
    }
    std::vector<Movie> all_movies = this->control.get_all_movies_from_wl();

    this->ui.watch_list_tableWidget->setRowCount(all_movies.size());

    for(int i = 0; i < all_movies.size(); i++){

        QTableWidgetItem* item = new QTableWidgetItem;
        item->setText(QString::fromStdString(all_movies[i].get_title()));
        this->ui.watch_list_tableWidget->setItem(i, 0, item);
        QTableWidgetItem* item2 = new QTableWidgetItem;
        item2->setText(QString::fromStdString(all_movies[i].get_genre()));
        this->ui.watch_list_tableWidget->setItem(i, 1, item2);
        QTableWidgetItem* item3 = new QTableWidgetItem;
        item3->setText(QString::fromStdString(all_movies[i].get_trailer()));
        this->ui.watch_list_tableWidget->setItem(i, 2, item3);
        QTableWidgetItem* item4 = new QTableWidgetItem;
        item4->setText(QString::number(all_movies[i].get_year_of_release()));
        this->ui.watch_list_tableWidget->setItem(i, 3, item4);
        QTableWidgetItem* item5 = new QTableWidgetItem;
        item5->setText(QString::number(all_movies[i].get_number_of_likes()));
        this->ui.watch_list_tableWidget->setItem(i, 4, item5);

    }
    this->ui.watch_list_tableWidget->setAlternatingRowColors(true);
}

void UserGUI::play_trailer() {
    this->ui.Add_Button->setEnabled(true);
    int selected_index = this->get_selected_index();
    if(selected_index < 0){
        QMessageBox::critical(this, "Error", "No movie was selected.");
        return ;
    }
    Movie m = this->control.get_movies()[selected_index];
    std::string link = "start ";
    link += m.get_trailer();
    system(link.c_str());
}

void UserGUI::connectSignalsAndSlots() {
    this->ui.Add_Button->setEnabled(false);
    this->ui.Delete_Button->setEnabled(false);
    this->ui.Like_Button->setEnabled(false);
    QObject::connect(this->ui.Add_Button, &QPushButton::clicked, this, &UserGUI::add_movie);
    QObject::connect(this->ui.play_Button, &QPushButton::clicked, this, &UserGUI::play_trailer);
    QObject::connect(this->ui.Delete_Button, &QPushButton::clicked, this, &UserGUI::delete_movie);
    QObject::connect(this->ui.Csv_Button, &QPushButton::clicked, this, &UserGUI::open_csv);
    QObject::connect(this->ui.Html_Button, &QPushButton::clicked, this, &UserGUI::open_html);
    QObject::connect(this->ui.Like_Button, &QPushButton::clicked, this, &UserGUI::like_movie);
}

void UserGUI::add_movie() {
    int selected_index = this->get_selected_index();
    if(selected_index < 0){
        QMessageBox::critical(this, "Error", "No movie was selected.");
        return ;
    }
    this->ui.Add_Button->setEnabled(false);
    this->ui.Delete_Button->setEnabled(true);
    Movie m = this->control.get_movies()[selected_index];
    this->control.add_movie_watch_list(m);
    this->populate_watch_list();
}

int UserGUI::get_selected_index() const {
    QModelIndexList selected_indexes = this->ui.movie_listWidget->selectionModel()->selectedIndexes();
    if(selected_indexes.empty())
        return -1;
    int selected_index = selected_indexes.at(0).row();
    return selected_index;
}

void UserGUI::delete_movie() {
    QModelIndexList selected_indexes = this->ui.watch_list_tableWidget->selectionModel()->selectedIndexes();
    if(selected_indexes.empty()){
        QMessageBox::critical(this, "Error", "No movie was selected.");
        return ;
    }
    this->ui.Delete_Button->setEnabled(false);
    this->ui.Like_Button->setEnabled(true);
    int selected_index = selected_indexes.at(0).row();
    Movie m = this->control.get_all_movies_from_wl()[selected_index];
    this->control.delete_movie_from_watch_list(m.get_title());
    this->populate_watch_list();
}

void UserGUI::like_movie() {
    QModelIndexList selected_indexes = this->ui.watch_list_tableWidget->selectionModel()->selectedIndexes();
    if(selected_indexes.empty()){
        QMessageBox::critical(this, "Error", "No movie was selected.");
        return ;
    }
    this->ui.Like_Button->setEnabled(false);
    int selected_index = selected_indexes.at(0).row();
    Movie m = this->control.get_all_movies_from_wl()[selected_index];
    this->control.increment_likes_for_a_movie(m.get_title());
    this->populate_watch_list();
    this->populate_list();
}

void UserGUI::open_csv() {
    CsvFiles a("etc.csv");
    a.save_f(this->control.get_all_movies_from_wl());
    ShellExecute(nullptr, nullptr, L"etc.csv", nullptr, nullptr, SW_SHOW);
}

void UserGUI::open_html() {
    HtmlFile a("etc.html");
    a.save_f(this->control.get_all_movies_from_wl());
    ShellExecute(nullptr, nullptr, L"etc.html", nullptr, nullptr, SW_SHOW);
}





