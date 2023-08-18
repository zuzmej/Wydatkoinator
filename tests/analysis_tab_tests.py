import sys
sys.path.insert(0, '../')

from src.ui.analysis_tab import Ui_analisys_tab
from src.tabs.analysis_tab import Analysis_tab

from PyQt5 import QtWidgets
from src.database.database import Database
from src.charts.pie_chart import Pie_chart
db = Database("../src/database/expenses.db")

expenses = db.get_all_expenses()

app = QtWidgets.QApplication(sys.argv)

w = Analysis_tab()
pie_chart = Pie_chart(w.chart)
pie_chart.draw_chart(expenses)
w.show()

sys.exit(app.exec_())   