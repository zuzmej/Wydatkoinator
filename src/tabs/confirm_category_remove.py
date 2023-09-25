from PyQt5.QtWidgets import QDialog
from src.ui.confirm_category_remove import Ui_Confirm_category_remove

class Confirm_category_remove(QDialog, Ui_Confirm_category_remove):
    def __init__(self, parent=None):
        super(Confirm_category_remove, self).__init__(parent)
        self.setupUi(self)