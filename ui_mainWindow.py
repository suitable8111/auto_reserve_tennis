# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowwozwnc.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QLabel, QListView, QPushButton, QSizePolicy,
    QWidget)

class Ui_Auto(object):
    def setupUi(self, Auto):
        if not Auto.objectName():
            Auto.setObjectName(u"Auto")
        Auto.resize(648, 587)
        self.actionButton = QPushButton(Auto)
        self.actionButton.setObjectName(u"actionButton")
        self.actionButton.setGeometry(QRect(500, 120, 100, 32))
        self.label = QLabel(Auto)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 150, 151, 20))
        self.label_3 = QLabel(Auto)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 80, 58, 16))
        self.fail_list_view = QListView(Auto)
        self.fail_list_view.setObjectName(u"fail_list_view")
        self.fail_list_view.setGeometry(QRect(40, 180, 571, 171))
        self.mon_chk_box = QCheckBox(Auto)
        self.mon_chk_box.setObjectName(u"mon_chk_box")
        self.mon_chk_box.setGeometry(QRect(40, 110, 51, 20))
        self.tue_chk_box = QCheckBox(Auto)
        self.tue_chk_box.setObjectName(u"tue_chk_box")
        self.tue_chk_box.setGeometry(QRect(80, 110, 51, 20))
        self.wed_chk_box = QCheckBox(Auto)
        self.wed_chk_box.setObjectName(u"wed_chk_box")
        self.wed_chk_box.setGeometry(QRect(120, 110, 41, 20))
        self.thu_chk_box = QCheckBox(Auto)
        self.thu_chk_box.setObjectName(u"thu_chk_box")
        self.thu_chk_box.setGeometry(QRect(160, 110, 41, 20))
        self.fri_chk_box = QCheckBox(Auto)
        self.fri_chk_box.setObjectName(u"fri_chk_box")
        self.fri_chk_box.setGeometry(QRect(200, 110, 41, 20))
        self.sat_chk_box = QCheckBox(Auto)
        self.sat_chk_box.setObjectName(u"sat_chk_box")
        self.sat_chk_box.setGeometry(QRect(240, 110, 41, 20))
        self.sun_chk_box = QCheckBox(Auto)
        self.sun_chk_box.setObjectName(u"sun_chk_box")
        self.sun_chk_box.setGeometry(QRect(280, 110, 51, 20))
        self.time_combo_box = QComboBox(Auto)
        self.time_combo_box.setObjectName(u"time_combo_box")
        self.time_combo_box.setGeometry(QRect(420, 80, 181, 31))
        self.label_4 = QLabel(Auto)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(430, 50, 58, 16))
        self.pass_list_view = QListView(Auto)
        self.pass_list_view.setObjectName(u"pass_list_view")
        self.pass_list_view.setGeometry(QRect(40, 400, 571, 161))
        self.label_2 = QLabel(Auto)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 370, 151, 20))
        self.jungu1_chk_box = QCheckBox(Auto)
        self.jungu1_chk_box.setObjectName(u"jungu1_chk_box")
        self.jungu1_chk_box.setGeometry(QRect(40, 50, 51, 20))
        self.label_5 = QLabel(Auto)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 20, 71, 16))
        self.jungu2_chk_box = QCheckBox(Auto)
        self.jungu2_chk_box.setObjectName(u"jungu2_chk_box")
        self.jungu2_chk_box.setGeometry(QRect(100, 50, 51, 20))
        self.jungu3_chk_box = QCheckBox(Auto)
        self.jungu3_chk_box.setObjectName(u"jungu3_chk_box")
        self.jungu3_chk_box.setGeometry(QRect(160, 50, 51, 20))
        self.jungu4_chk_box = QCheckBox(Auto)
        self.jungu4_chk_box.setObjectName(u"jungu4_chk_box")
        self.jungu4_chk_box.setGeometry(QRect(220, 50, 51, 20))

        self.retranslateUi(Auto)

        QMetaObject.connectSlotsByName(Auto)
    # setupUi

    def retranslateUi(self, Auto):
        Auto.setWindowTitle(QCoreApplication.translate("Auto", u"Dialog", None))
        self.actionButton.setText(QCoreApplication.translate("Auto", u"\uc790\ub3d9\uc608\uc57d", None))
        self.label.setText(QCoreApplication.translate("Auto", u"\uc2e4\ud328\ud55c \ub0a0\uc9dc", None))
        self.label_3.setText(QCoreApplication.translate("Auto", u"\uc694\uc77c", None))
        self.mon_chk_box.setText(QCoreApplication.translate("Auto", u"\uc6d4", None))
        self.tue_chk_box.setText(QCoreApplication.translate("Auto", u"\ud654", None))
        self.wed_chk_box.setText(QCoreApplication.translate("Auto", u"\uc218", None))
        self.thu_chk_box.setText(QCoreApplication.translate("Auto", u"\ubaa9", None))
        self.fri_chk_box.setText(QCoreApplication.translate("Auto", u"\uae08", None))
        self.sat_chk_box.setText(QCoreApplication.translate("Auto", u"\ud1a0", None))
        self.sun_chk_box.setText(QCoreApplication.translate("Auto", u"\uc77c", None))
        self.label_4.setText(QCoreApplication.translate("Auto", u"\uc2dc\uac04\ub300", None))
        self.label_2.setText(QCoreApplication.translate("Auto", u"\uc131\uacf5\ud55c \ub0a0\uc9dc", None))
        self.jungu1_chk_box.setText(QCoreApplication.translate("Auto", u"\uc815\uad6c1", None))
        self.label_5.setText(QCoreApplication.translate("Auto", u"\ud14c\ub2c8\uc2a4 \uc7a5\uc18c", None))
        self.jungu2_chk_box.setText(QCoreApplication.translate("Auto", u"\uc815\uad6c2", None))
        self.jungu3_chk_box.setText(QCoreApplication.translate("Auto", u"\uc815\uad6c3", None))
        self.jungu4_chk_box.setText(QCoreApplication.translate("Auto", u"\uc815\uad6c4", None))
    # retranslateUi

