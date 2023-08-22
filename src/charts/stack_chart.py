# Draw bar graphs. Inherit abstract class Graph

from .chart import Chart
from PyQt5.QtChart import QChart, QStackedBarSeries, QBarSet,QBarCategoryAxis,QValueAxis
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



    def separate_weeks(self, date1, date2) -> dict:     #rozdzielenie przedziału czasowego na tygodnie
        pass




    # UWAGA -- data starsza musi być podana jako pierwszy argument
    def separate_months(self, start_date, end_date) -> dict:    #rozdzielenie przedziału czasowego na miesiące
        result_dates = {}
        while (start_date <= end_date):
            month_end = start_date + timedelta(days=32)  # wykracza poza podany miesiąc
            month_end = month_end - timedelta(days=month_end.day)   # wraca do końca poprzedniego miesiąca

            if month_end > end_date:
                month_end = end_date

            result_dates[start_date] = month_end

            start_date = month_end + timedelta(days=1)
        return result_dates     # typ datetime.date





    def draw_chart(self, expenses: list):
        series = QStackedBarSeries()

        all_categories = set(expense.category.name for expense in expenses)  # Tworzy zbiór wszystkich unikalnych kategorii
        sets = {category: QBarSet(category) for category in all_categories}  # Tworzy słownik zestawów danych, gdzie kluczem jest kategoria

        oldest, youngest = self.get_date_range([expense.date for expense in expenses])  # jakie daty wpisał użytkownik

        if self.check_dates(oldest, youngest):  # jeżeli dotyczą tego samego miesiąca
            print("daty dot. tego samego miesiąca")
        else:       # jeżeli dotyczą różnych miesięcy 
            separated_months = self.separate_months(oldest, youngest)
            for start_date, end_date in separated_months.items():
                sums = self.sum_expenses_by_category_in_date_range(expenses, start_date, end_date)
                for category, bar_set in sets.items():
                   if category in sums:
                       print("true")
                       bar_set.append(sums[category])
                   else:
                       bar_set.append(0)
                       print("false")



                #     category = expense.category.name
                #     sets[category].append(10)
        categories = [f"{start_date} - {end_date}" for start_date, end_date in separated_months.items()]
        


       


        for category, bar_set in sets.items():
            series.append(bar_set)         

        series.setLabelsVisible(True)
        

        # Tworzenie wykresu
        chart = QChart()
        chart.addSeries(series)
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)
        axisY = QValueAxis()  # Step 1: Create Y axis instance
        axisY.setTitleText("Kwota [zł]")  # Optional title for the Y axis
        axisY.setLabelFormat("%i")  # Step 2: Setting label format (integer in this case)
        chart.addAxis(axisY, Qt.AlignLeft)  # Step 3: Add Y axis to the chart
        series.attachAxis(axisY)  # Step 4: Attach Y axis to the series
        chart.setTitle("Wydatki w poszczególnych kategoriach w wybranych przedziałach czasowych")
        
        # Dodawanie wykresu do QChartView
        chart.setAnimationOptions(QChart.AllAnimations)
        self.chartview.setChart(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.chartview.show()