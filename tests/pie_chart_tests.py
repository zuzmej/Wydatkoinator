import sys
sys.path.insert(0, '../')

from src.charts.pie_chart import Pie_chart

from PyQt5 import QtWidgets
from src.database.database import Database
db = Database("../src/database/expenses.db")

expenses = db.get_all_expenses()

app = QtWidgets.QApplication(sys.argv)

pie_chart = Pie_chart()
pie_chart.draw_chart(expenses)

pie_chart.show()

sys.exit(app.exec_())   