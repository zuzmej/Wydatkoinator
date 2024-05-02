


# Wydatkoinator
This project was made: to ease the management of expenses and to have an insight into what we spend the most money on. It is available only in Polish language version (for now ;) ).

# Description
Technologies used in the projects are: Qt and Python. Wydatkoinator has several tabs on the left: Start, Incomes, Expenses, History of transactions and Analysis. Main view shows the summary of incomes and expenses during last 30 days.
![main_view](https://github.com/zuzmej/Wydatkoinator/assets/101196834/726257c7-4ed8-4a1d-b29f-3427eb4ca2b8)

Incomes tab shows last incomes and their value, and enables the user to add new incomes.
![incomes](https://github.com/zuzmej/Wydatkoinator/assets/101196834/7a6a70c0-71af-4e2a-be49-53e29eac9dc6)

Expenses tab lists all the categories that the user entered, provides options to add, delete or change the name of categories. It also enables the user to add expenses in two ways: either by entering date, name and price or by sending a csv file (for example bank statement).
![expenses](https://github.com/zuzmej/Wydatkoinator/assets/101196834/8b957b2b-8c90-41e0-8e73-24073f0df29a)
![csv](https://github.com/zuzmej/Wydatkoinator/assets/101196834/e7957360-6b07-4989-a34d-8bb06fd4d8e7)

History tab lists all the transactions. It is possible to edit or delete them. The transaction history can be filtered by date range, category, or price range.
![history](https://github.com/zuzmej/Wydatkoinator/assets/101196834/a70c98b9-a5c9-47f2-b4e9-6c22ed4f35d6)
![editing_transaction](https://github.com/zuzmej/Wydatkoinator/assets/101196834/dbc41cec-c253-477c-8753-146e96eacf9e)
![filtering_history](https://github.com/zuzmej/Wydatkoinator/assets/101196834/3f6bc96a-4ed4-45be-b7ac-f1f3407f5e85)

In analysis tab the user can view the graphs (pie chart or stacked chart) of chosen categories in the selected time period.  
![graph](https://github.com/zuzmej/Wydatkoinator/assets/101196834/fc08acc0-7c78-43d4-aaad-70c7323c4dcb)
![analysis_graph_circle](https://github.com/zuzmej/Wydatkoinator/assets/101196834/961fce9b-c0c6-47a8-9608-5f949e785cbf)

# Prerequirements
To execute the program, check in terminal:
```bash
pip show PyQt5
pip show PyQtChart
pip show sqlalchemy
sqlite3 --version
```
If not installed, do:
```bash
pip install PyQt5
pip install PyQtChart
pip install sqlalchemy
sudo apt-get install sqlite3
```
# Run
To run program do:
```bash
cd src/tabs
python3 main.py
```
<!-- # Build
In directory "build":
```bash
cmake ..
make
``` -->
