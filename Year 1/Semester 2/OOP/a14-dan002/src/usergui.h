//
// Created by moldo on 5/26/2022.
//

#ifndef A14_DANY002_USERGUI_H
#define A14_DANY002_USERGUI_H

#include <QMainWindow>
#include "ui_UserGUI.h"
#include "Controller.h"


class UserGUI : public QMainWindow {
Q_OBJECT

public:
    explicit UserGUI(Controller contr, QWidget *parent = nullptr);



private:
    Ui::usergui ui;
    Controller control;
    void populate_list();
    void populate_watch_list();
    void play_trailer();
    void connectSignalsAndSlots();
    void add_movie();
    void delete_movie();
    void like_movie();
    void open_csv();
    void open_html();
    int get_selected_index() const;
};


#endif //A14_DANY002_USERGUI_H
