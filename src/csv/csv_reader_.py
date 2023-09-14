from src.csv.csv_dialog import Csv_dialog
from src.csv.modify_csv import Modify_csv
import csv
from src.csv.choose_columns_csv import Choose_columns_csv
from PyQt5.QtCore import QDate

# klasa nadrzędna, obsługująca czytanie pliku csv
class Csv_reader_():
    chosen_column_date = None
    chosen_column_amount = None
    chosen_column_description = []

    field_with_date = None
    field_with_amount = None
    field_with_description = []

    def __init__(self, selected_file_csv, database):    # przekazanie pliku csv oraz bazy danych
        self.selected_file_csv = selected_file_csv
        self.database = database


    # otwarcie pliku csv i obsługa okna dialogowego do modyfikowania pliku przez użytkownika
    def dialog_modify_csv(self):
        with open(self.selected_file_csv, mode='r+') as file:
                csv_reader = csv.reader(file,  delimiter=';')
                csv_content = "\n".join(";".join(row) for row in csv_reader)

                modify_csv = Modify_csv(csv_content, self.selected_file_csv)
                result = modify_csv.exec_()
                if result == 1:
                    return True


    # otwarcie pliku csv i obsługa okna dialogowego do wybierania kolumn
    def dialog_choose_columns(self):
        with open(self.selected_file_csv, mode='r+') as file:  # Otwieramy plik CSV w trybie do odczytu
            csv_reader = csv.reader(file,  delimiter=';')
            data = list(csv_reader)

            choose_columns_csv = Choose_columns_csv(data, self.selected_file_csv)
            result = choose_columns_csv.exec_()
            if result == 1 and choose_columns_csv.are_num_columns_entered() and choose_columns_csv.correctness_of_description_columns():
                self.set_numbers_of_columns(choose_columns_csv)
                return True


    # przypisywanie numerów kolumn do odpowiednich zmiennych oraz ich formatowanie
    def set_numbers_of_columns(self, choose_columns_csv):
        self.chosen_column_date = choose_columns_csv.num_of_col_with_date.text()
        self.chosen_column_amount = choose_columns_csv.num_of_col_with_amount.text()
        self.chosen_column_description = choose_columns_csv.num_of_cols_with_description.text()
        self.chosen_column_description = self.chosen_column_description.split(',')  # zamiana na listę
        self.chosen_column_description = [int(element) for element in self.chosen_column_description]   # zamiana na int


    # odczytywanie wiersz po wierszu pliku csv, wyświetlanie okna dialogowego do dobierania kategorii wydatku, wpisywanie wydatku lub wpływu do bazy danych
    def csv_read(self):
        with open(self.selected_file_csv, mode='r+') as file:
            csv_reader = csv.reader(file,  delimiter=';')
            self.check_first_row(csv_reader)    # odrzucenie nagłówków

            for row in csv_reader:
                self.set_fields_in_row(row) # odczytanie wybranych przez użytkownika pól 
                formatted_date = self.format_date() 

                csv_dialog = Csv_dialog(self.database)
                self.display_fields(csv_dialog) 
                
                if self.field_with_amount.startswith('-'):  # odczytano wydatek
                    result = csv_dialog.exec_() # otwarcie okna dialogowego do dobrania kategorii
                    if result == 1:
                        self.write_outcome_to_database(csv_dialog, formatted_date)
                    elif result == 2:  # kliknięto "odrzuć"
                        pass
                    else:   # kliknięto "anuluj"
                        break

                else:   # odczytano wpływ
                    category_id = self.get_category_id_for_incomes()    # sprawdzenie id kategorii "wpływ"
                    if category_id is None:
                        category_id = self.add_category_for_incomes_to_database()
                    self.write_income_to_database(formatted_date, category_id)


    # wpisanie wpływu do bazy danych
    def write_income_to_database(self, formatted_date, category_id):
        self.database.add_expense(float(self.field_with_amount.replace(",", ".").replace(" ", "")), formatted_date, category_id)


    # wpisanie wydatku do bazy danych
    def write_outcome_to_database(self, csv_dialog, formatted_date):
        category_id = self.database.get_category_id_by_name(csv_dialog.category_combobox.currentText())
        self.database.add_expense(float(self.field_with_amount.replace("-","").replace(",", ".").replace(" ", "")), formatted_date, category_id) 


    # wyświetlenie danych w odpowiednich polach w oknie dialogowym
    def display_fields(self, csv_dialog):
        csv_dialog.date_line_edit.setText(self.field_with_date)
        csv_dialog.amount_line_edit.setText(self.field_with_amount)

        for num in range(len(self.chosen_column_description)):
            csv_dialog.description_text_edit.appendPlainText(self.field_with_description[num])


    # przypisanie danych z wybranych kolumn w danym wierszu
    def set_fields_in_row(self, row):
        self.field_with_description.clear()
        self.field_with_date = row[int(self.chosen_column_date)-1]
        self.field_with_amount = row[int(self.chosen_column_amount)-1]

        for num in range(len(self.chosen_column_description)):
            self.field_with_description.append(row[self.chosen_column_description[num]-1])


    # wyłuskanie numeru id wpływów
    def get_category_id_for_incomes(self):
        possible_category_names = ["Wpływy", "Wplywy", "Wplyw", "wpływy", "wplywy", "wplyw"]
        category_id = None
        for category_name in possible_category_names:
            try:
                category_id = self.database.get_category_id_by_name(category_name)
                if category_id:
                    break
            except ValueError:
                pass
        return category_id


    # dodanie kategorii "wpływy" do bazy danych (zwraca id)
    def add_category_for_incomes_to_database(self):
        self.database.add_category("Wpływy")
        return self.database.get_category_id_by_name("Wpływy")


    # odpowiednie formatowanie daty przed wpisaniem do bazy danych
    def format_date(self):
        possible_formats = ["yyyy-MM-dd", "dd-MM-yyyy", "dd.MM.yyyy", "dd/MM/yyyy", "yyyy/MM/dd", "yyyy-MM-dd"]
        for format in possible_formats:
            try:
                date = QDate.fromString(self.field_with_date, format)
                formatted_date = date.toString("yyyy-MM-dd")
                if formatted_date:
                    break
            except ValueError:
                print("Źle sformatowana data")

        return formatted_date


    # pominięcie pierwszego rzędu z tytułami
    def check_first_row(self, csv_reader):
        next(csv_reader)