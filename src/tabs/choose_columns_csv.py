from src.ui.choose_columns_csv import Ui_choose_columns_csv
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

class Choose_columns_csv(QDialog, Ui_choose_columns_csv):
    number_of_column_with_date = None
    number_of_column_with_amount = None
    numbers_of_columns_with_description = []

    def __init__(self, csv_content, csv_file):  #przekazanie zawartości pliku csv oraz ścieżki do pliku
        super().__init__()
        self.setupUi(self)
        self.csv_content = csv_content
        self.csv_file = csv_file

        self.ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        self.cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)

        self.ok_button.clicked.connect(self.confirm)

    def confirm(self):
        pass

    def get_columns_numbers(self):
        pass