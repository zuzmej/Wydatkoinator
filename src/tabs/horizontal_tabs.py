from PyQt5 import QtGui, QtCore, QtWidgets


class Horizontal_tabs(QtWidgets.QTabBar):
    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        option = QtWidgets.QStyleOptionTab()

        # Ustawienie czcionki i koloru
        font = QtGui.QFont()
        font.setPixelSize(14)  # Ustawia wielkość czcionki
        painter.setFont(font)
        color = QtGui.QColor("red")  # Ustawia kolor czcionki

        for index in range(self.count()):
            self.initStyleOption(option, index)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, option)
            painter.setPen(color)
            painter.drawText(self.tabRect(index), 
                             QtCore.Qt.AlignCenter | QtCore.Qt.TextDontClip, 
                             self.tabText(index))




class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        QtWidgets.QTabWidget.__init__(self, parent)
        self.setTabBar(Horizontal_tabs())
