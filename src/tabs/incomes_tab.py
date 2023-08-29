from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from src.ui.incomes_tab import Ui_incomes_tab
from src.database.database import Database
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta

class Incomes_tab(QWidget, Ui_incomes_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None
        self.date.setDate(datetime.today().date())
        validator = QDoubleValidator(0.00, 1000000.00, 2)
        self.lineEdit.setValidator(validator)
        self.incomes_list.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.incomes_list.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.incomes_list.setHorizontalHeaderLabels(["data", "kwota"])
        self.confirm_button.clicked.connect(self.add_income)

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
        incomes.sort(key=lambda x: x.date)
        self.incomes_list.setRowCount(0)
        for income in incomes:
            self.incomes_list.insertRow(self.incomes_list.rowCount())
            item1 = QTableWidgetItem(income.date.strftime("%Y-%m-%d"))
            item2 = QTableWidgetItem(str(income.amount))
            item1.setTextAlignment(Qt.AlignCenter)
            item2.setTextAlignment(Qt.AlignCenter)
            self.incomes_list.setItem(self.incomes_list.rowCount() - 1, 0, item1)
            self.incomes_list.setItem(self.incomes_list.rowCount() - 1, 1, item2)

    def add_income(self):
        amount = self.lineEdit.text()
        if amount.strip():
            self.database.add_expense(amount=amount, date=self.date.date().toString("yyyy-MM-dd"), category_id=self.database.get_category_id_by_name("Wpływy"))
            self.lineEdit.clear()
            self.set_incomes_list()
            
        
    







    





