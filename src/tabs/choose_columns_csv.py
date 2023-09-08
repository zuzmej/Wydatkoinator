from src.ui.choose_columns_csv import Ui_choose_columns_csv
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem

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
 
        num_rows = len(self.data)
        num_cols = len(self.data[0])   
        self.table_csv.setRowCount(num_rows)
        self.table_csv.setColumnCount(num_cols)

        try:
            for row in range(num_rows):
                for col in range(num_cols):
                    item = QTableWidgetItem(data[row][col])
                    self.table_csv.setItem(row, col, item)
        except Exception as e:
            print(f"Błąd podczas wczytywania pliku CSV: {str(e)}")



    def confirm(self):
        pass

    def get_columns_numbers(self):
        pass
