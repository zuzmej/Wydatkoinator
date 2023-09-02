from .chart import Chart
from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QBarCategoryAxis, QValueAxis
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta


class Bar_chart(Chart):

    def __init__(self, chartview):
        super().__init__(chartview)





    def draw_chart(self, expenses: list):
        series = QBarSeries()
        set_ = QBarSet("Wpływy")
        first_date ,last_date = self.get_date_range([expense.date for expense in expenses])
   
        months = self.separate_months(first_date, last_date)
        
        for f_date, l_date in months.items():
            sums_all = self.sum_expenses_by_category_in_date_range(expenses, f_date, l_date)
            set_.append(sums_all["Wpływy"])
        series.append(set_)
        chart = QChart()
        chart.setBackgroundBrush(QColor("#252525"))
        chart.setTitleBrush(QColor("#C8BEB7"))
        legend = chart.legend()
        legend.setLabelColor(QColor("#C8BEB7"))
        chart.addSeries(series)
        chart.setTitle("Prosty wykres słupkowy")
        categories = [f"{f_date.strftime('%Y-%m-%d')} - {l_date.strftime('%Y-%m-%d')}" for f_date, l_date in months.items()]
        axisX = QBarCategoryAxis()
        axisX.append(categories)

        # Utwórz osie wartości (osi Y)
        axisY = QValueAxis()
        # axisY.setRange(0, max(set_.sum()) + 10)  # Zakładając, że chcesz dodać trochę przestrzeni na górze
        axisX.setLabelsColor(QColor("#C8BEB7"))  # Ustaw kolor etykiet osi X na pomarańczowy
        axisY.setLabelsColor(QColor("#C8BEB7"))
        # Dodaj osie do wykresu
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        # Przyłącz serie do osi
        series.attachAxis(axisX)
        series.attachAxis(axisY)
        chart.setAnimationOptions(QChart.AllAnimations)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        self.chartview.setChart(chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.chartview.show()


    