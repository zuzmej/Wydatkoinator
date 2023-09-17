from PyQt5.QtWidgets import QTableWidgetItem

class Table_item(QTableWidgetItem):
    def __init__(self, text: str, id: int):
        super().__init__(text)
        self.id = id
