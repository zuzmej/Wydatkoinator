from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from src.ui.history_edit import Ui_history_edit
from PyQt5.QtGui import QDoubleValidator
class History_edit(QDialog, Ui_history_edit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.operation = None
        self.Database = None
        self.validator = QDoubleValidator(0.00, 1000000.00, 2)
        self.line_edit.setValidator(self.validator)
        ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        ok_button.clicked.connect(self.confirm_changes)
        self.setWindowTitle(" ")


    def set_database(self, database):
        self.database = database

    def set_categories(self, categories):
        self.combo_box.clear()
        for category in categories:
            self.combo_box.addItem(category.name)

    def set_operation(self, operation):
        self.operation = operation
        self.line_edit.setText(str(operation.amount))
        self.date_edit.setDate(operation.date)
        self.combo_box.setCurrentText(operation.category.name)

    def confirm_changes(self):
        amount = self.line_edit.text()
        if amount.strip():
           self.database.edit_expense(self.operation.id,float(self.line_edit.text()),self.date_edit.date().toString("yyyy-MM-dd"),self.database.get_category_id_by_name(self.combo_box.currentText()))
           self.close()
    

    

