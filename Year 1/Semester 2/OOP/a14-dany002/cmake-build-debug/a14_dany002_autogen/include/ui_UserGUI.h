/********************************************************************************
** Form generated from reading UI file 'usergui.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_USERGUI_H
#define UI_USERGUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_usergui
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QFormLayout *formLayout;
    QLabel *label;
    QLineEdit *Genre_lineEdit;
    QTableWidget *movie_listWidget;
    QTableWidget *watch_list_tableWidget;
    QHBoxLayout *horizontalLayout;
    QPushButton *play_Button;
    QPushButton *Add_Button;
    QPushButton *Csv_Button;
    QPushButton *Delete_Button;
    QPushButton *Like_Button;
    QPushButton *Html_Button;
    QPushButton *Undo_Button;
    QPushButton *Redo_Button;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *usergui)
    {
        if (usergui->objectName().isEmpty())
            usergui->setObjectName(QString::fromUtf8("usergui"));
        usergui->resize(696, 621);
        centralwidget = new QWidget(usergui);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        formLayout = new QFormLayout();
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));

        formLayout->setWidget(0, QFormLayout::LabelRole, label);

        Genre_lineEdit = new QLineEdit(centralwidget);
        Genre_lineEdit->setObjectName(QString::fromUtf8("Genre_lineEdit"));

        formLayout->setWidget(0, QFormLayout::FieldRole, Genre_lineEdit);


        verticalLayout->addLayout(formLayout);

        movie_listWidget = new QTableWidget(centralwidget);
        if (movie_listWidget->columnCount() < 5)
            movie_listWidget->setColumnCount(5);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        movie_listWidget->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        movie_listWidget->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        movie_listWidget->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        movie_listWidget->setHorizontalHeaderItem(3, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        movie_listWidget->setHorizontalHeaderItem(4, __qtablewidgetitem4);
        movie_listWidget->setObjectName(QString::fromUtf8("movie_listWidget"));

        verticalLayout->addWidget(movie_listWidget);

        watch_list_tableWidget = new QTableWidget(centralwidget);
        if (watch_list_tableWidget->columnCount() < 5)
            watch_list_tableWidget->setColumnCount(5);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        watch_list_tableWidget->setHorizontalHeaderItem(0, __qtablewidgetitem5);
        QTableWidgetItem *__qtablewidgetitem6 = new QTableWidgetItem();
        watch_list_tableWidget->setHorizontalHeaderItem(1, __qtablewidgetitem6);
        QTableWidgetItem *__qtablewidgetitem7 = new QTableWidgetItem();
        watch_list_tableWidget->setHorizontalHeaderItem(2, __qtablewidgetitem7);
        QTableWidgetItem *__qtablewidgetitem8 = new QTableWidgetItem();
        watch_list_tableWidget->setHorizontalHeaderItem(3, __qtablewidgetitem8);
        QTableWidgetItem *__qtablewidgetitem9 = new QTableWidgetItem();
        watch_list_tableWidget->setHorizontalHeaderItem(4, __qtablewidgetitem9);
        if (watch_list_tableWidget->rowCount() < 6)
            watch_list_tableWidget->setRowCount(6);
        QTableWidgetItem *__qtablewidgetitem10 = new QTableWidgetItem();
        watch_list_tableWidget->setVerticalHeaderItem(0, __qtablewidgetitem10);
        QTableWidgetItem *__qtablewidgetitem11 = new QTableWidgetItem();
        watch_list_tableWidget->setVerticalHeaderItem(1, __qtablewidgetitem11);
        QTableWidgetItem *__qtablewidgetitem12 = new QTableWidgetItem();
        watch_list_tableWidget->setVerticalHeaderItem(2, __qtablewidgetitem12);
        QTableWidgetItem *__qtablewidgetitem13 = new QTableWidgetItem();
        watch_list_tableWidget->setVerticalHeaderItem(3, __qtablewidgetitem13);
        QTableWidgetItem *__qtablewidgetitem14 = new QTableWidgetItem();
        watch_list_tableWidget->setVerticalHeaderItem(4, __qtablewidgetitem14);
        QTableWidgetItem *__qtablewidgetitem15 = new QTableWidgetItem();
        watch_list_tableWidget->setVerticalHeaderItem(5, __qtablewidgetitem15);
        watch_list_tableWidget->setObjectName(QString::fromUtf8("watch_list_tableWidget"));

        verticalLayout->addWidget(watch_list_tableWidget);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        play_Button = new QPushButton(centralwidget);
        play_Button->setObjectName(QString::fromUtf8("play_Button"));

        horizontalLayout->addWidget(play_Button);

        Add_Button = new QPushButton(centralwidget);
        Add_Button->setObjectName(QString::fromUtf8("Add_Button"));

        horizontalLayout->addWidget(Add_Button);

        Csv_Button = new QPushButton(centralwidget);
        Csv_Button->setObjectName(QString::fromUtf8("Csv_Button"));

        horizontalLayout->addWidget(Csv_Button);

        Delete_Button = new QPushButton(centralwidget);
        Delete_Button->setObjectName(QString::fromUtf8("Delete_Button"));

        horizontalLayout->addWidget(Delete_Button);

        Like_Button = new QPushButton(centralwidget);
        Like_Button->setObjectName(QString::fromUtf8("Like_Button"));

        horizontalLayout->addWidget(Like_Button);

        Html_Button = new QPushButton(centralwidget);
        Html_Button->setObjectName(QString::fromUtf8("Html_Button"));

        horizontalLayout->addWidget(Html_Button);

        Undo_Button = new QPushButton(centralwidget);
        Undo_Button->setObjectName(QString::fromUtf8("Undo_Button"));

        horizontalLayout->addWidget(Undo_Button);

        Redo_Button = new QPushButton(centralwidget);
        Redo_Button->setObjectName(QString::fromUtf8("Redo_Button"));

        horizontalLayout->addWidget(Redo_Button);


        verticalLayout->addLayout(horizontalLayout);

        usergui->setCentralWidget(centralwidget);
        menubar = new QMenuBar(usergui);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 696, 22));
        usergui->setMenuBar(menubar);
        statusbar = new QStatusBar(usergui);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        usergui->setStatusBar(statusbar);

        retranslateUi(usergui);

        QMetaObject::connectSlotsByName(usergui);
    } // setupUi

    void retranslateUi(QMainWindow *usergui)
    {
        usergui->setWindowTitle(QCoreApplication::translate("usergui", "MainWindow", nullptr));
        label->setText(QCoreApplication::translate("usergui", "Genre", nullptr));
        QTableWidgetItem *___qtablewidgetitem = movie_listWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QCoreApplication::translate("usergui", "Title", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = movie_listWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QCoreApplication::translate("usergui", "Genre", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = movie_listWidget->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QCoreApplication::translate("usergui", "Trailer", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = movie_listWidget->horizontalHeaderItem(3);
        ___qtablewidgetitem3->setText(QCoreApplication::translate("usergui", "Year of release", nullptr));
        QTableWidgetItem *___qtablewidgetitem4 = movie_listWidget->horizontalHeaderItem(4);
        ___qtablewidgetitem4->setText(QCoreApplication::translate("usergui", "Number of likes", nullptr));
        QTableWidgetItem *___qtablewidgetitem5 = watch_list_tableWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem5->setText(QCoreApplication::translate("usergui", "Title", nullptr));
        QTableWidgetItem *___qtablewidgetitem6 = watch_list_tableWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem6->setText(QCoreApplication::translate("usergui", "Genre", nullptr));
        QTableWidgetItem *___qtablewidgetitem7 = watch_list_tableWidget->horizontalHeaderItem(2);
        ___qtablewidgetitem7->setText(QCoreApplication::translate("usergui", "Trailer", nullptr));
        QTableWidgetItem *___qtablewidgetitem8 = watch_list_tableWidget->horizontalHeaderItem(3);
        ___qtablewidgetitem8->setText(QCoreApplication::translate("usergui", "Year of release", nullptr));
        QTableWidgetItem *___qtablewidgetitem9 = watch_list_tableWidget->horizontalHeaderItem(4);
        ___qtablewidgetitem9->setText(QCoreApplication::translate("usergui", "Number of likes", nullptr));
        QTableWidgetItem *___qtablewidgetitem10 = watch_list_tableWidget->verticalHeaderItem(0);
        ___qtablewidgetitem10->setText(QCoreApplication::translate("usergui", "1", nullptr));
        QTableWidgetItem *___qtablewidgetitem11 = watch_list_tableWidget->verticalHeaderItem(1);
        ___qtablewidgetitem11->setText(QCoreApplication::translate("usergui", "2", nullptr));
        QTableWidgetItem *___qtablewidgetitem12 = watch_list_tableWidget->verticalHeaderItem(2);
        ___qtablewidgetitem12->setText(QCoreApplication::translate("usergui", "3", nullptr));
        QTableWidgetItem *___qtablewidgetitem13 = watch_list_tableWidget->verticalHeaderItem(3);
        ___qtablewidgetitem13->setText(QCoreApplication::translate("usergui", "4", nullptr));
        QTableWidgetItem *___qtablewidgetitem14 = watch_list_tableWidget->verticalHeaderItem(4);
        ___qtablewidgetitem14->setText(QCoreApplication::translate("usergui", "5", nullptr));
        QTableWidgetItem *___qtablewidgetitem15 = watch_list_tableWidget->verticalHeaderItem(5);
        ___qtablewidgetitem15->setText(QCoreApplication::translate("usergui", "6", nullptr));
        play_Button->setText(QCoreApplication::translate("usergui", "Play", nullptr));
        Add_Button->setText(QCoreApplication::translate("usergui", "Add", nullptr));
        Csv_Button->setText(QCoreApplication::translate("usergui", "CSV", nullptr));
        Delete_Button->setText(QCoreApplication::translate("usergui", "Delete", nullptr));
        Like_Button->setText(QCoreApplication::translate("usergui", "Like", nullptr));
        Html_Button->setText(QCoreApplication::translate("usergui", "HTML", nullptr));
        Undo_Button->setText(QCoreApplication::translate("usergui", "Undo", nullptr));
        Redo_Button->setText(QCoreApplication::translate("usergui", "Redo", nullptr));
    } // retranslateUi

};

namespace Ui {
    class usergui: public Ui_usergui {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_USERGUI_H
