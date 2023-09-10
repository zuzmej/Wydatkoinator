from src.ui.choose_columns_csv import Ui_choose_columns_csv
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class Choose_columns_csv(QDialog, Ui_choose_columns_csv):
    num_of_col_with_date = None
    num_of_col_with_amount = None
    num_of_cols_with_description = []

    def __init__(self, data, csv_file):  #przekazanie zawartości pliku csv oraz ścieżki do pliku
        super().__init__()
        self.setupUi(self)
        self.data = data
        self.csv_file = csv_file

        self.ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        self.cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)
        self.ok_button.clicked.connect(self.confirm)



        # wpisywanie zawartości pliku csv do tabeli 
 
        self.num_rows = len(self.data)
        self.num_cols = len(self.data[0])   
        self.table_csv.setRowCount(self.num_rows)
        self.table_csv.setColumnCount(self.num_cols)

        try:
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    item = QTableWidgetItem(data[row][col])
                    self.table_csv.setItem(row, col, item)
        except Exception as e:
            print(f"Błąd podczas wczytywania pliku CSV: {str(e)}")


        # poprawnosc wpisywanych danych
        validator = QIntValidator(1, self.num_cols, self)
        self.date_column.setValidator(validator)
        self.amount_column.setValidator(validator)

        validator_description = QRegExpValidator(QRegExp("^[0-9,]+$"))
        self.description_column.setValidator(validator_description)

    def confirm(self):
        if self.correctness_of_description_columns:
            print("Poprawny format")

            if self.date_column.text().strip() and self.amount_column.text().strip() and self.description_column.text().strip():
                self.get_columns_numbers()
                print(self.date_column.text())
                print(self.amount_column.text())
                print(self.description_column.text())
            else:
                print("Nie wprowadzono numerów kolumn")
        else:
            pass


    def correctness_of_description_columns(self):   # do poprawy!!
        if self.description_column.hasAcceptableInput():
            values = self.description_column.text().split(',')
            for value in values:
                num = int(value)
                if num < 1 or num > self.num_cols:
                    print(f"Liczby muszą być w zakresie od 1 do {self.num_cols}.")
                    return False
        return True
    

    def get_columns_numbers(self):
        self.num_of_col_with_date = self.date_column
        self.num_of_col_with_amount = self.amount_column
        self.num_of_cols_with_description = self.description_column
