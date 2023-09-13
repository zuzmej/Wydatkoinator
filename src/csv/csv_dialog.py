from src.ui.csv_dialog import Ui_csv_dialog
from PyQt5.QtWidgets import QDialog

# okno dialogowe, w którym wyświetlane są odczytane z pliku data, kwota i opis, i użytkownik musi dobrać kategorię
class Csv_dialog(QDialog, Ui_csv_dialog):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)

        self.database = database
        categories = self.database.get_all_categories() # pobranie i wyświetlenie wszystkich kategorii
        category_names = [category.name for category in categories]
        self.category_combobox.addItems(category_names)