from src.ui.home_tab import Ui_home_tab
from PyQt5.QtWidgets import QWidget
from src.charts.pie_chart import Pie_chart
from src.charts.stack_chart import Stack_chart
from src.database.database import Database
from datetime import datetime, timedelta

class Home_tab(QWidget, Ui_home_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None

        self.pie_chart = Pie_chart(self.chart1)
        self.stack_chart = Stack_chart(self.chart2)

        self.date_from = (datetime.today().date() - timedelta(days=30))
        self.date_to = datetime.today().date()




    def set_database(self, database: Database):
        self.database = database


    def draw_pie_chart(self):
        expenses = self.database.get_all_expenses()
        sums = self.pie_chart.sum_expenses_by_category_in_date_range(expenses, self.date_from, self.date_to)
        sorted_sums = dict(sorted(sums.items(), key=lambda item: item[1], reverse=True))

        count = 0
        biggest_sums = []
        for key, value in sorted_sums.items():
            biggest_sums.append((key, value))
            count += 1
            if count == 4:
                break

        print(sorted_sums)
        print(biggest_sums)

        # get_all_expenses -- in date range bo jak ktos bedzie mial duza baze danych to ojojoj
        # rozważyć możliwości: Kubi mówi, żeby utworzyć obiekt Expenses, a id i date uzupełnić niczym i to przekazać do draw_chart  
        
        




    def draw_stack_chart(self):
        pass
        