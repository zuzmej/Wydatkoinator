from src.ui.modify_csv import Ui_modify_csv
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

class Modify_csv(QDialog, Ui_modify_csv):
    def __init__(self, csv_content, csv_file):  #przekazanie zawartości pliku csv oraz ścieżki do pliku
        super().__init__()
        self.setupUi(self)
        self.csv_content = csv_content
        self.csv_file = csv_file

        self.plain_text_modify.insertPlainText(self.csv_content)    # wyświetlenie zawartości pliku w odpowiednim miejscu

        self.ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        self.cancel_button = self.buttonBox.button(QDialogButtonBox.Cancel)

        self.ok_button.clicked.connect(self.confirm)

    def confirm(self):  # metoda do zatwierdzania zmian w pliku (nadpisywanie)
        csv_content = self.plain_text_modify.toPlainText()
        with open(self.csv_file, mode='w') as file:
            file.write(csv_content)

