from src.ui.filter_dialog import Ui_filter_dialog
from PyQt5.QtWidgets import QDialog

class Filter_dialog(QDialog, Ui_filter_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)