//
// Created by moldo on 5/25/2022.
//

#ifndef A14_DANY002_WATCHLISTGUI_H
#define A14_DANY002_WATCHLISTGUI_H

#include <QMainWindow>
#include "ui_WatchListGUI.h"
#include "Controller.h"

class WatchListGUI : public QMainWindow {
Q_OBJECT

public:
    WatchListGUI(Controller control, QWidget *parent = nullptr);

private:
    Controller control;
    Ui::WatchListGUIClass ui;

    void populate_list();
    void connectSignalsAndSlots();
    int get_selected_index() const;
    void add_movie();
    void delete_movie();
    void update_movie();
    void undo();
    void redo();
};


#endif //A14_DANY002_WATCHLISTGUI_H
