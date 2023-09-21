from PyQt5.QtWidgets import QWidget
from datetime import datetime, timedelta
from src.ui.analysis_tab import Ui_analisys_tab
from src.database.database import Database
from .combobox import Combo_box
from src.charts.pie_chart import Pie_chart
from src.charts.stack_chart import Stack_chart

class Analysis_tab(QWidget, Ui_analisys_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None
        self.is_pie_chart_set = False
        self.is_stack_chart_set = False
        self.pie_chart = Pie_chart(self.chart)
        self.stack_chart = Stack_chart(self.chart)

        self.combo_box = Combo_box(self.categories_list)

        self.date_from.setDate(datetime.today().date() - timedelta(days=7))
        self.date_to.setDate(datetime.today().date())
        self.date_from.dateChanged.connect(self.correctness_of_dates)



        self.pie_chart_button.clicked.connect(self.set_pie_chart)
        self.stack_chart_button.clicked.connect(self.set_stack_chart)

        self.confirm_button.clicked.connect(self.show_chart)
    
    def set_database(self, database: Database):
        self.database = database

    def set_pie_chart(self):
        self.is_pie_chart_set = True
        self.is_stack_chart_set = False

    def set_stack_chart(self):
        self.is_pie_chart_set = False
        self.is_stack_chart_set = True

    def get_date_from(self):
        return self.date_from.date().toPyDate()
    
    def get_date_to(self):
        return self.date_to.date().toPyDate()
    
    def correctness_of_dates(self):
        if self.get_date_from() > self.get_date_to():
            self.date_from.setDate(self.date_to.date())

    def set_categories_list(self):
        categories = self.database.get_all_categories()
        for category in categories:
            self.combo_box.add_item(category.name)

        self.combo_box.add_item("Wszystkie")

    def show_chart(self):
        expenses = []
        selected_categories = self.combo_box.get_checked_items()

        if "Wszystkie" in selected_categories:
            selected_categories.pop(selected_categories.index("Wszystkie"))

        for category in selected_categories:
            expenses.extend(self.database.get_expenses_by_category_name_in_date_range(category, self.date_from.date().toPyDate().strftime("%Y-%m-%d"), self.date_to.date().toPyDate().strftime("%Y-%m-%d")))

        if self.is_pie_chart_set:
            self.pie_chart.draw_chart(expenses)
        elif self.is_stack_chart_set:
            self.stack_chart.draw_chart(expenses)
        




    


    

