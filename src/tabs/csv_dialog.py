from src.ui.csv_dialog import Ui_csv_dialog
from PyQt5.QtWidgets import QDialog

class Csv_dialog(QDialog, Ui_csv_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)