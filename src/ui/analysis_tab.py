# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kubus/Pulpit/Wydatkoinator/ui/analysis_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_analisys_tab(object):
    def setupUi(self, analisys_tab):
        analisys_tab.setObjectName("analisys_tab")
        analisys_tab.resize(1145, 693)
        self.gridLayout = QtWidgets.QGridLayout(analisys_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.select_date = QtWidgets.QFrame(analisys_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_date.sizePolicy().hasHeightForWidth())
        self.select_date.setSizePolicy(sizePolicy)
        self.select_date.setMinimumSize(QtCore.QSize(0, 100))
        self.select_date.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.select_date.setFrameShadow(QtWidgets.QFrame.Raised)
        self.select_date.setObjectName("select_date")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.select_date)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.select_date)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 4)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.select_date)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout_4.addWidget(self.dateEdit_2, 4, 3, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.select_date)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_4.addWidget(self.dateEdit, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.select_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.select_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 4, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.select_date)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.select_date)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 5, 3, 1, 1)
        self.gridLayout.addWidget(self.select_date, 0, 2, 1, 1)
        self.select_categories = QtWidgets.QFrame(analisys_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_categories.sizePolicy().hasHeightForWidth())
        self.select_categories.setSizePolicy(sizePolicy)
        self.select_categories.setMinimumSize(QtCore.QSize(0, 100))
        self.select_categories.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.select_categories.setFrameShadow(QtWidgets.QFrame.Raised)
        self.select_categories.setObjectName("select_categories")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.select_categories)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.select_categories)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.select_categories)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.select_categories, 0, 1, 1, 1)
        self.chart = Pie_chart(analisys_tab)
        self.chart.setObjectName("chart")
        self.gridLayout.addWidget(self.chart, 2, 0, 1, 3)
        self.select_chart_type = QtWidgets.QFrame(analisys_tab)
        self.select_chart_type.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_chart_type.sizePolicy().hasHeightForWidth())
        self.select_chart_type.setSizePolicy(sizePolicy)
        self.select_chart_type.setMinimumSize(QtCore.QSize(0, 100))
        self.select_chart_type.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.select_chart_type.setFrameShadow(QtWidgets.QFrame.Raised)
        self.select_chart_type.setObjectName("select_chart_type")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.select_chart_type)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.select_chart_type)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 1, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.select_chart_type)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.select_chart_type)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.select_chart_type, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(analisys_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1, QtCore.Qt.AlignRight)

        self.retranslateUi(analisys_tab)
        QtCore.QMetaObject.connectSlotsByName(analisys_tab)

    def retranslateUi(self, analisys_tab):
        _translate = QtCore.QCoreApplication.translate
        analisys_tab.setWindowTitle(_translate("analisys_tab", "Form"))
        self.label_3.setText(_translate("analisys_tab", "Wybierz okres"))
        self.label_4.setText(_translate("analisys_tab", "Od:"))
        self.label_5.setText(_translate("analisys_tab", "Do:"))
        self.pushButton_2.setText(_translate("analisys_tab", "Pokaż kalendarz"))
        self.pushButton_3.setText(_translate("analisys_tab", "Pokaż kalendarz"))
        self.label_2.setText(_translate("analisys_tab", "Wybierz kategorie"))
        self.radioButton.setText(_translate("analisys_tab", "Wykres kołowy"))
        self.radioButton_2.setText(_translate("analisys_tab", "Wykres stosowy"))
        self.label.setText(_translate("analisys_tab", "Wybierz typ wykresu"))
        self.pushButton.setText(_translate("analisys_tab", "Zatwierdź"))
from src.charts.pie_chart import Pie_chart
