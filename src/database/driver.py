from database import Database
from datetime import date

from database import Database
from datetime import date

# Utworzenie bazy danych
db = Database('expenses.db')

# Dodawanie kategorii
categories = ['Food', 'Rent', 'Entertainment', 'Transport', 'Utilities']
for category in categories:
    try:
        db.add_category(category)
    except ValueError as e:
        print(e)

# Dodawanie wydatków
expenses = [
    {'amount': 150.0, 'date': date.today(), 'category_id': 1},
    {'amount': 1000.0, 'date': date.today(), 'category_id': 2},
    {'amount': 75.0, 'date': date.today(), 'category_id': 3},
    {'amount': 50.0, 'date': date.today(), 'category_id': 4},
    {'amount': 200.0, 'date': date.today(), 'category_id': 5}
]
for expense in expenses:
    try:
        db.add_expense(**expense)
    except ValueError as e:
        print(e)

# Wyświetlanie wszystkich kategorii
print("\nAll Categories:")
all_categories = db.get_categories()
for category in all_categories:
    print(f"ID: {category.id}, Name: {category.name}")

# Wyświetlanie kategorii po ID
print("\nCategory with ID=3:")
category = db.get_category(3)
print(f"ID: {category.id}, Name: {category.name}")

# Wyświetlanie wszystkich wydatków
print("\nAll Expenses:")
all_expenses = db.get_expenses()
for expense in all_expenses:
    print(f"ID: {expense.id}, Date: {expense.date}, Amount: {expense.amount}, Category ID: {expense.category_id}")

# Wyświetlanie wszystkich wydatków wraz z nazwą kategorii
print("\nAll Expenses with Category Name:")
expenses_with_category_name = db.get_expenses_with_category_name()
for expense in expenses_with_category_name:
    print(f"ID: {expense.id}, Date: {expense.date}, Amount: {expense.amount}, Category: {expense.category.name}")

# Wyświetlanie wydatku po ID
print("\nExpense with ID=2:")
expense = db.get_expenses_by_id(2)
print(f"ID: {expense.id}, Date: {expense.date}, Amount: {expense.amount}, Category ID: {expense.category_id}")

# Wyświetlanie wydatków na podstawie daty
print("\nExpenses on Date:")
date_expenses = db.get_expenses_by_date(date.today())
for expense in date_expenses:
    print(f"ID: {expense.id}, Date: {expense.date}, Amount: {expense.amount}, Category: {expense.category.name}")

# Wyświetlanie wydatków na podstawie kategorii
print("\nExpenses by Category ID:")
expenses_by_category_id = db.get_expenses_by_category_id(2)
for expense in expenses_by_category_id:
    print(f"ID: {expense.id}, Date: {expense.date}, Amount: {expense.amount}, Category: {expense.category.name}")

# Wyświetlanie wydatków na podstawie nazwy kategorii
print("\nExpenses by Category Name:")
expenses_by_category_name = db.get_expenses_by_category_name('Rent')
for expense in expenses_by_category_name:
    print(f"ID: {expense.id}, Date: {expense.date}, Amount: {expense.amount}, Category: {expense.category.name}")
