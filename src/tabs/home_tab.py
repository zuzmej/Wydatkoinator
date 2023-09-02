from src.ui.home_tab import Ui_home_tab
from PyQt5.QtWidgets import QWidget

class Home_tab(QWidget, Ui_home_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)