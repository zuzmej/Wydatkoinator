import sys
sys.path.insert(0, '../')


from src.tabs.incomes_tab import Incomes_tab
from PyQt5 import QtWidgets
from src.database.database import Database
db = Database("expenses.db")

expenses = db.get_all_expenses()

app = QtWidgets.QApplication(sys.argv)

w = Incomes_tab()
w.set_database(db)
w.set_incomes_list()
w.show_chart()

w.show()

sys.exit(app.exec_())   