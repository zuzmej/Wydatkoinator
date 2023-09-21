from src.ui.add_new_category_dialog import Ui_add_category_dialog
from PyQt5.QtWidgets import QDialog

class Add_new_category(QDialog, Ui_add_category_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")
