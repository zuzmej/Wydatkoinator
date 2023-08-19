from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QCheckBox

from PyQt5.QtCore import Qt


class Combo_box():
    def __init__(self, combobox):
        # Przypisujemy istniejący ComboBox do lokalnej zmiennej
        self.combobox = combobox
        
        # Inicjalizujemy pozostałe atrybuty
        self.list_widget = QListWidget(self.combobox)
        self.combobox.setLineEdit(None)
        self.combobox.setModel(self.list_widget.model())
        self.combobox.setView(self.list_widget)
        
        self.boxes = []
    
    def add_item(self, text):
        checkbox = QCheckBox(text, self.combobox)
        checkbox.stateChanged.connect(self.checkbox_state_changed)  # Dodajemy sygnał dla każdego checkboxa
        self.boxes.append(checkbox)

        item = QListWidgetItem(self.list_widget)
        item.setSizeHint(checkbox.sizeHint())
        self.list_widget.setItemWidget(item, checkbox)

    def checkbox_state_changed(self, state):
        # Sprawdzamy, czy zmieniony checkbox to "Wszystkie"
        sender = self.combobox.sender()
        if sender.text() == "Wszystkie":
            if state == Qt.Checked:  # Jeśli "Wszystkie" zostanie zaznaczony
                self.select_all()
            else:  # Jeśli "Wszystkie" zostanie odznaczony
                self.deselect_all()


    def select_all(self):
        for box in self.boxes:
            box.setChecked(True)

    def deselect_all(self):
        for box in self.boxes:
            box.setChecked(False)

    def get_checked_items(self):
        return [box.text() for box in self.boxes if box.isChecked()]
