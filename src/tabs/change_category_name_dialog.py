from src.ui.change_category_name_dialog import Ui_change_category_name_dialog
from PyQt5.QtWidgets import QDialog

class Change_category_name_dialog(QDialog, Ui_change_category_name_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)