from src.ui.filter_dialog import Ui_filter_dialog
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QMessageBox
from .filters import Filters
from src.database.database import Database
from datetime import datetime, timedelta
from PyQt5.QtGui import QDoubleValidator
from .combobox import Combo_box

class Filter_dialog(QDialog, Ui_filter_dialog):
    def __init__(self,filters: Filters):
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

        self.amount_widget.setVisible(False)
        self.category_widget.setVisible(False)
        self.dates_widget.setVisible(False)

        self.dates_checkbox.stateChanged.connect(self.is_dates_checkbox_checked)
        self.categories_checkbox.stateChanged.connect(self.is_categories_checkbox_checked)
        self.amount_checkbox.stateChanged.connect(self.is_amount_checkbox_checked)

        self.filters = filters

        self.message_box = QMessageBox()
        self.message_box.setWindowTitle("Informacja")
        self.message_box.setStyleSheet("color: #c8beb7; background-color: #3e3e3e")
        self.message_box.setIcon(QMessageBox.Information)
        self.message_box.resize(100,100)


    def set_database(self, database: Database):
        self.database = database

    def set_categories_list(self):
        categories = self.database.get_all_categories()
        for category in categories:
            self.combo_box.add_item(category.name)

        self.combo_box.add_item("Wszystkie")

    # Meotdy do sprawdzania poprawności wprowadzanych zakresów dat i kwot
    def check_correctness_amount(self):
        if float(self.amount_min.text().replace(",", ".")) < float(self.amount_max.text().replace(",", ".")):
            return True
        else:
            return False
        
    def check_correctnes_dates(self):
        if self.date_from.date() < self.date_to.date():
            return True
        else:
            return False
    
    # Metody do sprawdzania stanów checkboxów
    def is_dates_checkbox_checked(self):
        if self.dates_checkbox.isChecked():
             self.dates_widget.setVisible(True)
        else:
             self.dates_widget.setVisible(False)

    def is_amount_checkbox_checked(self):
        if self.amount_checkbox.isChecked():
            self.amount_widget.setVisible(True)
        else:
            self.amount_widget.setVisible(False)

    def is_categories_checkbox_checked(self):
        if self.categories_checkbox.isChecked():
            self.category_widget.setVisible(True)
        else:
            self.category_widget.setVisible(False)


    def confirm(self):  # po kliknięciu przycisku ,,ok'' wpisywane sa odpowiednie wartosci do klasy Filters
        if self.dates_checkbox.isChecked():
            if self.check_correctnes_dates():
                self.filters.start_date = self.date_from.date().toString("yyyy-MM-dd")
                self.filters.end_date = self.date_to.date().toString("yyyy-MM-dd")
            else:
                self.message_box.setText("Wprowadź poprawny zakres dat")
                self.message_box.exec_()
                
        if self.categories_checkbox.isChecked():
            self.filters.chosen_categories = self.combo_box.get_checked_items()

        if self.amount_checkbox.isChecked():
            if self.check_correctness_amount():
                self.filters.amount_min = self.amount_min.text()
                self.filters.amount_max = self.amount_max.text()
            else:
                self.message_box.setText("Wprowadź poprawny zakres kwot")
                self.message_box.exec_()