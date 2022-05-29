//
// Created by moldo on 5/26/2022.
//

#ifndef A14_DANY002_ADMIN_OR_USER_H
#define A14_DANY002_ADMIN_OR_USER_H

#include <QMainWindow>
#include "ui_admin_or_user.h"
#include "Controller.h"
#include "WatchListGUI.h"
#include "usergui.h"

class admin_or_user : public QMainWindow {
Q_OBJECT

public:
    explicit admin_or_user(Controller control, QWidget *parent = nullptr);


private:
    Ui::Admin_or_user ui;
    WatchListGUI* admin_gui;
    UserGUI* user_gui;
    Controller controll;

    void connectButtons();
    void admin_time();
    void user_time();
};


#endif //A14_DANY002_ADMIN_OR_USER_H
