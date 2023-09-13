from src.csv.csv_dialog import Csv_dialog
from src.csv.modify_csv import Modify_csv
import csv
from src.csv.choose_columns_csv import Choose_columns_csv
from PyQt5.QtCore import QDate

class Csv_reader_():
    chosen_column_date = None
    chosen_column_amount = None
    chosen_column_description = []

    column_with_date = None
    column_with_amount = None
    column_with_description = []

    def __init__(self, selected_file_csv, database):
        self.selected_file_csv = selected_file_csv
        self.database = database

    def dialog_modify_csv(self):
        with open(self.selected_file_csv, mode='r+') as file:  # Otwieramy plik CSV w trybie do odczytu
                csv_reader = csv.reader(file,  delimiter=';')
                csv_content = "\n".join(";".join(row) for row in csv_reader)
                                

                modify_csv = Modify_csv(csv_content, self.selected_file_csv)
                result = modify_csv.exec_()
                if result == 1:
                    return True


    def dialog_choose_columns(self):
        with open(self.selected_file_csv, mode='r+') as file:  # Otwieramy plik CSV w trybie do odczytu
            csv_reader = csv.reader(file,  delimiter=';')
            data = list(csv_reader)

            choose_columns_csv = Choose_columns_csv(data, self.selected_file_csv)
            result = choose_columns_csv.exec_()
            if result == 1:
                if choose_columns_csv.num_of_col_with_date is not None and choose_columns_csv.num_of_col_with_amount is not None and choose_columns_csv.num_of_cols_with_description:   #jesli sa niepuste - !!! + jeśli są akceptowane
                    if choose_columns_csv.correctness_of_description_columns():
                        self.chosen_column_date = choose_columns_csv.num_of_col_with_date.text()
                        self.chosen_column_amount = choose_columns_csv.num_of_col_with_amount.text()
                        self.chosen_column_description = choose_columns_csv.num_of_cols_with_description.text()
                        self.chosen_column_description = self.chosen_column_description.split(',')  #zamiana na listę
                        self.chosen_column_description = [int(element) for element in self.chosen_column_description]   # zamiana na int


                        print(self.chosen_column_description)
                        return True
            # else:
            #     return False
                    
    # tutaj będzie kod obsługujący okienko z wybieraniem kolumn

    def dialog_csv(self):
        pass
    # nie wiem czy będzie konieczne

    def csv_read(self):
        with open(self.selected_file_csv, mode='r+') as file:
            csv_reader = csv.reader(file,  delimiter=';')
            self.check_first_row(csv_reader)

            for row in csv_reader:
                self.column_with_description.clear()
                self.column_with_date = row[int(self.chosen_column_date)-1]
                self.column_with_amount = row[int(self.chosen_column_amount)-1]


                for num in range(len(self.chosen_column_description)):
                    self.column_with_description.append(row[self.chosen_column_description[num]-1])
                    print(self.column_with_description)

                formatted_date = self.format_date()

                csv_dialog = Csv_dialog(self.database)
                csv_dialog.date_line_edit.setText(self.column_with_date)
                csv_dialog.amount_line_edit.setText(self.column_with_amount)

                for num in range(len(self.chosen_column_description)):
                    print(num)
                    print(self.column_with_description)
                    csv_dialog.description_text_edit.appendPlainText(self.column_with_description[num])

                if self.column_with_amount.startswith('-'):  # jezeli odczytany jest wydatek
                    result = csv_dialog.exec_()
                    if result == 1:
                        category_id = self.database.get_category_id_by_name(csv_dialog.category_combobox.currentText())
                        self.database.add_expense(float(self.column_with_amount.replace("-","").replace(",", ".").replace(" ", "")), formatted_date, category_id) 
                    else:   # jeśli nacisnie anuluj to sie przerwie petla
                        break

                else:   # odczytany jest wpływ, czyli kwota na plusie
                    print("To jest wpływ - wpisuję do bazy")

                    category_id = self.get_category_id_for_incomes()
                    if category_id is None:
                        category_id = self.add_category_for_incomes_to_database()
                    
                    self.database.add_expense(float(self.column_with_amount.replace(",", ".").replace(" ", "")), formatted_date, category_id)


             
    def count_numbers_in_list(self, input_str):
        numbers = [num.strip() for num in numbers if num.strip()]
        return len(numbers)

    def get_category_id_for_incomes(self):  # zwraca category_id lub None
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


    def add_category_for_incomes_to_database(self):
        self.database.add_category("Wpływy")
        return self.database.get_category_id_by_name("Wpływy")
        


    def format_date(self):
        possible_formats = ["yyyy-MM-dd", "dd-MM-yyyy", "dd.MM.yyyy", "dd/MM/yyyy", "yyyy-MM-dd"]
        for format in possible_formats:
            try:
                date = QDate.fromString(self.column_with_date, format)
                formatted_date = date.toString("yyyy-MM-dd")
                if formatted_date:
                    break
            except ValueError:
                print("Źle sformatowana data")

        return formatted_date


    def prepare_data(self):
        pass


    # metoda, która będzie: 
    # 1) ustawiać odpowiedni format daty
    # 2) odpowiednio ustawiać kwotę (replace -, , ,)
    # 3) łączyć opisy, jeśli już będzie można wpisywać więcej niż 1 cyfrę

    def check_first_row(self, csv_reader):
        next(csv_reader)    # pomija pierwszy rząd z tytułami
    # metoda do sprawdzania czy pierwszy rząd pliku to na pewno tytuły