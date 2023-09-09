from src.csv.csv_dialog import Csv_dialog
from src.csv.modify_csv import Modify_csv
import csv
from src.csv.choose_columns_csv import Choose_columns_csv

class Csv_reader_():
    chosen_column_date = None
    chosen_column_amount = None
    chosen_column_description = []

    def __init__(self, selected_file_csv, database):
        self.selected_file_csv = selected_file_csv
        self.database = database

    def dialog_modify_csv(self):
        with open(self.selected_file_csv, mode='r+') as file:  # Otwieramy plik CSV w trybie do odczytu
                csv_reader = csv.reader(file,  delimiter=';')
                print("wczytany plik")
                csv_content = "\n".join(";".join(row) for row in csv_reader)
                                

                modify_csv = Modify_csv(csv_content, self.selected_file_csv)
                modify_csv.exec_()
    # tutaj będzie kod obsługujący modyfikację pliku
    # rozwazyc czy nie zapisywac w nowym pliku

    def dialog_choose_columns(self):
        with open(self.selected_file_csv, mode='r+') as file:  # Otwieramy plik CSV w trybie do odczytu
                csv_reader = csv.reader(file,  delimiter=';')
                print("wczytany plik")
                data = list(csv_reader)
                print(data)

                choose_columns_csv = Choose_columns_csv(data, self.selected_file_csv)
                result = choose_columns_csv.exec_()
                if choose_columns_csv.num_of_col_with_date is not None and choose_columns_csv.num_of_col_with_amount is not None and choose_columns_csv.num_of_cols_with_description:   #jesli sa niepuste
                    self.chosen_column_date = choose_columns_csv.num_of_col_with_date.text()
                    self.chosen_column_amount = choose_columns_csv.num_of_col_with_amount.text()
                    self.chosen_column_description = choose_columns_csv.num_of_cols_with_description.text()
                    
    # tutaj będzie kod obsługujący okienko z wybieraniem kolumn

    def dialog_csv(self):
        pass
    # nie wiem czy będzie konieczne

    def csv_read(self):
        with open(self.selected_file_csv, mode='r+') as file:
            csv_reader = csv.reader(file,  delimiter=';')
            print("wczytany plik")
            self.check_first_row(csv_reader)

            for row in csv_reader:
                    column_with_date = row[int(self.chosen_column_date)-1]
                    column_with_amount = row[int(self.chosen_column_amount)-1]
                    column_with_description = row[int(self.chosen_column_description)-1]

                    csv_dialog = Csv_dialog(self.database)

                    csv_dialog.date_line_edit.setText(column_with_date)
                    csv_dialog.amount_line_edit.setText(column_with_amount)
                    csv_dialog.description_text_edit.setPlainText(column_with_description)


                    result = csv_dialog.exec_()
                    if result == 1:
                        category_id = self.database.get_category_id_by_name(csv_dialog.category_combobox.currentText())
                        print(category_id)
                        self.database.add_expense(float(csv_dialog.amount_line_edit.text().replace("-","").replace(",", ".").replace(" ", "")), csv_dialog.date_line_edit.text(), category_id)
                    else:   # jeśli nacisnie anuluj to sie przerwie petla
                        break

             
    # właściwa metoda czytania pliku

    def prepare_data(self):
        pass
    # metoda, która będzie: 
    # 1) ustawiać odpowiedni format daty
    # 2) odpowiednio ustawiać kwotę (replace -, , ,)
    # 3) łączyć opisy, jeśli już będzie można wpisywać więcej niż 1 cyfrę

    def check_first_row(self, csv_reader):
        next(csv_reader)    # pomija pierwszy rząd z tytułami
    # metoda do sprawdzania czy pierwszy rząd pliku to na pewno tytuły