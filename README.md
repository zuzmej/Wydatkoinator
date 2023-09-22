# Wydatkoinator
This project was created in order to ease the management of our spending, to have more control over it and to have an insight into what we spend the most money on.

# Description
The project was created in Qt and Python. It includes several options listed below:
- adding expenses in two ways: either by adding name, price and date or by sending a csv file (for example bank statement),
- viewing reports and graphs comparing the amount of money spent on a chosen category in the selected time period,
- showing database that stores all expenses added to the app.

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
