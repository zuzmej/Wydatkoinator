# Draw bar graphs. Inherit abstract class Graph

from .chart import Chart
from PyQt5.QtChart import QChart, QStackedBarSeries, QBarSet,QBarCategoryAxis,QValueAxis
from PyQt5.QtGui import QPainter, QColor
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



    def separate_weeks(self, start_date, end_date) -> dict:     #rozdzielenie przedziału czasowego na tygodnie
        result_dates = {}
        while (start_date <= end_date):
            week_end  = start_date + timedelta(days=6)
            
            if week_end > end_date:
                week_end = end_date

            result_dates[start_date] = week_end

            start_date = week_end + timedelta(days=1)

        return result_dates

    def _on_bar_hovered(self, status, index):
        """Obsługuje zdarzenie najechania myszą na segment wykresu."""
        if status:
            bar_set = self.sender()
            category_name = bar_set.label()
            value = bar_set.at(index)
            self.chartview.setToolTip(f"Kategoria: {category_name}\nKwota: {value:.2f} zł")
        else:
            self.chartview.setToolTip("")





    def draw_chart(self, expenses: list):
        series = QStackedBarSeries()

        all_categories = set(expense.category.name for expense in expenses)  # Tworzy zbiór wszystkich unikalnych kategorii
        sets = {category: QBarSet(category) for category in all_categories}  # Tworzy słownik zestawów danych, gdzie kluczem jest kategoria

        oldest, youngest = self.get_date_range([expense.date for expense in expenses])  # jakie daty wpisał użytkownik

        if self.check_dates(oldest, youngest):  # jeżeli dotyczą tego samego miesiąca
            separated_weeks = self.separate_weeks(oldest, youngest)
            for start_date, end_date in separated_weeks.items():
                sums = self.sum_expenses_by_category_in_date_range(expenses, start_date, end_date)
                for category, bar_set in sets.items():
                   if category in sums:
                       bar_set.append(sums[category])
                   else:
                       bar_set.append(0)
            categories = [f"{start_date} - {end_date}" for start_date, end_date in separated_weeks.items()]
        else:       # jeżeli dotyczą różnych miesięcy 
            separated_months = self.separate_months(oldest, youngest)
            for start_date, end_date in separated_months.items():
                sums = self.sum_expenses_by_category_in_date_range(expenses, start_date, end_date)  #sumuj względem kategorii tylko w jednym miesiącu
                for category, bar_set in sets.items():
                   if category in sums:
                       bar_set.append(sums[category])
                   else:
                       bar_set.append(0)
            categories = [f"{start_date} - {end_date}" for start_date, end_date in separated_months.items()]

        for category, bar_set in sets.items():
            bar_set.hovered.connect(self._on_bar_hovered)
            series.append(bar_set)         



        series.setLabelsVisible(True)
        # Tworzenie wykresu
        chart = QChart()
        chart.setBackgroundBrush(QColor("#252525"))
        chart.setTitleBrush(QColor("#C8BEB7"))
        legend = chart.legend()
        legend.setLabelColor(QColor("#C8BEB7"))  # Ustawia kolor czcionki legendy na pomarańczowy (#FF5733)


        chart.addSeries(series)
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)
        axisY = QValueAxis()  
        axisY.setTitleText("Kwota [zł]") 
        axisY.setLabelFormat("%i")  

        axisX.setLabelsColor(QColor("#C8BEB7"))  # Ustaw kolor etykiet osi X na pomarańczowy
        axisY.setLabelsColor(QColor("#C8BEB7")) 

        chart.addAxis(axisY, Qt.AlignLeft) 
        series.attachAxis(axisY) 
        chart.setTitle("Wydatki w poszczególnych kategoriach w wybranych przedziałach czasowych")
        
        # Dodawanie wykresu do QChartView
        chart.setAnimationOptions(QChart.AllAnimations)
        self.chartview.setChart(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.chartview.show()