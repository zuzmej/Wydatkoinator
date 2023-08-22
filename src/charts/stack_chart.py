# Draw bar graphs. Inherit abstract class Graph

from .chart import Chart
from PyQt5.QtChart import QChart, QStackedBarSeries, QBarSet
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

import sys

sys.path.insert(0, '../../')  # Dodaj katalog nadrzędny do ścieżki

from src.database.expense import Expense
from datetime import datetime, timedelta


class Stack_chart(Chart):
    def __init__(self, chartview):
        super().__init__(chartview)


    def check_dates(self, date1, date2):  # metoda do sprawdzania czy daty wybrane przez użytkownika dotyczą tego samego miesiąca
        return date1.year == date2.year and date1.month == date2.month


    def get_months_between_dates(self, date1, date2):
        months = []
        current_date = date1

        while current_date <= date2:
            months.append(current_date.strftime('%Y-%m'))
            current_date += timedelta(days=1)  # Dodawanie jednego dnia do daty
            if current_date.day == 1:  # Sprawdzamy, czy przeskoczyliśmy na kolejny miesiąc
                current_date = current_date.replace(day=1)
                if current_date.month == 12:
                    current_date = current_date.replace(year=current_date.year + 1, month=1)
                else:
                    current_date = current_date.replace(month=current_date.month + 1)    
        return months


    def draw_chart(self, expenses: list):
        oldest, youngest = self.get_date_range([expense.date for expense in expenses])  # jakie daty wpisał użytkownik

        sums = self.sum_expenses_by_category_in_date_range(expenses, oldest, youngest)
        
        print(sums)
        # months = self.get_months_between_dates(oldest, youngest)


        # print(month_sums)
        # if (self.check_dates(expenses)):
        #     print("daty są z tego samego miesiąca")
        # else:
        #     print("daty nie sa z tego samego miesiaca")

        # if not self.check_dates(oldest, youngest):  # jeżeli daty dotyczą różnych miesięcy
        #     print("daty nie sa z tego samego miesiaca")

        # series = QStackedBarSeries()

        # for category_name, month_data in month_sums.items():
        #     set = QBarSet(category_name)
        #     for month in months:
        #         category_sum = month_data.get(month, 0)
        #         set.append(float(category_sum))
        #     series.append(set)        



        # for category_name in month_sums.values():
        #     for month in month_sums.keys():
        #         set = QBarSet(month)
        #         category_sum = month_sums.get(month, 0)
        #         set.append(float(category_sum))
        #         series.append(set)
        
        # for name, amount in category_sums.items():
        #     set = QBarSet(name)
        #     set.append(amount)
        #     series.append(set)

        # # Tworzenie wykresu
        # chart = QChart()
        # chart.addSeries(series)
        # chart.createDefaultAxes()
        # chart.setTitle("Stacked Bar Chart")
        
        # # Dodawanie wykresu do QChartView
        # chart.setAnimationOptions(QChart.AllAnimations)
        # self.chartview.setChart(chart)
        # self.chartview.setRenderHint(QPainter.Antialiasing)
        # self.chartview.show()