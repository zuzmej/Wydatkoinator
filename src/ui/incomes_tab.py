# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kubus/Pulpit/Wydatkoinator/ui/incomes_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_incomes_tab(object):
    def setupUi(self, incomes_tab):
        incomes_tab.setObjectName("incomes_tab")
        incomes_tab.resize(1143, 718)
        incomes_tab.setStyleSheet("QWidget{\n"
"background-color: #202020;\n"
"}\n"
"QFrame{\n"
"background-color: #252525;\n"
"}\n"
"\n"
"QLabel{\n"
"color:#C8BEB7;\n"
"}\n"
"QPushButton{\n"
"color:#C8BEB7;\n"
"background-color:#515151\n"
"}\n"
"QLineEdit{\n"
"background-color:#182B32;\n"
"color:#C8BEB7;\n"
"}\n"
"QDateEdit{\n"
"background-color:#182B32;\n"
"color:#C8BEB7;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(incomes_tab)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.frame = QtWidgets.QFrame(incomes_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 517, 640))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.incomes_list = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.incomes_list.setFont(font)
        self.incomes_list.setStyleSheet("QHeaderView::section {\n"
"    background-color: transparent;  /* brak tła */\n"
"    color:#C8BEB7;  /* kolor napisu */\n"
"    border: none;  /* brak ramki */\n"
" font-size: 20px;  /* Ustawienie rozmiaru czcionki */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    font-size: 20px;\n"
"     color:#C8BEB7\n"
"}")
        self.incomes_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.incomes_list.setTabKeyNavigation(False)
        self.incomes_list.setProperty("showDropIndicator", False)
        self.incomes_list.setDragDropOverwriteMode(False)
        self.incomes_list.setTextElideMode(QtCore.Qt.ElideRight)
        self.incomes_list.setShowGrid(False)
        self.incomes_list.setWordWrap(False)
        self.incomes_list.setCornerButtonEnabled(False)
        self.incomes_list.setRowCount(0)
        self.incomes_list.setColumnCount(2)
        self.incomes_list.setObjectName("incomes_list")
        self.incomes_list.horizontalHeader().setVisible(True)
        self.incomes_list.horizontalHeader().setCascadingSectionResizes(False)
        self.incomes_list.horizontalHeader().setSortIndicatorShown(False)
        self.incomes_list.horizontalHeader().setStretchLastSection(False)
        self.incomes_list.verticalHeader().setVisible(False)
        self.incomes_list.verticalHeader().setCascadingSectionResizes(False)
        self.incomes_list.verticalHeader().setHighlightSections(True)
        self.incomes_list.verticalHeader().setStretchLastSection(False)
        self.gridLayout_4.addWidget(self.incomes_list, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 3, 1)
        self.frame_3 = QtWidgets.QFrame(incomes_tab)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout.addWidget(self.frame_3, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(incomes_tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 3)
        self.confirm_button = QtWidgets.QPushButton(self.frame_2)
        self.confirm_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.confirm_button.setFont(font)
        self.confirm_button.setObjectName("confirm_button")
        self.gridLayout_3.addWidget(self.confirm_button, 2, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 2)
        self.date = QtWidgets.QDateEdit(self.frame_2)
        self.date.setMinimumSize(QtCore.QSize(0, 40))
        self.date.setStyleSheet("QCalendarWidget QWidget { background-color: #c8beb7; }    /* calosc */ \n"
"\n"
"QCalendarWidget QWidget { alternate-background-color: #c8beb7; } /* naglowek z nazwami dni */\n"
"\n"
"QCalendarWidget QToolButton { color: black; }    /* najwyzszy naglowek - czcionka*/")
        self.date.setCalendarPopup(True)
        self.date.setObjectName("date")
        self.gridLayout_3.addWidget(self.date, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 2, 1, 1)

        self.retranslateUi(incomes_tab)
        QtCore.QMetaObject.connectSlotsByName(incomes_tab)

    def retranslateUi(self, incomes_tab):
        _translate = QtCore.QCoreApplication.translate
        incomes_tab.setWindowTitle(_translate("incomes_tab", "Form"))
        self.label.setText(_translate("incomes_tab", "Ostatnie wpływy"))
        self.label_3.setText(_translate("incomes_tab", "zł"))
        self.label_2.setText(_translate("incomes_tab", "Dodaj wpływ "))
        self.confirm_button.setText(_translate("incomes_tab", "Zatwierdź"))
