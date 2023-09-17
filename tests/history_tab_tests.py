import sys

sys.path.insert(0, '../')
from src.tabs.history_tab import History_tab
from PyQt5 import QtWidgets
from src.database.database import Database
db = Database("expenses.db")
app = QtWidgets.QApplication(sys.argv)

w = History_tab()
w.set_database(db)
w.set_default_filters()
w.set_default_history_list()
w.show()

sys.exit(app.exec_())