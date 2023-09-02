from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from src.ui.history_tab import Ui_history_tab
from src.database.database import Database
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta

class History_tab(QWidget, Ui_history_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(["data", "kwota", "kategoria"," "," "])


    def set_database(self, database):
        self.database = database

    def set_default_history_list(self):
        self.table.setRowCount(0)
        operations = self.database.get_expenses_by_date_range((datetime.today().date() - timedelta(weeks = 2)).strftime("%Y-%m-%d"), datetime.today().date().strftime("%Y-%m-%d"))
        operations.sort(key=lambda x: x.date)
        icon = QIcon("o_16.png")
        for operation in operations:
            self.table.insertRow(self.table.rowCount())
            item1 = QTableWidgetItem(operation.date.strftime("%Y-%m-%d"))
            item2 = QTableWidgetItem(str(operation.amount))
            item3 = QTableWidgetItem(operation.category.name)
            item4 = QTableWidgetItem()
            item4.setIcon(icon)
            item1.setTextAlignment(Qt.AlignCenter)
            item2.setTextAlignment(Qt.AlignCenter)
            # item3.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(self.table.rowCount() - 1, 0, item1)
            self.table.setItem(self.table.rowCount() - 1, 1, item2)
            self.table.setItem(self.table.rowCount() - 1, 2, item3)
            self.table.setItem(self.table.rowCount() - 1, 3, item4)


