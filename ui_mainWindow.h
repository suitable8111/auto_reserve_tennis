/********************************************************************************
** Form generated from reading UI file 'mainWindowhLPXMB.ui'
**
** Created by: Qt User Interface Compiler version 6.5.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef MAINWINDOWHLPXMB_H
#define MAINWINDOWHLPXMB_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDateEdit>
#include <QtWidgets/QDialog>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListView>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_Auto
{
public:
    QPushButton *actionButton;
    QDateEdit *reserveDate;
    QLineEdit *numberPeopleLabel;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QPushButton *actionButton2;
    QPushButton *actionButton3;
    QComboBox *departureComboBox;
    QComboBox *arriveralComboBox;
    QLabel *label_5;
    QListView *trainListView;
    QComboBox *timeComboBox;

    void setupUi(QDialog *Auto)
    {
        if (Auto->objectName().isEmpty())
            Auto->setObjectName("Auto");
        Auto->resize(658, 618);
        actionButton = new QPushButton(Auto);
        actionButton->setObjectName("actionButton");
        actionButton->setGeometry(QRect(110, 240, 100, 32));
        reserveDate = new QDateEdit(Auto);
        reserveDate->setObjectName("reserveDate");
        reserveDate->setGeometry(QRect(120, 120, 91, 31));
        numberPeopleLabel = new QLineEdit(Auto);
        numberPeopleLabel->setObjectName("numberPeopleLabel");
        numberPeopleLabel->setGeometry(QRect(120, 170, 161, 21));
        label = new QLabel(Auto);
        label->setObjectName("label");
        label->setGeometry(QRect(50, 120, 58, 16));
        label_2 = new QLabel(Auto);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(50, 170, 58, 16));
        label_3 = new QLabel(Auto);
        label_3->setObjectName("label_3");
        label_3->setGeometry(QRect(50, 50, 58, 16));
        label_4 = new QLabel(Auto);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(50, 80, 58, 16));
        actionButton2 = new QPushButton(Auto);
        actionButton2->setObjectName("actionButton2");
        actionButton2->setGeometry(QRect(103, 470, 100, 32));
        actionButton3 = new QPushButton(Auto);
        actionButton3->setObjectName("actionButton3");
        actionButton3->setGeometry(QRect(103, 500, 100, 32));
        departureComboBox = new QComboBox(Auto);
        departureComboBox->setObjectName("departureComboBox");
        departureComboBox->setGeometry(QRect(112, 40, 181, 32));
        arriveralComboBox = new QComboBox(Auto);
        arriveralComboBox->setObjectName("arriveralComboBox");
        arriveralComboBox->setGeometry(QRect(112, 80, 181, 32));
        label_5 = new QLabel(Auto);
        label_5->setObjectName("label_5");
        label_5->setGeometry(QRect(110, 440, 81, 20));
        trainListView = new QListView(Auto);
        trainListView->setObjectName("trainListView");
        trainListView->setGeometry(QRect(350, 20, 291, 571));
        timeComboBox = new QComboBox(Auto);
        timeComboBox->setObjectName("timeComboBox");
        timeComboBox->setGeometry(QRect(220, 120, 71, 31));

        retranslateUi(Auto);

        QMetaObject::connectSlotsByName(Auto);
    } // setupUi

    void retranslateUi(QDialog *Auto)
    {
        Auto->setWindowTitle(QCoreApplication::translate("Auto", "Dialog", nullptr));
        actionButton->setText(QCoreApplication::translate("Auto", "\354\260\276\354\225\204\353\263\264\352\270\260", nullptr));
        numberPeopleLabel->setText(QCoreApplication::translate("Auto", "1", nullptr));
        label->setText(QCoreApplication::translate("Auto", "\353\202\240\354\247\234", nullptr));
        label_2->setText(QCoreApplication::translate("Auto", "\354\235\270\354\233\220", nullptr));
        label_3->setText(QCoreApplication::translate("Auto", "\354\266\234\353\260\234\354\247\200", nullptr));
        label_4->setText(QCoreApplication::translate("Auto", "\353\252\251\354\240\201\354\247\200", nullptr));
        actionButton2->setText(QCoreApplication::translate("Auto", "\354\236\220\353\217\231\354\202\254\353\203\245", nullptr));
        actionButton3->setText(QCoreApplication::translate("Auto", "\354\202\254\353\203\245\354\244\221\354\247\200", nullptr));
        label_5->setText(QCoreApplication::translate("Auto", "\354\236\254\355\203\235 \354\236\220\353\217\231\354\202\254\353\203\245", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Auto: public Ui_Auto {};
} // namespace Ui

QT_END_NAMESPACE

#endif // MAINWINDOWHLPXMB_H
