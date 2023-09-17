import sys
sys.path.insert(0, '../')


from src.tabs.filter_dialog import Filter_dialog

from PyQt5 import QtWidgets
from src.database.database import Database
db = Database("expenses.db")

expenses = db.get_all_expenses()

app = QtWidgets.QApplication(sys.argv)

w = Filter_dialog()
w.set_database(db)
w.set_categories_list()

w.show()

sys.exit(app.exec_())  