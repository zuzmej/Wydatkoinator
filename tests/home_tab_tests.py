import sys
sys.path.insert(0, '../')


from src.tabs.home_tab import Home_tab

from PyQt5 import QtWidgets
from src.database.database import Database
db = Database("../../Pobrane/expenses.db")

expenses = db.get_all_expenses()

app = QtWidgets.QApplication(sys.argv)

w = Home_tab()

w.show()

sys.exit(app.exec_())  