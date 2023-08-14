# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kubus/Pulpit/Wydatkoinator/ui/home_tab.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home_tab(object):
    def setupUi(self, Home_tab):
        Home_tab.setObjectName("Home_tab")
        Home_tab.resize(742, 500)
        self.gridLayout = QtWidgets.QGridLayout(Home_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Home_tab)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 2, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(Home_tab)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.retranslateUi(Home_tab)
        QtCore.QMetaObject.connectSlotsByName(Home_tab)

    def retranslateUi(self, Home_tab):
        _translate = QtCore.QCoreApplication.translate
        Home_tab.setWindowTitle(_translate("Home_tab", "Form"))
