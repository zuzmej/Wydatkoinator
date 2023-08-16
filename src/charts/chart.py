# Abstract class to draw graphs

from abc import ABC, abstractmethod
from PyQt5 import QtWidgets

import sys
sys.path.insert(0, '../../')  # Dodaj katalog nadrzędny do ścieżki

from src.ui.chart import Ui_Chart
from datetime import datetime


class Chart_meta(QtWidgets.QWidget.__class__, ABC.__class__):
    pass

class Chart(QtWidgets.QWidget, Ui_Chart, metaclass=Chart_meta):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

    @abstractmethod
    def draw_chart(self, expenses: list):
        pass

    def sum_expenses_by_category(self, expenses: list) -> dict:
        category_sums = {}
        for expense in expenses:
            category_name = expense.category.name
            if category_name not in category_sums:
                category_sums[category_name] = 0
            category_sums[category_name] += expense.amount
        return category_sums
    
    def get_date_range(self, dates_list: list) -> tuple:
        return min(dates_list), max(dates_list)
