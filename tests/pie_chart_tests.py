import sys
sys.path.insert(0, '../')

from src.charts.pie_chart import Pie_chart

from PyQt5 import QtWidgets
from src.database.database import Database
from src.ui.chart import Ui_Chart
db = Database("../src/database/expenses.db")

expenses = db.get_all_expenses()

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
ui = Ui_Chart()
ui.setupUi(w)

pie_chart = Pie_chart(ui.chart)
pie_chart.draw_chart(expenses)

w.show()

sys.exit(app.exec_())   