from PyQt5.QtWidgets import QWidget
from datetime import datetime, timedelta
from src.ui.expenses_tab import Ui_expenses_tab
from src.database.database import Database
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import Qt
from src.tabs.add_new_category import Add_new_category
from src.tabs.delete_category import Delete_category
from src.tabs.change_category_name_dialog import Change_category_name_dialog

class Expenses_tab(QWidget, Ui_expenses_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None

        self.date_edit.setDate(datetime.today().date()) #ustawienie domyślnej daty
        
        validator = QDoubleValidator(0.00, 1000000.00, 2)
        self.amount_line_edit.setValidator(validator)

        self.add_category_button.clicked.connect(self.add_new_category)
        self.change_category_button.clicked.connect(self.change_category_name)
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
        self.categories_list_list.setSpacing(20)

    def clear_categories_list(self):
        self.categories_combobox.clear()
        self.categories_list_list.clear()

    def add_new_category(self):     # dodawanie nowej kategorii po nacisnieciu przycisku
        add_new_category_dialog = Add_new_category()
        add_new_category_dialog.exec_() # wyświetlenie okna dialogowego z wstrzymaniem dzialania reszty aplikacji
        if add_new_category_dialog.add_category_line_edit.text().strip():   # sprawdzenie czy został wprowadzony tekst, ktory nie jest bialymi znakami
            self.database.add_category(add_new_category_dialog.add_category_line_edit.text())
            self.clear_categories_list()
            self.set_categories_list()

    def delete_category(self):  # usuwanie nowej kategorii po nacisnieciu przycisku
        delete_category = Delete_category() 
        categories = self.database.get_all_categories() # pobranie i wyświetlenie wszystkich kategorii
        category_names = [category.name for category in categories]
        delete_category.delete_category_combobox.addItems(category_names)
        delete_category.exec_() # wyświetlenie okna dialogowego z wstrzymaniem dzialania reszty aplikacji
        self.database.delete_category(delete_category.delete_category_combobox.currentText())
        self.clear_categories_list()
        self.set_categories_list()

    def change_category_name(self):
        print("klikniety")
        change_category_name_dialog = Change_category_name_dialog()
        categories = self.database.get_all_categories() # pobranie i wyświetlenie wszystkich kategorii
        category_names = [category.name for category in categories]
        change_category_name_dialog.change_category_combobox.addItems(category_names)
        change_category_name_dialog.exec_()
        self.database.change_category_name(change_category_name_dialog.change_category_combobox.currentText(), change_category_name_dialog.change_category_line_edit.text())
        self.clear_categories_list()
        self.set_categories_list()
        







    def confirm_and_write_to_database(self):    # wpisywanie do bazy danych po zatwierdzeniu danych 
        if self.amount_line_edit.text():    # sprawdzenie czy pole z kwotą zostało wypełnione
            date_edit_str = self.date_edit.date().toString("yyyy-MM-dd")
            self.database.add_expense(float(self.amount_line_edit.text().replace(',', '.')), date_edit_str, self.categories_combobox.currentIndex()+1)
            self.amount_line_edit.clear()


    def csv_read(self): # wpisywanie do bazy danych po przesłaniu pliku csv -- przemyslec
        pass

    def browse_file(self):  # przegladaj pliki po nacisnieciu przycisku
        pass