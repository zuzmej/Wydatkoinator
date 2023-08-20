# Draw bar graphs. Inherit abstract class Graph

from .chart import Chart
from PyQt5.QtChart import QChart, QStackedBarSeries, QBarSet
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

import sys

sys.path.insert(0, '../../')  # Dodaj katalog nadrzędny do ścieżki

from src.database.expense import Expense


class Stack_chart(Chart):
    def __init__(self, chartview):
        super().__init__(chartview)
        
    def draw_chart(self, expenses: list):
        category_sums = self.sum_expenses_by_category(expenses)

        series = QStackedBarSeries()
        for name, amount in category_sums.items():
            set = QBarSet(name)
            set.append(amount)
            series.append(set)

        # Tworzenie wykresu
        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("Stacked Bar Chart")
        
        # Dodawanie wykresu do QChartView
        chart.setAnimationOptions(QChart.AllAnimations)
        self.chartview.setChart(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.chartview.show()