import sys
sys.path.insert(0, '../../')

from src.tabs.main_window import Main_window
from PyQt5 import QtWidgets
from src.database.database import Database


if __name__ == "__main__":

    db = Database("expenses.db")

    app = QtWidgets.QApplication(sys.argv)

    w = Main_window(db)

    w.show()

    sys.exit(app.exec_())
