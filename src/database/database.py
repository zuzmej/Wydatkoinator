from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from base import Base
from category import Category
from expense import Expense

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

    def add_expense(self, amount: float, date: str, category_id: int):
        session = self.Session()
        category = session.query(Category).filter_by(id=category_id).first()

        if not category:
            raise ValueError(f"No category found with id {category_id}")
        
        session.add(Expense(amount=amount, date=date, category_id=category_id))
        session.commit()
        session.close()
    
    def get_categories(self):
        session = self.Session()
        categories = session.query(Category).all()
        session.close()
        return categories
    
    def get_category(self, category_id: int):
        session = self.Session()
        category = session.query(Category).filter_by(id=category_id).first()
        session.close()
        return category
    
    def get_expenses(self):
        session = self.Session()
        expenses = session.query(Expense).all()
        session.close()
        return expenses
    
    def get_expenses_with_category_name(self):
        session = self.Session()
        expenses = session.query(Expense).options(joinedload(Expense.category)).all()
        session.close()
        return expenses
    
    def get_expenses_by_id(self, expense_id: int):
        session = self.Session()
        expenses = session.query(Expense).filter_by(id=expense_id).first()
        session.close()
        return expenses
    
    def get_expenses_by_date(self, date: str):
        session = self.Session()
        expenses = session.query(Expense).options(joinedload(Expense.category)).filter_by(date=date).all()
        session.close()
        return expenses
    
    def get_expenses_by_category_id(self, category_id: int):
        session = self.Session()
        expenses = session.query(Expense).options(joinedload(Expense.category)).filter_by(category_id=category_id).all()
        session.close()
        return expenses
    
    
    def get_expenses_by_category_name(self, category_name: str):
        session = self.Session()
        expenses = session.query(Expense).join(Category).filter(Category.name == category_name).options(joinedload(Expense.category)).all()
        session.close()
        return expenses