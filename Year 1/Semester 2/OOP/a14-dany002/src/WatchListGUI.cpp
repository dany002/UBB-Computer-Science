//
// Created by moldo on 5/25/2022.
//

// You may need to build the project (run Qt uic code generator) to get "ui_WatchListGUI.h" resolved

#include <QMessageBox>
#include "WatchListGUI.h"
#include "ui_WatchListGUI.h"
#include "Exceptions.h"
#include <QShortcut>

WatchListGUI::WatchListGUI(Controller control, QWidget *parent) :
        QMainWindow(parent), control{control}{
    ui.setupUi(this);
    this->populate_list();
    this->connectSignalsAndSlots();

}



void WatchListGUI::populate_list() {
    this->ui.movie_list_Widget->clear();
    std::vector<Movie> all_movies = this->control.get_movies();
    for(Movie& m : all_movies)
        this->ui.movie_list_Widget->addItem(QString::fromStdString(m.toString()));
}

void WatchListGUI::connectSignalsAndSlots() {
    QObject::connect(this->ui.add_Button, &QPushButton::clicked, this, &WatchListGUI::add_movie);
    QObject::connect(this->ui.delete_Button, &QPushButton::clicked,this, &WatchListGUI::delete_movie);
    QObject::connect(this->ui.update_Button, &QPushButton::clicked, this, &WatchListGUI::update_movie);
    QObject::connect(this->ui.undo_Button, &QPushButton::clicked, this, &WatchListGUI::undo);
    QObject::connect(this->ui.redo_Button, &QPushButton::clicked, this, &WatchListGUI::redo);
}

int WatchListGUI::get_selected_index() const {
    QModelIndexList selected_indexes = this->ui.movie_list_Widget->selectionModel()->selectedIndexes();
    if(selected_indexes.size() == 0){
        this->ui.title_lineEdit->clear();
        this->ui.genre_lineEdit->clear();
        this->ui.likes_lineEdit->clear();
        this->ui.link_lineEdit->clear();
        this->ui.year_lineEdit_2->clear();
        return -1;
    }
    int selected_index = selected_indexes.at(0).row();
    return selected_index;
}

void WatchListGUI::add_movie() {
    std::string title, genre, likes, link, year;
    title = this->ui.title_lineEdit->text().toStdString();
    genre = this->ui.genre_lineEdit->text().toStdString();
    link = this->ui.link_lineEdit->text().toStdString();
    year = this->ui.year_lineEdit_2->text().toStdString();
    likes = this->ui.likes_lineEdit->text().toStdString();
    int like = std::stoi(likes);
    int years = std::stoi(year);
    this->control.add_movie_admin(title, genre, link, years, like);
    this->populate_list();
    int last_elem = this->control.get_movies().size() - 1;
    this->ui.movie_list_Widget->setCurrentRow(last_elem);
}

void WatchListGUI::delete_movie() {
    int selected_index = this->get_selected_index();
    if(selected_index < 0){
        QMessageBox::critical(this, "Error", "No movie was selected!");
        return;
    }

    Movie m = this->control.get_movies()[selected_index];
    this->control.remove_movie_admin(m.get_title());
    this->populate_list();

}

void WatchListGUI::update_movie() {

    std::string title = this->ui.title_lineEdit->text().toStdString();
    std::string link = this->ui.link_lineEdit->text().toStdString();
    try {
        this->control.update_movie_admin(title, link);
    }
    catch(MovieDoesntExist const&){
        QMessageBox::critical(this, "Error", "The given movie doesn't exist!");
        return;
    }
    this->populate_list();
}

void WatchListGUI::undo() {
    try{
        this->control.undo();
    }
    catch(UndoException const&){
        QMessageBox::critical(this, "Error", "You cant undo anymore!");
        return;
    }
    this->populate_list();
}

void WatchListGUI::redo() {
    try{
        this->control.redo();
    }
    catch(RedoException const&){
        QMessageBox::critical(this, "Error", "You cant redo anymore!");
        return;
    }
    this->populate_list();
}





