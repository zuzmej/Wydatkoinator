from PyQt5.QtWidgets import QWidget
from datetime import datetime, timedelta
from src.ui.analysis_tab import Ui_analisys_tab

class Analysis_tab(QWidget, Ui_analisys_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_pie_chart_set = False
        self.is_stack_chart_set = False
        self.date_from.setDate(datetime.today().date() - timedelta(days=7))
        self.date_to.setDate(datetime.today().date())
        self.date_from.setCalendarPopup(True)
        self.date_to.setCalendarPopup(True)
        self.pie_chart_button.clicked.connect(self.set_pie_chart)
        self.stack_chart_button.clicked.connect(self.set_stack_chart)
        

    def set_pie_chart(self):
        self.is_pie_chart_set = True
        self.is_stack_chart_set = False
        print("pie chart set")

    def set_stack_chart(self):
        self.is_pie_chart_set = False
        self.is_stack_chart_set = True
        print("stack chart set")
    


    

