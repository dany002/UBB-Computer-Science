//
// Created by moldo on 5/11/2022.
//

#ifndef A11_12_DANY002_GUI_H
#define A11_12_DANY002_GUI_H

#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QFormLayout>
#include "Controller.h"


class GUI : public QWidget{
    Q_OBJECT
private:
    QListWidget* movies_list;
    std::vector<Movie> movies_list_vector;
    QListWidget* watch_list;
    std::vector<Movie> watch_list_vector;
    Movie last_deleted;
    QPushButton* like_button;
    QPushButton* add_button;
    QPushButton* delete_button;
    QPushButton* update_button;
    QPushButton* clear_button;
    QLineEdit* filter_items_edit;
    QLineEdit* title_edit;
    QLineEdit* genre_edit;
    QLineEdit* trailer_edit;
    QLineEdit* year_edit;
    QLineEdit* likes_edit;
    Controller control;

public:
    GUI(Controller control);
    void initial_list();
    void filter_list();
    void add_to_list();
    void clear_selected_item();
    void select_item();
    void delete_item();
    void update_item();
    void admin_mode();
    void user_mode();
    void double_clicked_item();
    void filter_list_user();
    void open_html();
    void open_csv();
    void add_to_watch_list();
    void delete_from_watch_list();
    void like_movie();
};


#endif //A11_12_DANY002_GUI_H
