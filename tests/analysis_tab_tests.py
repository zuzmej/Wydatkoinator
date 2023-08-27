import sys
sys.path.insert(0, '../')


from src.tabs.analysis_tab import Analysis_tab

from PyQt5 import QtWidgets
from src.database.database import Database
db = Database("/home/kubus/Pulpit/wyadtki/expenses.db")

expenses = db.get_all_expenses()

app = QtWidgets.QApplication(sys.argv)

w = Analysis_tab()
w.set_database(db)
w.set_categories_list()

w.show()

sys.exit(app.exec_())   