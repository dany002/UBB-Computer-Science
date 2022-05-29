/********************************************************************************
** Form generated from reading UI file 'WatchListGUI.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WATCHLISTGUI_H
#define UI_WATCHLISTGUI_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_WatchListGUIClass
{
public:
    QAction *actionadmin_mode;
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_2;
    QVBoxLayout *verticalLayout;
    QListWidget *movie_list_Widget;
    QFormLayout *formLayout;
    QLabel *label;
    QLineEdit *title_lineEdit;
    QLabel *label_2;
    QLineEdit *genre_lineEdit;
    QLabel *label_3;
    QLineEdit *link_lineEdit;
    QLabel *label_4;
    QLineEdit *year_lineEdit_2;
    QLabel *label_5;
    QLineEdit *likes_lineEdit;
    QHBoxLayout *horizontalLayout;
    QPushButton *add_Button;
    QPushButton *delete_Button;
    QPushButton *update_Button;
    QPushButton *undo_Button;
    QPushButton *redo_Button;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *WatchListGUIClass)
    {
        if (WatchListGUIClass->objectName().isEmpty())
            WatchListGUIClass->setObjectName(QString::fromUtf8("WatchListGUIClass"));
        WatchListGUIClass->resize(421, 310);
        actionadmin_mode = new QAction(WatchListGUIClass);
        actionadmin_mode->setObjectName(QString::fromUtf8("actionadmin_mode"));
        centralwidget = new QWidget(WatchListGUIClass);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout_2 = new QVBoxLayout(centralwidget);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        movie_list_Widget = new QListWidget(centralwidget);
        movie_list_Widget->setObjectName(QString::fromUtf8("movie_list_Widget"));

        verticalLayout->addWidget(movie_list_Widget);

        formLayout = new QFormLayout();
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));

        formLayout->setWidget(0, QFormLayout::LabelRole, label);

        title_lineEdit = new QLineEdit(centralwidget);
        title_lineEdit->setObjectName(QString::fromUtf8("title_lineEdit"));

        formLayout->setWidget(0, QFormLayout::FieldRole, title_lineEdit);

        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_2);

        genre_lineEdit = new QLineEdit(centralwidget);
        genre_lineEdit->setObjectName(QString::fromUtf8("genre_lineEdit"));

        formLayout->setWidget(1, QFormLayout::FieldRole, genre_lineEdit);

        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        formLayout->setWidget(2, QFormLayout::LabelRole, label_3);

        link_lineEdit = new QLineEdit(centralwidget);
        link_lineEdit->setObjectName(QString::fromUtf8("link_lineEdit"));

        formLayout->setWidget(2, QFormLayout::FieldRole, link_lineEdit);

        label_4 = new QLabel(centralwidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        formLayout->setWidget(3, QFormLayout::LabelRole, label_4);

        year_lineEdit_2 = new QLineEdit(centralwidget);
        year_lineEdit_2->setObjectName(QString::fromUtf8("year_lineEdit_2"));

        formLayout->setWidget(3, QFormLayout::FieldRole, year_lineEdit_2);

        label_5 = new QLabel(centralwidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        formLayout->setWidget(4, QFormLayout::LabelRole, label_5);

        likes_lineEdit = new QLineEdit(centralwidget);
        likes_lineEdit->setObjectName(QString::fromUtf8("likes_lineEdit"));

        formLayout->setWidget(4, QFormLayout::FieldRole, likes_lineEdit);


        verticalLayout->addLayout(formLayout);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        add_Button = new QPushButton(centralwidget);
        add_Button->setObjectName(QString::fromUtf8("add_Button"));

        horizontalLayout->addWidget(add_Button);

        delete_Button = new QPushButton(centralwidget);
        delete_Button->setObjectName(QString::fromUtf8("delete_Button"));

        horizontalLayout->addWidget(delete_Button);

        update_Button = new QPushButton(centralwidget);
        update_Button->setObjectName(QString::fromUtf8("update_Button"));

        horizontalLayout->addWidget(update_Button);

        undo_Button = new QPushButton(centralwidget);
        undo_Button->setObjectName(QString::fromUtf8("undo_Button"));

        horizontalLayout->addWidget(undo_Button);

        redo_Button = new QPushButton(centralwidget);
        redo_Button->setObjectName(QString::fromUtf8("redo_Button"));

        horizontalLayout->addWidget(redo_Button);


        verticalLayout->addLayout(horizontalLayout);


        verticalLayout_2->addLayout(verticalLayout);

        WatchListGUIClass->setCentralWidget(centralwidget);
        menubar = new QMenuBar(WatchListGUIClass);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 421, 22));
        WatchListGUIClass->setMenuBar(menubar);
        statusbar = new QStatusBar(WatchListGUIClass);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        WatchListGUIClass->setStatusBar(statusbar);

        retranslateUi(WatchListGUIClass);

        QMetaObject::connectSlotsByName(WatchListGUIClass);
    } // setupUi

    void retranslateUi(QMainWindow *WatchListGUIClass)
    {
        WatchListGUIClass->setWindowTitle(QCoreApplication::translate("WatchListGUIClass", "MainWindow", nullptr));
        actionadmin_mode->setText(QCoreApplication::translate("WatchListGUIClass", "admin_mode", nullptr));
        label->setText(QCoreApplication::translate("WatchListGUIClass", "Title", nullptr));
        label_2->setText(QCoreApplication::translate("WatchListGUIClass", "Genre", nullptr));
        label_3->setText(QCoreApplication::translate("WatchListGUIClass", "Link", nullptr));
        label_4->setText(QCoreApplication::translate("WatchListGUIClass", "Year of release", nullptr));
        label_5->setText(QCoreApplication::translate("WatchListGUIClass", "Likes", nullptr));
        add_Button->setText(QCoreApplication::translate("WatchListGUIClass", "Add", nullptr));
        delete_Button->setText(QCoreApplication::translate("WatchListGUIClass", "Delete", nullptr));
        update_Button->setText(QCoreApplication::translate("WatchListGUIClass", "Update", nullptr));
        undo_Button->setText(QCoreApplication::translate("WatchListGUIClass", "Undo", nullptr));
#if QT_CONFIG(shortcut)
        undo_Button->setShortcut(QCoreApplication::translate("WatchListGUIClass", "Ctrl+Z", nullptr));
#endif // QT_CONFIG(shortcut)
        redo_Button->setText(QCoreApplication::translate("WatchListGUIClass", "Redo", nullptr));
#if QT_CONFIG(shortcut)
        redo_Button->setShortcut(QCoreApplication::translate("WatchListGUIClass", "Ctrl+Y", nullptr));
#endif // QT_CONFIG(shortcut)
    } // retranslateUi

};

namespace Ui {
    class WatchListGUIClass: public Ui_WatchListGUIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WATCHLISTGUI_H
