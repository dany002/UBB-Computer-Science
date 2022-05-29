//
// Created by moldo on 5/26/2022.
//

// You may need to build the project (run Qt uic code generator) to get "ui_admin_or_user.h" resolved

#include "admin_or_user.h"
#include "ui_admin_or_user.h"
#include "WatchListGUI.h"
#include <iostream>


admin_or_user::admin_or_user(Controller ctrl, QWidget *parent) :
        QMainWindow(parent), controll{ctrl}{
    ui.setupUi(this);
    this->connectButtons();
    this->show();
}

void admin_or_user::connectButtons() {
    QObject::connect(this->ui.admin_button, &QPushButton::clicked, this, &admin_or_user::admin_time);
    QObject::connect(this->ui.user_button, &QPushButton::clicked, this, &admin_or_user::user_time);
}

void admin_or_user::admin_time() {
    admin_gui = new WatchListGUI(controll, this);
    admin_gui->show();

}

void admin_or_user::user_time() {
    user_gui = new UserGUI(controll, this);
    user_gui->show();
}



