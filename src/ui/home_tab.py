# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zuzanna/Wydatkoinator/ui/home_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home_tab(object):
    def setupUi(self, home_tab):
        home_tab.setObjectName("home_tab")
        home_tab.resize(1145, 693)
        home_tab.setStyleSheet("QWidget { background-color: #202020 }\n"
"\n"
"QLabel {color: #c8beb7 }")
        self.gridLayout = QtWidgets.QGridLayout(home_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.hello_widget = QtWidgets.QWidget(home_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hello_widget.sizePolicy().hasHeightForWidth())
        self.hello_widget.setSizePolicy(sizePolicy)
        self.hello_widget.setMinimumSize(QtCore.QSize(0, 160))
        self.hello_widget.setObjectName("hello_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.hello_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.hello_widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.hello_widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.gridLayout.addWidget(self.hello_widget, 0, 0, 1, 2)
        self.chart1 = QChartView(home_tab)
        self.chart1.setObjectName("chart1")
        self.gridLayout.addWidget(self.chart1, 1, 0, 1, 1)
        self.chart2 = QChartView(home_tab)
        self.chart2.setObjectName("chart2")
        self.gridLayout.addWidget(self.chart2, 1, 1, 1, 1)

        self.retranslateUi(home_tab)
        QtCore.QMetaObject.connectSlotsByName(home_tab)

    def retranslateUi(self, home_tab):
        _translate = QtCore.QCoreApplication.translate
        home_tab.setWindowTitle(_translate("home_tab", "Form"))
        self.label.setText(_translate("home_tab", "Wydatkoinator 1.0"))
        self.label_2.setText(_translate("home_tab", "Miej wydatki pod kontrolą."))
from PyQt5.QtChart import QChartView
