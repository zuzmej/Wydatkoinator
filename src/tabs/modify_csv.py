from src.ui.modify_csv import Ui_modify_csv
from PyQt5.QtWidgets import QDialog

class Modify_csv(QDialog, Ui_modify_csv):
    def __init__(self):
        super().__init__()
        self.setupUi(self)