from PyQt5.QtWidgets import QWidget
from datetime import datetime, timedelta
from src.ui.expenses_tab import Ui_expenses_tab
from src.database.database import Database
from PyQt5.QtGui import QDoubleValidator

class Expenses_tab(QWidget, Ui_expenses_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None

        self.date_edit.setDate(datetime.today().date()) #ustawienie domyślnej daty
        
        validator = QDoubleValidator(0.00, 1000000.00, 2)
        self.amount_line_edit.setValidator(validator)

        self.add_category_button.clicked.connect(self.add_new_category)
        self.delete_category_button.clicked.connect(self.delete_category)
        self.ok_button.clicked.connect(self.confirm_and_write_to_database)
        self.ok_button_csv.clicked.connect(self.csv_read)
        self.browse_file_button.clicked.connect(self.browse_file)

    def set_database(self, database: Database):
        self.database = database

    def set_categories_list(self):
        categories = self.database.get_all_categories()
        category_names = [category.name for category in categories]
        self.categories_combobox.addItems(category_names)
        self.categories_list_list.addItems(category_names)


    def add_new_category(self):     # dodawanie nowej kategorii po nacisnieciu przycisku
        pass
        #self.database.add_category()
        # tworzenie nowego okna dialogowego

    def delete_category(self):  # usuwanie nowej kategorii po nacisnieciu przycisku
        pass
        
    def confirm_and_write_to_database(self):    # wpisywanie do bazy danych po zatwierdzeniu danych 
        if self.amount_line_edit.text():    # sprawdzenie czy pole z kwotą zostało wypełnione
            date_edit_str = self.date_edit.date().toString("yyyy-MM-dd")
            self.database.add_expense(float(self.amount_line_edit.text().replace(',', '.')), date_edit_str, self.categories_combobox.currentIndex()+1)
            self.amount_line_edit.clear()


    def csv_read(self): # wpisywanie do bazy danych po przesłaniu pliku csv -- przemyslec
        pass

    def browse_file(self):  # przegladaj pliki po nacisnieciu przycisku
        pass