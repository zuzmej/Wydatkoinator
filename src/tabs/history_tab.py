from PyQt5.QtWidgets import QWidget, QHeaderView
from src.ui.history_tab import Ui_history_tab
from src.tabs.filters import Filters
from src.database.database import Database
from src.tabs.table_item import Table_item
from src.tabs.filter_dialog import Filter_dialog
from src.tabs.history_edit import History_edit
from src.tabs.delete_history import Delete_history
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta
import os

class History_tab(QWidget, Ui_history_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        # self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        # self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(["data", "kwota", "kategoria"," "," "])
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.filters = Filters()
        self.table.cellDoubleClicked.connect(self.operation_edit)
        self.table.cellDoubleClicked.connect(self.operation_remove)
        self.filter_button.clicked.connect(self.set_filtres)
        self.remove_filters_button.clicked.connect(self.clear_filters)


    def set_database(self, database):
        self.database = database

    def set_default_filters(self):
        self.filters.start_date = (datetime.today().date() - timedelta(weeks = 2)).strftime("%Y-%m-%d")
        self.filters.end_date = datetime.today().date().strftime("%Y-%m-%d")
        self.filters.amount_min = 0
        self.filters.amount_max = 1000000
        self.filters.chosen_categories = [category.name for category in self.database.get_all_categories()]

    def set_default_history_list(self):
        self.table.setRowCount(0)
        operations = self.database.get_expenses_by_date_range((datetime.today().date() - timedelta(weeks = 2)).strftime("%Y-%m-%d"), datetime.today().date().strftime("%Y-%m-%d"))
        operations.sort(key = lambda operation: operation.date)
        icon = QIcon(os.path.join(self.path, "../resources/pencil_16.png"))
        icon_bin = QIcon(os.path.join(self.path, "../resources/bin(1)_16.png"))
        for operation in operations:
            self.table.insertRow(self.table.rowCount())
            item1 = Table_item(operation.date.strftime("%Y-%m-%d"), operation.id)
            item2 = Table_item(str(operation.amount), operation.id)
            item3 = Table_item(operation.category.name, operation.id)
            item4 = Table_item(None, None)
            item5 = Table_item(None, None)
            item4.setIcon(icon)
            item5.setIcon(icon_bin)
            item1.setTextAlignment(Qt.AlignCenter)
            item2.setTextAlignment(Qt.AlignCenter)
            # item3.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(self.table.rowCount() - 1, 0, item1)
            self.table.setItem(self.table.rowCount() - 1, 1, item2)
            self.table.setItem(self.table.rowCount() - 1, 2, item3)
            self.table.setItem(self.table.rowCount() - 1, 3, item4)
            self.table.setItem(self.table.rowCount() - 1, 4, item5)

    def set_history_list(self):
         self.table.setRowCount(0)
         operations = self.database.get_expenses_in_date_and_cost_range(self.filters.start_date, self.filters.end_date, self.filters.amount_min, self.filters.amount_max)
         operations = [operation for operation in operations if operation.category.name in self.filters.chosen_categories]
         operations.sort(key = lambda operation: operation.date)

         icon = QIcon(os.path.join(self.path, "../resources/pencil_16.png"))
         icon_bin = QIcon(os.path.join(self.path, "../resources/bin(1)_16.png"))
         for operation in operations:
            self.table.insertRow(self.table.rowCount())
            item1 = Table_item(operation.date.strftime("%Y-%m-%d"), operation.id)
            item2 = Table_item(str(operation.amount), operation.id)
            item3 = Table_item(operation.category.name, operation.id)
            item4 = Table_item(None, None)
            item5 = Table_item(None, None)
            item4.setIcon(icon)
            item5.setIcon(icon_bin)
            item1.setTextAlignment(Qt.AlignCenter)
            item2.setTextAlignment(Qt.AlignCenter)
            # item3.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(self.table.rowCount() - 1, 0, item1)
            self.table.setItem(self.table.rowCount() - 1, 1, item2)
            self.table.setItem(self.table.rowCount() - 1, 2, item3)
            self.table.setItem(self.table.rowCount() - 1, 3, item4)
            self.table.setItem(self.table.rowCount() - 1, 4, item5)


    def operation_edit(self, row, column):
        if(column == 3):
            operation_edit = History_edit()
            operation_edit.set_database(self.database)
            operation_edit.set_categories(self.database.get_all_categories())
            operation = self.database.get_expense_by_id(self.table.item(row, 0).id)
            operation_edit.set_operation(operation)
            operation_edit.exec_()
            self.set_history_list()

    def operation_remove(self, row, column):
        if(column == 4):
           window = Delete_history()
           result = window.exec_()
           if result == 1:
               self.database.delete_expense(self.table.item(row, 0).id)
               self.set_history_list()

    def set_filtres(self):
        window = Filter_dialog(self.filters)
        window.set_database(self.database)
        window.set_categories_list()
        window.exec_()
        self.set_history_list()

    def clear_filters(self):
        self.set_default_filters()
        self.set_default_history_list()

