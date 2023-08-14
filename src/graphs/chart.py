# Abstract class to draw graphs

from abc import ABC, abstractmethod
from PyQt5 import QtWidgets


class Chart(ABC, QtWidgets.QWidget ):
    def __init__(self):
        pass

    @abstractmethod
    def draw_chart(self, expenses: list):
        pass
