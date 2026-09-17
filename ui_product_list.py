# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productslist.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_PeoductList(object):
    def setupUi(self, PeoductList):
        if not PeoductList.objectName():
            PeoductList.setObjectName(u"PeoductList")
        PeoductList.resize(800, 600)
        self.centralwidget = QWidget(PeoductList)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 110, 781, 471))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(17, 21, 761, 71))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_3)

        PeoductList.setCentralWidget(self.centralwidget)

        self.retranslateUi(PeoductList)

        QMetaObject.connectSlotsByName(PeoductList)
    # setupUi

    def retranslateUi(self, PeoductList):
        PeoductList.setWindowTitle(QCoreApplication.translate("PeoductList", u"ProductsList", None))
        self.pushButton_2.setText(QCoreApplication.translate("PeoductList", u"Add", None))
        self.pushButton.setText(QCoreApplication.translate("PeoductList", u"Edit", None))
        self.pushButton_3.setText(QCoreApplication.translate("PeoductList", u"Delete", None))
    # retranslateUi

