import sys
sys.path.insert(0, '../')

from src.ui.analysis_tab import Ui_analisys_tab

from PyQt5 import QtWidgets
from src.database.database import Database
db = Database("../src/database/expenses.db")

expenses = db.get_all_expenses()

app = QtWidgets.QApplication(sys.argv)

w = QtWidgets.QWidget()
ui = Ui_analisys_tab()
ui.setupUi(w)
ui.chart.draw_chart(expenses)
w.show()

sys.exit(app.exec_())   