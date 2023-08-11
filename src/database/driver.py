import sys
sys.path.insert(0, '../../')  # Dodaj katalog nadrzędny do ścieżki

from src.database.database import Database
db = Database("expenses.db")

# Add categories
try:
    print("\nAdding categories...")
    db.add_category("Groceries")
    db.add_category("Rent")
    db.add_category("Transport")
except ValueError as e:
    print(e)  # handle error if category already exists

try:
    # Add expenses
    print("\nAdding expenses...")
    db.add_expense(amount=100.50, date="2023-07-01", category_id=1)
    db.add_expense(amount=800.00, date="2023-07-05", category_id=2)
    db.add_expense(amount=50.00, date="2023-07-10", category_id=3)
except ValueError as e:
    print(e)  # handle error if try to add expense with non-existing category


# Get all categories
print("\nGetting all categories...")
categories = db.get_all_categories()
for category in categories:
    print(category.name)

# Get category by id
print("\nGetting category by id...")
category = db.get_category_by_id(1)
print(f"Category ID: {category.id}, Name: {category.name}")

# Get all expenses
print("\nGetting all expenses...")
expenses = db.get_all_expenses()
for expense in expenses:
    print(f"Expense ID: {expense.id}, Amount: {expense.amount}, Date: {expense.date}, Category: {expense.category.name}")

# Get expense by id
print("\nGetting expense by id...")
expense = db.get_expense_by_id(2)
print(f"Expense ID: {expense.id}, Amount: {expense.amount}, Date: {expense.date}, Category: {expense.category.name}")

# Get expenses by date
print("\nGetting expenses by date...")
expenses_by_date = db.get_expenses_by_date("2023-07-01")
for expense in expenses_by_date:
    print(f"Expense ID: {expense.id}, Amount: {expense.amount}, Date: {expense.date}, Category: {expense.category.name}")

# Get expenses by date range
print("\nGetting expenses by date range...")
expenses_by_date_range = db.get_expenses_by_date_range("2023-07-01", "2023-07-10")
for expense in expenses_by_date_range:
    print(f"Expense ID: {expense.id}, Amount: {expense.amount}, Date: {expense.date}, Category: {expense.category.name}")

# Get expenses by category id in date range
print("\nGetting expenses by category id in date range...")
expenses_by_category_id_date_range = db.get_expenses_by_category_id_in_date_range(1, "2023-07-01", "2023-07-10")
for expense in expenses_by_category_id_date_range:
    print(f"Expense ID: {expense.id}, Amount: {expense.amount}, Date: {expense.date}, Category: {expense.category.name}")

# Get expenses by category name
print("\nGetting expenses by category name...")
expenses_by_category_name = db.get_expenses_by_category_name_in_date_range("Rent", "2023-07-01", "2023-07-10")
for expense in expenses_by_category_name:
    print(f"Expense ID: {expense.id}, Amount: {expense.amount}, Date: {expense.date}, Category: {expense.category.name}")

print("Getting expenses in date and cost range...")
expenses_in_range = db.get_expenses_in_date_and_cost_range("2023-07-01", "2023-07-31", 50.00, 200.00)
for expense in expenses_in_range:
    print(f"Expense ID: {expense.id}, Amount: {expense.amount}, Date: {expense.date}, Category: {expense.category.name}")
    
# Edit expense
try:
    print("\nEditing expense...")
    db.edit_expense(expense_id=1, amount=150.00, date="2023-07-02", category_id=2)
except ValueError as e:
    print(e)  # handle error if try to edit non-existing expense or category

# Get expense by id to check the edit
print("\nGetting expense by id...")
expense = db.get_expense_by_id(1)
if expense is not None:
    print(f"Expense ID: {expense.id}, Amount: {expense.amount}, Date: {expense.date}, Category: {expense.category.name}")
else:
    print("No expense found with this ID")

# Delete expense
try:
    print("\nDeleting expense...")
    db.delete_expense(expense_id=1)
except ValueError as e:
    print(e)  # handle error if try to delete non-existing expense

# Get all expenses to check the delete
print("\nGetting all expenses...")
expenses = db.get_all_expenses()
for expense in expenses:
    print(f"Expense ID: {expense.id}, Amount: {expense.amount}, Date: {expense.date}, Category: {expense.category.name}")   