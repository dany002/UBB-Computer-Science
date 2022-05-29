/********************************************************************************
** Form generated from reading UI file 'admin_or_user.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ADMIN_OR_USER_H
#define UI_ADMIN_OR_USER_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Admin_or_user
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QPushButton *admin_button;
    QPushButton *user_button;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *Admin_or_user)
    {
        if (Admin_or_user->objectName().isEmpty())
            Admin_or_user->setObjectName(QString::fromUtf8("Admin_or_user"));
        Admin_or_user->resize(546, 217);
        centralwidget = new QWidget(Admin_or_user);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        admin_button = new QPushButton(centralwidget);
        admin_button->setObjectName(QString::fromUtf8("admin_button"));

        horizontalLayout->addWidget(admin_button);

        user_button = new QPushButton(centralwidget);
        user_button->setObjectName(QString::fromUtf8("user_button"));

        horizontalLayout->addWidget(user_button);


        verticalLayout->addLayout(horizontalLayout);

        Admin_or_user->setCentralWidget(centralwidget);
        menubar = new QMenuBar(Admin_or_user);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 546, 22));
        Admin_or_user->setMenuBar(menubar);
        statusbar = new QStatusBar(Admin_or_user);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        Admin_or_user->setStatusBar(statusbar);

        retranslateUi(Admin_or_user);

        QMetaObject::connectSlotsByName(Admin_or_user);
    } // setupUi

    void retranslateUi(QMainWindow *Admin_or_user)
    {
        Admin_or_user->setWindowTitle(QCoreApplication::translate("Admin_or_user", "MainWindow", nullptr));
        admin_button->setText(QCoreApplication::translate("Admin_or_user", "Admin", nullptr));
        user_button->setText(QCoreApplication::translate("Admin_or_user", "User", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Admin_or_user: public Ui_Admin_or_user {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ADMIN_OR_USER_H
