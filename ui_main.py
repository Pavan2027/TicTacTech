# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainrOdYED.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 600)
        MainWindow.setMinimumSize(QSize(720, 600))
        MainWindow.setMaximumSize(QSize(720, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.main_pg = QWidget()
        self.main_pg.setObjectName(u"main_pg")
        self.verticalLayout_2 = QVBoxLayout(self.main_pg)
        self.verticalLayout_2.setSpacing(40)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 20)
        self.label = QLabel(self.main_pg)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(30)

        self.verticalLayout_2.addWidget(self.label)

        self.pvp_change_btn = QPushButton(self.main_pg)
        self.pvp_change_btn.setObjectName(u"pvp_change_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pvp_change_btn.sizePolicy().hasHeightForWidth())
        self.pvp_change_btn.setSizePolicy(sizePolicy)
        self.pvp_change_btn.setMinimumSize(QSize(300, 100))
        self.pvp_change_btn.setMaximumSize(QSize(300, 100))
        font1 = QFont()
        font1.setPointSize(15)
        self.pvp_change_btn.setFont(font1)

        self.verticalLayout_2.addWidget(self.pvp_change_btn, 0, Qt.AlignHCenter)

        self.pva_change_btn = QPushButton(self.main_pg)
        self.pva_change_btn.setObjectName(u"pva_change_btn")
        self.pva_change_btn.setMinimumSize(QSize(300, 100))
        self.pva_change_btn.setMaximumSize(QSize(300, 100))
        self.pva_change_btn.setFont(font1)
        self.pva_change_btn.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.pva_change_btn, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.main_pg)
        self.pva_pg = QWidget()
        self.pva_pg.setObjectName(u"pva_pg")
        self.verticalLayout_4 = QVBoxLayout(self.pva_pg)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.pvabtn4 = QPushButton(self.pva_pg)
        self.pvabtn4.setObjectName(u"pvabtn4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.pvabtn4.sizePolicy().hasHeightForWidth())
        self.pvabtn4.setSizePolicy(sizePolicy1)
        self.pvabtn4.setMinimumSize(QSize(100, 100))
        font2 = QFont()
        font2.setPointSize(40)
        self.pvabtn4.setFont(font2)

        self.gridLayout_3.addWidget(self.pvabtn4, 1, 0, 1, 1)

        self.pvabtn3 = QPushButton(self.pva_pg)
        self.pvabtn3.setObjectName(u"pvabtn3")
        sizePolicy1.setHeightForWidth(self.pvabtn3.sizePolicy().hasHeightForWidth())
        self.pvabtn3.setSizePolicy(sizePolicy1)
        self.pvabtn3.setMinimumSize(QSize(100, 100))
        self.pvabtn3.setFont(font2)

        self.gridLayout_3.addWidget(self.pvabtn3, 0, 2, 1, 1)

        self.pvabtn1 = QPushButton(self.pva_pg)
        self.pvabtn1.setObjectName(u"pvabtn1")
        sizePolicy1.setHeightForWidth(self.pvabtn1.sizePolicy().hasHeightForWidth())
        self.pvabtn1.setSizePolicy(sizePolicy1)
        self.pvabtn1.setMinimumSize(QSize(100, 100))
        self.pvabtn1.setFont(font2)

        self.gridLayout_3.addWidget(self.pvabtn1, 0, 0, 1, 1)

        self.pvabtn2 = QPushButton(self.pva_pg)
        self.pvabtn2.setObjectName(u"pvabtn2")
        sizePolicy1.setHeightForWidth(self.pvabtn2.sizePolicy().hasHeightForWidth())
        self.pvabtn2.setSizePolicy(sizePolicy1)
        self.pvabtn2.setMinimumSize(QSize(100, 100))
        self.pvabtn2.setFont(font2)

        self.gridLayout_3.addWidget(self.pvabtn2, 0, 1, 1, 1)

        self.pvabtn7 = QPushButton(self.pva_pg)
        self.pvabtn7.setObjectName(u"pvabtn7")
        sizePolicy1.setHeightForWidth(self.pvabtn7.sizePolicy().hasHeightForWidth())
        self.pvabtn7.setSizePolicy(sizePolicy1)
        self.pvabtn7.setMinimumSize(QSize(100, 100))
        self.pvabtn7.setFont(font2)

        self.gridLayout_3.addWidget(self.pvabtn7, 2, 0, 1, 1)

        self.pvabtn5 = QPushButton(self.pva_pg)
        self.pvabtn5.setObjectName(u"pvabtn5")
        sizePolicy1.setHeightForWidth(self.pvabtn5.sizePolicy().hasHeightForWidth())
        self.pvabtn5.setSizePolicy(sizePolicy1)
        self.pvabtn5.setMinimumSize(QSize(100, 100))
        self.pvabtn5.setFont(font2)

        self.gridLayout_3.addWidget(self.pvabtn5, 1, 1, 1, 1)

        self.pvabtn6 = QPushButton(self.pva_pg)
        self.pvabtn6.setObjectName(u"pvabtn6")
        sizePolicy1.setHeightForWidth(self.pvabtn6.sizePolicy().hasHeightForWidth())
        self.pvabtn6.setSizePolicy(sizePolicy1)
        self.pvabtn6.setMinimumSize(QSize(100, 100))
        self.pvabtn6.setFont(font2)

        self.gridLayout_3.addWidget(self.pvabtn6, 1, 2, 1, 1)

        self.pvabtn8 = QPushButton(self.pva_pg)
        self.pvabtn8.setObjectName(u"pvabtn8")
        sizePolicy1.setHeightForWidth(self.pvabtn8.sizePolicy().hasHeightForWidth())
        self.pvabtn8.setSizePolicy(sizePolicy1)
        self.pvabtn8.setMinimumSize(QSize(100, 100))
        self.pvabtn8.setFont(font2)

        self.gridLayout_3.addWidget(self.pvabtn8, 2, 1, 1, 1)

        self.pvabtn9 = QPushButton(self.pva_pg)
        self.pvabtn9.setObjectName(u"pvabtn9")
        sizePolicy1.setHeightForWidth(self.pvabtn9.sizePolicy().hasHeightForWidth())
        self.pvabtn9.setSizePolicy(sizePolicy1)
        self.pvabtn9.setMinimumSize(QSize(100, 100))
        self.pvabtn9.setFont(font2)

        self.gridLayout_3.addWidget(self.pvabtn9, 2, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)

        self.pva_label = QLabel(self.pva_pg)
        self.pva_label.setObjectName(u"pva_label")
        font3 = QFont()
        font3.setPointSize(20)
        self.pva_label.setFont(font3)
        self.pva_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.pva_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(50, 5, 50, 5)
        self.pva_restart_btn = QPushButton(self.pva_pg)
        self.pva_restart_btn.setObjectName(u"pva_restart_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pva_restart_btn.sizePolicy().hasHeightForWidth())
        self.pva_restart_btn.setSizePolicy(sizePolicy2)
        self.pva_restart_btn.setMinimumSize(QSize(0, 20))
        self.pva_restart_btn.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pva_restart_btn)

        self.pva_to_home_btn = QPushButton(self.pva_pg)
        self.pva_to_home_btn.setObjectName(u"pva_to_home_btn")
        sizePolicy2.setHeightForWidth(self.pva_to_home_btn.sizePolicy().hasHeightForWidth())
        self.pva_to_home_btn.setSizePolicy(sizePolicy2)
        self.pva_to_home_btn.setMinimumSize(QSize(0, 50))
        self.pva_to_home_btn.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pva_to_home_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.pva_pg)
        self.pvp_pg = QWidget()
        self.pvp_pg.setObjectName(u"pvp_pg")
        self.verticalLayout_3 = QVBoxLayout(self.pvp_pg)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.pvpbtn4 = QPushButton(self.pvp_pg)
        self.pvpbtn4.setObjectName(u"pvpbtn4")
        sizePolicy1.setHeightForWidth(self.pvpbtn4.sizePolicy().hasHeightForWidth())
        self.pvpbtn4.setSizePolicy(sizePolicy1)
        self.pvpbtn4.setMinimumSize(QSize(100, 100))
        self.pvpbtn4.setFont(font2)

        self.gridLayout.addWidget(self.pvpbtn4, 1, 0, 1, 1)

        self.pvpbtn3 = QPushButton(self.pvp_pg)
        self.pvpbtn3.setObjectName(u"pvpbtn3")
        sizePolicy1.setHeightForWidth(self.pvpbtn3.sizePolicy().hasHeightForWidth())
        self.pvpbtn3.setSizePolicy(sizePolicy1)
        self.pvpbtn3.setMinimumSize(QSize(100, 100))
        self.pvpbtn3.setFont(font2)

        self.gridLayout.addWidget(self.pvpbtn3, 0, 2, 1, 1)

        self.pvpbtn1 = QPushButton(self.pvp_pg)
        self.pvpbtn1.setObjectName(u"pvpbtn1")
        sizePolicy1.setHeightForWidth(self.pvpbtn1.sizePolicy().hasHeightForWidth())
        self.pvpbtn1.setSizePolicy(sizePolicy1)
        self.pvpbtn1.setMinimumSize(QSize(100, 100))
        self.pvpbtn1.setFont(font2)

        self.gridLayout.addWidget(self.pvpbtn1, 0, 0, 1, 1)

        self.pvpbtn2 = QPushButton(self.pvp_pg)
        self.pvpbtn2.setObjectName(u"pvpbtn2")
        sizePolicy1.setHeightForWidth(self.pvpbtn2.sizePolicy().hasHeightForWidth())
        self.pvpbtn2.setSizePolicy(sizePolicy1)
        self.pvpbtn2.setMinimumSize(QSize(100, 100))
        self.pvpbtn2.setFont(font2)

        self.gridLayout.addWidget(self.pvpbtn2, 0, 1, 1, 1)

        self.pvpbtn7 = QPushButton(self.pvp_pg)
        self.pvpbtn7.setObjectName(u"pvpbtn7")
        sizePolicy1.setHeightForWidth(self.pvpbtn7.sizePolicy().hasHeightForWidth())
        self.pvpbtn7.setSizePolicy(sizePolicy1)
        self.pvpbtn7.setMinimumSize(QSize(100, 100))
        self.pvpbtn7.setFont(font2)

        self.gridLayout.addWidget(self.pvpbtn7, 2, 0, 1, 1)

        self.pvpbtn5 = QPushButton(self.pvp_pg)
        self.pvpbtn5.setObjectName(u"pvpbtn5")
        sizePolicy1.setHeightForWidth(self.pvpbtn5.sizePolicy().hasHeightForWidth())
        self.pvpbtn5.setSizePolicy(sizePolicy1)
        self.pvpbtn5.setMinimumSize(QSize(100, 100))
        self.pvpbtn5.setFont(font2)

        self.gridLayout.addWidget(self.pvpbtn5, 1, 1, 1, 1)

        self.pvpbtn6 = QPushButton(self.pvp_pg)
        self.pvpbtn6.setObjectName(u"pvpbtn6")
        sizePolicy1.setHeightForWidth(self.pvpbtn6.sizePolicy().hasHeightForWidth())
        self.pvpbtn6.setSizePolicy(sizePolicy1)
        self.pvpbtn6.setMinimumSize(QSize(100, 100))
        self.pvpbtn6.setFont(font2)

        self.gridLayout.addWidget(self.pvpbtn6, 1, 2, 1, 1)

        self.pvpbtn8 = QPushButton(self.pvp_pg)
        self.pvpbtn8.setObjectName(u"pvpbtn8")
        sizePolicy1.setHeightForWidth(self.pvpbtn8.sizePolicy().hasHeightForWidth())
        self.pvpbtn8.setSizePolicy(sizePolicy1)
        self.pvpbtn8.setMinimumSize(QSize(100, 100))
        self.pvpbtn8.setFont(font2)

        self.gridLayout.addWidget(self.pvpbtn8, 2, 1, 1, 1)

        self.pvpbtn9 = QPushButton(self.pvp_pg)
        self.pvpbtn9.setObjectName(u"pvpbtn9")
        sizePolicy1.setHeightForWidth(self.pvpbtn9.sizePolicy().hasHeightForWidth())
        self.pvpbtn9.setSizePolicy(sizePolicy1)
        self.pvpbtn9.setMinimumSize(QSize(100, 100))
        self.pvpbtn9.setFont(font2)

        self.gridLayout.addWidget(self.pvpbtn9, 2, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.pvp_label = QLabel(self.pvp_pg)
        self.pvp_label.setObjectName(u"pvp_label")
        self.pvp_label.setFont(font3)
        self.pvp_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.pvp_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 5, 50, 5)
        self.pvp_restart_btn = QPushButton(self.pvp_pg)
        self.pvp_restart_btn.setObjectName(u"pvp_restart_btn")
        sizePolicy2.setHeightForWidth(self.pvp_restart_btn.sizePolicy().hasHeightForWidth())
        self.pvp_restart_btn.setSizePolicy(sizePolicy2)
        self.pvp_restart_btn.setMinimumSize(QSize(0, 20))
        self.pvp_restart_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.pvp_restart_btn)

        self.pvp_to_home_btn = QPushButton(self.pvp_pg)
        self.pvp_to_home_btn.setObjectName(u"pvp_to_home_btn")
        sizePolicy2.setHeightForWidth(self.pvp_to_home_btn.sizePolicy().hasHeightForWidth())
        self.pvp_to_home_btn.setSizePolicy(sizePolicy2)
        self.pvp_to_home_btn.setMinimumSize(QSize(0, 50))
        self.pvp_to_home_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.pvp_to_home_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.pvp_pg)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TicTacTech", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TIC TAC TOE GAME", None))
        self.pvp_change_btn.setText(QCoreApplication.translate("MainWindow", u"Player vs Player", None))
        self.pva_change_btn.setText(QCoreApplication.translate("MainWindow", u"Player vs AI", None))
        self.pvabtn4.setText("")
        self.pvabtn3.setText("")
        self.pvabtn1.setText("")
        self.pvabtn2.setText("")
        self.pvabtn7.setText("")
        self.pvabtn5.setText("")
        self.pvabtn6.setText("")
        self.pvabtn8.setText("")
        self.pvabtn9.setText("")
        self.pva_label.setText(QCoreApplication.translate("MainWindow", u"X goes first!", None))
        self.pva_restart_btn.setText(QCoreApplication.translate("MainWindow", u"Restart Game", None))
        self.pva_to_home_btn.setText(QCoreApplication.translate("MainWindow", u"Go to Home", None))
        self.pvpbtn4.setText("")
        self.pvpbtn3.setText("")
        self.pvpbtn1.setText("")
        self.pvpbtn2.setText("")
        self.pvpbtn7.setText("")
        self.pvpbtn5.setText("")
        self.pvpbtn6.setText("")
        self.pvpbtn8.setText("")
        self.pvpbtn9.setText("")
        self.pvp_label.setText(QCoreApplication.translate("MainWindow", u"X goes first!", None))
        self.pvp_restart_btn.setText(QCoreApplication.translate("MainWindow", u"Restart Game", None))
        self.pvp_to_home_btn.setText(QCoreApplication.translate("MainWindow", u"Go to Home", None))
    # retranslateUi

