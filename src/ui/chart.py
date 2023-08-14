# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kubus/Pulpit/Wydatkoinator/ui/chart.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Chart(object):
    def setupUi(self, Chart):
        Chart.setObjectName("Chart")
        Chart.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Chart)
        self.gridLayout.setObjectName("gridLayout")
        self.chart = QChartView(Chart)
        self.chart.setObjectName("chart")
        self.gridLayout.addWidget(self.chart, 0, 0, 1, 1)

        self.retranslateUi(Chart)
        QtCore.QMetaObject.connectSlotsByName(Chart)

    def retranslateUi(self, Chart):
        _translate = QtCore.QCoreApplication.translate
        Chart.setWindowTitle(_translate("Chart", "Form"))
from  PyQt5.QtChart import QChartView
