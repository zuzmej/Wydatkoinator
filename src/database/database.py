from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from .base import Base
from .category import Category
from .expense import Expense
from datetime import datetime

class Database:
    def __init__(self, db_string: str):
        self.engine = create_engine("sqlite:///" + db_string)
        Base.metadata.create_all(self.engine) # create all tables in the database
        self.Session = sessionmaker(bind=self.engine)
        
    
    def add_category(self, category_name: str):
        session = self.Session()
        existing_category = session.query(Category).filter_by(name=category_name).first()

        if existing_category:
            raise ValueError(f"Category '{category_name}' already exists.")
        
        session.add(Category(name=category_name))
        session.commit()
        session.close()

    def delete_category(self, category_name: str):
        session = self.Session()
        category_to_delete = session.query(Category).filter_by(name=category_name).first()

        if not category_to_delete:  # jeżeli nie ma takiej kategorii
            raise ValueError(f"Category '{category_name}' does not exist.")
        
        session.delete(category_to_delete)
        session.commit()
        session.close()

    def change_category_name(self, category_name: str, category_new_name: str):
        session = self.Session()
        category_to_update = session.query(Category).filter_by(name=category_name).first()

        if not category_to_update:
            raise ValueError(f"No category found with name {category_name}")
        
        category_to_update.name = category_new_name
        session.commit()
        session.close()

    def add_expense(self, amount: float, date: str, category_id: int):
        session = self.Session()
        category = session.query(Category).filter_by(id=category_id).first()

        if not category:
            raise ValueError(f"No category found with id {category_id}")
        
        date = datetime.strptime(date, "%Y-%m-%d").date()
        session.add(Expense(amount=amount, date=date, category_id=category_id))
        session.commit()
        session.close()
    
    def get_category_id_by_name(self, category_name: str) -> int:
        session = self.Session()
        category = session.query(Category).filter_by(name=category_name).first()
        session.close()
        
        if not category:
            raise ValueError(f"No category found with name {category_name}")

        return category.id

    def get_all_categories(self):
        session = self.Session()
        categories = session.query(Category).all()
        session.close()
        return categories
    
    def get_category_by_id(self, category_id: int):
        session = self.Session()
        category = session.query(Category).filter_by(id=category_id).first()
        session.close()
        return category
    
    def get_category_id_by_name(self, category_name: str) -> int:
        session = self.Session()
        category = session.query(Category).filter_by(name=category_name).first()
        session.close()
        
        if not category:
            raise ValueError(f"No category found with name {category_name}")

        return category.id

    
    def get_all_expenses(self):
        session = self.Session()
        expenses = session.query(Expense).options(joinedload(Expense.category)).all()
        session.close()
        return expenses
    
    def get_expense_by_id(self, expense_id: int):
        session = self.Session()
        expenses = session.query(Expense).options(joinedload(Expense.category)).filter_by(id=expense_id).first()
        session.close()
        return expenses
    
    def get_expenses_by_date(self, date: str):
        session = self.Session()
        date = datetime.strptime(date, "%Y-%m-%d").date()
        expenses = session.query(Expense).options(joinedload(Expense.category)).filter_by(date=date).all()
        session.close()
        return expenses
    
    def get_expenses_by_date_range(self, start_date: str, end_date: str):
        session = self.Session()
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        expenses = session.query(Expense).options(joinedload(Expense.category)).filter(Expense.date.between(start_date, end_date)).all()
        session.close()
        return expenses
    
    def get_expenses_by_category_id_in_date_range(self, category_id: int, start_date: str, end_date: str):
        session = self.Session()
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        expenses = session.query(Expense).options(joinedload(Expense.category)).filter(Expense.category_id == category_id,Expense.date.between(start_date, end_date)).all()
        session.close()
        return expenses
    
    
    def get_expenses_by_category_name_in_date_range(self, category_name: str, start_date: str, end_date: str):
        session = self.Session()
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        expenses = session.query(Expense).options(joinedload(Expense.category)).join(Category).filter(Category.name == category_name, Expense.date.between(start_date, end_date)).all()
        session.close()
        return expenses
    
    def get_expenses_in_date_and_cost_range(self, start_date: str, end_date: str, min_cost: float, max_cost: float):
        session = self.Session()
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        expenses = session.query(Expense).options(joinedload(Expense.category)).filter(Expense.date.between(start_date, end_date),Expense.amount.between(min_cost, max_cost)).all()
        session.close()
        return expenses
    

    def delete_expense(self, expense_id: int):
        session = self.Session()
        expense = session.query(Expense).filter_by(id=expense_id).first()
        
        if not expense:
            raise ValueError(f"No expense found with id {expense_id}")

        session.delete(expense)
        session.commit()
        session.close()



    def edit_expense(self, expense_id: int, amount: float = None, date: str = None, category_id: int = None):
        session = self.Session()
        expense = session.query(Expense).filter_by(id=expense_id).first()
        
        if not expense:
            raise ValueError(f"No expense found with id {expense_id}")

        if amount is not None:
            expense.amount = amount

        if date is not None:
            expense.date = datetime.strptime(date, "%Y-%m-%d").date()

        if category_id is not None:
            category = session.query(Category).filter_by(id=category_id).first()
            if not category:
                raise ValueError(f"No category found with id {category_id}")
            expense.category_id = category_id

        session.commit()
        session.close()



    def delete_expenses_by_category_id(self, category_id: int):
        session = self.Session()
        expenses_to_delete = session.query(Expense).filter_by(category_id=category_id).all()

        for expense in expenses_to_delete:
            session.delete(expense)

        session.commit()
        session.close()