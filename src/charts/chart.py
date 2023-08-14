# Abstract class to draw graphs

from abc import ABC, abstractmethod
from PyQt5 import QtWidgets

import sys
sys.path.insert(0, '../../')  # Dodaj katalog nadrzędny do ścieżki

from src.ui.chart import Ui_Chart


class Chart(ABC, QtWidgets.QWidget, Ui_Chart):
    def __init__(self):
        pass

    @abstractmethod
    def draw_chart(self, expenses: list):
        pass
