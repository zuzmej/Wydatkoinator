# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zuzanna/Wydatkoinator/ui/add_new_category_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_category_dialog(object):
    def setupUi(self, add_category_dialog):
        add_category_dialog.setObjectName("add_category_dialog")
        add_category_dialog.resize(400, 300)
        add_category_dialog.setStyleSheet("QDialog { background-color: #202020 }\n"
"\n"
"QLabel { color: #c8beb7 }\n"
"\n"
"QLineEdit { \n"
"    color: #c8beb7;\n"
"    background-color: #3e3e3e\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton {\n"
"    background-color: #3e3e3e;\n"
"    color: #c8beb7\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(add_category_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(add_category_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.add_category_line_edit = QtWidgets.QLineEdit(add_category_dialog)
        self.add_category_line_edit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_category_line_edit.setFont(font)
        self.add_category_line_edit.setObjectName("add_category_line_edit")
        self.gridLayout.addWidget(self.add_category_line_edit, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(add_category_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(add_category_dialog)
        self.buttonBox.accepted.connect(add_category_dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(add_category_dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(add_category_dialog)

    def retranslateUi(self, add_category_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_category_dialog.setWindowTitle(_translate("add_category_dialog", "Dialog"))
        self.label.setText(_translate("add_category_dialog", "Wpisz nazwę nowej kategorii:"))
