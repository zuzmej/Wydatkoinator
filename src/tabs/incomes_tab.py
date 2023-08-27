from PyQt5.QtWidgets import QWidget
from src.ui.incomes_tab import Ui_incomes_tab
from src.database.database import Database
from PyQt5.QtGui import QDoubleValidator

from datetime import datetime, timedelta

class Incomes_tab(QWidget, Ui_incomes_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None
        validator = QDoubleValidator(0.00, 1000000.00, 2)
        self.lineEdit.setValidator(validator)


    def set_database(self, database: Database):
        self.database = database

    def set_incomes_list(self):
        try:
            self.database.add_category("Wpływy")
        except ValueError as e:
            print(e)
        start_date =datetime.today().date() - timedelta(weeks = 12)
        end_date = datetime.today().date()
        incomes = self.database.get_expenses_by_category_name_in_date_range("Wpływy",start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
        for income in incomes:
            self.incomes_list.addItem(income)







    





