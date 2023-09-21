from src.ui.home_tab import Ui_home_tab
from PyQt5.QtWidgets import QWidget
from src.charts.pie_chart import Pie_chart
from src.database.database import Database
from datetime import datetime, timedelta
from PyQt5.QtChart import QChart, QPieSeries, QPieSlice, QStackedBarSeries, QBarSet
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QMargins

class Home_tab(QWidget, Ui_home_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None

        self.pie_chart = Pie_chart(self.chart1)

        self.date_from = (datetime.today().date() - timedelta(days=30)).strftime("%Y-%m-%d")
        self.date_to = datetime.today().date().strftime("%Y-%m-%d")

        self.hello_widget.setStyleSheet("background-color: #252525")

    def set_database(self, database: Database):
        self.database = database


    def draw_pie_chart(self):
        expenses = self.database.get_expenses_by_date_range(self.date_from, self.date_to)
        sums = self.pie_chart.sum_expenses_by_category(expenses)
        sorted_sums = dict(sorted(sums.items(), key=lambda item: item[1], reverse=True))    # sortowanie malejąco

        count = 0
        biggest_sums = {}
        others = 0

        for key, value in sorted_sums.items():  
            if count < 4:
                biggest_sums[key] = value #biggest_sums.append((key, value)) -- dla listy
            else:
                others += value
            count += 1
            
        biggest_sums["Inne"] = others #biggest_sums["Inne"].append(others)

        series = QPieSeries()
        for key, value in biggest_sums.items():
            series.append(key, value)
        series.setLabelsVisible(True)
        series.setLabelsPosition(QPieSlice.LabelOutside)
        for slice in series.slices():
            slice.setLabel("{:.0f}%".format(100 * slice.percentage()) + " / " + "{:.2f}zł".format(slice.value()))
            slice.setLabelColor(QColor("#C8BEB7")) 
        
        
        chart = QChart()
        chart.setMargins(QMargins(10,10,10,10))
        chart.setBackgroundBrush(QColor("#252525"))
        chart.setTitleBrush(QColor("#C8BEB7"))
        legend = chart.legend()
        legend.setLabelColor(QColor("#C8BEB7"))

        chart.addSeries(series)
        chart.setTitle(f"W ostatnich 30 dniach najwięcej wydano na:")
        title_font = QFont("Ubuntu Bold", 12, QFont.Bold)
        chart.setTitleFont(title_font)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        x = 0
        for category_name, category_sum in biggest_sums.items():
            legend.markers(series)[x].setLabel(category_name)
            x += 1
       
        chart.setAnimationOptions(QChart.AllAnimations)
        self.chart1.setChart(chart)
        self.chart1.setRenderHint(QPainter.Antialiasing)
        self.chart1.show()
        



    def draw_stack_chart(self):
        expenses = self.database.get_expenses_by_date_range(self.date_from, self.date_to)
        sums = self.pie_chart.sum_expenses_by_category(expenses)
        
        incomes_outcomes_sums = {}
        others = 0
        
        for key, value in sums.items():
            if key == "Wpływy" or key == "wpływy" or key == "wplywy" or key == "wplyw":
                incomes_outcomes_sums[key] = value
            else:
                others += value

        incomes_outcomes_sums["Wydatki"] = others


        series = QStackedBarSeries()
        series.setLabelsVisible(True)

        bar_set_incomes = QBarSet("Wpływy")
        bar_set_expenses = QBarSet("Wydatki")

        for category, value in incomes_outcomes_sums.items():
            if category == 'Wpływy':
                bar_set_incomes.append(value)
            elif category == 'Wydatki':
                bar_set_expenses.append(value)

        # Dodawanie zestawów danych do serii słupków
        series.append(bar_set_incomes)
        series.append(bar_set_expenses)
        
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Bilans z ostatnich 30 dni:")
        chart.setBackgroundBrush(QColor("#252525"))
        chart.setTitleBrush(QColor("#C8BEB7"))
        chart.setMargins(QMargins(10,10,10,10))

        title_font = QFont("Ubuntu Bold", 12, QFont.Bold)
        chart.setTitleFont(title_font)

        # Tworzenie legendy
        legend = chart.legend()
        legend.setLabelColor(QColor("#C8BEB7"))  
        legend.setAlignment(Qt.AlignBottom)
        chart.setAnimationOptions(QChart.AllAnimations)
        
        self.chart2.setChart(chart)
        self.chart2.setRenderHint(QPainter.Antialiasing)
        self.chart2.show()

        
                

        