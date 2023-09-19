from PyQt5 import QtGui, QtCore, QtWidgets

class Horizontal_tabs(QtWidgets.QTabBar):
    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        option = QtWidgets.QStyleOptionTab()

        # Ustawienie czcionki i koloru
        font = QtGui.QFont()
        font.setPixelSize(16)  # Dostosuj do własnych potrzeb
        painter.setFont(font)
        color = QtGui.QColor("#C8BEB7")

        fm = QtGui.QFontMetrics(font)
        text_height = fm.height()
        space_width = fm.width(' ')

        for index in range(self.count()):
            self.initStyleOption(option, index)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, option)
            painter.setPen(color)

            # Rysowanie ikony, jeśli istnieje
            icon = self.tabIcon(index)
            if not icon.isNull():
                iconSize = QtCore.QSize(text_height, text_height)
                iconRect = self.tabRect(index)
                iconRect.setSize(iconSize)

                # Wycentrowanie ikony w pionie
                yOffset = (self.tabRect(index).height() - iconSize.height()) // 2
                iconRect.moveTop(iconRect.top() + yOffset)
                
                # Dostosuj pozycję ikony tak, aby była przed tekstem
                iconRect.moveLeft(space_width)
                painter.drawPixmap(iconRect, icon.pixmap(iconSize))
            
            # Narysuj tekst po ikonie
            textRect = self.tabRect(index)
            textRect.setLeft(textRect.left() + text_height + 2 * space_width)
            painter.drawText(textRect, 
                             QtCore.Qt.AlignCenter | QtCore.Qt.TextDontClip, 
                             self.tabText(index))


    
    def tabSizeHint(self, index):
        # Ustawienie czcionki
        font = QtGui.QFont()
        font.setPixelSize(14)
        # Pobranie wielkości tekstu
        fm = QtGui.QFontMetrics(font)
        width = fm.width(self.tabText(index)) + 20  # Dodanie trochę miejsca z boku
        height = super().tabSizeHint(index).height()

        return QtCore.QSize(width, height)  # Zapewniamy, że zawsze zwracamy obiekt QSize


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        QtWidgets.QTabWidget.__init__(self, parent)
        self.setTabBar(Horizontal_tabs())
