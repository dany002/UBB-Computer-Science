//
// Created by moldo on 5/11/2022.
//

#include "GUI.h"
#include <QtWidgets/QMessageBox>


GUI::GUI(Controller control) {
    this->control = control;
    this->setWindowTitle("Movies");
    auto* layout_wrapper = new QVBoxLayout{ this };

    auto* layout_widget = new QWidget;
    this->filter_items_edit = new QLineEdit{};

    layout_wrapper->addWidget(filter_items_edit);
    layout_wrapper->addWidget(layout_widget);

    auto* layout = new QVBoxLayout{ layout_widget };

    auto* left_side = new QWidget;
    layout->addWidget(left_side);
    auto* left_v_box = new QVBoxLayout(left_side);

    auto* movies_list_name = new QLabel{ "Movies list"};
    left_v_box->addWidget(movies_list_name);
    this->movies_list = new QListWidget;
    this->movies_list->setSelectionMode(QAbstractItemView::SingleSelection);
    left_v_box->addWidget(this->movies_list);

    auto* right_side = new QWidget;
    layout->addWidget(right_side);
    auto* right_v_box = new QVBoxLayout(right_side);

    auto* movies_data_widget = new QWidget;
    auto* fields_form = new QFormLayout{ movies_data_widget };
    right_v_box->addWidget(movies_data_widget);

    this->title_edit = new QLineEdit;
    auto* title_label = new QLabel{"Title:"};
    fields_form->addRow(title_label, this->title_edit);

    this->genre_edit = new QLineEdit;
    auto* genre_label = new QLabel{"Genre:"};
    fields_form->addRow(genre_label, this->genre_edit);

    this->trailer_edit = new QLineEdit;
    auto* trailer_label = new QLabel{"Trailer:"};
    fields_form->addRow(trailer_label, this->trailer_edit);

    this->year_edit = new QLineEdit;
    auto* year_label = new QLabel{"Year:"};
    fields_form->addRow(year_label, this->year_edit);

    this->likes_edit = new QLineEdit;
    auto* likes_label = new QLabel{"Likes:"};
    fields_form->addRow(likes_label, this->likes_edit);

    auto* buttons_layout = new QHBoxLayout;
    this->add_button = new QPushButton("Add");
    this->delete_button = new QPushButton("Delete");
    this->update_button = new QPushButton("Update");
    this->clear_button = new QPushButton("Clear");
    buttons_layout->addWidget(this->add_button);
    buttons_layout->addWidget(this->delete_button);
    buttons_layout->addWidget(this->update_button);
    buttons_layout->addWidget(this->clear_button);
    right_v_box->addLayout(buttons_layout);


    connect(this->filter_items_edit, &QLineEdit::textChanged, this, &GUI::filter_list);
    connect(this->movies_list, &QListWidget::itemSelectionChanged, this, &GUI::select_item);
    connect(this->add_button, &QPushButton::clicked, this, &GUI::add_to_list);
    connect(this->update_button, &QPushButton::clicked, this, &GUI::update_item);
    connect(this->delete_button, &QPushButton::clicked, this, &GUI::delete_item);
    connect(this->clear_button, &QPushButton::clicked, this, &GUI::clear_selected_item);

    this->initial_list();

}

void GUI::initial_list() {
    if(this->movies_list->count() > 0){
        this->movies_list->clear();
        movies_list_vector.clear();
    }
    for(const auto& movie : this->control.get_movies()){
        QString movie_in_list = QString::fromStdString(movie.toString());
        auto* mov = new QListWidgetItem{ movie_in_list };
        movies_list_vector.push_back(movie);
        this->movies_list->addItem(mov);
    }
}

void GUI::filter_list() {
    if(this->movies_list->count() > 0){
        this->movies_list->clear();
        movies_list_vector.clear();
    }
    for (const auto& movie : this->control.get_movies(this->filter_items_edit->text().toStdString())){
        QString movie_in_list = QString::fromStdString(movie.toString());
        auto* mov = new QListWidgetItem{ movie_in_list };
        movies_list_vector.push_back(movie);
        this->movies_list->addItem(mov);
    }
}

void GUI::add_to_list() {
    QString title_QString = title_edit->text();
    QString genre_QString = genre_edit->text();
    QString trailer_QString = trailer_edit->text();
    QString likes_QString = likes_edit->text();
    QString year_QString = year_edit->text();

    int year = std::stoi(year_QString.toStdString());
    int likes = std::stoi(likes_QString.toStdString());

    this->control.add_movie_admin(title_QString.toStdString(), genre_QString.toStdString(), trailer_QString.toStdString(), year, likes);
    this->filter_list();

    title_edit->clear();
    genre_edit->clear();
    trailer_edit->clear();
    likes_edit->clear();
    year_edit->clear();
}

void GUI::clear_selected_item() {
    movies_list->clearSelection();
    title_edit->clear();
    genre_edit->clear();
    trailer_edit->clear();
    likes_edit->clear();
    year_edit->clear();
}

void GUI::select_item() {
    auto movie = movies_list_vector[movies_list->currentRow()];
    title_edit->setText(QString::fromStdString(movie.get_title()));
    genre_edit->setText(QString::fromStdString(movie.get_genre()));
    trailer_edit->setText(QString::fromStdString(movie.get_trailer()));
    likes_edit->setText(QString::fromStdString(std::to_string(movie.get_number_of_likes())));
    year_edit->setText(QString::fromStdString(std::to_string(movie.get_year_of_release())));

}

void GUI::delete_item() {
    auto movie = movies_list_vector[movies_list->currentRow()];
    this->control.remove_movie_admin(movie.get_title());
    movies_list->clearSelection();
    title_edit->clear();
    genre_edit->clear();
    trailer_edit->clear();
    likes_edit->clear();
    year_edit->clear();
    this->filter_list();
}

void GUI::update_item() {
    QString title_QString = title_edit->text();
    QString trailer_QString = trailer_edit->text();

    this->control.update_movie_admin(title_QString.toStdString(), trailer_QString.toStdString());
    this->filter_list();
}




