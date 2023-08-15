import unittest
import sys
sys.path.insert(0, '../')  # Dodaj katalog nadrzędny do ścieżki

from src.database.database import Database

class Database_test(unittest.TestCase):
    db = Database("../src/database/expenses.db")

    def test_add_category(self):
        self.assertRaises(ValueError, self.db.add_category, "Groceries")
    def test_add_expense(self):
        self.assertRaises(ValueError, self.db.add_expense, 100.50, "2023-07-01", 10)

    def test_get_all_category(self):
        categories = self.db.get_all_categories()
        categories_list = ["Groceries","Rent","Transport"]
        for i in categories:
            self.assertIn(i.name,categories_list)

    def test_get_category_by_id(self):
        category = self.db.get_category_by_id(1)
        self.assertEqual(category.name,"Groceries")

    def test_get_all_expenses(self):
        expenses = self.db.get_all_expenses()
        expenses_list = [100.50,800.00,50.00]
        for i in expenses:
            self.assertIn(i.amount,expenses_list)

    def test_get_expense_by_id(self):
        expense = self.db.get_expense_by_id(1)
        self.assertEqual(expense.amount,100.50)

    def test_get_expenses_by_date(self):
        expenses = self.db.get_expenses_by_date("2023-07-01")
        expenses_list = [100.50]
        for i in expenses:
            self.assertIn(i.amount,expenses_list)

    def test_get_expenses_by_date_range(self):
        expenses = self.db.get_expenses_by_date_range("2023-07-01", "2023-07-10")
        expenses_list = [100.50,800.00,50.00]
        for i in expenses:
            self.assertIn(i.amount,expenses_list)
    
    def test_get_expenses_by_category_id_in_date_range(self):
        expenses = self.db.get_expenses_by_category_id_in_date_range(1, "2023-07-01", "2023-07-10")
        expenses_list = [100.50]
        for i in expenses:
            self.assertIn(i.amount,expenses_list)
        
    def test_get_expenses_by_category_name_in_date_range(self):
        expenses = self.db.get_expenses_by_category_name_in_date_range("Rent", "2023-07-01", "2023-07-10")
        expenses_list = [800.00]
        for i in expenses:
            self.assertIn(i.amount,expenses_list)

    def test_get_expenses_in_date_and_cost_range(self):
        expenses = self.db.get_expenses_in_date_and_cost_range("2023-07-01", "2023-07-10", 0, 100)
        expenses_list = [100.50,50.00]
        for i in expenses:
            self.assertIn(i.amount,expenses_list)

    def test_get_expenses_by_date_2(self):
        expenses = self.db.get_expenses_by_date("2021-07-01")
        self.assertEqual(len(expenses),0)        

    def test_get_expenses_by_date_range_2(self):
        expenses = self.db.get_expenses_by_date_range("2022-07-01", "2022-07-10")
        self.assertEqual(len(expenses),0)        

    
    def test_get_expenses_by_category_id_in_date_range_2(self):
        expenses = self.db.get_expenses_by_category_id_in_date_range(1, "2022-07-01", "2022-07-10")
        self.assertEqual(len(expenses),0)        
        
        
    def test_get_expenses_by_category_name_in_date_range_2(self):
        expenses = self.db.get_expenses_by_category_name_in_date_range("Rent", "2022-07-01", "2022-07-10")
        self.assertEqual(len(expenses),0)        


    def test_get_expenses_in_date_and_cost_range_2(self):
        expenses = self.db.get_expenses_in_date_and_cost_range("2022-07-01", "2022-07-10", 0, 100)
        self.assertEqual(len(expenses),0)

            
    
unittest.main()