from src.ui.filter_dialog import Ui_filter_dialog
from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from .filters import Filters
from src.database.database import Database
from datetime import datetime, timedelta
from PyQt5.QtGui import QDoubleValidator
from .combobox import Combo_box

class Filter_dialog(QDialog, Ui_filter_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None

        self.date_from.setDate(datetime.today().date()- timedelta(days=7)) #ustawienie domyślnej daty
        self.date_to.setDate(datetime.today().date())

        validator = QDoubleValidator(0.00, 1000000.00, 2)
        self.amount_min.setValidator(validator)
        self.amount_max.setValidator(validator)

        self.combo_box = Combo_box(self.category_combobox)

        self.ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        self.cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)

        self.ok_button.clicked.connect(self.confirm)

    def set_database(self, database: Database):
        self.database = database

    def set_categories_list(self):
        categories = self.database.get_all_categories()
        for category in categories:
            self.combo_box.add_item(category.name)

        self.combo_box.add_item("Wszystkie")

    def check_correctness_amount(self):
        if float(self.amount_min.text()) < float(self.amount_max.text()):
            return True
        else:
            return False
        
    def confirm(self):
        print("confirm")
        # sprawdzenie dat
        # sprawdzenie kwot
        # wpisac do obiektu filters

# UWAGA. czyszczenie pola z datami / domyslnie nieustawianie zadnej ? -- przypadek, kiedy uzytkownik otwiera okno, ale nie chce filtrowac po datach