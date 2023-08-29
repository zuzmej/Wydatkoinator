from src.ui.delete_category_dialog import Ui_delete_category_dialog
from PyQt5.QtWidgets import QDialog

class Delete_category(QDialog, Ui_delete_category_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)