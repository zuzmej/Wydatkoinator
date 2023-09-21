from PyQt5.QtWidgets import QDialog
from src.ui.delete_history import Ui_delete_history

class Delete_history(QDialog, Ui_delete_history):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")



        