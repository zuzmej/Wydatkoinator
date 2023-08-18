# Draw pie chart. Inherit abstract class Graph

from .chart import Chart
from PyQt5.QtChart import QChart, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

import sys

sys.path.insert(0, '../../')  # Dodaj katalog nadrzędny do ścieżki

from src.database.expense import Expense

class Pie_chart(Chart):
    def __init__(self):
        super().__init__()

    def draw_chart(self, expenses: list):
        series = QPieSeries()
        category_sums = self.sum_expenses_by_category(expenses)
        for category_name, category_sum in category_sums.items():
            series.append(category_name, category_sum)
        series.setLabelsVisible(True)
        series.setLabelsPosition(QPieSlice.LabelOutside)
        for slice in series.slices():
            slice.setLabel("{:.0f}%".format(100 * slice.percentage()))
        
        chart = QChart()
        
        chart.addSeries(series)
        oldest, youngest  = self.get_date_range([expense.date for expense in expenses])
        chart.setTitle(f"Wydatki w poszczególnych kategoriach w okresie od {oldest} do {youngest}")
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        x = 0
        for category_name, category_sum in category_sums.items():
            chart.legend().markers(series)[x].setLabel(category_name)
            x += 1
        chart.setAnimationOptions(QChart.AllAnimations)
        self.chart.setChart(chart)
        self.chart.setRenderHint(QPainter.Antialiasing)
